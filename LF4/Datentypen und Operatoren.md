---
fach: LF4
thema: Datentypen und Operatoren
tags: [lf4, python, datentypen, operatoren]
datum: 2026-04-20
typ: notiz
---

# Datentypen und Operatoren

## Numerische Datentypen

| Datentyp   | Beschreibung             | Beispiel                      |
| ---------- | ------------------------ | ----------------------------- |
| `int`      | Ganzzahl                 | `x = 42`                     |
| `float`    | Gleitkommazahl           | `x = 3.14`                   |
| `complex`  | Komplexe Zahl            | `x = 2 + 3j`                 |
| `str`      | Zeichenkette             | `x = "Hallo"`                |
| `bool`     | Wahrheitswert            | `x = True`                   |

### Typkonvertierung

```python
x = "42"
y = int(x)        # str -> int:    42
z = float(x)      # str -> float:  42.0
w = str(42)       # int -> str:    "42"

# Typ prüfen
print(type(x))    # <class 'str'>
print(type(y))    # <class 'int'>
```

> [!info] Python erkennt Datentypen automatisch (dynamische Typisierung), aber bei `input()` muss manuell konvertiert werden.

---

## Arithmetische Operatoren

| Operator | Beschreibung            | Beispiel       | Ergebnis |
| -------- | ----------------------- | -------------- | -------- |
| `+`      | Addition                | `5 + 3`        | `8`      |
| `-`      | Subtraktion             | `5 - 3`        | `2`      |
| `*`      | Multiplikation          | `5 * 3`        | `15`     |
| `/`      | Division                | `7 / 2`        | `3.5`    |
| `//`     | Ganzzahldivision        | `7 // 2`       | `3`      |
| `%`      | Modulo (Rest)           | `7 % 2`        | `1`      |
| `**`     | Potenz                  | `2 ** 3`       | `8`      |

### Modulo-Beispiele

```python
120 % 10   # = 0    (120 / 10 = 12, Rest 0)
14 % 3     # = 2    (14 / 3 = 4, Rest 2)
61 % 17    # = 10   (61 / 17 = 3, Rest 10)
243 % 13   # = 9    (243 / 13 = 18, Rest 9)
4 % 5      # = 4    (4 / 5 = 0, Rest 4)
5 % 4      # = 1    (5 / 4 = 1, Rest 1)
```

> [!tip] Modulo ist nützlich um zu prüfen, ob eine Zahl gerade ist: `zahl % 2 == 0`

### Operatorpriorität (absteigend)

| Priorität | Operator         |
| --------- | ---------------- |
| 1 (hoch)  | `**`             |
| 2         | `*`, `/`, `//`, `%` |
| 3 (niedrig) | `+`, `-`       |

Klammern `()` haben immer höchste Priorität.

---

## Zuweisungsoperatoren

| Operator | Langform          | Beispiel   | Bedeutung         |
| -------- | ----------------- | ---------- | ----------------- |
| `=`      | Zuweisung         | `a = 5`    | a ist 5           |
| `+=`     | `a = a + b`       | `a += 3`   | a ist jetzt 8     |
| `-=`     | `a = a - b`       | `a -= 2`   | a ist jetzt 6     |
| `*=`     | `a = a * b`       | `a *= 4`   | a ist jetzt 24    |
| `/=`     | `a = a / b`       | `a /= 3`   | a ist jetzt 8.0   |
| `//=`    | `a = a // b`      | `a //= 3`  | Ganzzahldivision  |
| `%=`     | `a = a % b`       | `a %= 3`   | Rest der Division |
| `**=`    | `a = a ** b`      | `a **= 2`  | Potenz            |

> [!warning] In Python gibt es kein `++` oder `--` wie in C/Java! Stattdessen: `a += 1`

---

## Vergleichsoperatoren

| Operator | Beschreibung        | Beispiel     | Ergebnis |
| -------- | ------------------- | ------------ | -------- |
| `==`     | Gleich              | `5 == 5`     | `True`   |
| `!=`     | Ungleich            | `5 != 3`     | `True`   |
| `>`      | Größer als          | `5 > 3`      | `True`   |
| `<`      | Kleiner als         | `5 < 3`      | `False`  |
| `>=`     | Größer oder gleich  | `5 >= 5`     | `True`   |
| `<=`     | Kleiner oder gleich | `3 <= 5`     | `True`   |

---

## Logische (Boolesche) Operatoren

| Operator | Beschreibung          | Beispiel                       |
| -------- | --------------------- | ------------------------------ |
| `and`    | Beide wahr            | `x > 0 and x < 10`            |
| `or`     | Mindestens eines wahr | `x < 0 or x > 10`             |
| `not`    | Negation              | `not x > 5`                   |

### Wahrheitstabelle

| `a`     | `b`     | `a and b` | `a or b` | `not a` |
| ------- | ------- | --------- | -------- | ------- |
| `True`  | `True`  | `True`    | `True`   | `False` |
| `True`  | `False` | `False`   | `True`   | `False` |
| `False` | `True`  | `False`   | `True`   | `True`  |
| `False` | `False` | `False`   | `False`  | `True`  |

---

## Bit-Operatoren

| Operator | Beschreibung       | Beispiel     |
| -------- | ------------------ | ------------ |
| `~`      | Bitweises NOT      | `~5`         |
| `&`      | Bitweises AND      | `5 & 3`      |
| `\|`     | Bitweises OR       | `5 \| 3`     |
| `^`      | Bitweises XOR      | `5 ^ 3`      |
| `<<`     | Links-Shift        | `5 << 1`     |
| `>>`     | Rechts-Shift       | `5 >> 1`     |

---

## Identity- und Membership-Operatoren

```python
# Identity: Prüft ob gleiche Objekt-ID
a = [1, 2]
b = a
print(a is b)       # True  (selbes Objekt)
print(a is not b)   # False

# Membership: Prüft ob Element enthalten
print(3 in [1, 2, 3])       # True
print(4 not in [1, 2, 3])   # True
print("a" in "Hallo")       # True
```

---

## Aufgaben: Operatoren

> [!example] Aufgabe 1 - Modulo berechnen
> Berechne schriftlich, dann prüfe mit Python:
>
> | Anweisung          | Ergebnis |
> | ------------------ | -------- |
> | `120 % 10`         |          |
> | `14 % 3`           |          |
> | `61 % 17`          |          |
> | `243 % 13`         |          |
> | `4 % 5`            |          |
> | `5 % 4`            |          |
> | `-5 % 4`           |          |
> | `-5 % -4`          |          |
> | `5 % -4`           |          |

> [!success] Lösung – Aufgabe 1
> | Anweisung          | Ergebnis | Herleitung                          |
> | ------------------ | -------- | ----------------------------------- |
> | `120 % 10`         | `0`      | 120 / 10 = 12, Rest **0**           |
> | `14 % 3`           | `2`      | 14 / 3 = 4, Rest **2**              |
> | `61 % 17`          | `10`     | 61 / 17 = 3, Rest **10**            |
> | `243 % 13`         | `9`      | 243 / 13 = 18, Rest **9**           |
> | `4 % 5`            | `4`      | 4 / 5 = 0, Rest **4**              |
> | `5 % 4`            | `1`      | 5 / 4 = 1, Rest **1**              |
> | `-5 % 4`           | `3`      | Python: Ergebnis hat Vorzeichen des Divisors: -5 = (-2)*4 + **3** |
> | `-5 % -4`          | `-1`     | Python: Ergebnis hat Vorzeichen des Divisors: -5 = 1*(-4) + **-1** |
> | `5 % -4`           | `-3`     | Python: Ergebnis hat Vorzeichen des Divisors: 5 = (-1)*(-4) + **-3** |
>
> Hinweis: In Python gilt immer `a == (a // b) * b + (a % b)`. Bei negativen Zahlen richtet sich das Vorzeichen des Ergebnisses nach dem **Divisor**.

> [!example] Aufgabe 2 - Zuweisungsoperatoren (a = 11)
> Berechne schrittweise, was `a` nach jeder Zeile ist:
>
> ```python
> a = 11
> a = a % 10         # a = ?
> a = a % a           # a = ?
> a = a * a           # a = ?
> a -= a / a          # a = ?
> a += a + a          # a = ?
> a += a * a + a      # a = ?
> a = a + a * 3 + a   # a = ?
> a = (a - 1) / 2 + 7 # a = ?
> ```

> [!success] Lösung – Aufgabe 2
> | Zeile                    | Berechnung                        | Wert von `a` |
> | ------------------------ | --------------------------------- | ------------ |
> | `a = 11`                 | Startwert                         | `11`         |
> | `a = a % 10`             | 11 % 10 = **1**                   | `1`          |
> | `a = a % a`              | 1 % 1 = **0**                     | `0`          |
> | `a = a * a`              | 0 * 0 = **0**                     | `0`          |
> | `a -= a / a`             | 0 / 0 → **ZeroDivisionError!**    | Fehler       |
>
> Ab `a -= a / a` tritt eine **ZeroDivisionError**-Exception auf, da `a = 0` ist. Das Programm bricht hier ab.
>
> Wenn man die Division überspringt und mit `a = 0` weitermacht (zur Demonstration):
>
> | Zeile (hypothetisch, a=1 angenommen) | Berechnung                | Wert von `a` |
> | ------------------------------------- | ------------------------- | ------------ |
> | `a -= a / a`   (mit a=1)             | 1 - 1/1 = 1 - 1.0 = **0.0** | `0.0`     |
> | `a += a + a`   (mit a=0.0)           | 0.0 + 0.0 + 0.0 = **0.0**   | `0.0`     |
>
> Korrekte schrittweise Ausführung bis zum Fehler:
> ```python
> a = 11       # a = 11
> a = a % 10   # a = 1
> a = a % a    # a = 0
> a = a * a    # a = 0
> a -= a / a   # ZeroDivisionError: division by zero
> ```

> [!example] Aufgabe 3 - Buchaufgaben (S. 544)
> 1. Lege Variablen für Mitarbeiterdaten an und bestimme den Datentyp:
>
>    | Feld                    | Wert                          | Typ     |
>    | ----------------------- | ----------------------------- | ------- |
>    | Laufende Nummer         | 3                             | `int`   |
>    | Name des Mitarbeiters   | Müller, Karl                  | `str`   |
>    | Alter                   | 34                            | `int`   |
>    | Adresse                 | Mühlenweg 1A, 01069 Dresden   | `str`   |
>    | Telefonnummer           | 0177-1234567                  | `str`   |
>    | Beruf                   | Fachinformatiker              | `str`   |
>    | Verheiratet, Steuer     | Ja, 3                         | `bool`, `int` |
>    | Kinder                  | 2                             | `int`   |
>    | Lohn/Gehalt             | 2870.00                       | `float` |
>
> 2. Modulo-Aufgaben: `123 % 7`, `12345 % 100`, `121 % 11`, `8 % 2`, `9 % 2`, `3 % 5`
> 3. Programm: Durchschnittsverbrauch Kraftstoff auf 100 km berechnen
> 4. Programm: Elektrischen Widerstand berechnen (U/I = R)
> 5. Programm: Speicherplatzbedarf von Bildern in GiB berechnen

> [!success] Lösung – Aufgabe 3
>
> **Teilaufgabe 1 – Variablendeklaration:**
>
> ```python
> laufende_nummer = 3                          # int
> name           = "Müller, Karl"              # str
> alter          = 34                          # int
> adresse        = "Mühlenweg 1A, 01069 Dresden"  # str
> telefon        = "0177-1234567"              # str  (Bindestriche -> kein int!)
> beruf          = "Fachinformatiker"          # str
> verheiratet    = True                        # bool
> steuerklasse   = 3                           # int
> kinder         = 2                           # int
> lohn           = 2870.00                     # float
> ```
>
> **Teilaufgabe 2 – Modulo-Ergebnisse:**
>
> | Ausdruck        | Ergebnis | Herleitung                     |
> | --------------- | -------- | ------------------------------ |
> | `123 % 7`       | `4`      | 123 / 7 = 17, Rest **4**       |
> | `12345 % 100`   | `45`     | 12345 / 100 = 123, Rest **45** |
> | `121 % 11`      | `0`      | 121 / 11 = 11, Rest **0**      |
> | `8 % 2`         | `0`      | 8 / 2 = 4, Rest **0** (gerade) |
> | `9 % 2`         | `1`      | 9 / 2 = 4, Rest **1** (ungerade) |
> | `3 % 5`         | `3`      | 3 / 5 = 0, Rest **3**          |
>
> **Teilaufgabe 3 – Kraftstoffverbrauch auf 100 km:**
>
> ```python
> # Kraftstoffverbrauch in L/100km berechnen
> distanz_km    = float(input("Gefahrene Strecke (km): "))
> verbrauch_l   = float(input("Verbrauchter Kraftstoff (Liter): "))
>
> verbrauch_100km = (verbrauch_l / distanz_km) * 100
>
> print(f"Durchschnittsverbrauch: {verbrauch_100km:.2f} L/100km")
> ```
>
> **Teilaufgabe 4 – Elektrischen Widerstand berechnen (R = U / I):**
>
> ```python
> # Ohmsches Gesetz: R = U / I
> spannung_V  = float(input("Spannung U (Volt): "))
> stromstaerke_A = float(input("Stromstärke I (Ampere): "))
>
> widerstand_Ohm = spannung_V / stromstaerke_A
>
> print(f"Widerstand R = {widerstand_Ohm:.2f} Ohm")
> ```
>
> **Teilaufgabe 5 – Speicherplatzbedarf von Bildern in GiB:**
>
> ```python
> # Speicherbedarf: Breite * Höhe * Farbtiefe (Bit) / 8 -> Byte -> GiB
> breite_px    = int(input("Bildbreite (Pixel): "))
> hoehe_px     = int(input("Bildhöhe (Pixel): "))
> farbtiefe_bit = int(input("Farbtiefe (Bit, z.B. 24 für RGB): "))
> anzahl_bilder = int(input("Anzahl der Bilder: "))
>
> groesse_byte = breite_px * hoehe_px * (farbtiefe_bit / 8) * anzahl_bilder
> groesse_gib  = groesse_byte / (1024 ** 3)   # 1 GiB = 2^30 Byte
>
> print(f"Speicherbedarf: {groesse_gib:.4f} GiB")
> ```

> [!example] Aufgabe 4 - Praxisaufgaben
> 1. **Übertragungsrate:** Berechne die Zeit für eine Datenübertragung (Eingabe: MB + Kbit/s, Ausgabe: Minuten)
> 2. **Nettolohn:** Berechne aus dem Bruttolohn den Nettolohn (Steuerklasse I: 30%, + KV, RV, AV)
> 3. **Zinsrechnung:** Berechne den Zinsbetrag (Eingabe: Geldbetrag + Zinssatz)

> [!success] Lösung – Aufgabe 4
>
> **Teilaufgabe 1 – Übertragungszeit berechnen:**
>
> ```python
> # Übertragungszeit: t = Datenmenge / Übertragungsrate
> # Einheiten: MB -> Mbit (1 MB = 8 Mbit), Kbit/s -> Mbit/s (/1000)
> datenmenge_mb  = float(input("Datenmenge (MB): "))
> rate_kbit_s    = float(input("Übertragungsrate (Kbit/s): "))
>
> datenmenge_kbit = datenmenge_mb * 8 * 1000   # MB -> Kbit (1 MB = 8 Mbit = 8000 Kbit)
> zeit_sekunden   = datenmenge_kbit / rate_kbit_s
> zeit_minuten    = zeit_sekunden / 60
>
> print(f"Übertragungszeit: {zeit_sekunden:.2f} Sekunden ({zeit_minuten:.2f} Minuten)")
> ```
>
> Beispiel: 100 MB bei 512 Kbit/s → 100 * 8000 / 512 = 1562,5 s ≈ 26,04 Minuten
>
> **Teilaufgabe 2 – Nettolohn berechnen (Steuerklasse I):**
>
> ```python
> # Abzüge Steuerklasse I (Näherungswerte):
> #   Lohnsteuer:           19,0 %
> #   Solidaritätszuschlag:  5,5 % der Lohnsteuer (= 1,045 % vom Brutto)
> #   Krankenversicherung:   7,3 %
> #   Rentenversicherung:    9,3 %
> #   Arbeitslosenversicherung: 1,3 %
> brutto = float(input("Bruttolohn (€): "))
>
> lohnsteuer   = brutto * 0.190
> soli         = lohnsteuer * 0.055
> kv           = brutto * 0.073
> rv           = brutto * 0.093
> av           = brutto * 0.013
>
> gesamt_abzug = lohnsteuer + soli + kv + rv + av
> netto        = brutto - gesamt_abzug
>
> print(f"Bruttolohn:            {brutto:>10.2f} €")
> print(f"  - Lohnsteuer:        {lohnsteuer:>10.2f} €")
> print(f"  - Solidaritätszuschlag: {soli:>7.2f} €")
> print(f"  - Krankenversicherung: {kv:>8.2f} €")
> print(f"  - Rentenversicherung:  {rv:>8.2f} €")
> print(f"  - Arbeitslosenvers.:   {av:>8.2f} €")
> print(f"Gesamtabzüge:          {gesamt_abzug:>10.2f} €")
> print(f"Nettolohn:             {netto:>10.2f} €")
> ```
>
> **Teilaufgabe 3 – Zinsrechnung:**
>
> ```python
> # Einfache Zinsrechnung: Z = K * p / 100
> # Mit Laufzeit: Z = K * p * t / 100
> kapital    = float(input("Kapital (€): "))
> zinssatz   = float(input("Zinssatz (% pro Jahr): "))
> laufzeit   = float(input("Laufzeit (Jahre): "))
>
> zinsbetrag     = kapital * zinssatz * laufzeit / 100
> endkapital     = kapital + zinsbetrag
>
> print(f"Kapital:      {kapital:.2f} €")
> print(f"Zinssatz:     {zinssatz:.2f} % p.a.")
> print(f"Laufzeit:     {laufzeit:.1f} Jahre")
> print(f"Zinsbetrag:   {zinsbetrag:.2f} €")
> print(f"Endkapital:   {endkapital:.2f} €")
> ```

---

## Fehlerbehandlung mit try/except

```python
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 10 / zahl
    print(f"Ergebnis: {ergebnis}")
except ValueError:
    print("Das war keine gültige Zahl!")
except ZeroDivisionError:
    print("Division durch 0 ist nicht erlaubt!")
```

---

## Siehe auch

- [[Python Grundlagen]]
- [[Verzweigungen und Funktionen]]
- [[Schleifen und Listen]]
