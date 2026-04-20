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

> [!success] Lösung
> **Teil 1: Eingabe mit Anzeige der Liste**
> ```python
> anzahl = 6
> i = 0
> summe = 0
> temperaturen = []
>
> while i < anzahl:
>     print(f"Geben Sie die {i + 1}. Temperatur in °C ein: ")
>     temperatur = float(input())
>     temperaturen.append(temperatur)
>     summe = summe + temperatur
>     i = i + 1
>
> # Temperaturen aus der Liste anzeigen
> print("\nEingegebene Temperaturen:")
> for j in range(len(temperaturen)):
>     print(f"  Temperatur {j + 1}: {temperaturen[j]:.1f} °C")
>
> durchschnitt = summe / anzahl
> print(f"\nDurchschnitt: {durchschnitt:.2f} °C")
> ```
>
> **Teil 2: Zufallszahlen, erhöhte Anzahl**
> ```python
> import random
>
> anzahl = 20
> summe = 0
> temperaturen = []
>
> for i in range(anzahl):
>     temperatur = round(random.uniform(-15.0, 40.0), 1)
>     temperaturen.append(temperatur)
>     summe += temperatur
>
> print("Gemessene Temperaturen:")
> for i in range(len(temperaturen)):
>     print(f"  Messung {i + 1:2d}: {temperaturen[i]:5.1f} °C")
>
> durchschnitt = summe / anzahl
> print(f"\nDurchschnitt aus {anzahl} Messungen: {durchschnitt:.2f} °C")
> ```

> [!example] Aufgabe 2 - Gerade Zahlen
> Gib alle geraden Zahlen von 0 bis 20 aus.
> - a) Welchen Schleifentyp brauchst du?
> - b) Erweitere: Der Benutzer bestimmt die Anzahl
> - c) Gib auch die Summe aller geraden Zahlen aus

> [!success] Lösung
> **a) Gerade Zahlen 0–20 (for-Schleife mit Schrittweite 2)**
> ```python
> # Eine for-Schleife mit range und Schrittweite 2 ist am einfachsten
> for i in range(0, 21, 2):
>     print(i)
> # Ausgabe: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
>
> # Alternativ mit while und Modulo:
> i = 0
> while i <= 20:
>     if i % 2 == 0:
>         print(i)
>     i += 1
> ```
>
> **b) Benutzer bestimmt die Obergrenze**
> ```python
> grenze = int(input("Bis zu welcher Zahl sollen gerade Zahlen ausgegeben werden? "))
>
> for i in range(0, grenze + 1, 2):
>     print(i)
> ```
>
> **c) Mit Summe**
> ```python
> grenze = int(input("Bis zu welcher Zahl? "))
> summe = 0
>
> for i in range(0, grenze + 1, 2):
>     print(i)
>     summe += i
>
> print(f"\nSumme aller geraden Zahlen von 0 bis {grenze}: {summe}")
> ```

> [!example] Aufgabe 3 - Sternfigur
> Gib mit Schleifen folgende Figur aus (pro Schreibvorgang nur ein `*`):
> ```
> *******
> *****
>  ***
>   *
> ```

> [!success] Lösung
> ```python
> # Zeile 0: 0 Leerzeichen, 7 Sterne
> # Zeile 1: 0 Leerzeichen, 5 Sterne
> # Zeile 2: 1 Leerzeichen, 3 Sterne
> # Zeile 3: 2 Leerzeichen, 1 Stern
> #
> # Muster: Leerzeichen = max(0, zeile - 1), Sterne = 7 - 2*zeile
>
> zeilen = 4
> for zeile in range(zeilen):
>     sterne = 7 - 2 * zeile
>     leerzeichen = zeile - 1 if zeile > 0 else 0
>
>     # Leerzeichen drucken
>     for _ in range(leerzeichen):
>         print(" ", end="")
>
>     # Sterne drucken
>     for _ in range(sterne):
>         print("*", end="")
>
>     print()  # Zeilenumbruch
> ```
> Ausgabe:
> ```
> *******
> *****
>  ***
>   *
> ```

> [!example] Aufgabe 4 - Fakultät
> Berechne die Fakultät einer eingegebenen Zahl.
> Hinweis: `0! = 1`, `5! = 5 × 4 × 3 × 2 × 1 = 120`

> [!success] Lösung
> **Iterative Lösung (mit Schleife)**
> ```python
> n = int(input("Zahl für Fakultät eingeben: "))
>
> if n < 0:
>     print("Fehler: Fakultät ist nur für nicht-negative Zahlen definiert.")
> else:
>     ergebnis = 1
>     for i in range(2, n + 1):
>         ergebnis *= i
>     print(f"{n}! = {ergebnis}")
> ```
>
> **Rekursive Lösung**
> ```python
> def fakultaet(n):
>     if n < 0:
>         raise ValueError("Fakultät nur für n >= 0 definiert")
>     if n == 0 or n == 1:
>         return 1
>     return n * fakultaet(n - 1)
>
> n = int(input("Zahl für Fakultät eingeben: "))
> print(f"{n}! = {fakultaet(n)}")
> ```
>
> Beispielausgabe für `n = 5`:
> ```
> 5! = 120
> ```

> [!example] Aufgabe 5 - Zahlenfolgen
> Programmiere Schleifen für folgende Folgen:
> - a) `99, 96, 93, ... 12, 9`
> - b) `1, 4, 9, 16, 25, ... 361, 400`
> - c) `2, 6, 10, 14, ... 98, 102`
> - d) `4, 16, 36, 64, 100 ... 900, 1024`
> - e) `2, 4, 8, 16, 32, ..., 16384, 32768`

> [!success] Lösung
> **a) 99, 96, 93, ... 9 — rückwärts in 3er-Schritten**
> ```python
> # for-Schleife
> for i in range(99, 8, -3):
>     print(i, end=", ")
>
> # while-Schleife
> i = 99
> while i >= 9:
>     print(i, end=", ")
>     i -= 3
> ```
>
> **b) 1, 4, 9, 16, ... 400 — Quadratzahlen**
> ```python
> # for-Schleife
> for i in range(1, 21):
>     print(i ** 2, end=", ")
>
> # while-Schleife
> i = 1
> while i <= 20:
>     print(i ** 2, end=", ")
>     i += 1
> ```
>
> **c) 2, 6, 10, 14, ... 102 — Schrittweite 4**
> ```python
> # for-Schleife
> for i in range(2, 103, 4):
>     print(i, end=", ")
>
> # while-Schleife
> i = 2
> while i <= 102:
>     print(i, end=", ")
>     i += 4
> ```
>
> **d) 4, 16, 36, 64, ... 1024 — Quadrate gerader Zahlen**
> ```python
> # for-Schleife (gerade Zahlen quadrieren: 2²=4, 4²=16, 6²=36, ...)
> for i in range(2, 34, 2):
>     print(i ** 2, end=", ")
>
> # while-Schleife
> i = 2
> while i <= 32:
>     print(i ** 2, end=", ")
>     i += 2
> ```
>
> **e) 2, 4, 8, 16, ... 32768 — Potenzen von 2**
> ```python
> # for-Schleife
> for i in range(1, 16):
>     print(2 ** i, end=", ")
>
> # while-Schleife
> wert = 2
> while wert <= 32768:
>     print(wert, end=", ")
>     wert *= 2
> ```

> [!example] Aufgabe 6 - Einmaleins
> Gib das kleine Einmaleins aus (1×1 bis 10×10) als formatierte Tabelle.

> [!success] Lösung
> ```python
> # Kopfzeile
> print("   ", end="")
> for j in range(1, 11):
>     print(f"{j:4d}", end="")
> print()
> print("   " + "-" * 40)
>
> # Tabellenzeilen
> for i in range(1, 11):
>     print(f"{i:2d}|", end="")
>     for j in range(1, 11):
>         print(f"{i * j:4d}", end="")
>     print()
> ```
> Ausgabe (Ausschnitt):
> ```
>       1   2   3   4   5   6   7   8   9  10
>    ----------------------------------------
>  1|   1   2   3   4   5   6   7   8   9  10
>  2|   2   4   6   8  10  12  14  16  18  20
>  3|   3   6   9  12  15  18  21  24  27  30
> ...
> 10|  10  20  30  40  50  60  70  80  90 100
> ```

> [!example] Aufgabe 7 - Quadrat zeichnen
> Eingabe: Seitenlänge. Ausgabe: Quadrat im Textmodus.
> ```
> Anzahl: 3
>
> * * *
> *   *
> * * *
> ```

> [!success] Lösung
> ```python
> n = int(input("Seitenlänge des Quadrats: "))
>
> for zeile in range(n):
>     for spalte in range(n):
>         # Rand: erste/letzte Zeile oder erste/letzte Spalte
>         if zeile == 0 or zeile == n - 1 or spalte == 0 or spalte == n - 1:
>             print("*", end=" ")
>         else:
>             print(" ", end=" ")
>     print()
> ```
> Ausgabe für `n = 5`:
> ```
> * * * * *
> *       *
> *       *
> *       *
> * * * * *
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

> [!success] Lösung
> ```python
> h = int(input("Treppenhöhe: "))
> b = int(input("Stufenbreite: "))
>
> gesamtbreite = h * b
>
> for stufe in range(1, h + 1):
>     sterne = stufe * b
>     leerzeichen = gesamtbreite - sterne
>
>     for _ in range(leerzeichen):
>         print(" ", end="")
>     for _ in range(sterne):
>         print("*", end="")
>     print()
> ```
> Ausgabe für `h=4, b=3`:
> ```
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

> [!success] Lösung
> ```python
> zahl = int(input("Zahl eingeben: "))
>
> # Vorzeichen ignorieren
> n = abs(zahl)
> quersumme = 0
>
> while n > 0:
>     quersumme += n % 10   # letzte Ziffer addieren
>     n = n // 10           # letzte Ziffer abschneiden
>
> print(f"Quersumme von {zahl}: {quersumme}")
> ```
> Beispiel für `12345`:
> - Schritt 1: `12345 % 10 = 5`, `n = 1234`
> - Schritt 2: `1234 % 10 = 4`, `n = 123`
> - Schritt 3: `123 % 10 = 3`, `n = 12`
> - Schritt 4: `12 % 10 = 2`, `n = 1`
> - Schritt 5: `1 % 10 = 1`, `n = 0`
> - Quersumme: `5 + 4 + 3 + 2 + 1 = 15`

> [!example] Aufgabe 10 - Sprinter-Wettkampf
> Zwei Läufer über 1000 m:
> - Sprinter A: 9,5 m/s
> - Sprinter B: 7 m/s, aber 250 m Vorsprung
>
> Zeige eine Tabelle mit den gelaufenen Strecken pro Sekunde. Abbruch wenn einer im Ziel ist.

> [!success] Lösung
> ```python
> strecke = 1000
> geschwindigkeit_a = 9.5
> geschwindigkeit_b = 7.0
> vorsprung_b = 250.0
>
> position_a = 0.0
> position_b = vorsprung_b
> sekunde = 0
>
> print(f"{'Sek':>5} | {'Sprinter A':>12} | {'Sprinter B':>12}")
> print("-" * 38)
> print(f"{'0':>5} | {position_a:>10.1f} m | {position_b:>10.1f} m")
>
> while position_a < strecke and position_b < strecke:
>     sekunde += 1
>     position_a += geschwindigkeit_a
>     position_b += geschwindigkeit_b
>
>     # Positionen auf max. Streckenlänge begrenzen
>     position_a = min(position_a, strecke)
>     position_b = min(position_b, strecke)
>
>     print(f"{sekunde:>5} | {position_a:>10.1f} m | {position_b:>10.1f} m")
>
>     if position_a >= strecke or position_b >= strecke:
>         break
>
> print()
> if position_a >= strecke and position_b >= strecke:
>     print("Gleichzeitig im Ziel!")
> elif position_a >= strecke:
>     print(f"Sprinter A gewinnt nach {sekunde} Sekunden!")
> else:
>     print(f"Sprinter B gewinnt nach {sekunde} Sekunden!")
> ```
> Ausgabe (Ausschnitt):
> ```
>  Sek |   Sprinter A |   Sprinter B
> --------------------------------------
>    0 |        0.0 m |      250.0 m
>    1 |        9.5 m |      257.0 m
>    2 |       19.0 m |      264.0 m
> ...
>   79 |      750.5 m |      803.0 m
>   80 |      760.0 m |      810.0 m
> ...
> Sprinter B gewinnt nach 107 Sekunden!
> ```

> [!example] Aufgabe 11 - Multiplikationsmatrix
> Zeige eine 10×10-Matrix. Nach Eingabe einer Ziffer (2-9) werden alle Zahlen markiert (`*`), die:
> - die Ziffer enthalten, oder
> - durch die Zahl teilbar sind, oder
> - deren Quersumme der Zahl entspricht

> [!success] Lösung
> ```python
> def quersumme(n):
>     """Berechnet die Quersumme einer Zahl."""
>     q = 0
>     while n > 0:
>         q += n % 10
>         n //= 10
>     return q
>
> def ist_markiert(produkt, ziffer):
>     """Prüft ob ein Produkt markiert werden soll."""
>     # Kriterium 1: Ziffer ist im Produkt enthalten
>     if str(ziffer) in str(produkt):
>         return True
>     # Kriterium 2: Produkt ist durch die Ziffer teilbar
>     if produkt % ziffer == 0:
>         return True
>     # Kriterium 3: Quersumme des Produkts ist gleich der Ziffer
>     if quersumme(produkt) == ziffer:
>         return True
>     return False
>
> ziffer = int(input("Ziffer eingeben (2-9): "))
> while ziffer < 2 or ziffer > 9:
>     ziffer = int(input("Ungültige Eingabe. Ziffer (2-9): "))
>
> # Kopfzeile
> print(f"\nMarkiert (*) = enthält {ziffer} | teilbar durch {ziffer} | Quersumme = {ziffer}\n")
> print("    ", end="")
> for j in range(1, 11):
>     print(f"{j:5d}", end="")
> print()
> print("    " + "-" * 50)
>
> for i in range(1, 11):
>     print(f"{i:3d}|", end="")
>     for j in range(1, 11):
>         produkt = i * j
>         if ist_markiert(produkt, ziffer):
>             print(f"{'*':>5}", end="")
>         else:
>             print(f"{produkt:5d}", end="")
>     print()
> ```
> Beispielausgabe für Ziffer `3`:
> ```
>        1    2    3    4    5    6    7    8    9   10
>     --------------------------------------------------
>   1|   1    2    *    4    5    *    7    8    *   10
>   2|   2    4    *    8   10   12    *   16   18   20
>   3|   *    *    *    *   15   18   21   *    *    *
> ...
> ```

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

> [!success] Lösung
> ```python
> def roemisch_zu_dezimal(roemisch):
>     """Wandelt eine römische Zahl in eine Dezimalzahl um."""
>     werte = {
>         'I': 1, 'V': 5, 'X': 10, 'L': 50,
>         'C': 100, 'D': 500, 'M': 1000
>     }
>
>     roemisch = roemisch.upper().strip()
>
>     # Validierung: nur gültige Zeichen
>     for zeichen in roemisch:
>         if zeichen not in werte:
>             raise ValueError(f"Ungültiges Zeichen: '{zeichen}'")
>
>     # Validierung: V, L, D nicht mehrfach
>     for zeichen in ['V', 'L', 'D']:
>         if roemisch.count(zeichen) > 1:
>             raise ValueError(f"'{zeichen}' darf nicht mehrfach vorkommen")
>
>     # Validierung: max. 3 gleiche hintereinander
>     for i in range(len(roemisch) - 3):
>         if roemisch[i] == roemisch[i+1] == roemisch[i+2] == roemisch[i+3]:
>             raise ValueError("Mehr als 3 gleiche Zeichen hintereinander")
>
>     # Umrechnung: von rechts nach links aufsummieren
>     ergebnis = 0
>     vorheriger_wert = 0
>
>     for i in range(len(roemisch) - 1, -1, -1):
>         aktueller_wert = werte[roemisch[i]]
>         if aktueller_wert < vorheriger_wert:
>             ergebnis -= aktueller_wert   # Subtraktionsregel
>         else:
>             ergebnis += aktueller_wert   # Additionsregel
>         vorheriger_wert = aktueller_wert
>
>     if ergebnis < 1 or ergebnis > 3999:
>         raise ValueError(f"Ergebnis {ergebnis} liegt außerhalb des gültigen Bereichs (1–3999)")
>
>     return ergebnis
>
> # Hauptprogramm
> while True:
>     eingabe = input("Römische Zahl eingeben (oder 'q' zum Beenden): ")
>     if eingabe.lower() == 'q':
>         break
>     try:
>         dezimal = roemisch_zu_dezimal(eingabe)
>         print(f"{eingabe.upper()} = {dezimal}")
>     except ValueError as e:
>         print(f"Fehler: {e}")
> ```
> Beispiele:
> ```
> Römische Zahl: IV
> IV = 4
> Römische Zahl: XVII
> XVII = 17
> Römische Zahl: MCMXCIX
> MCMXCIX = 1999
> Römische Zahl: MMMDCCCLXXXVIII
> MMMDCCCLXXXVIII = 3888
> ```

> [!example] Aufgabe 13 - Erweiterung Getränkeautomat
> Erweitere den Getränkeautomaten (→ [[Verzweigungen und Funktionen]]) mit einer Schleife, sodass der Benutzer mehrere Getränke hintereinander wählen kann.

> [!success] Lösung
> ```python
> def zeige_menu():
>     print("\n--- Getränkeautomat ---")
>     print("1 - Wasser       (1,00 €)")
>     print("2 - Cola         (1,50 €)")
>     print("3 - Saft         (1,80 €)")
>     print("4 - Kaffee       (2,00 €)")
>     print("0 - Beenden")
>
> def berechne_preis(auswahl):
>     preise = {
>         1: ("Wasser", 1.00),
>         2: ("Cola",   1.50),
>         3: ("Saft",   1.80),
>         4: ("Kaffee", 2.00),
>     }
>     return preise.get(auswahl, None)
>
> gesamtbetrag = 0.0
> anzahl_kaeufe = 0
>
> while True:
>     zeige_menu()
>     try:
>         auswahl = int(input("Ihre Wahl: "))
>     except ValueError:
>         print("Bitte eine gültige Zahl eingeben.")
>         continue
>
>     if auswahl == 0:
>         break
>
>     ergebnis = berechne_preis(auswahl)
>     if ergebnis is None:
>         print("Ungültige Auswahl. Bitte 0–4 eingeben.")
>         continue
>
>     name, preis = ergebnis
>     einwurf = float(input(f"{name} kostet {preis:.2f} €. Betrag einwerfen: "))
>
>     if einwurf < preis:
>         print(f"Nicht genug Geld! Fehlend: {preis - einwurf:.2f} €")
>         continue
>
>     rueckgeld = einwurf - preis
>     print(f"{name} wird ausgegeben.")
>     if rueckgeld > 0:
>         print(f"Rückgeld: {rueckgeld:.2f} €")
>
>     gesamtbetrag += preis
>     anzahl_kaeufe += 1
>
> print(f"\nSitzung beendet.")
> print(f"Gekaufte Getränke: {anzahl_kaeufe}")
> print(f"Gesamtumsatz:      {gesamtbetrag:.2f} €")
> ```
> Beispielablauf:
> ```
> --- Getränkeautomat ---
> 1 - Wasser       (1,00 €)
> 2 - Cola         (1,50 €)
> 3 - Saft         (1,80 €)
> 4 - Kaffee       (2,00 €)
> 0 - Beenden
> Ihre Wahl: 2
> Cola kostet 1,50 €. Betrag einwerfen: 2.00
> Cola wird ausgegeben.
> Rückgeld: 0,50 €
> ...
> Sitzung beendet.
> Gekaufte Getränke: 3
> Gesamtumsatz:      5,30 €
> ```

---

## Siehe auch

- [[Python Grundlagen]]
- [[Datentypen und Operatoren]]
- [[Verzweigungen und Funktionen]]
