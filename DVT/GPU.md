---
fach: DVT
thema: GPU
tags: [hardware, grafikkarte]
datum: 2024-04-18
typ: notiz
---

## Definition
- **GPU** = Graphics Processing Unit (Grafikprozessor)
- Spezialisierter Prozessor, der ursprünglich für die Berechnung von Grafiken entwickelt wurde
- Heute auch für allgemeine parallele Berechnungen eingesetzt (GPGPU)

## Aufgaben
- **Grafikberechnung**: Darstellung von 2D- und 3D-Grafiken auf dem Bildschirm
- **Parallele Verarbeitung**: Kann tausende kleine Aufgaben gleichzeitig berechnen (viele Kerne)
- Umwandlung von 3D-Koordinaten in 2D-Bildpunkte (Rendering)
- Berechnung von Texturen, Beleuchtung, Schatten und Effekten

## Unterschied zur CPU
| Merkmal | CPU | GPU |
|---|---|---|
| Kerne | Wenige (4–32), aber leistungsstark | Tausende, aber einfacher |
| Aufgaben | Sequenzielle, komplexe Aufgaben | Viele parallele, gleichartige Aufgaben |
| Takt | Hoch (3–5 GHz) | Niedriger, aber massiv parallel |
| Einsatz | Allgemeine Steuerung | Grafik, KI, Simulation |

## Einsatzgebiete
- **Gaming**: Echtzeit-Darstellung aufwendiger 3D-Spielgrafiken
- **Künstliche Intelligenz (KI)**: Training von neuronalen Netzen (Deep Learning)
- **Kryptomining**: Berechnung von Hashes für Kryptowährungen (z. B. Bitcoin)
- **Videobearbeitung**: Schnelles Rendern und Kodieren von Videos
- **Wissenschaftliche Simulationen**: Wettermodelle, Physik-Simulationen

## Wichtige Hersteller
- **NVIDIA**: Marktführer; GeForce-Serie (Gaming), Tesla/H100-Serie (KI & Rechenzentrum)
- **AMD**: Radeon-Serie (Gaming), Instinct-Serie (KI & HPC)
- **Intel**: Arc-Serie (neuerer Markteinstieg im Bereich Grafikkarten)

## Aufbau (vereinfacht)
- **VRAM** (Videospeicher): eigener, schneller Arbeitsspeicher auf der Grafikkarte
- **Shader-Kerne**: führen parallele Berechnungen durch
- **Kühlsystem**: GPU erzeugt viel Wärme, benötigt aktive Kühlung

## Siehe auch
- [[Anatomie eines PCs]]
- [[CPU]]
- [[Ram]]
- [[DVT Index]]
