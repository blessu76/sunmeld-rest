---
title: Ein beendetes Spiel noch einmal ansehen, Zug für Zug
description: Wie die Wiederholung eines beendeten Sunmeld-Spiels funktioniert und wie wir geprüft haben, dass sie genauso abläuft.
slug: replay
lang: de
category: devlog
keywords: Sunmeld, Wiederholung, nochmal ansehen, Spiel, Journal
translation_of: en
published: 2026-11-23T18:00+09:00
---
Sunmeld ist weiterhin in Entwicklung für iOS und Android. Diese Notiz handelt von einer Funktion, mit der du ein beendetes Spiel Zug für Zug noch einmal ansehen kannst.

## Warum noch einmal ansehen

Wenn ein Spiel vorbei ist, fragt man sich, warum es verloren ging. Man weiß, dass der letzte Stein übergelaufen ist, aber wo es zu kippen begann, ist schwerer zu erinnern. Deshalb gibt es auf dem Ergebnisbildschirm jetzt „Noch einmal ansehen“.

## Wir notieren Züge, kein Video

Das Spiel wird nicht als Video aufgenommen. Wir notieren nur, was zum Wiederaufbau nötig ist: den Zufallswert, mit dem das Spiel begann, wer zuerst gespielt hat, und für jeden fallenden Stein, in welchem Schritt, wo und welche Art Stein. Ein Stein, der von selbst fiel, weil die Zeit ablief, wird genauso notiert.

## Im selben Schritt wieder eingespeist

Wenn du „Noch einmal ansehen“ drückst, werden die gespeicherten Züge in denselben Schritten wieder in die Spielengine eingespeist. Gleiche Eingabe, gleiches Ergebnis. Nicht nur die Punkte, auch Position und Stufe jedes Steins müssen übereinstimmen, und ein automatischer Test hält das fest. Die Tests umfassen Steine, die durch Zeitablauf fielen, Spezialsteine, ein Spiel, das der Gegner begann, und das erneute Einlesen eines gespeicherten Verlaufs.

## So schaust du zu

Es gibt Abspielen und Pause, Neustart und nächster Zug, und du kannst zwischen langsamer und schneller wechseln. Ist „Bewegung reduzieren“ im System oder in der App eingeschaltet, startet die Wiederholung angehalten und ohne Leuchteffekte. Dann gehst du mit „Nächster Zug“ Zug für Zug weiter.

## Grenzen für den Moment

Nur Spiele gegen KI-Gegner lassen sich wiederholen. Alleine stapeln und Übungsspiele sind nicht enthalten. Es lässt sich nur das letzte Spiel ansehen, und der einzige Zugang ist der Ergebnisbildschirm. Die Zielbewegung der KI wird nicht nachgezeichnet; der Stein geht direkt dorthin, wo er gefallen ist. Das Ergebnis des Falls ist dasselbe.

## Was wir noch nicht geprüft haben

Wir haben noch nicht geprüft, wie es sich auf einem echten Gerät anfühlt oder wie es mit einem Screenreader klingt. Wir wissen auch noch nicht, wie groß der Verlauf bei einem sehr langen Spiel wird. Wenn sich das ändert, schreiben wir es hier auf. Es gibt noch kein Erscheinungsdatum.

## Häufige Fragen

### Kann ich ein früheres Spiel noch einmal ansehen?

Du kannst das zuletzt beendete Spiel gegen einen KI-Gegner auf dem Ergebnisbildschirm noch einmal ansehen.

### Kann die Wiederholung anders ausgehen?

Nein. Die gespeicherten Züge werden in denselben Schritten wieder eingespeist, und Tests prüfen, dass Punkte und Position jedes Steins übereinstimmen.

### Kann ich auch Allein stapeln wiederholen?

Noch nicht. Derzeit werden nur Spiele gegen KI-Gegner unterstützt.

### Gibt es ein Erscheinungsdatum?

Noch nicht. Ein Erscheinungsdatum steht nicht fest.
