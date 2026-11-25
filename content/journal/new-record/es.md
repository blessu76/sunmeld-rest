---
title: La marca de «nuevo récord» tras una partida de práctica
description: Cuándo la pantalla de resultados muestra un nuevo récord, qué récords cuentan y cómo aparece la marca.
slug: new-record
lang: es
category: devlog
keywords: Sunmeld, nuevo récord, resultado, racha, práctica, diario
translation_of: en
published: 2026-11-25T14:30+09:00
---
Sunmeld sigue en desarrollo para iOS y Android. Esta nota trata de una pequeña marca en la pantalla de resultados que aparece cuando una partida de práctica establece un nuevo récord.

## Por qué una marca en el resultado

Un récord solo sirve si lo notas. Antes de este cambio, una mejor puntuación o la racha de victorias más larga podían subir sin ninguna señal en la pantalla de resultados. Por eso añadimos una línea sobre el resumen que dice «Nuevo récord», seguida de los récords que esta partida estableció.

## Solo se muestra lo que subió

La línea lista solo los récords que subieron en esta partida: la mejor puntuación en el nivel difícil y la racha de victorias más larga. Si no subió nada, no aparece ninguna línea. Una primera victoria en el nivel difícil también cuenta como nuevo récord.

## Las rachas empiezan en dos

Una racha solo se muestra cuando la racha más larga es de al menos dos. Si no, cada primera victoria traería la marca, y no diría nada.

## Solo partidas de práctica

Las partidas de liga, el desafío diario y el modo rush no suman al récord de práctica, así que tampoco muestran la marca. Al pulsar «Jugar de nuevo» se borra, para que una marca antigua no pase a la siguiente partida.

## Cómo aparece

La marca crece desde un tamaño algo menor hasta su tamaño completo. Si el movimiento reducido está activado en el sistema o en la app, aparece directamente a tamaño completo, sin movimiento. Usa el mismo estilo de etiqueta que la marca de «nuevo mejor» en el apilado en solitario y en rush.

## Lo que aún no hemos comprobado

Aún no hemos visto cómo se ve la marca en un dispositivo real, ni cómo la lee un lector de pantalla. En una pantalla muy pequeña puede hacer falta desplazarse un poco más para llegar a los botones. Todavía no hay fecha de lanzamiento.

## Preguntas frecuentes

### ¿La marca aparece en las partidas de liga?

No. Las partidas de liga, el desafío diario y rush no la muestran.

### ¿Qué cuenta como nuevo récord?

Una mejor puntuación más alta en el nivel difícil, o una racha de victorias más larga. Una primera victoria en el nivel difícil también cuenta.

### ¿Por qué una racha necesita dos victorias?

Una racha de una sola victoria sería cada primera victoria. Empezar en dos mantiene la marca con significado.

### ¿Hay fecha de lanzamiento?

Todavía no. No se ha fijado ninguna fecha.
