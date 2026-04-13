---
thema: Prompt Engineering in der Anwendungsentwicklung
tags: [ki, prompt-engineering]
datum: 2026-04-13
typ: notiz
---
# Prompt Engineering in der Anwendungsentwicklung

## Bringen detailliertere Prompts was?

Ja, aber nur relevantes Detail. [Studie 2025](https://arxiv.org/html/2502.14255v1):

| Prompt-Typ | Ergebnis |
|---|---|
| Kurz (<50% der Standard-Tokens) | Schlechter. F1 -0.04 bis -0.09, Recall -0.10 bis -0.12 |
| Lang (>200% der Standard-Tokens) | Besser. F1 +0.07 bis +0.08 |
| Zu lang (mit irrelevantem Content) | [Sinkt wieder](https://gritdaily.com/impact-prompt-length-llm-performance/) - "Prompt Bloat" |

---

## Techniken

### XML-Tags (besonders Claude)

- Claude wurde [mit XML-Tags trainiert](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- Struktur schlägt Prosa
- Tags wie `<instructions>`, `<context>`, `<output_format>` nutzen

```xml
<instructions>
  Analysiere den Kundenfall und erstelle eine Empfehlung.
</instructions>
<context>
  Branche: E-Commerce
  Problem: Hohe Retourenquote bei Elektronik (32%)
</context>
<output_format>
  - Ursachenanalyse (3-5 Punkte)
  - Konkrete Maßnahmen mit geschätztem Impact
</output_format>
```

### Few-Shot Prompting

- [Höchster ROI](https://mem0.ai/blog/few-shot-prompting-guide) aller Techniken
- 3-5 Beispiele zeigen statt beschreiben
- In `<example>` Tags wrappen

```xml
<examples>
  <example>
    <input>Kunde beschwert sich über lange Lieferzeit</input>
    <output>Kategorie: Logistik | Priorität: Mittel | Aktion: Tracking-Link senden</output>
  </example>
  <example>
    <input>Produkt defekt bei Ankunft</input>
    <output>Kategorie: Qualität | Priorität: Hoch | Aktion: Sofortiger Ersatz</output>
  </example>
</examples>
```

### Chain-of-Thought (CoT)

- Für komplexe [Reasoning-Aufgaben](https://www.promptingguide.ai/techniques/cot)
- Zero-Shot: einfach "Denke Schritt für Schritt" anfügen
- Few-Shot: Beispiele mit ausgeschriebenem Denkprozess liefern (deutlich besser)

### Rollen-Prompting

- Dem Modell eine Rolle geben fokussiert Verhalten und Ton
- z.B. `Du bist ein Senior Software Architect mit 15 Jahren Erfahrung in verteilten Systemen.`

---

## Context Engineering > Prompt Engineering

[Paradigmenwechsel 2025/2026](https://neo4j.com/blog/agentic-ai/context-engineering-vs-prompt-engineering/) - in Production reicht ein guter Prompt allein nicht.

Context Engineering umfasst:
- **Memory** - was weiß das Modell aus vorherigen Interaktionen?
- **Retrieval** - welche Dokumente werden dynamisch injiziert?
- **Tool-Definitionen** - welche Werkzeuge stehen zur Verfügung?
- **Conversation History** - wie wird der Verlauf gemanaged?

[57% der Orgs](https://www.firecrawl.dev/blog/context-engineering) haben AI-Agents in Production, aber 32% nennen Qualität als Hauptproblem → schlechtes Context-Management, nicht Modell-Limitierungen.

Siehe auch: [Anthropic - Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

> [!important] Lost in the Middle
> LLMs verarbeiten Infos in der Mitte langer Kontexte am schlechtesten. Relevantes gehört an den Anfang oder ans Ende.

---

## Häufige Fehler

- Vage Prompts → "Mach ne Zusammenfassung" vs. "3 Bullet Points, fokussiert auf finanzielle Auswirkungen, max 100 Wörter"
- Kontext-Annahmen → das Modell kennt dein Business nicht, explizit erklären
- Alles in einen Prompt → komplexe Workflows aufbrechen (Prompt Chaining)
- Kein Output-Format → immer spezifizieren: JSON, Tabelle, Prosa, Bullets?
- [Nicht iterieren](https://treyworks.com/common-prompt-engineering-mistakes-to-avoid/) → erster Prompt ist selten optimal, systematisch testen
- Negative Anweisungen → "Benutze kein Markdown" schlechter als "Antworte in fließendem Prosatext"
- Veraltete Quelldaten → Zugang zu Dokumenten ≠ korrekte Antworten

---

## Production Best Practices

### System Prompt Design

Laut [Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices):
- System-Prompt für High-Level Setting (Rolle, Grundregeln)
- User-Prompt für konkrete Anweisungen (Claude folgt User-Messages besser)

> [!tip] Golden Rule
> Zeig deinen Prompt einem Kollegen ohne Kontext. Wenn der verwirrt ist, ist es das Modell auch.

### Prompt Scaffolding

- User-Input niemals direkt ans Modell
- Immer in strukturiertes Template wrappen

```xml
<system>Du bist ein Kundenservice-Bot für [Firma].
Du antwortest NUR zu Themen rund um unsere Produkte.</system>
<rules>
- Keine medizinischen/rechtlichen Ratschläge
- Bei Unsicherheit: an menschlichen Support verweisen
- Maximal 150 Wörter pro Antwort
</rules>
<user_input>{{USER_MESSAGE}}</user_input>
```

### Prompt Versioning

- Prompts versionieren wie Code
- Eine [Prompt-Änderung](https://www.lakera.ai/blog/prompt-engineering-guide) kann Output-Qualität, Safety und Tool-Auswahl über die ganze Pipeline verändern

### Testing

- Mit realen, chaotischen Inputs testen
- Edge Cases durchspielen
- Metriken definieren (Accuracy, Format-Compliance, Latenz)

---

## Wirksamkeit Übersicht

| Rang | Technik | Impact |
|------|---------|--------|
| 1 | Few-Shot Examples (3-5 Beispiele) | Höchster ROI |
| 2 | Strukturierung (XML-Tags, Sections) | Reduziert Fehlinterpretation |
| 3 | Spezifität (Format, Constraints, Kontext) | Eliminiert Raten |
| 4 | Chain-of-Thought | +10-40% bei Reasoning |
| 5 | Context Engineering (RAG, Memory, Tools) | Entscheidend für Production |
| 6 | Prompt Chaining (aufteilen) | Besser als Monster-Prompts |
| 7 | Iteration & Testing | Kumulativer Effekt |

## Siehe auch
- [[ZQ]]
- [[ZQ 2]]
