# Einteilung von Daten nach Struktur

## 🔹 Strukturierte Daten

**Beschreibung:**
- Fester Aufbau, meist in Tabellen / Datenbanken gespeichert.
    
- Leicht maschinell verarbeitbar.
    

**Eigenschaften:**
- Klare Datentypen (Zahlen, Strings, Datumswerte).
    
- Einfache Speicherung in relationalen DBs (SQL).
    
- Eindeutige Such- und Filtermöglichkeiten.
    

**Einsatzgebiete:**
- Finanzwesen, Kundendatenbanken, Lagerverwaltung, ERP-Systeme.
    

**Beispiele:**

- Kundennummer, Name, Adresse, Rechnungsbetrag, Temperaturwerte.
    

**Vorteile:**  
✅ Effiziente Verarbeitung und Analyse  
✅ Standardisierte Formate (SQL, CSV)  
✅ Hohe Datenqualität und Konsistenz

**Nachteile:**  
❌ Eingeschränkt in Vielfalt (nur vordefinierte Formate)  
❌ Keine Abbildung komplexer Daten (z. B. Bilder, Sprache)

---

## 🔹 Semi-strukturierte Daten

**Beschreibung:**
- Teilweise strukturierte Form, Mischung aus klarer Struktur + freiem Inhalt.
    
- Flexibler als strukturierte, aber besser maschinell lesbar als unstrukturierte Daten.
    

**Eigenschaften:**
- Daten enthalten Tags oder Schlüssel-Wert-Paare.
    
- Keine feste Tabellenstruktur nötig.
    
- Gut für Austausch und Speicherung in flexiblen Systemen.
    

**Einsatzgebiete:**
- Web- & App-Daten, Konfigurationsdateien, Datenintegration.
    

**Beispiele:**
- XML, JSON, HTML, E-Mails (Header = strukturiert, Body = unstrukturiert).
    

**Vorteile:**  
✅ Flexibel anpassbar  
✅ Mensch + Maschine können es lesen  
✅ Ideal für Datenaustausch (APIs, Webservices)

**Nachteile:**  
❌ Verarbeitung komplexer als bei strukturierten Daten  
❌ Höherer Speicher- und Analyseaufwand  
❌ Standardisierung schwieriger

---

## 🔹 Unstrukturierte Daten


**Beschreibung:**
- Keine feste Struktur, schwer automatisiert auswertbar.

**Eigenschaften:**
- Große Vielfalt (Texte, Bilder, Audio, Video).
- Wichtiger Bestandteil von Big Data.

**Einsatzgebiete:**
- Social Media, Kommunikation, Multimedia, Kundenfeedback.

**Beispiele:**
- E-Mails, Fotos, Videos, Chatnachrichten.

**Vorteile:**  
✅ Sehr vielfältig, flexibel  
✅ Reichhaltige Informationsquelle

**Nachteile:**  
❌ Schwer analysierbar  
❌ Hoher Speicher- & Verarbeitungsaufwand

### 📊 **Quantitative Daten**

- **Definition**: Zahlenbasierte, messbare Daten → liefern **Mengenangaben**.
    
- **Eigenschaften**:
    
    - Objektiv messbar (z. B. Länge, Gewicht, Temperatur, Zeit).
        
    - Lassen sich mathematisch/statistisch berechnen (Durchschnitt, Summe, Varianz).
        
    - Darstellung oft in Diagrammen wie Balken-, Linien- oder Punktdiagramm.
        
- **Unterarten**:
    
    - **Diskrete Daten** → Zählbar, nur ganze Zahlen möglich (z. B. Anzahl von Kindern, Autos, Fehlern im Code).
        
    - **Stetige Daten** → Messbar mit beliebiger Genauigkeit (z. B. Körpergröße in cm, Temperatur in °C).
        
- **Beispiele**:
    
    - Einkommen in Euro
        
    - Blutdruckwerte
        
    - Geschwindigkeit in km/h
        
- **Vorteile**:
    
    - Gut vergleichbar und analysierbar
        
    - Mathematisch/statistisch stark auswertbar
        
- **Nachteile**:
    
    - Keine direkten Informationen zu „Qualität“ oder „Art“
        
    - Abstrakter → kann manchmal den Kontext verbergen
        

---

### 📑 **Qualitative Daten**

- **Definition**: Beschreibende, nicht-messbare Daten → liefern **Merkmale/Kategorien**.
    
- **Eigenschaften**:
    
    - Subjektiver und beschreibender Charakter (z. B. Farbe, Meinung, Geschlecht).
        
    - Ordnen Objekte in **Klassen** oder **Merkmalsausprägungen** ein.
        
    - Keine mathematische Berechnung (kein Mittelwert sinnvoll).
        
- **Unterarten**:
    
    - **Nominalskaliert** → reine Kategorien, keine Rangfolge (z. B. Nationalität, Religion, Automarke).
        
    - **Ordinalskaliert** → Kategorien mit Rangordnung, aber ohne genaue Abstände (z. B. Schulnoten, Zufriedenheitsskala, Platzierung im Sport).
        
- **Beispiele**:
    
    - Haarfarbe (blond, braun, schwarz)
        
    - Ja/Nein-Antworten
        
    - Berufskategorie
        
- **Vorteile**:
    
    - Liefert wichtige Zusatzinfos (Meinungen, Eigenschaften, Gruppen).
        
    - Oft leichter zu erheben (z. B. Umfragen mit Kategorien).
        
- **Nachteile**:
    
    - Weniger genau, keine Berechnung von Mittelwerten etc.
        
    - Nur eingeschränkte statistische Verfahren möglich

Ist besser um gesamtbild der Situation zu bekommen

1  material manufacturing 
2 automotive technology wheels copany
3 sheetmetal-factory  
4 independent
5 IT sysintegration
