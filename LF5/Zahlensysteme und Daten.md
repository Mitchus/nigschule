---
fach: LF5
thema: Zahlensysteme und Daten
tags: [lf5, zahlensysteme, dezimal, dual, hexadezimal, speicher]
datum: 2026-04-20
typ: notiz
---

# Zahlensysteme und Daten

## Zahlensysteme im Überblick

| System        | Basis | Ziffern         | Verwendung                    |
| ------------- | ----- | --------------- | ----------------------------- |
| **Dezimal**   | 10    | 0-9             | Alltag                        |
| **Dual/Binär** | 2    | 0, 1            | Computerintern                |
| **Oktal**     | 8     | 0-7             | Unix-Berechtigungen           |
| **Hexadezimal** | 16  | 0-9, A-F        | Adressen, Farben, MAC         |

---

## Umrechnungsmethoden

### Dezimal → Dual (Divisionsmethode)

Teile die Zahl wiederholt durch 2 und notiere den Rest. Ergebnis von unten nach oben lesen.

```
171 ÷ 2 = 85  Rest 1  ↑
 85 ÷ 2 = 42  Rest 1  │
 42 ÷ 2 = 21  Rest 0  │
 21 ÷ 2 = 10  Rest 1  │  Ergebnis: 10101011
 10 ÷ 2 =  5  Rest 0  │
  5 ÷ 2 =  2  Rest 1  │
  2 ÷ 2 =  1  Rest 0  │
  1 ÷ 2 =  0  Rest 1  │
```

**Ergebnis:** 171₁₀ = **10101011**₂

### Dual → Dezimal (Additionsmethode / Multiplikationsmethode)

Jede Stelle mit ihrer Zweierpotenz multiplizieren und addieren:

```
1  0  0  0  1  0  1  1
×  ×  ×  ×  ×  ×  ×  ×
128 64 32 16 8  4  2  1

= 128 + 0 + 0 + 0 + 8 + 0 + 2 + 1 = 139
```

### Dezimal → Dual (Subtraktionsmethode)

Subtrahiere die größtmögliche Zweierpotenz und notiere 1, sonst 0:

```
171 - 128 = 43  → 1
 43 -  64 = -   → 0
 43 -  32 = 11  → 1
 11 -  16 = -   → 0
 11 -   8 = 3   → 1
  3 -   4 = -   → 0
  3 -   2 = 1   → 1
  1 -   1 = 0   → 1
                  10101011
```

### Hexadezimal ↔ Dual

Jede Hex-Ziffer = 4 Bit:

| Hex | Dual | Dez |
| --- | ---- | --- |
| 0   | 0000 | 0   |
| 1   | 0001 | 1   |
| 2   | 0010 | 2   |
| 3   | 0011 | 3   |
| 4   | 0100 | 4   |
| 5   | 0101 | 5   |
| 6   | 0110 | 6   |
| 7   | 0111 | 7   |
| 8   | 1000 | 8   |
| 9   | 1001 | 9   |
| A   | 1010 | 10  |
| B   | 1011 | 11  |
| C   | 1100 | 12  |
| D   | 1101 | 13  |
| E   | 1110 | 14  |
| F   | 1111 | 15  |

**Beispiel:** FE₁₆ = 1111 1110₂ = 254₁₀

### Hexadezimal → Dezimal

Jede Stelle × 16^Position:

```
FE₁₆ = F × 16¹ + E × 16⁰
     = 15 × 16 + 14 × 1
     = 240 + 14
     = 254₁₀
```

---

## Vorzeichenbehaftete Dualzahlen

### Zweierkomplement

Negative Zahlen werden im **Zweierkomplement** dargestellt:

1. Dualzahl schreiben
2. Alle Bits invertieren (0↔1)
3. +1 addieren

```
+5 = 0000 0101
     1111 1010  (invertiert)
+5 → 1111 1011  = -5
```

> [!info] Das höchste Bit (MSB) ist das Vorzeichenbit: `0` = positiv, `1` = negativ

---

## Gleitkommazahlen (IEEE 754)

Darstellung von Kommazahlen im Computer:

```
Zahl = (-1)^Vorzeichen × Mantisse × 2^Exponent
```

| Format       | Vorzeichen | Exponent | Mantisse | Gesamt |
| ------------ | ---------- | -------- | -------- | ------ |
| **Single**   | 1 Bit      | 8 Bit    | 23 Bit   | 32 Bit |
| **Double**   | 1 Bit      | 11 Bit   | 52 Bit   | 64 Bit |

---

## Speicherbedarf berechnen

**Formel für Bilder:**
```
Speicher = Breite × Höhe × Farbtiefe (Bit) / 8
```

**Beispiel:** Full-HD Bild, 24 Bit Farbtiefe:
```
1920 × 1080 × 24 / 8 = 6.220.800 Byte ≈ 5,93 MiB
```

**Einheiten:**

| Einheit | Binär (IEC)    | Dezimal (SI)   |
| ------- | -------------- | -------------- |
| KB/KiB  | 1.024 Byte     | 1.000 Byte     |
| MB/MiB  | 1.048.576 Byte | 1.000.000 Byte |
| GB/GiB  | 1.073.741.824  | 1.000.000.000  |

---

## Datendarstellung

### Audio

| Begriff          | Beschreibung                                  |
| ---------------- | --------------------------------------------- |
| **Sampling-Rate** | Abtastungen pro Sekunde (z.B. 44.100 Hz)    |
| **Sampling-Tiefe** | Bits pro Abtastung (z.B. 16 Bit)           |
| **Bitrate**      | Datenrate in kbit/s                           |

Tonformate: Dolby Digital, Dolby True HD, DTS Digital, DDS

### Grafik

Bildformate unterscheiden sich in Kompression und Farbtiefe (BMP, PNG, JPEG, GIF, SVG, ...).

---

## Aufgaben

> [!example] Aufgabe 1 - Dezimal → Dual (S. 472/486 A4)
> Rechne mit der Divisionsmethode um:
> - 1000₁₀, 256₁₀, 13₁₀, 347₁₀, 2189₁₀
> - 171₁₀ (alle Methoden)
> - 10001011₂ → Dezimal (Additions- und Multiplikationsmethode)

> [!example] Aufgabe 2 - Hexadezimal (S. 472/486 A3)
> Rechne in Dual- und Dezimalzahl um:
> FE₁₆, 33₁₆, 16₁₆, 11₁₆, 16D3₁₆, 167A04₁₆, F002₁₆

> [!example] Aufgabe 3 - Datendarstellungen (S. 474-480)
> 1. Erläutere Sampling-Rate und Sampling-Tiefe
> 2. Recherchiere Tonformate: Dolby Digital, True HD, Digital Plus, DTS, SDDS

> [!example] Aufgabe 4 - Speicherbedarf
> Berechne den Speicherbedarf für verschiedene Bild- und Audiodateien.

---

## Materialien

- ![[files/Zahlensysteme Einstieg.pdf]]
- ![[files/02_ZahlensystemeGesamt.pdf]]
- ![[files/02_ZahlensystemeGesamtLSG.pdf]]
- ![[files/VorzeichenbehafteDualzahlen.pdf]]
- ![[files/05_Zahlensysteme_HandoutSuS.pdf]]
- ![[files/Speicherbedarf ermitteln.pdf]]

---

## Siehe auch

- [[Projektmanagement und Softwareentwicklung]]
- [[Entwurfsmethoden]]
