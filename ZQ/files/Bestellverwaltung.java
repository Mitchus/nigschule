import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Bestellverwaltung {

    // ─────────────────────────────────────────────
    // Datenmodell
    // ─────────────────────────────────────────────

    static class Bestellposition {
        String produktname;
        double einzelpreis;
        int menge;

        Bestellposition(String produktname, double einzelpreis, int menge) {
            this.produktname = produktname;
            this.einzelpreis = einzelpreis;
            this.menge = menge;
        }

        double gesamtpreis() {
            return einzelpreis * menge;
        }
    }

    static class Bestellung {
        int id;
        String kundenname;
        List<Bestellposition> positionen = new ArrayList<>();

        Bestellung(int id, String kundenname) {
            this.id = id;
            this.kundenname = kundenname;
        }

        double gesamtpreis() {
            return positionen.stream().mapToDouble(Bestellposition::gesamtpreis).sum();
        }
    }

    // ─────────────────────────────────────────────
    // Globaler Zustand
    // ─────────────────────────────────────────────

    static final String JSON_DATEI = "bestellungen.json";
    static List<Bestellung> bestellungen = new ArrayList<>();
    static int naechsteId = 1;
    static Scanner scanner = new Scanner(System.in);

    // ─────────────────────────────────────────────
    // Main
    // ─────────────────────────────────────────────

    public static void main(String[] args) {
        laden();
        boolean laufen = true;
        while (laufen) {
            zeigeMenu();
            int wahl = leseInt("Ihre Wahl: ", 0, 6);
            System.out.println();
            switch (wahl) {
                case 0 -> laufen = false;
                case 1 -> neueBestellung();
                case 2 -> alleBestellungenAnzeigen();
                case 3 -> einzelneBestellungAnzeigen();
                case 4 -> produktHinzufuegen();
                case 5 -> bestellungLoeschen();
                case 6 -> gesamtsummeAnzeigen();
            }
            if (laufen) {
                System.out.println();
                System.out.print("Drücken Sie ENTER um fortzufahren...");
                scanner.nextLine();
                System.out.println();
            }
        }
        System.out.println("╔══════════════════════════════╗");
        System.out.println("║  Auf Wiedersehen!            ║");
        System.out.println("╚══════════════════════════════╝");
    }

    // ─────────────────────────────────────────────
    // Menü-Anzeige
    // ─────────────────────────────────────────────

    static void zeigeMenu() {
        System.out.println("╔══════════════════════════════════════╗");
        System.out.println("║       BESTELLVERWALTUNG              ║");
        System.out.println("╠══════════════════════════════════════╣");
        System.out.println("║  1  Neue Bestellung anlegen          ║");
        System.out.println("║  2  Alle Bestellungen anzeigen       ║");
        System.out.println("║  3  Einzelne Bestellung anzeigen     ║");
        System.out.println("║  4  Produkt hinzufügen               ║");
        System.out.println("║  5  Bestellung löschen               ║");
        System.out.println("║  6  Gesamtsumme aller Bestellungen   ║");
        System.out.println("║  0  Beenden                          ║");
        System.out.println("╚══════════════════════════════════════╝");
    }

    // ─────────────────────────────────────────────
    // Menü-Aktionen
    // ─────────────────────────────────────────────

    static void neueBestellung() {
        System.out.println("┌─────────────────────────────────┐");
        System.out.println("│     NEUE BESTELLUNG ANLEGEN     │");
        System.out.println("└─────────────────────────────────┘");
        String kundenname = leseNichtLeerenString("Kundenname: ");
        Bestellung bestellung = new Bestellung(naechsteId++, kundenname);

        System.out.println("Produkte eingeben (leerer Name = fertig):");
        while (true) {
            String produktname = leseOptionalenString("  Produktname (leer=fertig): ");
            if (produktname.isEmpty()) break;
            double preis = lesePositivenDouble("  Einzelpreis: ");
            int menge = lesePositivenInt("  Menge: ");
            bestellung.positionen.add(new Bestellposition(produktname, preis, menge));
            System.out.println("  ✓ Produkt hinzugefügt.");
        }

        bestellungen.add(bestellung);
        speichern();
        System.out.println("✓ Bestellung #" + bestellung.id + " für \"" + bestellung.kundenname + "\" angelegt.");
    }

    static void alleBestellungenAnzeigen() {
        if (bestellungen.isEmpty()) {
            System.out.println("Keine Bestellungen vorhanden.");
            return;
        }
        for (Bestellung b : bestellungen) {
            zeigeBestellung(b);
            System.out.println();
        }
        double gesamt = bestellungen.stream().mapToDouble(Bestellung::gesamtpreis).sum();
        zeigeGesamtsummenBox(gesamt, bestellungen.size());
    }

    static void einzelneBestellungAnzeigen() {
        int id = leseInt("Bestellungs-ID: ", 1, Integer.MAX_VALUE);
        Bestellung b = findeBestellungNachId(id);
        if (b == null) {
            System.out.println("⚠ Bestellung #" + id + " nicht gefunden.");
            return;
        }
        zeigeBestellung(b);
    }

    static void produktHinzufuegen() {
        int id = leseInt("Bestellungs-ID: ", 1, Integer.MAX_VALUE);
        Bestellung b = findeBestellungNachId(id);
        if (b == null) {
            System.out.println("⚠ Bestellung #" + id + " nicht gefunden.");
            return;
        }
        String produktname = leseNichtLeerenString("Produktname: ");
        double preis = lesePositivenDouble("Einzelpreis: ");
        int menge = lesePositivenInt("Menge: ");
        b.positionen.add(new Bestellposition(produktname, preis, menge));
        speichern();
        System.out.println("✓ Produkt zu Bestellung #" + id + " hinzugefügt.");
    }

    static void bestellungLoeschen() {
        int id = leseInt("Bestellungs-ID zum Löschen: ", 1, Integer.MAX_VALUE);
        Bestellung b = findeBestellungNachId(id);
        if (b == null) {
            System.out.println("⚠ Bestellung #" + id + " nicht gefunden.");
            return;
        }
        bestellungen.remove(b);
        speichern();
        System.out.println("✓ Bestellung #" + id + " gelöscht.");
    }

    static void gesamtsummeAnzeigen() {
        double gesamt = bestellungen.stream().mapToDouble(Bestellung::gesamtpreis).sum();
        zeigeGesamtsummenBox(gesamt, bestellungen.size());
    }

    // ─────────────────────────────────────────────
    // Ausgabe-Hilfsmethoden
    // ─────────────────────────────────────────────

    static void zeigeBestellung(Bestellung b) {
        String header = " Bestellung #" + b.id + " – " + b.kundenname;
        System.out.println("┌─────────────────────────────────────────────────────────────┐");
        System.out.printf("│ %-61s│%n", header);
        System.out.println("├───────────────────────────┬────────┬─────────────┬────────────┤");
        System.out.printf("│ %-25s │ %6s │ %11s │ %10s │%n", "Produkt", "Menge", "Einzelpreis", "Gesamtpreis");
        System.out.println("├───────────────────────────┼────────┼─────────────┼────────────┤");
        if (b.positionen.isEmpty()) {
            System.out.println("│           (Keine Positionen vorhanden)                      │");
        } else {
            for (Bestellposition p : b.positionen) {
                String name = p.produktname.length() > 25
                        ? p.produktname.substring(0, 22) + "..."
                        : p.produktname;
                System.out.printf("│ %-25s │ %6d │ %9.2f € │ %8.2f € │%n",
                        name, p.menge, p.einzelpreis, p.gesamtpreis());
            }
        }
        System.out.println("├───────────────────────────┴────────┴─────────────┴────────────┤");
        System.out.printf("│ %-44s %14.2f € │%n", "Gesamtpreis:", b.gesamtpreis());
        System.out.println("└─────────────────────────────────────────────────────────────────┘");
    }

    static void zeigeGesamtsummenBox(double gesamt, int anzahl) {
        System.out.println("╔══════════════════════════════════════════╗");
        System.out.printf( "║  Anzahl Bestellungen: %-20d║%n", anzahl);
        System.out.println("╠══════════════════════════════════════════╣");
        System.out.printf( "║  GESAMTSUMME: %26.2f € ║%n", gesamt);
        System.out.println("╚══════════════════════════════════════════╝");
    }

    static Bestellung findeBestellungNachId(int id) {
        return bestellungen.stream().filter(b -> b.id == id).findFirst().orElse(null);
    }

    // ─────────────────────────────────────────────
    // Eingabe-Hilfsmethoden
    // ─────────────────────────────────────────────

    static int leseInt(String prompt, int min, int max) {
        while (true) {
            System.out.print(prompt);
            String zeile = scanner.nextLine().trim();
            try {
                int wert = Integer.parseInt(zeile);
                if (wert >= min && wert <= max) return wert;
                System.out.println("⚠ Bitte einen Wert zwischen " + min + " und " + max + " eingeben.");
            } catch (NumberFormatException e) {
                System.out.println("⚠ Ungültige Eingabe. Bitte eine ganze Zahl eingeben.");
            }
        }
    }

    static int lesePositivenInt(String prompt) {
        while (true) {
            System.out.print(prompt);
            String zeile = scanner.nextLine().trim();
            try {
                int wert = Integer.parseInt(zeile);
                if (wert > 0) return wert;
                System.out.println("⚠ Bitte eine positive Zahl (> 0) eingeben.");
            } catch (NumberFormatException e) {
                System.out.println("⚠ Ungültige Eingabe. Bitte eine ganze Zahl eingeben.");
            }
        }
    }

    static double lesePositivenDouble(String prompt) {
        while (true) {
            System.out.print(prompt);
            String zeile = scanner.nextLine().trim().replace(',', '.');
            try {
                double wert = Double.parseDouble(zeile);
                if (wert > 0) return wert;
                System.out.println("⚠ Bitte eine positive Zahl eingeben.");
            } catch (NumberFormatException e) {
                System.out.println("⚠ Ungültige Eingabe. Bitte eine Dezimalzahl eingeben (z.B. 9,99).");
            }
        }
    }

    static String leseNichtLeerenString(String prompt) {
        while (true) {
            System.out.print(prompt);
            String zeile = scanner.nextLine().trim();
            if (!zeile.isEmpty()) return zeile;
            System.out.println("⚠ Eingabe darf nicht leer sein.");
        }
    }

    static String leseOptionalenString(String prompt) {
        System.out.print(prompt);
        return scanner.nextLine().trim();
    }

    // ─────────────────────────────────────────────
    // JSON-Writer
    // ─────────────────────────────────────────────

    static String zuJson() {
        StringBuilder sb = new StringBuilder();
        sb.append("[\n");
        for (int i = 0; i < bestellungen.size(); i++) {
            Bestellung b = bestellungen.get(i);
            sb.append("  {\n");
            sb.append("    \"id\": ").append(b.id).append(",\n");
            sb.append("    \"kundenname\": \"").append(jsonEscape(b.kundenname)).append("\",\n");
            sb.append("    \"positionen\": [\n");
            for (int j = 0; j < b.positionen.size(); j++) {
                Bestellposition p = b.positionen.get(j);
                sb.append("      {\n");
                sb.append("        \"produktname\": \"").append(jsonEscape(p.produktname)).append("\",\n");
                sb.append("        \"einzelpreis\": ").append(p.einzelpreis).append(",\n");
                sb.append("        \"menge\": ").append(p.menge).append("\n");
                sb.append("      }");
                if (j < b.positionen.size() - 1) sb.append(",");
                sb.append("\n");
            }
            sb.append("    ]\n");
            sb.append("  }");
            if (i < bestellungen.size() - 1) sb.append(",");
            sb.append("\n");
        }
        sb.append("]");
        return sb.toString();
    }

    static String jsonEscape(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            switch (c) {
                case '"'  -> sb.append("\\\"");
                case '\\' -> sb.append("\\\\");
                case '\n' -> sb.append("\\n");
                case '\r' -> sb.append("\\r");
                case '\t' -> sb.append("\\t");
                default   -> sb.append(c);
            }
        }
        return sb.toString();
    }

    // ─────────────────────────────────────────────
    // JSON-Parser (Zustandsautomat)
    // ─────────────────────────────────────────────

    static List<String> splitTopLevelObjects(String json) {
        List<String> objekte = new ArrayList<>();
        int tiefe = 0;
        int start = -1;
        boolean inString = false;
        boolean escape = false;
        for (int i = 0; i < json.length(); i++) {
            char c = json.charAt(i);
            if (escape) { escape = false; continue; }
            if (c == '\\' && inString) { escape = true; continue; }
            if (c == '"') { inString = !inString; continue; }
            if (inString) continue;
            if (c == '{') {
                if (tiefe == 0) start = i;
                tiefe++;
            } else if (c == '}') {
                tiefe--;
                if (tiefe == 0 && start >= 0) {
                    objekte.add(json.substring(start, i + 1));
                    start = -1;
                }
            }
        }
        return objekte;
    }

    static String jsonStringFeld(String json, String feld) {
        String suche = "\"" + feld + "\"";
        int pos = json.indexOf(suche);
        if (pos < 0) return "";
        pos += suche.length();
        while (pos < json.length() && json.charAt(pos) != '"') pos++;
        if (pos >= json.length()) return "";
        pos++; // überspringe öffnendes "
        StringBuilder sb = new StringBuilder();
        boolean escape = false;
        while (pos < json.length()) {
            char c = json.charAt(pos);
            if (escape) {
                switch (c) {
                    case '"'  -> sb.append('"');
                    case '\\' -> sb.append('\\');
                    case 'n'  -> sb.append('\n');
                    case 'r'  -> sb.append('\r');
                    case 't'  -> sb.append('\t');
                    default   -> sb.append(c);
                }
                escape = false;
            } else if (c == '\\') {
                escape = true;
            } else if (c == '"') {
                break;
            } else {
                sb.append(c);
            }
            pos++;
        }
        return sb.toString();
    }

    static String jsonFeld(String json, String feld) {
        String suche = "\"" + feld + "\"";
        int pos = json.indexOf(suche);
        if (pos < 0) return "";
        pos += suche.length();
        while (pos < json.length() && json.charAt(pos) != ':') pos++;
        pos++; // überspringe :
        while (pos < json.length() && Character.isWhitespace(json.charAt(pos))) pos++;
        StringBuilder sb = new StringBuilder();
        while (pos < json.length()) {
            char c = json.charAt(pos);
            if (c == ',' || c == '\n' || c == '\r' || c == '}') break;
            sb.append(c);
            pos++;
        }
        return sb.toString().trim();
    }

    static String jsonArray(String json, String feld) {
        String suche = "\"" + feld + "\"";
        int pos = json.indexOf(suche);
        if (pos < 0) return "[]";
        pos += suche.length();
        while (pos < json.length() && json.charAt(pos) != '[') pos++;
        int start = pos;
        int tiefe = 0;
        boolean inString = false;
        boolean escape = false;
        while (pos < json.length()) {
            char c = json.charAt(pos);
            if (escape) { escape = false; pos++; continue; }
            if (c == '\\' && inString) { escape = true; pos++; continue; }
            if (c == '"') { inString = !inString; pos++; continue; }
            if (!inString) {
                if (c == '[') tiefe++;
                else if (c == ']') {
                    tiefe--;
                    if (tiefe == 0) return json.substring(start, pos + 1);
                }
            }
            pos++;
        }
        return "[]";
    }

    static String jsonUnescape(String s) {
        StringBuilder sb = new StringBuilder();
        boolean escape = false;
        for (char c : s.toCharArray()) {
            if (escape) {
                switch (c) {
                    case '"'  -> sb.append('"');
                    case '\\' -> sb.append('\\');
                    case 'n'  -> sb.append('\n');
                    case 'r'  -> sb.append('\r');
                    case 't'  -> sb.append('\t');
                    default   -> sb.append(c);
                }
                escape = false;
            } else if (c == '\\') {
                escape = true;
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    // ─────────────────────────────────────────────
    // Persistenz
    // ─────────────────────────────────────────────

    static void laden() {
        Path pfad = Path.of(JSON_DATEI);
        if (!Files.exists(pfad)) {
            System.out.println("ℹ Keine Datei gefunden – starte mit leerer Bestellliste.");
            return;
        }
        try {
            String inhalt = Files.readString(pfad);
            bestellungen.clear();
            naechsteId = 1;
            List<String> objekte = splitTopLevelObjects(inhalt);
            for (String obj : objekte) {
                int id = 0;
                try { id = Integer.parseInt(jsonFeld(obj, "id")); } catch (NumberFormatException ignored) {}
                String kundenname = jsonStringFeld(obj, "kundenname");
                Bestellung b = new Bestellung(id, kundenname);
                String posArray = jsonArray(obj, "positionen");
                List<String> posObjekte = splitTopLevelObjects(posArray);
                for (String pObj : posObjekte) {
                    String produktname = jsonStringFeld(pObj, "produktname");
                    double einzelpreis = 0;
                    int menge = 0;
                    try { einzelpreis = Double.parseDouble(jsonFeld(pObj, "einzelpreis")); } catch (NumberFormatException ignored) {}
                    try { menge = Integer.parseInt(jsonFeld(pObj, "menge")); } catch (NumberFormatException ignored) {}
                    b.positionen.add(new Bestellposition(produktname, einzelpreis, menge));
                }
                bestellungen.add(b);
                if (id >= naechsteId) naechsteId = id + 1;
            }
            System.out.println("✓ " + bestellungen.size() + " Bestellung(en) geladen.");
        } catch (IOException e) {
            System.out.println("⚠ Fehler beim Laden: " + e.getMessage() + " – starte leer.");
        }
    }

    static void speichern() {
        try {
            Files.writeString(Path.of(JSON_DATEI), zuJson());
        } catch (IOException e) {
            System.out.println("⚠ Fehler beim Speichern: " + e.getMessage());
        }
    }
}
