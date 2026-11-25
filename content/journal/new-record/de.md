---
title: Die Marke „Neuer Rekord“ nach einer Übungspartie
description: Wann der Ergebnisbildschirm einen neuen Rekord zeigt, welche Rekorde zählen und wie die Marke erscheint.
slug: new-record
lang: de
category: devlog
keywords: Sunmeld, neuer Rekord, Ergebnis, Siegesserie, Übung, Journal
translation_of: en
published: 2026-11-25T14:30+09:00
---
Sunmeld ist weiterhin in Entwicklung für iOS und Android. Diese Notiz handelt von einer kleinen Marke auf dem Ergebnisbildschirm, die erscheint, wenn eine Übungspartie einen neuen Rekord aufstellt.

## Warum eine Marke auf dem Ergebnis

Ein Rekord nützt nur, wenn man ihn bemerkt. Vorher konnte eine Bestpunktzahl oder die längste Siegesserie steigen, ohne dass der Ergebnisbildschirm etwas davon zeigte. Deshalb haben wir oberhalb der Zusammenfassung eine Zeile mit „Neuer Rekord“ hinzugefügt, gefolgt von den Rekorden, die diese Partie aufgestellt hat.

## Nur was gestiegen ist, wird gezeigt

Die Zeile listet nur die Rekorde auf, die in dieser Partie gestiegen sind: die Bestpunktzahl auf der schweren Stufe und die längste Siegesserie. Wenn nichts gestiegen ist, erscheint keine Zeile. Ein erster Sieg auf der schweren Stufe zählt ebenfalls als neuer Rekord.

## Siegesserien beginnen bei zwei

Eine Serie wird nur angezeigt, wenn die längste Serie mindestens zwei beträgt. Sonst käme die Marke bei jedem ersten Sieg, und sie würde nichts aussagen.

## Nur Übungspartien

Ligaspiele, die tägliche Herausforderung und Rush-Spiele zählen nicht zum Übungsrekord, deshalb zeigen sie die Marke auch nicht. Ein Druck auf „Nochmal spielen“ löscht sie, sodass eine alte Marke nicht in die nächste Partie übernommen wird.

## So erscheint sie

Die Marke wächst von etwas kleiner auf ihre volle Größe. Ist die Bewegung im System oder in der App reduziert, erscheint sie direkt in voller Größe ohne Bewegung. Sie verwendet denselben Stil wie die Marke „Neue Bestleistung“ beim Stapeln allein und beim Rush.

## Was wir noch nicht geprüft haben

Wir haben noch nicht gesehen, wie die Marke auf einem echten Gerät aussieht oder wie ein Screenreader sie liest. Auf einem sehr kleinen Bildschirm muss man vielleicht etwas weiter scrollen, um die Knöpfe zu erreichen. Ein Veröffentlichungstermin steht noch nicht fest.

## FAQ

### Erscheint die Marke bei Ligaspielen?

Nein. Ligaspiele, die tägliche Herausforderung und Rush-Spiele zeigen sie nicht.

### Was zählt als neuer Rekord?

Eine höhere Bestpunktzahl auf der schweren Stufe oder eine längere beste Siegesserie. Ein erster Sieg auf der schweren Stufe zählt ebenfalls.

### Warum braucht eine Serie zwei Siege?

Eine Serie von eins wäre jeder erste Sieg. Ab zwei bleibt die Marke aussagekräftig.

### Gibt es einen Veröffentlichungstermin?

Noch nicht. Es ist kein Termin festgelegt.
