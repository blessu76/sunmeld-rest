---
title: El interruptor de sonido que no hacía nada
description: Por qué el ajuste de sonido de Sunmeld estuvo en silencio durante un tiempo y qué añadimos para que se pueda oír una fusión.
slug: sound-that-was-silent
lang: es
category: devlog
keywords: Sunmeld, sonido, audio, ajustes, modo silencio, diario
translation_of: en
published: 2026-11-19T17:45+09:00
---
Sunmeld sigue en desarrollo para iOS y Android. Esta nota trata de un ajuste que existía pero no podía hacer nada.

## El interruptor estaba, el sonido no

La pantalla de ajustes tenía un interruptor de sonido, y guardaba bien tu elección. El juego lo consultaba cada vez que una piedra caía o se fusionaba. Pero la parte que debía reproducir el sonido era un marcador vacío. Lo dejamos así a propósito, porque los archivos de sonido y su licencia aún no estaban decididos. El interruptor en sí nunca estuvo roto. Lo que faltaba era el sonido.

## Hacer los sonidos nosotros

En lugar de esperar una licencia, creamos los sonidos nosotros mismos. Hay dieciséis efectos cortos para cosas como caer, fusionar, las cadenas y el aviso de desbordamiento. Los genera un pequeño script que no usa números aleatorios, así que ejecutarlo dos veces da los mismos archivos. Entre todos ocupan unos 220 KB.

## En silencio cuando el teléfono está en silencio

El juego está preparado para respetar el interruptor de silencio en el iPhone, y para no cortar la música de otra app que ya esté sonando. En Android se reproduce como sonido de juego y no toma el foco de audio. Si un sonido no se reproduce, la partida sigue con normalidad.

## Lo que aún no hemos escuchado

Los sonidos están conectados y la app compila con ellos. Todavía no los hemos escuchado en un iPhone real, en una habitación real, a un volumen normal. El tono y el volumen quizá necesiten otro ajuste. Cuando llegue ese momento, basta con cambiar un archivo de sonido por otro con el mismo nombre.

## Preguntas frecuentes

### ¿Por qué antes no había sonido?

La salida de sonido era un marcador silencioso. Los archivos de sonido y la parte de audio de la app se añadieron hace poco.

### ¿El juego respeta el interruptor de silencio en el iPhone?

Así está configurado. Todavía no lo hemos comprobado en un dispositivo real; diremos más cuando lo hagamos.

### ¿Puedo desactivar el sonido?

Sí. El interruptor de sonido de los ajustes controla los efectos. Cuando está desactivado, el juego no reproduce nada.
