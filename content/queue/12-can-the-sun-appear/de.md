---
title: Könnte die Sonne jemals erscheinen?
description: Was passierte, als wir KI-Spieler Sunmeld immer wieder spielen ließen: Der höchste Stein tauchte fast nie auf, und die Lösung lag in den Regeln, nicht in der KI.
slug: can-the-sun-appear
lang: de
category: devlog
keywords: Sunmeld, Balancing, KI, Tests, Spieldesign, Journal
translation_of: en
---
Sunmeld ist weiterhin in Entwicklung für iOS und Android. Diese Notiz handelt von einem Problem, das wir nur gefunden haben, weil wir unserem eigenen Spielgefühl nicht getraut haben.

## Die KIs durchspielen lassen

Anfangs waren die Regeln ein schneller Prototyp. Bevor wir jemanden baten, sie auszuprobieren, ließen wir KI-Spieler viele Partien gegeneinander spielen, jedes Mal mit denselben Startbedingungen, damit sich ein Ergebnis wiederholen ließ. Wir erfassten, wie oft eine Partie durch Überlaufen endete, wie oft der erste Spieler gewann und wie oft überhaupt jemand den höchsten Stein, die Sonne, schaffte.

## Die Sonne kam nie

Mit den Regeln des Prototyps schaffte nie jemand eine Sonne. Nicht die einfache KI, nicht die stärkste. Zuerst sah es nach einem KI-Problem aus, also sahen wir uns die KI an. Dann rechneten wir nach.

Jede Verschmelzung macht aus zwei Steinen einen der nächsten Stufe, die Sonne steckt also in viel „Steinvolumen“. Die Steine, die ins Gefäß fallen, sind klein. Über die Anzahl der Würfe, die eine Partie erlaubte, lag das gesamte Volumen, das je ins Gefäß gelangen konnte, deutlich unter dem, was eine Sonne braucht. Kein Können baut etwas, wofür die Regeln nicht genug Material liefern. Es war ein Regelproblem, kein KI-Problem.

## Was wir geändert haben

Wir haben die Stufenleiter und die Größe des Gefäßes neu zugeschnitten und jedem Spieler ein Wurfbudget gegeben, das zur neuen Leiter passt. Danach brachten dieselben KI-Partien Sonnen hervor, bei den stärkeren KIs häufiger, und weniger Partien endeten durch Überlaufen. Die Sonne wurde selten, aber möglich, und genau das wollten wir von einer Endstufe.

## Eine zweite Überraschung: die Zielzeit

Die Testläufe zeigten außerdem, dass eine in Echtzeit gespielte Partie häufiger durch Überlaufen endete als dieselbe Partie, die sofort durchgespielt wurde. Das war kein Fehler der KI. Die Überlaufuhr lief weiter, während ein Spieler noch zielte, sodass derjenige, der gerade einen Stein in ein volles Gefäß gelassen hatte, verlieren konnte, während die Gegenseite noch nachdachte. Jetzt wartet die Gefahrenuhr, solange ein Spieler zielt.

## Warum wir das erzählen

Von Hand zu testen hätte lange gebraucht, um zu merken, dass die Sonne außer Reichweite war. Ein paar Zeilen Rechnung und viele automatische Partien haben es an einem Nachmittag gefunden. Ein Erscheinungsdatum gibt es noch nicht. Gibt es Neuigkeiten, erscheinen sie hier.
