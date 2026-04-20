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

> [!success] Lösung – Aufgabe 1
>
> **Divisionsmethode (Dezimal → Dual):**
>
> **1000₁₀:**
> ```
> 1000 ÷ 2 = 500  Rest 0  ↑
>  500 ÷ 2 = 250  Rest 0  │
>  250 ÷ 2 = 125  Rest 0  │
>  125 ÷ 2 =  62  Rest 1  │  Ergebnis von unten nach oben lesen
>   62 ÷ 2 =  31  Rest 0  │
>   31 ÷ 2 =  15  Rest 1  │
>   15 ÷ 2 =   7  Rest 1  │
>    7 ÷ 2 =   3  Rest 1  │
>    3 ÷ 2 =   1  Rest 1  │
>    1 ÷ 2 =   0  Rest 1  │
> ```
> **1000₁₀ = 1111101000₂**
>
> ---
>
> **256₁₀:**
> ```
> 256 ÷ 2 = 128  Rest 0  ↑
> 128 ÷ 2 =  64  Rest 0  │
>  64 ÷ 2 =  32  Rest 0  │
>  32 ÷ 2 =  16  Rest 0  │  Ergebnis von unten nach oben lesen
>  16 ÷ 2 =   8  Rest 0  │
>   8 ÷ 2 =   4  Rest 0  │
>   4 ÷ 2 =   2  Rest 0  │
>   2 ÷ 2 =   1  Rest 0  │
>   1 ÷ 2 =   0  Rest 1  │
> ```
> **256₁₀ = 100000000₂**
>
> ---
>
> **13₁₀:**
> ```
> 13 ÷ 2 = 6  Rest 1  ↑
>  6 ÷ 2 = 3  Rest 0  │  Ergebnis von unten nach oben lesen
>  3 ÷ 2 = 1  Rest 1  │
>  1 ÷ 2 = 0  Rest 1  │
> ```
> **13₁₀ = 1101₂**
>
> ---
>
> **347₁₀:**
> ```
> 347 ÷ 2 = 173  Rest 1  ↑
> 173 ÷ 2 =  86  Rest 1  │
>  86 ÷ 2 =  43  Rest 0  │
>  43 ÷ 2 =  21  Rest 1  │  Ergebnis von unten nach oben lesen
>  21 ÷ 2 =  10  Rest 1  │
>  10 ÷ 2 =   5  Rest 0  │
>   5 ÷ 2 =   2  Rest 1  │
>   2 ÷ 2 =   1  Rest 0  │
>   1 ÷ 2 =   0  Rest 1  │
> ```
> **347₁₀ = 101011011₂**
>
> ---
>
> **2189₁₀:**
> ```
> 2189 ÷ 2 = 1094  Rest 1  ↑
> 1094 ÷ 2 =  547  Rest 0  │
>  547 ÷ 2 =  273  Rest 1  │
>  273 ÷ 2 =  136  Rest 1  │
>  136 ÷ 2 =   68  Rest 0  │  Ergebnis von unten nach oben lesen
>   68 ÷ 2 =   34  Rest 0  │
>   34 ÷ 2 =   17  Rest 0  │
>   17 ÷ 2 =    8  Rest 1  │
>    8 ÷ 2 =    4  Rest 0  │
>    4 ÷ 2 =    2  Rest 0  │
>    2 ÷ 2 =    1  Rest 0  │
>    1 ÷ 2 =    0  Rest 1  │
> ```
> **2189₁₀ = 100010001101₂**
>
> ---
>
> **171₁₀ mit allen drei Methoden:**
>
> *Methode 1 – Divisionsmethode:*
> ```
> 171 ÷ 2 = 85  Rest 1  ↑
>  85 ÷ 2 = 42  Rest 1  │
>  42 ÷ 2 = 21  Rest 0  │
>  21 ÷ 2 = 10  Rest 1  │  Ergebnis von unten nach oben lesen
>  10 ÷ 2 =  5  Rest 0  │
>   5 ÷ 2 =  2  Rest 1  │
>   2 ÷ 2 =  1  Rest 0  │
>   1 ÷ 2 =  0  Rest 1  │
> ```
>
> *Methode 2 – Subtraktionsmethode:*
> ```
> Zweierpotenzen: 128  64  32  16   8   4   2   1
>
> 171 - 128 = 43   →  1
>  43 -  64 → n.m. →  0
>  43 -  32 = 11   →  1
>  11 -  16 → n.m. →  0
>  11 -   8 = 3    →  1
>   3 -   4 → n.m. →  0
>   3 -   2 = 1    →  1
>   1 -   1 = 0    →  1
>                     10101011
> ```
>
> *Methode 3 – Additionsmethode (Zweierpotenzen zusammensuchen):*
> ```
> Zweierpotenzen aufsteigend: 1, 2, 4, 8, 16, 32, 64, 128
> 128 + 32 + 8 + 2 + 1 = 171
>        ↓   ↓  ↓  ↓  ↓
> Bit:   1   0  1  0  1  0  1  1
> Pos:  128 64 32 16  8  4  2  1
> ```
>
> **171₁₀ = 10101011₂** (alle drei Methoden liefern dasselbe Ergebnis)
>
> ---
>
> **10001011₂ → Dezimal (Additionsmethode):**
> ```
>   1    0    0    0    1    0    1    1
> × 128 × 64 × 32 × 16 × 8  × 4  × 2  × 1
> = 128 +  0 +  0 +  0 +  8 +  0 +  2 +  1
> = 139
> ```
> **10001011₂ = 139₁₀**

> [!example] Aufgabe 2 - Hexadezimal (S. 472/486 A3)
> Rechne in Dual- und Dezimalzahl um:
> FE₁₆, 33₁₆, 16₁₆, 11₁₆, 16D3₁₆, 167A04₁₆, F002₁₆

> [!success] Lösung – Aufgabe 2
>
> Jede Hex-Ziffer entspricht genau 4 Bit. Für Dezimal: jede Stelle × 16^Position.
>
> **FE₁₆:**
> ```
> F = 1111,  E = 1110
> Dual:    1111 1110₂
> Dezimal: 15 × 16¹ + 14 × 16⁰ = 240 + 14 = 254
> ```
> **FE₁₆ = 11111110₂ = 254₁₀**
>
> ---
>
> **33₁₆:**
> ```
> 3 = 0011,  3 = 0011
> Dual:    0011 0011₂
> Dezimal: 3 × 16¹ + 3 × 16⁰ = 48 + 3 = 51
> ```
> **33₁₆ = 00110011₂ = 51₁₀**
>
> ---
>
> **16₁₆:**
> ```
> 1 = 0001,  6 = 0110
> Dual:    0001 0110₂
> Dezimal: 1 × 16¹ + 6 × 16⁰ = 16 + 6 = 22
> ```
> **16₁₆ = 00010110₂ = 22₁₀**
>
> ---
>
> **11₁₆:**
> ```
> 1 = 0001,  1 = 0001
> Dual:    0001 0001₂
> Dezimal: 1 × 16¹ + 1 × 16⁰ = 16 + 1 = 17
> ```
> **11₁₆ = 00010001₂ = 17₁₀**
>
> ---
>
> **16D3₁₆:**
> ```
> 1 = 0001,  6 = 0110,  D = 1101,  3 = 0011
> Dual:    0001 0110 1101 0011₂
> Dezimal: 1 × 16³ + 6 × 16² + 13 × 16¹ + 3 × 16⁰
>        = 1 × 4096 + 6 × 256 + 13 × 16 + 3 × 1
>        = 4096 + 1536 + 208 + 3
>        = 5843
> ```
> **16D3₁₆ = 0001011011010011₂ = 5843₁₀**
>
> ---
>
> **167A04₁₆:**
> ```
> 1 = 0001,  6 = 0110,  7 = 0111,  A = 1010,  0 = 0000,  4 = 0100
> Dual:    0001 0110 0111 1010 0000 0100₂
> Dezimal: 1 × 16⁵ + 6 × 16⁴ + 7 × 16³ + 10 × 16² + 0 × 16¹ + 4 × 16⁰
>        = 1 × 1.048.576 + 6 × 65.536 + 7 × 4096 + 10 × 256 + 0 × 16 + 4 × 1
>        = 1.048.576 + 393.216 + 28.672 + 2.560 + 0 + 4
>        = 1.473.028
> ```
> **167A04₁₆ = 000101100111101000000100₂ = 1.473.028₁₀**
>
> ---
>
> **F002₁₆:**
> ```
> F = 1111,  0 = 0000,  0 = 0000,  2 = 0010
> Dual:    1111 0000 0000 0010₂
> Dezimal: 15 × 16³ + 0 × 16² + 0 × 16¹ + 2 × 16⁰
>        = 15 × 4096 + 0 + 0 + 2
>        = 61.440 + 2
>        = 61.442
> ```
> **F002₁₆ = 1111000000000010₂ = 61.442₁₀**

> [!example] Aufgabe 3 - Datendarstellungen (S. 474-480)
> 1. Erläutere Sampling-Rate und Sampling-Tiefe
> 2. Recherchiere Tonformate: Dolby Digital, True HD, Digital Plus, DTS, SDDS

> [!success] Lösung – Aufgabe 3
>
> **1. Sampling-Rate und Sampling-Tiefe**
>
> **Sampling-Rate (Abtastrate):**
> Die Sampling-Rate gibt an, wie oft pro Sekunde ein analoges Tonsignal gemessen (abgetastet) wird. Die Einheit ist Hertz (Hz) bzw. Kilohertz (kHz). Je höher die Sampling-Rate, desto genauer wird das ursprüngliche analoge Signal rekonstruiert. Laut dem Nyquist-Shannon-Theorem muss die Abtastrate mindestens doppelt so hoch sein wie die höchste zu erfassende Frequenz. Da das menschliche Gehör bis ca. 20.000 Hz hört, reichen 44.100 Hz (CD-Standard) aus. Typische Werte:
> - 44.100 Hz – CD-Audio (Standard)
> - 48.000 Hz – Professionelles Audio, DVD, Broadcast
> - 96.000 Hz / 192.000 Hz – High-Resolution Audio
>
> **Sampling-Tiefe (Bittiefe):**
> Die Sampling-Tiefe gibt an, mit wie vielen Bits jeder einzelne Abtastwert gespeichert wird. Sie bestimmt die Dynamik (den Lautstärkeumfang) einer Aufnahme. Mit n Bit lassen sich 2ⁿ verschiedene Amplitudenstufen darstellen. Typische Werte:
> - 8 Bit – 256 Stufen (geringe Qualität, z.B. Telefonqualität)
> - 16 Bit – 65.536 Stufen (CD-Standard, guter Dynamikumfang ~96 dB)
> - 24 Bit – 16.777.216 Stufen (Studioqualität, ~144 dB Dynamik)
>
> ---
>
> **2. Tonformate im Überblick**
>
> | Format | Entwickler | Kanäle | Beschreibung |
> | --- | --- | --- | --- |
> | **Dolby Digital** | Dolby Laboratories | bis 5.1 | Verlustbehaftetes Surround-Format (AC-3). Standard für DVD und Kino. Bitrate ca. 640 kbit/s. Kodiert 6 unabhängige Kanäle. |
> | **Dolby TrueHD** | Dolby Laboratories | bis 7.1 (Atmos: 24+) | Verlustfreies Lossless-Format für Blu-ray. Identische Kopie der Studioaufnahme. Basis für Dolby Atmos (objektbasierter Raumklang). |
> | **Dolby Digital Plus** | Dolby Laboratories | bis 7.1 | Weiterentwicklung von Dolby Digital. Verlustbehaftet, aber bessere Effizienz und höhere Bitraten (bis 6 Mbit/s). Standard für Streaming (Netflix, Amazon). |
> | **DTS (Digital Theater Systems)** | DTS, Inc. | bis 5.1 | Verlustbehaftetes Surround-Format für Kino und DVD. Höhere Standardbitrate als Dolby Digital (1.536 kbit/s), daher oft als qualitativ besser wahrgenommen. |
> | **SDDS (Sony Dynamic Digital Sound)** | Sony | bis 7.1 | Kinoformat von Sony. Auf dem Filmstreifen außen neben den Perforationslöchern gespeichert. Unterstützt bis zu 8 Kanäle. Heute kaum noch im Einsatz. |

> [!example] Aufgabe 4 - Speicherbedarf
> Berechne den Speicherbedarf für verschiedene Bild- und Audiodateien.

> [!success] Lösung – Aufgabe 4
>
> **Formeln:**
> ```
> Bild:  Speicher (Byte) = Breite × Höhe × Farbtiefe (Bit) ÷ 8
> Audio: Speicher (Byte) = Sampling-Rate × Bittiefe (Bit) × Kanäle × Zeit (s) ÷ 8
> ```
>
> ---
>
> **Bild 1 – Full-HD (1920 × 1080, 24 Bit Farbtiefe):**
> ```
> Speicher = 1920 × 1080 × 24 ÷ 8
>          = 2.073.600 Pixel × 3 Byte/Pixel
>          = 6.220.800 Byte
>          = 6.220.800 ÷ 1.048.576
>          ≈ 5,93 MiB
>          ≈ 6,22 MB (dezimal)
> ```
> **Ergebnis: ca. 5,93 MiB (≈ 6,22 MB)**
>
> ---
>
> **Bild 2 – 4K (3840 × 2160, 32 Bit Farbtiefe):**
> ```
> Speicher = 3840 × 2160 × 32 ÷ 8
>          = 8.294.400 Pixel × 4 Byte/Pixel
>          = 33.177.600 Byte
>          = 33.177.600 ÷ 1.048.576
>          ≈ 31,64 MiB
>          ≈ 33,18 MB (dezimal)
> ```
> **Ergebnis: ca. 31,64 MiB (≈ 33,18 MB)**
>
> ---
>
> **Audio – 3 Minuten (44.100 Hz, 16 Bit, Stereo):**
> ```
> Zeit in Sekunden = 3 × 60 = 180 s
> Kanäle (Stereo)  = 2
>
> Speicher = 44.100 × 16 × 2 × 180 ÷ 8
>          = 44.100 × 2 × 180 × 2 Byte
>          = 44.100 × 720
>          = 31.752.000 Byte
>          = 31.752.000 ÷ 1.048.576
>          ≈ 30,28 MiB
>          ≈ 31,75 MB (dezimal)
> ```
> **Ergebnis: ca. 30,28 MiB (≈ 31,75 MB)**
>
> ---
>
> **Zusammenfassung:**
>
> | Datei | Parameter | Speicher (unkomprimiert) |
> | --- | --- | --- |
> | Full-HD Bild | 1920×1080, 24 Bit | ≈ 5,93 MiB |
> | 4K Bild | 3840×2160, 32 Bit | ≈ 31,64 MiB |
> | 3 min Audio | 44.100 Hz, 16 Bit, Stereo | ≈ 30,28 MiB |

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
