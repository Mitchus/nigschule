---
fach: LF5
thema: Vorgehensmodelle
tags: [lf5, vorgehensmodelle, wasserfall, scrum, agile]
datum: 2026-04-20
typ: notiz
---

# Vorgehensmodelle

## Übersicht

| Modell           | Typ          | Besonderheit                        |
| ---------------- | ------------ | ----------------------------------- |
| **Wasserfallmodell** | Sequentiell | Phasen nacheinander, dokumentgetrieben |
| **V-Modell**     | Sequentiell  | Jeder Entwicklungsphase steht eine Testphase gegenüber |
| **Spiralmodell** | Iterativ     | Risikogetrieben, wiederholende Zyklen |
| **SCRUM**        | Agil         | Sprints, Daily Standups, Product Backlog |
| **Kanban**       | Agil         | Kontinuierlicher Fluss, Boards      |
| **XP**           | Agil         | Pair Programming, TDD, kurze Releases |
| **DevOps**       | Kultur       | Entwicklung + Betrieb verschmelzen   |

---

## Wasserfallmodell

Dokumentgetriebenes, sequentielles Modell mit **Top-Down-Methode**.

```
Anforderungen
    └→ Entwurf
        └→ Implementierung
            └→ Test
                └→ Betrieb / Wartung
```

**Vorteile:**
- Einfach und klar strukturiert
- Gut dokumentiert
- Leicht planbar

**Nachteile:**
- Änderungen spät teuer
- Kein Feedback zwischendurch
- Fehler erst spät erkannt

---

## V-Modell

Erweiterung des Wasserfallmodells mit Testphasen:

```
Anforderungen ──────────────── Abnahmetest
    Grobentwurf ────────────── Systemtest
        Feinentwurf ────────── Integrationstest
            Implementierung ── Modultest
```

Jede Entwicklungsphase links hat eine korrespondierende Testphase rechts.

---

## SCRUM

Agiles Framework mit festen Rollen und Ereignissen:

**Rollen:**
- **Product Owner** - verantwortet das Produkt, pflegt das Backlog
- **Scrum Master** - beseitigt Hindernisse, schützt das Team
- **Development Team** - setzt die Anforderungen um (3-9 Personen)

**Artefakte:**
- **Product Backlog** - priorisierte Anforderungsliste
- **Sprint Backlog** - Aufgaben für den aktuellen Sprint
- **Increment** - fertiges, auslieferbares Teilergebnis

**Ereignisse:**
- **Sprint** (1-4 Wochen) - Zeitrahmen für Entwicklung
- **Sprint Planning** - Was wird im Sprint umgesetzt?
- **Daily Standup** (15 Min.) - Was habe ich getan? Was steht an? Gibt es Hindernisse?
- **Sprint Review** - Ergebnis vorstellen
- **Sprint Retrospektive** - Prozess verbessern

---

## DevOps

Kultur und Praxis, die **Softwareentwicklung (Dev)** und **IT-Betrieb (Ops)** zusammenführt.

**Vorteile:**
- Schnellere Releases
- Bessere Zusammenarbeit
- Automatisierte Prozesse (CI/CD)

**Nachteile:**
- Kulturwandel notwendig
- Komplexe Toolchain
- Sicherheitsrisiken bei schnellen Releases

---

## Extreme Programming (XP)

Agile Methode mit Fokus auf Codequalität:

- **Pair Programming** - zwei Entwickler, ein Rechner
- **Test-Driven Development (TDD)** - Tests vor dem Code
- **Continuous Integration** - häufiges Zusammenführen
- **Kurze Releases** - schnelles Kundenfeedback

---

## Kanban

Visualisierung des Arbeitsflusses auf einem Board:

```
┌──────────┬──────────┬──────────┐
│ To Do    │ In Work  │   Done   │
├──────────┼──────────┼──────────┤
│ Task A   │ Task C   │ Task E   │
│ Task B   │ Task D   │          │
│          │          │          │
└──────────┴──────────┴──────────┘
```

**Prinzipien:**
- **WIP-Limit** (Work in Progress) - max. Aufgaben gleichzeitig
- **Pull-Prinzip** - neue Aufgabe erst wenn Kapazität frei
- **Kontinuierliche Verbesserung**

---

## Aufgaben

> [!example] Aufgabe 1 - Vorgehensmodelle vergleichen
> 1. Recherchiere den Begriff **Top-Down-Methode**. In welchem Vorgehensmodell findet diese Anwendung?
> 2. Vergleiche Vor- und Nachteile der Modelle und ordne passende Projektthemen zu
> 3. Kompetenzcheck S. 519/499
> 4. Erläutere den DevOps-Ansatz mit je zwei Vor- und Nachteilen
> 5. Recherchiere zu XP und Kanban - Vor- und Nachteile vorstellen

> [!example] Aufgabe 2 - Wasserfallmodell
> Ordne die Phasen und passenden Handlungsprodukte des Wasserfallmodells zu.

> [!example] Aufgabe 3 - Aspekte des Wasserfallmodells
> 1. Definiere die Begriffe "Dokumentgetrieben" und "Top-Down-Methode"
> 2. Notiere mind. drei Vor- und Nachteile

---

## Materialien

- ![[files/VorgehensmodelleGrafiken.pdf]]
- ![[files/Vorgehensmodell_ITK_GHI_19_20.pdf]]

---

## Siehe auch

- [[Projektmanagement und Softwareentwicklung]]
- [[Software und Qualität]]
