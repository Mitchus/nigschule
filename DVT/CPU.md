# CPU (Central Processing Unit)
- CPU ist das Gehirn des Computers.
- Sie besteht aus mehreren Kernen, auf denen Threads ausgeführt werden können.


**Allgemeiner Befehlszyklus:**
- **Fetch (Holen):** Abruf der nächsten Instruktion aus dem Speicher
- **Decode (Dekodieren):** Übersetzung der Instruktion in Steuerbefehle.
- **Execute (Ausführen):** Durchführung der Operation (Rechenoperation, Datenzugriff etc.).
- Dieser Zyklus wiederholt sich ständig, solange der Prozessor in Betrieb ist.
  
**Aufbau und Komponenten**
- Mehrere Kerne, die parallel arbeiten.
- Cache-Hierarchien (L1, L2, L3) zur Beschleunigung von Speicherzugriffen.
- Integrierte Grafik- und andere spezialisierte Einheiten.
- Steuerwerk, Rechenwerk, Registersatz und Bussystem, die zusammenarbeiten, um Instruktionen effizient zu verarbeiten.


- **Aufgaben der Komponenten:**
    - **Steuerwerk:** Koordiniert den Befehlszyklus und steuert alle Komponenten.
    - **Rechenwerk:** Führt arithmetische und logische Operationen durch.
    - **Registersatz:** Kurzzeitspeicher für schnelle Datenzugriffe.
    - **Bussystem:** Verbindet die einzelnen Komponenten und ermöglicht Datentransfer.

## Ablauf eines Befehls

- Befehl laden (vordefinierter Befehlssatz).
- Benötigte Daten laden und in Registern zwischenspeichern.
- Daten verarbeiten in der Arithmetisch-Logischen-Einheit (ALU).
- Daten zurückschreiben.

## Takt

- Die CPU arbeitet in Takten (Einheit in GHz).
- Übertaktung ermöglicht kurzfristige Erhöhung der Taktfrequenz.

## Kerne

- Virtuelle Aufteilung der Kerne steigert die Anzahl der Kerne.
- Ein Kern kann mehrere Threads bearbeiten, erhöht die Auslastung der Kerne.

## Threads

- Threads sind Bearbeitungsabfolgen von Befehlen auf der CPU.
- Mehrere Threads können auf einem Kern ausgeführt werden.

## Benchmarks

- Leistungsmessung durch Tests.
- Vollständige Auslastung der Systemkomponenten.
- Benchmarks ermöglichen Vergleichswerte.

## Zusammenfassung

- CPU ist das zentrale Gehirn des Computers.
- Besteht aus mehreren Kernen, auf denen Threads ausgeführt werden können.