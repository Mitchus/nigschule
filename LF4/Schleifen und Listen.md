---
fach: LF4
thema: Schleifen und Listen
tags: [lf4, python, schleifen, listen, iteration]
datum: 2026-04-20
typ: notiz
---

# Schleifen und Listen

## Schleifenarten

```
Schleifen
├── kopfgesteuert  (while) — Bedingung am Anfang
├── fußgesteuert   (while + break) — Bedingung am Ende
└── Zählschleife   (for + range) — feste Anzahl
```

---

## Kopfgesteuerte Schleife (`while`)

Die Bedingung wird **vor** jedem Durchlauf geprüft. Ist sie von Anfang an `False`, wird der Block nie ausgeführt.

```python
def ausgabe_zahlen():
    i = 0
    while i <= 10:
        print(i)
        i = i + 1

ausgabe_zahlen()
```

### Beispiel: Durchschnittstemperatur

```python
anzahl = 6
i = 0
summe = 0
temperaturen = []

while i < anzahl:
    print("Geben Sie die {0}. Temperatur in °C ein: ".format(i + 1))
    temperatur = float(input())
    temperaturen.append(temperatur)
    summe = summe + temperatur
    i = i + 1

durchschnitt = summe / anzahl
print(f"Durchschnitt: {durchschnitt:.2f} °C")
```

---

## Fußgesteuerte Schleife (Simulation)

Python hat keine native `do...while`-Schleife. Simulation mit `while True` und `break`:

```python
while True:
    eingabe = input("Geben Sie 'q' zum Beenden ein: ")
    if eingabe == 'q':
        break
    print(f"Sie haben '{eingabe}' eingegeben.")
```

---

## Zählschleife (`for` + `range`)

Die Schleifenwiederholung ist fest vorgegeben:

```python
# range(stop) — von 0 bis stop-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(1, 11):
    print(i)  # 1 bis 10

# range(start, stop, step)
for i in range(0, 20, 2):
    print(i)  # 0, 2, 4, ..., 18

# Rückwärts zählen
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

---

## Listen (Arrays)

Listen speichern mehrere Werte in einer Variable. Werte müssen nicht vom gleichen Typ sein.

```python
# Liste erstellen
zahlen = [1.3, 2.0, 33.01, -23.22, 5.23]

# Zugriff über Index (beginnt bei 0!)
print(zahlen[0])   # 1.3
print(zahlen[-1])  # 5.23 (letztes Element)

# Länge
print(len(zahlen)) # 5

# Element anhängen
zahlen.append(7.5)

# Element entfernen
zahlen.remove(2.0)
```

| Index | 0    | 1    | 2      | 3       | 4    |
| ----- | ---- | ---- | ------ | ------- | ---- |
| Wert  | 1.3  | 2.0  | 33.01  | -23.22  | 5.23 |

### Listen mit Schleifen durchlaufen

```python
namen = ["Max", "Anna", "Tom"]

# Mit for-in
for name in namen:
    print(name)

# Mit Index
for i in range(len(namen)):
    print(f"{i}: {namen[i]}")
```

---

## Aufgaben: Schleifen

> [!example] Aufgabe 1 - Temperaturen mit Liste
> Passe das Durchschnittsprogramm an:
> - Zeige die eingegebenen Temperaturen am Ende mit einer Schleife an
> - Ersetze die Eingabe durch Zufallszahlen (`import random`)
> - Erhöhe die Anzahl der Temperaturen

> [!example] Aufgabe 2 - Gerade Zahlen
> Gib alle geraden Zahlen von 0 bis 20 aus.
> - a) Welchen Schleifentyp brauchst du?
> - b) Erweitere: Der Benutzer bestimmt die Anzahl
> - c) Gib auch die Summe aller geraden Zahlen aus

> [!example] Aufgabe 3 - Sternfigur
> Gib mit Schleifen folgende Figur aus (pro Schreibvorgang nur ein `*`):
> ```
> *******
> *****
>  ***
>   *
> ```

> [!example] Aufgabe 4 - Fakultät
> Berechne die Fakultät einer eingegebenen Zahl.
> Hinweis: `0! = 1`, `5! = 5 × 4 × 3 × 2 × 1 = 120`

> [!example] Aufgabe 5 - Zahlenfolgen
> Programmiere Schleifen für folgende Folgen:
> - a) `99, 96, 93, ... 12, 9`
> - b) `1, 4, 9, 16, 25, ... 361, 400`
> - c) `2, 6, 10, 14, ... 98, 102`
> - d) `4, 16, 36, 64, 100 ... 900, 1024`
> - e) `2, 4, 8, 16, 32, ..., 16384, 32768`

> [!example] Aufgabe 6 - Einmaleins
> Gib das kleine Einmaleins aus (1×1 bis 10×10) als formatierte Tabelle.

> [!example] Aufgabe 7 - Quadrat zeichnen
> Eingabe: Seitenlänge. Ausgabe: Quadrat im Textmodus.
> ```
> Anzahl: 3
>
> * * *
> *   *
> * * *
> ```

> [!example] Aufgabe 8 - Treppe zeichnen
> Zeichne eine Treppe aus `h` Stufen mit Breite `b`:
> ```
> Treppenhöhe: 4
> Stufenbreite: 3
>
>          ***
>       ******
>    *********
> ************
> ```

> [!example] Aufgabe 9 - Quersumme
> Berechne die Quersumme einer Ganzzahl.
>
> Tipp: Nutze den Modulo-Operator `% 10` um die letzte Ziffer zu bekommen und `// 10` um sie abzuschneiden.
> ```
> Eingabe: 12345
> Quersumme: 15
> ```

> [!example] Aufgabe 10 - Sprinter-Wettkampf
> Zwei Läufer über 1000 m:
> - Sprinter A: 9,5 m/s
> - Sprinter B: 7 m/s, aber 250 m Vorsprung
>
> Zeige eine Tabelle mit den gelaufenen Strecken pro Sekunde. Abbruch wenn einer im Ziel ist.

> [!example] Aufgabe 11 - Multiplikationsmatrix
> Zeige eine 10×10-Matrix. Nach Eingabe einer Ziffer (2-9) werden alle Zahlen markiert (`*`), die:
> - die Ziffer enthalten, oder
> - durch die Zahl teilbar sind, oder
> - deren Quersumme der Zahl entspricht

> [!example] Aufgabe 12 - Römische Zahlen
> Konsolenanwendung: Eingabe einer römischen Zahl → Ausgabe als Dezimalzahl (bis 3999).
>
> **Regeln:**
> | Zeichen | Wert |
> | ------- | ---- |
> | I       | 1    |
> | V       | 5    |
> | X       | 10   |
> | L       | 50   |
> | C       | 100  |
> | D       | 500  |
> | M       | 1000 |
>
> - **Additionsregel:** Kleinere folgen größeren → addieren (XVII = 17)
> - **Subtraktionsregel:** Kleinere **vor** größeren → subtrahieren (IV = 4)
> - Max. 3 gleiche Zeichen hintereinander
> - V, L, D stehen nie mehrfach

> [!example] Aufgabe 13 - Erweiterung Getränkeautomat
> Erweitere den Getränkeautomaten (→ [[Verzweigungen und Funktionen]]) mit einer Schleife, sodass der Benutzer mehrere Getränke hintereinander wählen kann.

---

## Siehe auch

- [[Python Grundlagen]]
- [[Datentypen und Operatoren]]
- [[Verzweigungen und Funktionen]]
