---
title: Der Schalter für den Ton, der nichts tat
description: Warum die Toneinstellung von Sunmeld eine Zeit lang stumm blieb und was wir ergänzt haben, damit man einen Zusammenschluss hören kann.
slug: sound-that-was-silent
lang: de
category: devlog
keywords: Sunmeld, Ton, Audio, Einstellungen, lautloser Modus, Journal
translation_of: en
---
Sunmeld ist weiterhin in Entwicklung für iOS und Android. Diese Notiz handelt von einer Einstellung, die es gab, die aber nichts bewirken konnte.

## Der Schalter war da, der Ton nicht

Der Einstellungsbildschirm hatte einen Tonschalter, und er speicherte deine Wahl richtig. Das Spiel prüfte ihn jedes Mal, wenn ein Stein landete oder sich zusammenschloss. Der Teil, der den Ton abspielen sollte, war aber ein leerer Platzhalter. Das hatten wir absichtlich so belassen, weil die Tondateien und ihre Lizenz noch nicht entschieden waren. Der Schalter selbst war nie kaputt. Es fehlte der Ton.

## Die Töne selbst gemacht

Statt auf eine Lizenz zu warten, haben wir die Töne selbst erzeugt. Es gibt sechzehn kurze Effekte für Dinge wie Landen, Zusammenschließen, Ketten und die Warnung bei Überlauf. Sie entstehen durch ein kleines Skript ohne Zufallszahlen, sodass zweimaliges Ausführen dieselben Dateien ergibt. Zusammen sind sie etwa 220 KB groß.

## Still, wenn dein Telefon still ist

Das Spiel ist so eingerichtet, dass auf dem iPhone der lautlose Schalter gilt und die Musik einer anderen App, die bereits läuft, nicht abgebrochen wird. Auf Android läuft es als Spielton und übernimmt keinen Audiofokus. Wenn ein Ton nicht abgespielt werden kann, geht die Runde ganz normal weiter.

## Was wir noch nicht gehört haben

Die Töne sind verdrahtet, und die App baut mit ihnen. Wir haben sie aber noch nicht auf einem echten iPhone in einem echten Raum bei normaler Lautstärke gehört. Klang und Lautstärke müssen unter Umständen noch einmal überarbeitet werden. Dann lässt sich eine Tondatei mit demselben Namen austauschen.

## Häufige Fragen

### Warum gab es vorher keinen Ton?

Die Tonausgabe war ein stiller Platzhalter. Die Tondateien und der Audioteil der App wurden erst vor Kurzem hinzugefügt.

### Beachtet das Spiel auf dem iPhone den lautlosen Schalter?

So ist es eingerichtet. Auf einem echten Gerät haben wir das noch nicht geprüft, dazu sagen wir mehr, sobald wir es getan haben.

### Kann ich den Ton ausschalten?

Ja. Der Tonschalter in den Einstellungen steuert die Effekte. Ist er aus, spielt das Spiel nichts ab.
