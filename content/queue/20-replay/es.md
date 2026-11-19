---
title: Volver a ver una partida terminada, jugada a jugada
description: Cómo funciona la repetición de una partida terminada de Sunmeld y cómo comprobamos que se reproduce igual.
slug: replay
lang: es
category: devlog
keywords: Sunmeld, repetición, volver a ver, partida, diario
translation_of: en
---
Sunmeld sigue en desarrollo para iOS y Android. Esta nota trata de una función que te deja volver a ver una partida terminada, jugada a jugada.

## Por qué volver a verla

Al terminar una partida uno se pregunta por qué la perdió. Sabes que la última piedra se desbordó, pero cuesta recordar dónde empezó a torcerse. Por eso añadimos «Volver a ver» a la pantalla de resultado.

## Anotamos jugadas, no vídeo

La partida no se graba en vídeo. Solo anotamos lo necesario para reconstruirla: el valor aleatorio con el que empezó, quién jugó primero y, por cada piedra lanzada, en qué paso cayó, dónde se colocó y de qué tipo era. Una piedra que cayó sola al acabarse el tiempo se anota igual.

## Se devuelve al motor en el mismo paso

Al pulsar «Volver a ver», las jugadas guardadas se vuelven a introducir en el motor del juego en los mismos pasos. La misma entrada da el mismo resultado. No solo la puntuación: la posición y la etapa de cada piedra deben coincidir, y una prueba automática lo fija. Las pruebas incluyen piedras caídas por tiempo agotado, piedras especiales, una partida que empezó el rival y la lectura de un registro guardado.

## Cómo verla

Hay reproducir y pausa, reiniciar y siguiente jugada, y puedes cambiar entre más lento y más rápido. Si «reducir movimiento» está activado en el sistema o en la app, la repetición empieza en pausa y sin efectos de brillo. Entonces puedes avanzar jugada a jugada con «Siguiente jugada».

## Límites por ahora

Solo se pueden repetir partidas contra rivales de IA. El apilado en solitario y las partidas de práctica no están incluidos. Solo se puede ver la última partida y la única entrada es la pantalla de resultado. El movimiento de apuntar de la IA no se vuelve a dibujar; la piedra va directa a donde cayó. El resultado de la caída es el mismo.

## Lo que aún no hemos comprobado

No hemos comprobado cómo se siente en un dispositivo real ni cómo suena con un lector de pantalla. Tampoco sabemos aún cuánto crece el registro en una partida muy larga. Si cambia, lo anotaremos aquí. Todavía no hay fecha de lanzamiento.

## Preguntas frecuentes

### ¿Puedo volver a ver una partida anterior?

Puedes volver a ver la última partida terminada contra un rival de IA desde la pantalla de resultado.

### ¿Puede la repetición salir distinta?

No. Las jugadas guardadas se vuelven a introducir en los mismos pasos, y las pruebas comprueban que la puntuación y la posición de cada piedra coinciden.

### ¿Puedo repetir también el apilado en solitario?

Todavía no. Por ahora solo se admiten partidas contra rivales de IA.

### ¿Hay fecha de lanzamiento?

Todavía no. No se ha fijado ninguna fecha de lanzamiento.
