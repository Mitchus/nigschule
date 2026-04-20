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

> [!success] Lösung
> ```python
> # Aufgabe 1 - MwSt-Berechnung
>
> netto = float(input("Nettopreis eingeben: "))
> kennung = int(input("Steuersatz (1 = voll 19%, andere = ermäßigt 7%): "))
>
> msatz = 0.19
> ermsatz = 0.07
>
> if kennung == 1:
>     mwst = netto * msatz
> else:
>     mwst = netto * ermsatz
>
> brutto = netto + mwst
>
> print(f"MwSt:   {mwst:.2f} €")
> print(f"Brutto: {brutto:.2f} €")
> ```

> [!example] Aufgabe 2 - Passwort-Prüfung
> Ein Passwort soll eingelesen und mit einer festen Zeichenkette verglichen werden.
> - Korrekt: positive Rückmeldung
> - Falsch: negative Rückmeldung
>
> ```
> Ausgabe: Bitte geben Sie das Passwort ein: 321
>          Das eingegebene Passwort ist korrekt!
> ```

> [!success] Lösung
> ```python
> # Aufgabe 2 - Passwort-Prüfung
>
> RICHTIGES_PASSWORT = "321"
>
> eingabe = input("Bitte geben Sie das Passwort ein: ")
>
> if eingabe == RICHTIGES_PASSWORT:
>     print("Das eingegebene Passwort ist korrekt!")
> else:
>     print("Das eingegebene Passwort ist falsch!")
> ```

> [!example] Aufgabe 3 - Kleinste von zwei Zahlen
> Schreibe ein Programm, das nach Eingabe zweier Gleitkommazahlen die kleinste ausgibt.

> [!success] Lösung
> ```python
> # Aufgabe 3 - Kleinste von zwei Zahlen
>
> a = float(input("Erste Zahl eingeben: "))
> b = float(input("Zweite Zahl eingeben: "))
>
> if a < b:
>     kleinste = a
> else:
>     kleinste = b
>
> print(f"Die kleinste Zahl ist: {kleinste}")
> ```

> [!example] Aufgabe 4 - Größte von drei Zahlen
> Schreibe ein Programm, das nach Eingabe dreier Gleitkommazahlen die größte ausgibt.

> [!success] Lösung
> ```python
> # Aufgabe 4 - Größte von drei Zahlen
>
> a = float(input("Erste Zahl eingeben: "))
> b = float(input("Zweite Zahl eingeben: "))
> c = float(input("Dritte Zahl eingeben: "))
>
> if a >= b and a >= c:
>     groesste = a
> elif b >= a and b >= c:
>     groesste = b
> else:
>     groesste = c
>
> print(f"Die größte Zahl ist: {groesste}")
> ```

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

> [!success] Lösung
> ```python
> # Aufgabe 5 - Schaltjahr
>
> jahr = int(input("Jahr eingeben: "))
>
> if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
>     print(f"Das Jahr {jahr} ist ein Schaltjahr.")
> else:
>     print(f"Das Jahr {jahr} ist kein Schaltjahr.")
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

> [!success] Lösung
> **Version 1 – mit direkter Ausgabe (print):**
> ```python
> # Aufgabe 6 - Parkhaus-Statusanzeige
>
> GESAMT = 500
>
> def status_anzeigen(anzahl_belegt, eingang_frei, ausgang_frei, vermietet):
>     frei = GESAMT - anzahl_belegt
>
>     # Entscheidungstabelle:
>     # Sonderfall: Parkhaus vermietet
>     if vermietet:
>         print("Status: Parkhaus vermietet – kein öffentlicher Zugang.")
>     # Parkhaus voll (kein freier Platz)
>     elif frei <= 0:
>         if ausgang_frei:
>             print("Status: VOLL – bitte wenden. Ausfahrt möglich.")
>         else:
>             print("Status: VOLL – Ein- und Ausfahrt gesperrt.")
>     # Mehr als 80% belegt → fast voll
>     elif anzahl_belegt / GESAMT >= 0.8:
>         if eingang_frei:
>             print(f"Status: Fast voll – noch {frei} Plätze frei. Einfahrt möglich.")
>         else:
>             print(f"Status: Fast voll – noch {frei} Plätze frei. Einfahrt gesperrt.")
>     # Normalbetrieb
>     else:
>         if eingang_frei:
>             print(f"Status: Geöffnet – {frei} von {GESAMT} Plätzen frei.")
>         else:
>             print(f"Status: Geöffnet (Einfahrt gesperrt) – {frei} Plätze frei.")
>
> def main():
>     status_anzeigen(330, True, True, False)   # Normalbetrieb
>     status_anzeigen(420, True, True, False)   # Fast voll
>     status_anzeigen(500, False, True, False)  # Voll
>     status_anzeigen(200, True, True, True)    # Vermietet
>
> main()
> ```
>
> **Version 2 – mit `return` (kein print in der Funktion):**
> ```python
> GESAMT = 500
>
> def status_anzeigen(anzahl_belegt, eingang_frei, ausgang_frei, vermietet):
>     frei = GESAMT - anzahl_belegt
>
>     if vermietet:
>         return "Status: Parkhaus vermietet – kein öffentlicher Zugang."
>     elif frei <= 0:
>         if ausgang_frei:
>             return "Status: VOLL – bitte wenden. Ausfahrt möglich."
>         else:
>             return "Status: VOLL – Ein- und Ausfahrt gesperrt."
>     elif anzahl_belegt / GESAMT >= 0.8:
>         if eingang_frei:
>             return f"Status: Fast voll – noch {frei} Plätze frei. Einfahrt möglich."
>         else:
>             return f"Status: Fast voll – noch {frei} Plätze frei. Einfahrt gesperrt."
>     else:
>         if eingang_frei:
>             return f"Status: Geöffnet – {frei} von {GESAMT} Plätzen frei."
>         else:
>             return f"Status: Geöffnet (Einfahrt gesperrt) – {frei} Plätze frei."
>
> def main():
>     meldung = status_anzeigen(330, True, True, False)
>     print(meldung)
>
> main()
> ```

> [!example] Aufgabe 7 - Bankautomat
> Schreibe ein Programm "Bankautomat" mit Menü-Auswahl für verschiedene Bankoperationen.

> [!success] Lösung
> ```python
> # Aufgabe 7 - Bankautomat
>
> kontostand = 1000.00  # Startguthaben
>
> print("=== Bankautomat ===")
> print("1 - Kontostand anzeigen")
> print("2 - Geld einzahlen")
> print("3 - Geld abheben")
> print("4 - Beenden")
>
> auswahl = int(input("Bitte wählen Sie eine Option: "))
>
> if auswahl == 1:
>     print(f"Ihr aktueller Kontostand: {kontostand:.2f} €")
> elif auswahl == 2:
>     betrag = float(input("Einzahlungsbetrag in €: "))
>     if betrag > 0:
>         kontostand += betrag
>         print(f"{betrag:.2f} € eingezahlt. Neuer Kontostand: {kontostand:.2f} €")
>     else:
>         print("Ungültiger Betrag.")
> elif auswahl == 3:
>     betrag = float(input("Abhebungsbetrag in €: "))
>     if betrag <= 0:
>         print("Ungültiger Betrag.")
>     elif betrag > kontostand:
>         print("Nicht genügend Guthaben auf dem Konto.")
>     else:
>         kontostand -= betrag
>         print(f"{betrag:.2f} € abgehoben. Neuer Kontostand: {kontostand:.2f} €")
> elif auswahl == 4:
>     print("Auf Wiedersehen!")
> else:
>     print("Ungültige Auswahl.")
> ```

---

## Aufgaben: Vertiefung

> [!example] Aufgabe 8 - Getränkeautomat
> Entwickle die Anzeigesteuerung für einen Getränkeautomaten nach einem vorgegebenen Struktogramm. Das Programm soll ein Menü anzeigen und Getränke auswählen lassen.
>
> Erweitere den Automaten anschließend mit Schleifen (→ [[Schleifen und Listen]]).

> [!success] Lösung
> ```python
> # Aufgabe 8 - Getränkeautomat
>
> print("=== Getränkeautomat ===")
> print("1 - Cola        (1,50 €)")
> print("2 - Wasser      (1,00 €)")
> print("3 - Orangensaft (1,80 €)")
> print("4 - Kaffee      (2,00 €)")
> print("0 - Beenden")
>
> auswahl = int(input("Bitte wählen Sie ein Getränk: "))
>
> if auswahl == 1:
>     print("Cola wird ausgegeben. Bitte entnehmen Sie Ihr Getränk (1,50 €).")
> elif auswahl == 2:
>     print("Wasser wird ausgegeben. Bitte entnehmen Sie Ihr Getränk (1,00 €).")
> elif auswahl == 3:
>     print("Orangensaft wird ausgegeben. Bitte entnehmen Sie Ihr Getränk (1,80 €).")
> elif auswahl == 4:
>     print("Kaffee wird ausgegeben. Bitte entnehmen Sie Ihr Getränk (2,00 €).")
> elif auswahl == 0:
>     print("Auf Wiedersehen!")
> else:
>     print("Ungültige Auswahl. Bitte wählen Sie eine Zahl zwischen 0 und 4.")
> ```

> [!example] Aufgabe 9 - Funktionen-Theorie (S. 549-552)
> Beantworte folgende Fragen:
> 1. Was sind Funktionen?
> 2. Was ist ein Übergabeparameter?
> 3. Was ist ein Rückgabeparameter?
> 4. Wie verwende ich diese in Funktionen?
> 5. Was ist ein rekursiver Funktionsaufruf und was birgt dieser für Gefahren?

> [!success] Lösung
> **1. Was sind Funktionen?**
> Funktionen sind benannte, wiederverwendbare Codeblöcke, die eine bestimmte Aufgabe erfüllen. Sie werden mit dem Schlüsselwort `def` definiert und können an beliebigen Stellen im Programm aufgerufen werden. Funktionen fördern die Strukturierung, Lesbarkeit und Wartbarkeit von Code, da gleiche Logik nicht mehrfach geschrieben werden muss (Prinzip DRY – Don't Repeat Yourself).
>
> **2. Was ist ein Übergabeparameter?**
> Ein Übergabeparameter (auch Argument oder Parameter) ist ein Wert, der beim Aufruf einer Funktion an diese übergeben wird. Er steht in den runden Klammern der Funktionsdefinition und ist innerhalb der Funktion als lokale Variable verfügbar. Beispiel: Bei `def addiere(a, b):` sind `a` und `b` die Übergabeparameter.
>
> **3. Was ist ein Rückgabeparameter?**
> Ein Rückgabeparameter (Rückgabewert) ist der Wert, den eine Funktion nach ihrer Ausführung mit `return` zurückliefert. Der aufrufende Code kann diesen Wert in einer Variablen speichern oder direkt weiterverarbeiten. Gibt eine Funktion kein `return` an, gibt sie implizit `None` zurück.
>
> **4. Wie verwende ich diese in Funktionen?**
> ```python
> # Definition mit Übergabeparametern a und b
> def multipliziere(a, b):
>     ergebnis = a * b
>     return ergebnis  # Rückgabewert
>
> # Aufruf: Übergabeparameter werden als Argumente mitgegeben
> produkt = multipliziere(4, 5)  # produkt = 20
> print(produkt)
> ```
> Übergabeparameter werden in der Funktionsdefinition in den Klammern angegeben. Der Rückgabewert wird mit `return` zurückgegeben und kann vom Aufrufer genutzt werden.
>
> **5. Was ist ein rekursiver Funktionsaufruf und was birgt dieser für Gefahren?**
> Bei einem rekursiven Funktionsaufruf ruft sich eine Funktion selbst auf. Dies eignet sich für Probleme, die sich in kleinere gleichartige Teilprobleme zerlegen lassen (z. B. Fakultät, Fibonacci). Jeder rekursive Aufruf legt einen neuen Aufrufrahmen auf den Call-Stack.
>
> **Gefahren:** Fehlt eine korrekte Abbruchbedingung oder wird diese nie erreicht, entsteht eine Endlosrekursion. Python bricht diese nach einer bestimmten Tiefe (Standard: 1000 Ebenen) mit einem `RecursionError` ab. Außerdem verbraucht tiefe Rekursion viel Arbeitsspeicher, da für jeden Aufruf Speicher reserviert wird.
> ```python
> def fakultaet(n):
>     if n <= 1:       # Abbruchbedingung – verhindert Endlosrekursion
>         return 1
>     return n * fakultaet(n - 1)  # rekursiver Aufruf
> ```

---

## Siehe auch

- [[Python Grundlagen]]
- [[Datentypen und Operatoren]]
- [[Schleifen und Listen]]
