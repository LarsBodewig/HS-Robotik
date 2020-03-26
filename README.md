# SS_20_Robotik_T01

## Challenges

1. Fahren/Steuern: beliebige Bewegung
2. Random Walk: zufällige Bewegung ohne überfahren der Außenlinien
    Außenlinie: Verwendung der Sensoren am Unterboden
3. Billiard: bei Treffen der Außenlinie im Winkel abprallen
    Außenlinie: Verwendung der Sensoren am Unterboden
    Winkel: Verwendung der Kamera und Ecken
4. Kamera Lokalisierung: Positionsbestimmung auf dem Spielfeld
    Winkel und Farben: Verwendung der Kamera und farblich markierte Ecken
5. Fernsteuerung mit Bild via mobile Device (inkl. Dashboard)
    Bild: Verwendung der Kamera
    Verbindung: ?

## Projektstruktur

- `commons` enthält die wiederverwendbaren Module
- Hardwarefunktionen (Servo, Kamera, Entfernungssensor, etc.) sind Attribute von `AlphaBot`
- Aufgaben importieren `AlphaBot`, um die Hardwarefunktionen verwenden zu können
- Aufgaben können als Script ausgeführt oder als Modul importiert werden

## Abgabe

- in Form eines Videos, das die Erfüllung der Aufgabe zeigt
- Namensschema: SS20-OptRob-T01-Ch[0-5]

---

Run `git config --add include.path ../.gitconfig` to include the template config in your project config.
