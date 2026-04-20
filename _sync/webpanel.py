#!/usr/bin/env python3
"""Web panel for Schul-Sync + Claude Code Processing."""

import json
import os
import subprocess
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
VAULT_DIR = BASE_DIR.parent
CONFIG_FILE = BASE_DIR / "config.json"
STATE_FILE = BASE_DIR / "sync_state.json"

# ---------------------------------------------------------------------------
# Global process state
# ---------------------------------------------------------------------------
processes = {
    "sync": {"proc": None, "output": [], "status": "idle", "started": None},
    "process": {"proc": None, "output": [], "status": "idle", "started": None},
}
proc_lock = threading.Lock()


def _read_output(proc, target_key):
    """Background thread that reads subprocess stdout/stderr into memory."""
    for line in iter(proc.stdout.readline, ""):
        with proc_lock:
            processes[target_key]["output"].append(line.rstrip("\n"))
    proc.wait()
    with proc_lock:
        processes[target_key]["status"] = (
            "error" if proc.returncode != 0 else "done"
        )


def _start_process(target_key, cmd, cwd=None):
    """Start a subprocess and attach a reader thread."""
    with proc_lock:
        if processes[target_key]["status"] == "running":
            return False, "Already running"
        processes[target_key] = {
            "proc": None,
            "output": [],
            "status": "running",
            "started": datetime.now().isoformat(),
        }

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        cwd=cwd or str(BASE_DIR),
        bufsize=1,
    )
    with proc_lock:
        processes[target_key]["proc"] = proc

    t = threading.Thread(target=_read_output, args=(proc, target_key), daemon=True)
    t.start()
    return True, "Started"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)


def load_state():
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"iserv_files": {}, "moodle_files": {}, "last_sync": None}


def get_new_files():
    """Detect new/modified files via git status."""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            cwd=str(VAULT_DIR),
        )
        files = []
        for line in result.stdout.strip().splitlines():
            if not line.strip():
                continue
            status = line[:2].strip()
            filepath = line[3:].strip().strip('"')
            # skip _sync internal files
            if filepath.startswith("_sync/") or filepath.startswith(".obsidian/"):
                continue
            # determine source
            source = "unknown"
            for prefix in ["LF2", "LF3", "LF4", "LF5", "LF6", "DVT", "Deutsch",
                           "Englisch", "Mathe", "Sozialkunde", "Religion", "Sport",
                           "ZQ", "BBS-Allgemein"]:
                if filepath.startswith(prefix):
                    source = prefix
                    break
            files.append({
                "path": filepath,
                "status": status,
                "source": source,
            })
        return files
    except Exception as e:
        return [{"path": f"Error: {e}", "status": "E", "source": "error"}]


# ---------------------------------------------------------------------------
# API Routes
# ---------------------------------------------------------------------------

@app.route("/api/sync/iserv", methods=["POST"])
def sync_iserv():
    ok, msg = _start_process("sync", [sys.executable, "sync.py", "--iserv"])
    return jsonify({"ok": ok, "message": msg}), 200 if ok else 409


@app.route("/api/sync/moodle", methods=["POST"])
def sync_moodle():
    ok, msg = _start_process("sync", [sys.executable, "moodle_browser.py"])
    return jsonify({"ok": ok, "message": msg}), 200 if ok else 409


@app.route("/api/sync/all", methods=["POST"])
def sync_all():
    # Chain: iserv first, then moodle
    cmd = f"{sys.executable} sync.py --iserv && {sys.executable} moodle_browser.py"
    ok, msg = _start_process("sync", ["bash", "-c", cmd])
    return jsonify({"ok": ok, "message": msg}), 200 if ok else 409


@app.route("/api/sync/status")
def sync_status():
    with proc_lock:
        s = processes["sync"]
        return jsonify({
            "status": s["status"],
            "output": s["output"],
            "started": s["started"],
            "lines": len(s["output"]),
        })


@app.route("/api/files/new")
def files_new():
    files = get_new_files()
    # group by source
    grouped = {}
    for f in files:
        grouped.setdefault(f["source"], []).append(f)
    return jsonify({"files": files, "grouped": grouped})


@app.route("/api/process", methods=["POST"])
def start_process():
    new_files = get_new_files()
    if not new_files:
        return jsonify({"ok": False, "message": "No new files to process"}), 400

    file_list = "\n".join(f"- {f['path']}" for f in new_files)
    prompt = (
        "Du bist im Obsidian Vault. Folgende neue Dateien wurden synchronisiert:\n"
        f"{file_list}\n\n"
        "Verarbeite die PDFs: Erstelle für jede PDF-Datei eine Obsidian-Note mit "
        "Zusammenfassung im selben Ordner. "
        "Nutze das bestehende Frontmatter-Format (fach, thema, tags, datum, typ)."
    )

    cmd = [
        "claude",
        "-p", prompt,
        "--allowedTools", "Read,Write,Edit,Bash(python3*)",
        "--add-dir", str(VAULT_DIR),
    ]
    ok, msg = _start_process("process", cmd, cwd=str(VAULT_DIR))
    return jsonify({"ok": ok, "message": msg}), 200 if ok else 409


@app.route("/api/process/status")
def process_status():
    with proc_lock:
        s = processes["process"]
        return jsonify({
            "status": s["status"],
            "output": s["output"],
            "started": s["started"],
            "lines": len(s["output"]),
        })


@app.route("/api/state")
def get_state():
    state = load_state()
    return jsonify({
        "last_sync": state.get("last_sync"),
        "iserv_count": len(state.get("iserv_files", {})),
        "moodle_count": len(state.get("moodle_files", {})),
    })


# ---------------------------------------------------------------------------
# Dashboard HTML
# ---------------------------------------------------------------------------
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="de" class="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Schul-Sync Panel</title>
<script src="https://cdn.tailwindcss.com"></script>
<script>tailwind.config={darkMode:'class',theme:{extend:{colors:{bg:'#0f172a',card:'#1e293b',accent:'#3b82f6',green:'#22c55e',red:'#ef4444',yellow:'#eab308'}}}}</script>
<style>
  body{background:#0f172a;color:#e2e8f0;font-family:ui-monospace,monospace}
  .log-box{max-height:400px;overflow-y:auto;font-size:0.8rem;line-height:1.4}
  .log-box::-webkit-scrollbar{width:6px}
  .log-box::-webkit-scrollbar-thumb{background:#475569;border-radius:3px}
  .badge{display:inline-flex;align-items:center;padding:2px 10px;border-radius:9999px;font-size:0.75rem;font-weight:600}
  .badge-idle{background:#334155;color:#94a3b8}
  .badge-running{background:#1e3a5f;color:#60a5fa;animation:pulse 1.5s infinite}
  .badge-done{background:#14532d;color:#4ade80}
  .badge-error{background:#7f1d1d;color:#fca5a5}
  @keyframes pulse{0%,100%{opacity:1}50%{opacity:.6}}
  .btn{padding:8px 20px;border-radius:8px;font-weight:600;font-size:0.875rem;cursor:pointer;transition:all .15s}
  .btn:disabled{opacity:.4;cursor:not-allowed}
  .btn-blue{background:#3b82f6;color:#fff}.btn-blue:hover:not(:disabled){background:#2563eb}
  .btn-green{background:#22c55e;color:#fff}.btn-green:hover:not(:disabled){background:#16a34a}
  .btn-purple{background:#8b5cf6;color:#fff}.btn-purple:hover:not(:disabled){background:#7c3aed}
  details summary{cursor:pointer;user-select:none}
  details summary::-webkit-details-marker{color:#64748b}
</style>
</head>
<body class="min-h-screen p-4 md:p-8">

<div class="max-w-5xl mx-auto space-y-6">

  <!-- Header -->
  <div class="flex items-center justify-between flex-wrap gap-4">
    <h1 class="text-2xl font-bold tracking-tight">Schul-Sync Panel</h1>
    <div class="flex gap-3 items-center text-sm">
      <span>Sync: <span id="syncBadge" class="badge badge-idle">idle</span></span>
      <span>Claude: <span id="procBadge" class="badge badge-idle">idle</span></span>
    </div>
  </div>

  <!-- Stats -->
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
    <div class="bg-card rounded-xl p-5">
      <div class="text-xs text-slate-400 uppercase tracking-wide mb-1">Letzter Sync</div>
      <div id="lastSync" class="text-lg font-semibold">—</div>
    </div>
    <div class="bg-card rounded-xl p-5">
      <div class="text-xs text-slate-400 uppercase tracking-wide mb-1">IServ-Dateien</div>
      <div id="iservCount" class="text-lg font-semibold">—</div>
    </div>
    <div class="bg-card rounded-xl p-5">
      <div class="text-xs text-slate-400 uppercase tracking-wide mb-1">Moodle-Dateien</div>
      <div id="moodleCount" class="text-lg font-semibold">—</div>
    </div>
  </div>

  <!-- Sync Controls -->
  <div class="bg-card rounded-xl p-5 space-y-4">
    <h2 class="text-lg font-semibold">Synchronisation</h2>
    <div class="flex flex-wrap gap-3">
      <button class="btn btn-blue" onclick="doSync('iserv')">IServ Sync</button>
      <button class="btn btn-blue" onclick="doSync('moodle')">Moodle Sync</button>
      <button class="btn btn-green" onclick="doSync('all')">Alles Syncen</button>
    </div>
    <div id="syncLog" class="log-box bg-slate-900/60 rounded-lg p-3 hidden">
      <pre id="syncLogPre" class="whitespace-pre-wrap text-slate-300"></pre>
    </div>
  </div>

  <!-- New Files -->
  <div class="bg-card rounded-xl p-5 space-y-4">
    <div class="flex items-center justify-between">
      <h2 class="text-lg font-semibold">Neue Dateien</h2>
      <button class="btn btn-blue text-xs !py-1 !px-3" onclick="loadFiles()">Aktualisieren</button>
    </div>
    <div id="fileList" class="space-y-2 text-sm">
      <p class="text-slate-500">Laden...</p>
    </div>
  </div>

  <!-- Claude Processing -->
  <div class="bg-card rounded-xl p-5 space-y-4">
    <h2 class="text-lg font-semibold">Claude Code Verarbeitung</h2>
    <p class="text-sm text-slate-400">Startet Claude Code CLI um neue PDFs zu Obsidian-Notes zu verarbeiten.</p>
    <button class="btn btn-purple" onclick="startProcess()">Verarbeitung starten</button>
    <div id="procLog" class="log-box bg-slate-900/60 rounded-lg p-3 hidden">
      <pre id="procLogPre" class="whitespace-pre-wrap text-slate-300"></pre>
    </div>
  </div>

</div>

<script>
const $ = s => document.querySelector(s);

function setBadge(el, status) {
  el.textContent = status;
  el.className = 'badge badge-' + (status === 'running' ? 'running' : status === 'done' ? 'done' : status === 'error' ? 'error' : 'idle');
}

async function api(path, method='GET') {
  const r = await fetch('/api/' + path, {method});
  return r.json();
}

// --- State ---
async function loadState() {
  const d = await api('state');
  $('#lastSync').textContent = d.last_sync ? new Date(d.last_sync).toLocaleString('de-DE') : 'Nie';
  $('#iservCount').textContent = d.iserv_count;
  $('#moodleCount').textContent = d.moodle_count;
}

// --- Files ---
async function loadFiles() {
  const d = await api('files/new');
  const el = $('#fileList');
  if (!d.files.length) {
    el.innerHTML = '<p class="text-slate-500">Keine neuen Dateien.</p>';
    return;
  }
  let html = '';
  for (const [source, files] of Object.entries(d.grouped)) {
    html += `<details open><summary class="font-semibold text-slate-300 mb-1">${source} <span class="text-slate-500 font-normal">(${files.length})</span></summary><ul class="ml-4 space-y-0.5">`;
    for (const f of files) {
      const icon = f.status === '?' || f.status === '??' ? '🆕' : '✏️';
      html += `<li class="text-slate-400"><span class="mr-1">${icon}</span>${f.path}</li>`;
    }
    html += '</ul></details>';
  }
  el.innerHTML = html;
}

// --- Sync ---
let syncPoll = null;
async function doSync(type) {
  const d = await api('sync/' + type, 'POST');
  if (!d.ok) { alert(d.message); return; }
  $('#syncLog').classList.remove('hidden');
  $('#syncLogPre').textContent = 'Gestartet...\n';
  clearInterval(syncPoll);
  syncPoll = setInterval(pollSync, 2000);
}

async function pollSync() {
  const d = await api('sync/status');
  setBadge($('#syncBadge'), d.status);
  $('#syncLogPre').textContent = d.output.join('\n') || 'Warte auf Output...';
  $('#syncLog').scrollTop = $('#syncLog').scrollHeight;
  if (d.status !== 'running') {
    clearInterval(syncPoll);
    loadState();
    loadFiles();
  }
}

// --- Process ---
let procPoll = null;
async function startProcess() {
  const d = await api('process', 'POST');
  if (!d.ok) { alert(d.message); return; }
  $('#procLog').classList.remove('hidden');
  $('#procLogPre').textContent = 'Claude Code gestartet...\n';
  clearInterval(procPoll);
  procPoll = setInterval(pollProc, 2000);
}

async function pollProc() {
  const d = await api('process/status');
  setBadge($('#procBadge'), d.status);
  $('#procLogPre').textContent = d.output.join('\n') || 'Warte auf Output...';
  $('#procLog').scrollTop = $('#procLog').scrollHeight;
  if (d.status !== 'running') {
    clearInterval(procPoll);
    loadFiles();
  }
}

// --- Init ---
async function checkRunning() {
  const [s, p] = await Promise.all([api('sync/status'), api('process/status')]);
  setBadge($('#syncBadge'), s.status);
  setBadge($('#procBadge'), p.status);
  if (s.status === 'running') {
    $('#syncLog').classList.remove('hidden');
    syncPoll = setInterval(pollSync, 2000);
  }
  if (p.status === 'running') {
    $('#procLog').classList.remove('hidden');
    procPoll = setInterval(pollProc, 2000);
  }
}

loadState();
loadFiles();
checkRunning();
</script>
</body>
</html>"""


@app.route("/")
def dashboard():
    return DASHBOARD_HTML


if __name__ == "__main__":
    print(f"Schul-Sync Panel: http://localhost:5001")
    print(f"Vault: {VAULT_DIR}")
    print(f"Config: {CONFIG_FILE}")
    app.run(host="0.0.0.0", port=5001, debug=False)
