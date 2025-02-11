# Verschluesselung_v1

## Über das Projekt

Dieses Python-Projekt bietet eine einfache Möglichkeit, Dateien zu verschlüsseln und zu entschlüsseln. Es basiert auf einer symmetrischen Verschlüsselungsmethode, um sensible Daten sicher zu speichern oder zu übertragen.

## Installation

### Voraussetzungen
- Python 3.x
- Virtuelle Umgebung (`venv`)
- Abhängigkeiten aus `requirements.txt`

### Einrichtung
1. Klone das Repository:
   ```bash
   git clone https://github.com/OnkelT/verschluesselung_v1.git
   cd verschluesselung_v1
   ```
2. Aktiviere die virtuelle Umgebung:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Installiere die erforderlichen Pakete:
   ```bash
   pip install -r requirements.txt
   ```

## Nutzung

Das Programm bietet die Möglichkeit, Dateien zu verschlüsseln und zu entschlüsseln.

### Datei verschlüsseln
```bash
python encrypt.py -i <input_datei> -o <output_datei>
```

### Datei entschlüsseln
```bash
python decrypt.py -i <input_datei> -o <output_datei>
```

## Features
- Einfache Dateiverschlüsselung mit Python
- Nutzung einer sicheren symmetrischen Verschlüsselung
- Befehlsgesteuerte Nutzung für einfache Automatisierung

## Lizenz
Dieses Projekt ist unlizensiert.

## Autor
Erstellt von [OnkelT](https://github.com/OnkelT).

*Dieser Text ist KI-Generiert

