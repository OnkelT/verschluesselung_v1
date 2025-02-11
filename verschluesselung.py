import os
import secrets
import string
import pandas as pd
import py7zr

def generiere_passwort(laenge=16):
    """
    Generiert ein zufälliges Passwort mit der gewünschten Länge.
    Enthalten sind Groß-/Kleinbuchstaben, Ziffern und einige Sonderzeichen.
    """
    zeichen = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(secrets.choice(zeichen) for _ in range(laenge))

def main():
    # Bestimme den Ordner, in dem sich dieses Skript befindet
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Der Ordner mit den zu verschlüsselnden Dateien – hier verwenden wir den Ordner "generierte_dateien"
    input_folder = os.path.join(script_dir, "erzeugte_dateien")
    if not os.path.isdir(input_folder):
        print(f"Der Eingabeordner '{input_folder}' existiert nicht. Bitte stelle sicher, dass er angelegt und befüllt wurde.")
        return

    # Output-Ordner: "verschluesselte_dateien" im gleichen Verzeichnis
    output_folder = os.path.join(script_dir, "verschluesselte_dateien")
    os.makedirs(output_folder, exist_ok=True)

    # CSV-Datei für den Bitwarden-Import (wird im Skriptverzeichnis erstellt)
    csv_filename = os.path.join(script_dir, "bitwarden_import.csv")
    bitwarden_folder_name = "Gesicherte Dokumente"

    # Liste aller Dateien im Input-Ordner
    dateien = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    if not dateien:
        print(f"Es wurden keine Dateien im Ordner '{input_folder}' gefunden.")
        return

    csv_eintraege = []

    print(f"Starte die Verschlüsselung von {len(dateien)} Dateien aus '{input_folder}'...\n")

    for datei in dateien:
        quellpfad = os.path.join(input_folder, datei)
        # Erstelle den Namen der verschlüsselten Datei (Originalname + ".7z")
        ausgabe_datei = datei + ".7z"
        ausgabe_pfad = os.path.join(output_folder, ausgabe_datei)

        passwort = generiere_passwort(16)

        # Verschlüssele die Datei mit py7zr und aktiviere die Header-Verschlüsselung (entspricht -mhe=on)
        try:
            with py7zr.SevenZipFile(ausgabe_pfad, 'w', password=passwort) as archive:
                # Füge die Datei hinzu und speichere sie unter ihrem ursprünglichen Namen im Archiv
                archive.write(quellpfad, arcname=os.path.basename(quellpfad))
            print(f"✔ '{datei}' wurde erfolgreich verschlüsselt.")
        except Exception as e:
            print(f"❌ Fehler beim Verschlüsseln von '{datei}': {e}")
            continue

        # Füge einen Eintrag für die Bitwarden-CSV hinzu
        csv_eintraege.append([bitwarden_folder_name, 0, 0, datei, "", "", "", "", passwort, ""])

    df = pd.DataFrame(csv_eintraege, columns=[
        "folder", "favorite", "type", "name", "notes", "fields",
        "login_uri", "login_username", "login_password", "login_totp"
    ])
    df.to_csv(csv_filename, index=False)

    print(f"\n✅ Verschlüsselung abgeschlossen.")
    print(f"Die verschlüsselten Dateien befinden sich in:\n  {output_folder}")
    print(f"Die Bitwarden-CSV-Datei wurde erstellt:\n  {csv_filename}")

if __name__ == "__main__":
    main()
