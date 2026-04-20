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

> [!example] Aufgabe 4 - Praxisaufgaben
> 1. **Übertragungsrate:** Berechne die Zeit für eine Datenübertragung (Eingabe: MB + Kbit/s, Ausgabe: Minuten)
> 2. **Nettolohn:** Berechne aus dem Bruttolohn den Nettolohn (Steuerklasse I: 30%, + KV, RV, AV)
> 3. **Zinsrechnung:** Berechne den Zinsbetrag (Eingabe: Geldbetrag + Zinssatz)

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
