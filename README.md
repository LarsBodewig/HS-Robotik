# SS_20_Robotik_T01

## Challenges

1. Fahren/Steuern: beliebige Bewegung
2. Random Walk: zuf�llige Bewegung ohne �berfahren der Au�enlinien
    Au�enlinie: Verwendung der Sensoren am Unterboden
3. Billiard: bei Treffen der Au�enlinie im Winkel abprallen
    Au�enlinie: Verwendung der Sensoren am Unterboden
    Winkel: Verwendung der Kamera und Ecken
4. Kamera Lokalisierung: Positionsbestimmung auf dem Spielfeld
    Winkel und Farben: Verwendung der Kamera und farblich markierte Ecken
5. Fernsteuerung mit Bild via mobile Device (inkl. Dashboard)
    Bild: Verwendung der Kamera
    Verbindung: ?

## Projektstruktur
- `commons` enth�lt die wiederverwendbaren Module
- Hardwarefunktionen (Servo, Kamera, Entfernungssensor, etc.) sind Attribute von `AlphaBot`
- Aufgaben importieren `AlphaBot`, um die Hardwarefunktionen verwenden zu k�nnen
- Aufgaben k�nnen als Script ausgef�hrt oder als Modul importiert werden

## Abgabe
- in Form eines Videos, das die Erf�llung der Aufgabe zeigt
- Namensschema: SS20-OptRob-T01-Ch[0-5]

##Fragen
- Was passiert wenn der Bot mit 90 ° auf eine Linie trifft (Aufgabe 3 Billiard) bzw. knapp 90 grad

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


hinweis herr kuntze: Odometrie des robotors getrennt (links / rechts)
  kamara hat ebenfalls motoren
