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

> [!success] Lösung – Beispiel Netzplantechnik
>
> **Vorgangsliste:**
>
> | Vorgang | Dauer | Vorgänger |
> | ------- | ----- | --------- |
> | A       | 3     | –         |
> | B       | 5     | A         |
> | C       | 2     | A         |
> | D       | 4     | B, C      |
> | E       | 3     | D         |
>
> **Vorwärtsrechnung (FAZ / FEZ):**
>
> | Vorgang | Dauer | FAZ | FEZ |
> | ------- | ----- | --- | --- |
> | A       | 3     | 0   | 3   |
> | B       | 5     | 3   | 8   |
> | C       | 2     | 3   | 5   |
> | D       | 4     | 8   | 12  |
> | E       | 3     | 12  | 15  |
>
> Projektdauer = **15 Tage** (FEZ des letzten Vorgangs)
>
> **Rückwärtsrechnung (SEZ / SAZ):**
>
> | Vorgang | Dauer | SEZ | SAZ |
> | ------- | ----- | --- | --- |
> | E       | 3     | 15  | 12  |
> | D       | 4     | 12  | 8   |
> | B       | 5     | 8   | 3   |
> | C       | 2     | 8   | 6   |
> | A       | 3     | 3   | 0   |
>
> **Gesamtpuffer GP = SAZ − FAZ:**
>
> | Vorgang | SAZ | FAZ | GP | Kritisch? |
> | ------- | --- | --- | -- | --------- |
> | A       | 0   | 0   | 0  | ja        |
> | B       | 3   | 3   | 0  | ja        |
> | C       | 6   | 3   | 3  | nein      |
> | D       | 8   | 8   | 0  | ja        |
> | E       | 12  | 12  | 0  | ja        |
>
> **Kritischer Pfad: A → B → D → E** (alle GP = 0, Verzögerung verlängert das gesamte Projekt)

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
