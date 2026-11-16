---
title: Die Steine auf eine Spiel-Engine bringen
description: Warum die fallenden Steine und andere bewegte Teile von Sunmeld jetzt auf einer Spiel-Engine laufen und wie wir sie geprüft haben.
slug: stones-on-a-game-engine
lang: de
category: devlog
keywords: Sunmeld, Flame, Engine, Animation, Leistung, Journal
translation_of: en
---
Sunmeld ist weiterhin in Entwicklung für iOS und Android. Diese Notiz handelt davon, wie die bewegten Teile des Spiels gezeichnet werden.

## Zuerst jede Bewegung auflisten

Bevor wir etwas änderten, haben wir jede Bewegung im Spiel aufgeschrieben: Steine, die fallen und anstoßen, das Leuchten beim Zusammenschluss, die Punkte, die aufpoppen, die Warnlinie, die Zielhilfe und die obere Leiste mit Punkten und Zeit. Bei jeder fragten wir, wie viel Arbeit sie pro Bild auf dem Bildschirm verursacht. Manche waren günstig. Andere waren teuer, etwa das Zeichnen eines Steins mit Verlauf und weichem Glanz bei jedem einzelnen Bild.

## Einmal zeichnen, viele Mal bewegen

Die gewählte Engine ist Flame, eine Spiel-Engine, die auf Flutter läuft. Die Steine und das Glas werden jetzt einmal als Bilder gezeichnet und bei jedem Bild platziert. Das Leuchten beim Zusammenschluss ist eine fertige weiche Form mit darübergelegter Farbe. Der Punktetext wird im Voraus vorbereitet. Die Regeln haben sich nicht geändert: Dieselbe Physik übernimmt das Fallen und das Zusammenschließen.

## Auf dem Computer geprüft, noch nicht auf dem Telefon

Wir haben auf einem Mac im Profilmodus gemessen, und die Bilder blieben innerhalb ihres Zeitbudgets. Das ist ein Computer, nicht dein Telefon. Das Ergebnis auf einem echten iPhone oder Android-Gerät mit voller Bildwiederholrate haben wir noch nicht geprüft, daher ist die Flüssigkeit auf echten Geräten noch offen.

## Warum die Engine

Die Zeichenwerkzeuge von Flutter könnten das auch. Wir haben keinen Vergleichstest nebeneinander gemacht, deshalb behaupten wir nicht, dass die Engine schneller ist. Wir haben sie gewählt, weil alle bewegten Teile jetzt in einer Schleife laufen, was es leichter macht, das Spiel flüssig zu halten, während es wächst.

## Was als Nächstes kommt

Der letzte Schritt ist, das Gefühl auf echten Geräten mit hoher Bildwiederholrate zu prüfen und die kleinen Bildschirme noch einmal anzusehen. Ein Veröffentlichungstermin steht noch nicht fest.

## Häufige Fragen

### Hat sich die Spielweise geändert?

Nein. Die Regeln und die Physik sind geblieben. Geändert haben sich nur das Zeichnen und das Timing der bewegten Teile.

### Warum eine Spiel-Engine verwenden?

Alle bewegten Teile laufen jetzt in einer Schleife, sodass das Spiel nicht mehr den ganzen Bildschirm für jede kleine Bewegung neu aufbauen muss.

### Wurde es auf einem Telefon getestet?

Bisher wurde auf einem Computer gemessen. Der Test auf einem echten Telefon steht noch aus.
