---
fach: DVT
thema: Rechnerarchitekturen
tags: [hardware, architektur]
datum: 2025-04-07
typ: notiz
---
### Vergleich von John-von-Neumann- und Harvard-Architektur

**John-von-Neumann-Architektur:**
- Gemeinsamer Speicher für Programme (Instruktionen) und Daten.
- Einheitlicher Datenpfad: gleicher Bus für Daten und Instruktionen.
- Vorteil: einfacherer Aufbau.
- Nachteil: sogenannter „Von-Neumann-Flaschenhals“, da Daten und Instruktionen nicht parallel abgerufen werden können.
        
**Harvard-Architektur:**
- Getrennte Speicherbereiche für Programme und Daten.
- Unabhängige Busse, was parallelen Zugriff ermöglicht.
- Vorteil: höhere Effizienz bei parallelen Daten-/Instruktionszugriffen.
- Nachteil: komplexerer Aufbau und höherer Aufwand bei der Programmierung.

![[Pasted image 20250407133908.png]]