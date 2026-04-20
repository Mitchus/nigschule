---
fach: LF2
thema: Kalkulation und Beschaffung
tags: [lf2, kalkulation, beschaffung, finanzierung]
datum: 2026-04-20
typ: notiz
---

# Kalkulation und Beschaffung

## Handelskalkulation (Zuschlagskalkulation)

Vom Einkaufspreis zum Verkaufspreis:

```
  Listeneinkaufspreis
- Liefererrabatt
= Zieleinkaufspreis
- Liefererskonto
= Bareinkaufspreis
+ Bezugskosten
= Bezugspreis (Einstandspreis)
+ Handlungskosten
= Selbstkosten
+ Gewinnzuschlag
= Barverkaufspreis
+ Kundenskonto
+ Vertreterprovision
= Zielverkaufspreis
+ Kundenrabatt
= Listenverkaufspreis (netto)
+ Umsatzsteuer (19%)
= Bruttoverkaufspreis
```

### Rechenbeispiel

| Kalkulation             | Vorgabe | Berechnung |
| ----------------------- | ------- | ---------- |
| Listeneinkaufspreis     | 300,00€ | 300,00€    |
| - Liefererrabatt (20%)  |         | -60,00€    |
| **= Zieleinkaufspreis** |         | **240,00€** |
| - Liefererskonto (3%)   |         | -7,20€     |
| **= Bareinkaufspreis**  |         | **232,80€** |
| + Bezugskosten (3%)     |         | +6,98€     |
| **= Bezugspreis**       |         | **239,78€** |
| + Handlungskosten       | 70,00€  | +70,00€    |
| **= Selbstkosten**      |         | **309,78€** |
| + Gewinnzuschlag (8%)   |         | +24,78€    |
| **= Barverkaufspreis**  |         | **334,57€** |
| + USt (19%)             |         | +63,57€    |
| **= Bruttopreis**       |         | **398,14€** |

> [!tip] Skonto und Rabatt werden "im Hundert" berechnet (auf den reduzierten Betrag), Zuschläge "vom Hundert".

---

## Finanzierungsoptionen

| Option         | Beschreibung                                  |
| -------------- | --------------------------------------------- |
| **Kauf**       | Sofortige Zahlung, Eigentum sofort             |
| **Leasing**    | Monatliche Rate, kein Eigentum                 |
| **Miete**      | Flexible Nutzung, jederzeit kündbar            |
| **Kredit**     | Bankfinanzierung, Zinsen, Eigentum nach Tilgung |

---

## Projektmanagement

### Gantt-Diagramm

Visualisiert Projektaufgaben als Balken auf einer Zeitachse.

```
Aufgabe A:  ████████
Aufgabe B:       ████████
Aufgabe C:              ██████
Aufgabe D:                    ████
            ─────────────────────→ Zeit
```

### Netzplantechnik

Berechnet den **kritischen Pfad** (längster Weg = Mindestprojektdauer).

| Begriff          | Beschreibung                              |
| ---------------- | ----------------------------------------- |
| **FAZ**          | Frühester Anfangszeitpunkt                |
| **FEZ**          | Frühester Endzeitpunkt = FAZ + Dauer      |
| **SAZ**          | Spätester Anfangszeitpunkt                |
| **SEZ**          | Spätester Endzeitpunkt                    |
| **GP**           | Gesamtpuffer = SAZ - FAZ                  |
| **FP**           | Freier Puffer                             |
| **Kritischer Pfad** | Vorgänge mit GP = 0 (keine Verzögerung möglich) |

---

## Materialien

- ![[files/01_Zuschlagskalkulation.pdf]]
- ![[files/02_Handelskalkulation.pdf]]
- ![[files/01_Finanzierungsoptionen des Kunden.pdf]]
- ![[files/01_IT25B_Projektmanagement.pdf]]
- ![[files/01_Gantt_Netzplantechnik_Lösung.pdf]]
- ![[files/02_Übungen Netzplantechnik_Lösungen.pdf]]

---

## Siehe auch

- [[Marketing und Recht]]
- [[IT-Hardware und Sicherheit]]
