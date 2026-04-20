---
fach: LF4
thema: Verzweigungen und Funktionen
tags: [lf4, python, verzweigung, selektion, funktion]
datum: 2026-04-20
typ: notiz
---

# Verzweigungen und Funktionen

## Arten von Verzweigungen

```
Verzweigungen
├── einfache      (if)
├── zweiseitige   (if/else)
└── Fallunterscheidung (if/elif/else, match/case)
```

---

## Einseitige Verzweigung (`if`)

Trifft die Bedingung zu, wird der eingerückte Block ausgeführt.

```python
zahl = int(input("Geben Sie eine ganze Zahl ein: "))

if zahl > 0:
    print("Die Zahl {} ist größer als Null".format(zahl))
```

> [!important] Einrückung ist Pflicht!
> Python nutzt Einrückungen (4 Leerzeichen) statt geschweifter Klammern. Der Doppelpunkt `:` nach der Bedingung ist ebenfalls Pflicht.

---

## Zweiseitige Verzweigung (`if/else`)

```python
zahl = float(input("Geben Sie eine Gleitkommazahl ein: "))

if zahl >= 10.0 and zahl <= 20.0:
    print("Die Zahl {0} liegt im Bereich von 10 bis 20".format(zahl))
else:
    print("Die Zahl {0} liegt nicht im Bereich von 10 bis 20".format(zahl))
```

### Struktogramm-Darstellung

```
┌──────────────────────────────────────────────┐
│           zahl >= 10.0 and zahl <= 20.0      │
├──────────────────────┬───────────────────────┤
│        Wahr          │        Falsch         │
│ A: Zahl liegt im     │ A: Zahl liegt nicht   │
│    Bereich 10-20     │    im Bereich 10-20   │
└──────────────────────┴───────────────────────┘
```

---

## Mehrfache Verzweigung (`if/elif/else`)

```python
x = 5
y = 3

if x > y:
    print("{0} ist groesser als {1}.".format(x, y))
elif x < y:
    print("{0} ist groesser als {1}.".format(y, x))
else:
    print("{0} und {1} sind gleich.".format(x, y))
```

**Syntax-Übersicht:**
```
if Bedingung:
    Anweisung
elif Bedingung:
    Anweisung
else:
    Anweisung
```

### Alternative String-Ausgabe

```python
# Mit Konkatenation
print(str(x) + " ist groesser als " + str(y))

# Mit .format()
print("{0} ist groesser als {1}.".format(x, y))

# Mit f-String
print(f"{x} ist groesser als {y}.")
```

---

## Fallunterscheidung mit `match/case`

Ab Python 3.10 verfügbar. Ideal bei vielen festen Vergleichswerten:

```python
note = int(input("Geben Sie die Note in Ganzzahl ein: "))

match note:
    case 1:
        print("Die Note 1 entspricht einer sehr gut.")
    case 2:
        print("Die Note 2 entspricht einer gut.")
    case 3:
        print("Die Note 3 entspricht einer befriedigend.")
    case 4:
        print("Die Note 4 entspricht einer ausreichend.")
    case 5:
        print("Die Note 5 entspricht einer mangelhaft.")
    case 6:
        print("Die Note 6 entspricht einer ungenügend.")
    case _:
        print("Sie haben keine passende Note eingegeben.")
```

> [!tip] `case _:` ist der Default-Fall (wie `else` bei `if`).

---

## Funktionen

Funktionen kapseln wiederverwendbare Codeblöcke.

### Grundsyntax

```python
def begruessung(name):
    """Gibt eine Begrüßung aus."""
    print(f"Hallo, {name}!")

begruessung("Max")  # Aufruf
```

### Übergabeparameter und Rückgabewert

```python
def addiere(a, b):
    """Addiert zwei Zahlen und gibt das Ergebnis zurück."""
    return a + b

ergebnis = addiere(3, 5)
print(ergebnis)  # 8
```

| Begriff              | Beschreibung                                    |
| -------------------- | ----------------------------------------------- |
| **Übergabeparameter** | Werte, die an die Funktion übergeben werden    |
| **Rückgabeparameter** | Wert, den die Funktion mit `return` zurückgibt |
| **Rekursion**         | Funktion ruft sich selbst auf                  |

> [!warning] Rekursion
> Ein rekursiver Funktionsaufruf muss eine Abbruchbedingung haben, sonst entsteht eine Endlosrekursion (`RecursionError`).

```python
def fakultaet(n):
    if n <= 1:
        return 1
    return n * fakultaet(n - 1)

print(fakultaet(5))  # 120
```

---

## Aufgaben: Selektion

> [!example] Aufgabe 1 - MwSt-Berechnung
> Für einen Nettoverkaufspreis wird die Mehrwertsteuer berechnet (voller Satz = 19%, ermäßigter Satz = 7%).
>
> Struktogramm:
> ```
> ┌─────────────────────────────────────────────────┐
> │ E: netto, kennung                               │
> │ msatz = 0.19; ermsatz = 0.07                    │
> ├─────────────────────────────────────────────────┤
> │              kennung == 1                        │
> ├────────────────────────┬────────────────────────┤
> │        Wahr            │        Falsch           │
> │ mwst = netto * msatz   │ mwst = netto * ermsatz │
> ├────────────────────────┴────────────────────────┤
> │ brutto = netto + mwst                           │
> │ A: mwst, brutto                                 │
> └─────────────────────────────────────────────────┘
> ```
>
> Erstelle ein Python-Programm basierend auf diesem Struktogramm.

> [!example] Aufgabe 2 - Passwort-Prüfung
> Ein Passwort soll eingelesen und mit einer festen Zeichenkette verglichen werden.
> - Korrekt: positive Rückmeldung
> - Falsch: negative Rückmeldung
>
> ```
> Ausgabe: Bitte geben Sie das Passwort ein: 321
>          Das eingegebene Passwort ist korrekt!
> ```

> [!example] Aufgabe 3 - Kleinste von zwei Zahlen
> Schreibe ein Programm, das nach Eingabe zweier Gleitkommazahlen die kleinste ausgibt.

> [!example] Aufgabe 4 - Größte von drei Zahlen
> Schreibe ein Programm, das nach Eingabe dreier Gleitkommazahlen die größte ausgibt.

> [!example] Aufgabe 5 - Schaltjahr
> Prüfe ob ein eingegebenes Jahr ein Schaltjahr ist.
>
> **Regeln:**
> - Teilbar durch 4 **und nicht** durch 100 → Schaltjahr
> - **Oder** teilbar durch 400 → Schaltjahr
>
> ```
> Ausgabe: Das Jahr 2024 ist ein Schaltjahr.
> ```

> [!example] Aufgabe 6 - Parkhaus-Statusanzeige (mit Funktion)
> Ein Parkhaus hat 500 Stellplätze. Schreibe eine Funktion `status_anzeigen` die anhand einer Entscheidungstabelle den Status ausgibt.
>
> ```python
> def status_anzeigen(anzahl_belegt, eingang_frei, ausgang_frei, vermietet):
>     # Entscheidungstabelle auswerten
>     # Statustext zurückgeben
>     pass
>
> # Beispielaufruf
> def main():
>     status_anzeigen(330, True, True, False)
>
> main()
> ```
>
> Erweitere: Die Funktion soll den Text nur zurückgeben (`return`), nicht selbst ausgeben.

> [!example] Aufgabe 7 - Bankautomat
> Schreibe ein Programm "Bankautomat" mit Menü-Auswahl für verschiedene Bankoperationen.

---

## Aufgaben: Vertiefung

> [!example] Aufgabe 8 - Getränkeautomat
> Entwickle die Anzeigesteuerung für einen Getränkeautomaten nach einem vorgegebenen Struktogramm. Das Programm soll ein Menü anzeigen und Getränke auswählen lassen.
>
> Erweitere den Automaten anschließend mit Schleifen (→ [[Schleifen und Listen]]).

> [!example] Aufgabe 9 - Funktionen-Theorie (S. 549-552)
> Beantworte folgende Fragen:
> 1. Was sind Funktionen?
> 2. Was ist ein Übergabeparameter?
> 3. Was ist ein Rückgabeparameter?
> 4. Wie verwende ich diese in Funktionen?
> 5. Was ist ein rekursiver Funktionsaufruf und was birgt dieser für Gefahren?

---

## Siehe auch

- [[Python Grundlagen]]
- [[Datentypen und Operatoren]]
- [[Schleifen und Listen]]
