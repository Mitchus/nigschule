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

> [!success] Lösung
> **1. Top-Down-Methode:**
> Bei der Top-Down-Methode wird vom Allgemeinen zum Speziellen vorgegangen: Zuerst wird das Gesamtsystem grob geplant, dann schrittweise in immer kleinere Teilbereiche aufgeteilt und ausgearbeitet. Anwendung findet diese Methode vor allem im **Wasserfallmodell**, da dort zuerst die Gesamtanforderungen definiert werden und jede Phase die Ergebnisse der vorherigen als Grundlage nutzt.
>
> **2. Vergleich der Modelle:**
> | Modell | Vorteile | Nachteile | Geeignet für |
> | ------ | -------- | --------- | ------------ |
> | Wasserfallmodell | Klar strukturiert, gut dokumentiert, leicht planbar | Änderungen spät sehr teuer, kein Kundenfeedback zwischendurch | Projekte mit stabilen, klaren Anforderungen (z.B. Brückenbau-Software) |
> | V-Modell | Qualität durch parallele Testplanung, gut für sicherheitskritische Systeme | Starr, teuer bei Änderungen | Behörden, Luft- und Raumfahrt, Medizintechnik |
> | SCRUM | Flexibel, schnelles Kundenfeedback, hohe Transparenz | Erfordert erfahrenes Team, schwer skalierbar | Softwareprojekte mit sich ändernden Anforderungen |
> | Kanban | Einfach einzuführen, flexibel, gut visualisierbar | Kein fester Zeitplan, wenig Struktur | Support-Teams, kontinuierliche Wartungsaufgaben |
>
> **3. Kompetenzcheck (S. 519/499):**
> Klassische Modelle (Wasserfall, V-Modell) eignen sich für Projekte mit fixen Anforderungen und hohem Dokumentationsbedarf. Agile Modelle (SCRUM, Kanban, XP) eignen sich für dynamische Projekte, bei denen Kundenfeedback kontinuierlich eingearbeitet werden soll.
>
> **4. DevOps – Erläuterung mit Vor- und Nachteilen:**
> DevOps verbindet die Softwareentwicklung (Development) und den IT-Betrieb (Operations) zu einem gemeinsamen, automatisierten Prozess. Ziel ist es, Software schneller, zuverlässiger und häufiger auszuliefern – durch Automatisierung (CI/CD-Pipelines), gemeinsame Verantwortung und enge Zusammenarbeit beider Teams.
> - Vorteile: Schnellere Releases durch Automatisierung; bessere Zusammenarbeit und weniger Schnittstellenprobleme zwischen Entwicklung und Betrieb.
> - Nachteile: Erfordert einen tiefgreifenden Kulturwandel im Unternehmen; die Toolchain (z.B. Docker, Jenkins, Kubernetes) ist komplex und muss beherrscht werden.
>
> **5. XP und Kanban – Vor- und Nachteile:**
> *Extreme Programming (XP):*
> - Vorteile: Hohe Codequalität durch TDD und Pair Programming; schnelles Kundenfeedback durch kurze Releases.
> - Nachteile: Pair Programming erhöht kurzfristig den Personalaufwand; erfordert hohe Disziplin und Erfahrung im Team.
>
> *Kanban:*
> - Vorteile: Einfach einzuführen ohne feste Rollen; WIP-Limits reduzieren Überlastung und erhöhen den Durchsatz.
> - Nachteile: Kein fester Zeitplan oder Iterationsrahmen – Termine sind schwer verbindlich zu planen; wenig Struktur für komplexe Neuentwicklungen.

> [!example] Aufgabe 2 - Wasserfallmodell
> Ordne die Phasen und passenden Handlungsprodukte des Wasserfallmodells zu.

> [!success] Lösung
> | Phase | Handlungsprodukt (Ergebnis/Deliverable) |
> | ----- | --------------------------------------- |
> | Anforderungen | Lastenheft, Anforderungsdokument |
> | Entwurf | Pflichtenheft, Systemarchitektur, UML-Diagramme |
> | Implementierung | Quellcode, Datenbankschema, ausführbares Programm |
> | Test | Testprotokolle, Fehlerberichte, Testberichte |
> | Betrieb / Wartung | Betriebshandbuch, Wartungsberichte, Updates |

> [!example] Aufgabe 3 - Aspekte des Wasserfallmodells
> 1. Definiere die Begriffe "Dokumentgetrieben" und "Top-Down-Methode"
> 2. Notiere mind. drei Vor- und Nachteile

> [!success] Lösung
> **1. Begriffsdefinitionen:**
>
> *Dokumentgetrieben:* Beim dokumentgetriebenen Ansatz ist jede Phase an ein verbindliches Dokument geknüpft, das am Ende der Phase fertiggestellt und genehmigt werden muss, bevor die nächste Phase beginnt. Diese Dokumente (z.B. Lastenheft, Pflichtenheft) dienen als Grundlage für alle weiteren Schritte und ermöglichen eine lückenlose Nachvollziehbarkeit des Entwicklungsprozesses.
>
> *Top-Down-Methode:* Die Top-Down-Methode beschreibt eine Vorgehensweise, bei der man vom Groben zum Detail arbeitet. Zunächst wird das Gesamtsystem auf hoher Abstraktionsebene geplant und in der Folge schrittweise in kleinere, detailliertere Teilbereiche aufgegliedert. Im Wasserfallmodell bedeutet dies: erst Gesamtanforderungen, dann Architektur, dann Implementierung einzelner Module.
>
> **2. Vor- und Nachteile des Wasserfallmodells:**
>
> Vorteile:
> - Klar strukturierter Ablauf – alle Beteiligten wissen, was wann zu tun ist.
> - Umfangreiche Dokumentation erleichtert Wartung und ermöglicht Nachvollziehbarkeit.
> - Leicht planbar und kalkulierbar (Zeit, Kosten, Ressourcen).
> - Gut geeignet für Projekte mit stabilen, vollständig bekannten Anforderungen.
>
> Nachteile:
> - Änderungen der Anforderungen führen zu hohem Aufwand, da frühere Phasen wiederholt werden müssen.
> - Kein Kundenfeedback während der Entwicklung – Fehler in der Anforderungsphase werden oft erst bei der Abnahme erkannt.
> - Späte Risikoerkennung: Probleme treten erst in der Test- oder Betriebsphase auf.
> - Unflexibel gegenüber modernen, agilen Anforderungen der Softwareentwicklung.

---

## Materialien

- ![[files/VorgehensmodelleGrafiken.pdf]]
- ![[files/Vorgehensmodell_ITK_GHI_19_20.pdf]]

---

## Siehe auch

- [[Projektmanagement und Softwareentwicklung]]
- [[Software und Qualität]]
