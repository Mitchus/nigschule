---
fach: LF4
thema: Python Grundlagen
tags: [lf4, python, grundlagen]
datum: 2026-04-20
typ: notiz
---

# Python Grundlagen

## Entwicklungsumgebung einrichten

Empfohlene IDEs:
- **PyCharm** (empfohlen in der Schule)
- Visual Studio Code
- Thonny (einsteigerfreundlich)
- Anaconda

> [!tip] Dateien haben die Endung `.py` und werden mit `python3 datei.py` ausgeführt.

---

## Erstes Programm

```python
# Autor: Max Mustermann
# Datum: 01.01.2026

print("Mein erstes Python Programm in der Schule")
print("Mein Name ist Max")
```

### Ausgabe mit `print()`

```python
# Einfache Ausgabe
print("Hallo Welt")

# Mehrere print-Befehle in einer Zeile (mit Semikolon)
print("Hallo"); print("Welt")

# Einfache Anführungszeichen für Strings mit "
print('Mein Name ist "Max"')

# Escape-Zeichen für " innerhalb von "
print("Hallo \"Helmut\"")
```

### Escape-Zeichen

| Zeichen | Bedeutung         | Beispiel                         |
| ------- | ----------------- | -------------------------------- |
| `\n`    | Zeilenumbruch     | `print("Zeile1\nZeile2")`       |
| `\t`    | Tabulator         | `print("Name:\tMax")`            |
| `\\`    | Backslash         | `print("Pfad: C:\\Users")`       |
| `\"`    | Anführungszeichen  | `print("Er sagte \"Hallo\"")`   |

---

## Kommentare

```python
# Einzeiliger Kommentar

'''
Mehrzeiliger
Kommentar
'''
```

---

## Bezeichner und Namensregeln

Bezeichner identifizieren Variablen, Klassen und Methoden eindeutig.

**Regeln:**
- Beginnen mit Buchstabe oder `_`
- Keine Leerzeichen, keine Sonderzeichen
- Groß-/Kleinschreibung wird unterschieden
- Keine Schlüsselwörter als Namen (`if`, `while`, `class`, ...)

```python
# Gültige Bezeichner
mein_name = "Max"
_privat = 42
temperatur1 = 23.5

# Ungültige Bezeichner
# 1name = "Fehler"      # Beginnt mit Zahl
# mein name = "Fehler"  # Leerzeichen
# class = "Fehler"      # Schlüsselwort
```

---

## Schlüsselwörter

Reservierte Wörter, die nicht als Bezeichner verwendet werden dürfen:

```
False   True    None    and     or      not     if      elif
else    for     while   break   continue return  def     class
import  from    as      try     except  finally raise   pass
in      is      lambda  with    yield   global  nonlocal del
```

---

## Built-in-Funktionen

Funktionen, die ohne Import verfügbar sind:

| Funktion    | Beschreibung                        |
| ----------- | ----------------------------------- |
| `print()`   | Ausgabe auf Konsole                 |
| `input()`   | Benutzereingabe lesen               |
| `int()`     | In Ganzzahl konvertieren            |
| `float()`   | In Gleitkommazahl konvertieren      |
| `str()`     | In Zeichenkette konvertieren        |
| `type()`    | Datentyp ermitteln                  |
| `len()`     | Länge eines Objekts                 |
| `range()`   | Zahlenfolge erzeugen                |
| `abs()`     | Betrag einer Zahl                   |
| `round()`   | Runden                              |

---

## Module und Namensräume

Module sind Python-Dateien, die Funktionen und Klassen enthalten.

```python
# Ganzes Modul importieren
import math
print(math.sqrt(16))  # 4.0

# Einzelne Funktion importieren
from math import pi
print(pi)  # 3.141592653589793

# Mit Alias
import random as rnd
print(rnd.randint(1, 10))
```

**Namensräume** (Scopes) bestimmen die Sichtbarkeit von Variablen:
- **Lokal** - innerhalb einer Funktion
- **Global** - auf Modulebene
- **Built-in** - vordefinierte Python-Funktionen

---

## Eingabe und Typkonvertierung

`input()` liest immer einen **String** ein:

```python
name = input("Wie heißt du? ")           # str
alter = int(input("Wie alt bist du? "))   # int
groesse = float(input("Größe in m: "))    # float
```

> [!warning] Ohne Konvertierung ist die Eingabe immer `str` - Rechnen damit führt zu Fehlern!

### Formatierte Ausgabe

```python
name = "Max"
alter = 25

# Mit .format()
print("Name: {0}, Alter: {1}".format(name, alter))

# Mit f-Strings (moderner)
print(f"Name: {name}, Alter: {alter}")
```

---

## Siehe auch

- [[Datentypen und Operatoren]]
- [[Verzweigungen und Funktionen]]
- [[Schleifen und Listen]]
