---
title: Ein eigener Bildschirm für Tablets
description: Warum Sunmeld auf dem Tablet nicht einfach der gestreckte Handybildschirm ist und wie wir viele Bildschirmgrößen prüfen.
slug: tablet-layouts
lang: de
category: devlog
keywords: Sunmeld, iPad, Layout, Bildschirmgröße, Tests, Journal
translation_of: en
---
Sunmeld ist weiterhin in Entwicklung für iOS und Android. Diese Notiz handelt davon, was passiert, wenn dasselbe Spiel auf einen viel größeren Bildschirm trifft.

## Der erste Versuch: ein Handy in der Mitte

Anfangs zeigte das Spiel auf einem Tablet einfach den Handybildschirm in einer schmalen Spalte in der Mitte. Alles funktionierte, aber der größte Teil des Bildschirms blieb leer. Drehte man das Tablet quer, war es ein in die Breite gezogener Handybildschirm. Zum Testen des Spiels war das in Ordnung, zum Spielen nicht.

## Zwei Layouts statt einem

Tablets zeichnen wir jetzt in zwei getrennten Layouts, Hochformat und Querformat. Im Hochformat wird das Gefäß größer, dein Gegner oben und du unten. Im Querformat sitzt dein Gegner links, das Gefäß in der Mitte und du rechts. Der Ergebnisbildschirm zeigt das Bild auf der einen Seite und Punkte und Buttons auf der anderen. Handys behalten wie bisher ihren eigenen Bildschirm. Das Layout wählen wir nach der Fensterbreite, nicht nach dem Gerätenamen.

## Größen prüfen, ohne eine Schublade voller Geräte

Wir können nicht jedes Tablet in die Hand nehmen, deshalb wird das Layout von automatischen Tests geprüft, die die Bildschirme in mehreren Handy- und Tablet-Größen zeichnen, hoch und quer, und fehlschlagen, wenn etwas überläuft oder ein unerwartetes Layout gewählt wird. Dieselben Prüfungen laufen für alle 12 Sprachen, denn ein langes Wort in einer Sprache kann ein Layout sprengen, das in einer anderen gut aussieht. Außerdem behalten wir ein paar echte Screenshots aus Tablet-Simulatoren, die wir mit eigenen Augen ansehen.

## Eine kleine Falle in den Werkzeugen

Eine Überraschung steckte in den Screenshot-Werkzeugen. Auf einem neueren Tablet-System kann der Simulator eine Querformat-App in einem Fenster öffnen, statt das Gerät zu drehen, sodass das aufgenommene Bild seitwärts herauskam. Für diese Aufnahmen zeichnen wir den Bildschirm jetzt absichtlich gedreht und drehen die Datei wieder aufrecht.

## Was noch nicht geprüft ist

Wir haben noch nicht gesehen, wie eine Partie auf einem echten Tablet mittendrin gedreht wird, und Fenster, die etwa so schmal sind wie ein Handy, fallen auf das Handy-Layout zurück, das wir ebenfalls noch nicht genau angesehen haben. Wir sagen es hier, sobald sich das ändert. Ein Erscheinungsdatum gibt es noch nicht.
