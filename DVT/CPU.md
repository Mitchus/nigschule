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

Hyperthreading
Die Intel® Hyper-Threading-Technik ist eine Hardware-Innovation, mit der mehr als ein Thread auf jedem Kern ausgeführt werden kann. Mehr Threads bedeutet, dass mehr Arbeit parallel erfolgen kann.

Wie funktioniert Hyper-Threading? Wenn die Intel® Hyper-Threading-Technik aktiv ist, legt die CPU zwei Ausführungskontexte pro physischem Kern frei. Das bedeutet, dass nun ein physischer Kern wie zwei „logische Kerne“ funktioniert, die verschiedene Software-Threads verwenden können.

Zwei logische Kerne können sich effizienter durch Aufgaben arbeiten als ein traditioneller Single-Thread-Kern. Durch die Nutzung der Leerlaufzeit, in der ein CPU-Kern zuvor auf den Abschluss der Ausführung anderer Aufgaben gewartet hätte, erhöht die Intel® Hyper-Threading-Technik den CPU-Durchsatz.


	
Turbo Boost
Wie funktioniert es?
	
Der Prozessor taktet vorübergehend höher, wenn er unter Last arbeitet und noch thermische Reserven hat
Wann wird es aktiviert?
	
Automatisch, wenn das Betriebssystem die höchstmögliche Leistung abfragt
Was bringt es?
	
Steigerung der Leistung bei Single- und Multi-Thread Anwendungen


# Ausführung eines Befehls durch die CPU

Die Ausführung eines Befehls durch die CPU durchläuft verschiedene Phasen. Ein solcher Durchlauf wird als _Befehlszyklus_bezeichnet.

Liegt eine von Neumann Architektur vor, wird dieser Befehlszyklus in fünf Phasen eingeteilt (Von Neumann Zyklus).  
Liegt eine Harvard Architektur vor können zwei der fünf Phasen zusammengefasst werden. Der Befehlszyklus besteht dann aus vier Phasen.

## Von Neumann Zyklus

![Von Neumann Zyklus](http://mathe-mit-methode.com/schlaufuchs_web/elektrotechnik/computer_lernmaterial/computer_grundlagen/cpu_aufbau/formeln/von_neumann_zyklus_01.png "Von Neumann Zyklus")

Von Neumann Zyklus

1. `FETCH`  
    Die Instruktion (Maschinenbefehl) muss aus dem Speicher geladen werden. Dies bedeutet, dass auf dem Datenbus der Maschinencode für den Befehl liegt.
2. `DECODE`  
    Der Maschinenbefehl muss nun von der CU decodiert werden. Diese gibt über den Steuerbus die Funktion der ALU und ggf. weiterer Komponenten vor.
3. `FETCH OPERANDS`  
    In dieser Phase werden ggf. für die Ausführung des Befehls benötigte Operanden in die dafür vorgesehenen Register geladen.
4. `EXECUTE`  
    Der Befehl wird von der ALU ausgeführt.
5. `WRITE BACK`  
    Die Ergebnisse der Berechnung werden in den Speicher geschrieben.

## Harvard Zyklus

Für die Harvard Architektur können die Phasen 1 und 3 des von Neumann Zyklus zusammengefasst werden. Operanden und Instruktionen können gleichzeitig geladen werden, da unterschiedliche Bus-Systeme involviert sind. Der Befehlszyklus hat also nur vier Phasen.

1. `FETCH`  
    Die Instruktion (Maschinenbefehl) muss aus dem Programmspeicher geladen werden. Aus dem Datenspeicher werden die Operanden in die dafür vorgesehenen Register geladen.
2. `DECODE`  
    Der Maschinenbefehl muss nun von der CU decodiert werden. Diese gibt über den Steuerbus die Funktion der ALU und ggf. weiterer Komponenten vor.
3. `EXECUTE`  
    Der Befehl wird von der ALU ausgeführt.
4. `WRITE BACK`  
    Die Ergebnisse der Berechnung werden in den Speicher geschrieben.


A
D
S
T
