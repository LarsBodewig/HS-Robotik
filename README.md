# SS_20_Robotik_T01

## Challenges

1. Fahren/Steuern: beliebige Bewegung
2. Random Walk: zufällige Bewegung ohne Überfahren der Außenlinien
  * Außenlinie: Verwendung der Sensoren am Unterboden
3. Billiard: bei Treffen der Außenlinie im Winkel abprallen
  * Außenlinie: Verwendung der Sensoren am Unterboden
  * Winkel: Verwendung der Kamera und Ecken
4. Kamera Lokalisierung: Positionsbestimmung auf dem Spielfeld
  * Winkel und Farben: Verwendung der Kamera und farblich markierte Ecken
5. Fernsteuerung mit Bild via mobile Device (inkl. Dashboard)
  * Bild: Verwendung der Kamera
  * Verbindung: ?

## Abgabe

- in Form eines Videos, das die Erfüllung der Aufgabe zeigt, und Code
- Namensschema: SS20-OptRob-T01-Ch`[0-5]`

## Fragen

- Was passiert wenn der Bot mit 90 grad auf eine Linie trifft (Aufgabe 3 Billiard) bzw. knapp 90 grad
- Wie präzise sind die Boden Sensoren
  - 5 sensoren an der unterseite , fast 90 grad
  - wie präzise ist der strich
  - mit den äßeren sensoren messen
  - zeitliche diferenz messen
  - in relation zur vorwärtsbewegung
  - sensor nach unten
  - kamera stellen und spielfed aufnehmen - spiefeld
- Wie soll der Bot reagieren wenn keine Säule im Bild ist, um sich auszurichten
  kamera stellen und spielfed aufnehmen - spiefeld erkennung

## Hinweise von Herr Kuntze

- Odometrie des robotors getrennt (links / rechts)
- Kamera hat ebenfalls motoren

## Frage für Donnerstag
 - Können wir Farbe vor die Säulen malen? da der Roboter bei Treffen genau auf eine Säule sich mit dem Kabel verheddert
  - Linie vor die Säule, oder Säulen ausserhalb des Spielfeldes
  - Bevorzugt Säulen außerhalb des Spielfeldes

## TODO

[X] - SSH deploy key generieren und eintragen
[X] - Werte für Kontrastsensor ermitteln mittels `calibrateSensor.py` -> Werte in `alphabot.py` setzen
[ ] - Aufg3 testen
[ ] - Winkelbestimmung mittels Kontrastsensor konfigurieren

---

Run `git config --add include.path ../.gitconfig` to include the template config in your project config.
