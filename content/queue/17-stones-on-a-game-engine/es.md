---
title: Llevar las piedras a un motor de juego
description: Por qué las piedras que caen y las demás partes en movimiento de Sunmeld ahora funcionan con un motor de juego, y cómo lo comprobamos.
slug: stones-on-a-game-engine
lang: es
category: devlog
keywords: Sunmeld, Flame, motor, animación, rendimiento, diario
translation_of: en
---
Sunmeld sigue en desarrollo para iOS y Android. Esta nota trata de cómo se dibujan las partes en movimiento del juego.

## Primero, listar cada movimiento

Antes de cambiar nada, anotamos cada movimiento del juego: piedras que caen y chocan, el brillo al fusionarse, la puntuación que aparece, la línea de aviso, la línea de apuntado y la barra superior con puntuación y tiempo. Para cada uno nos preguntamos cuánto trabajo le exige a la pantalla en cada fotograma. Algunos eran baratos. Otros eran caros, como dibujar una piedra con degradado y un brillo suave en cada fotograma.

## Dibujar una vez, mover muchas veces

El motor elegido es Flame, un motor de juegos que funciona sobre Flutter. Las piedras y el cristal ahora se dibujan una vez como imágenes y se colocan en cada fotograma. El brillo de la fusión es una forma suave ya hecha con un color encima. El texto de la puntuación se prepara de antemano. Las reglas no cambiaron: la misma física se encarga de caer y de fusionarse.

## Comprobado en un ordenador, todavía no en el teléfono

Medimos en un Mac en modo de perfil, y los fotogramas se mantuvieron dentro de su presupuesto. Eso es un ordenador, no tu teléfono. Todavía no hemos comprobado el resultado en un iPhone o un Android reales a su frecuencia de actualización completa, así que la fluidez en dispositivos reales sigue pendiente.

## Por qué el motor

Las herramientas de dibujo de Flutter también podrían hacerlo. No hicimos una prueba comparativa lado a lado, así que no afirmamos que el motor sea más rápido. Lo elegimos porque ahora todas las partes en movimiento se ejecutan en un mismo bucle, y eso facilita mantener la fluidez a medida que el juego crece.

## Lo que viene

El último paso es comprobar la sensación en dispositivos reales con altas frecuencias de actualización, y revisar de nuevo las pantallas pequeñas. Todavía no hay fecha de lanzamiento.

## Preguntas frecuentes

### ¿Cambió la forma de jugar?

No. Se mantuvieron las reglas y la física. Solo cambiaron el dibujo y el orden de las partes en movimiento.

### ¿Por qué usar un motor de juego?

Ahora todas las partes en movimiento se ejecutan en un mismo bucle, así que el juego no tiene que reconstruir toda la pantalla por cada pequeño movimiento.

### ¿Se ha probado en un teléfono?

Hasta ahora se ha medido en un ordenador. La prueba en un teléfono real todavía está por llegar.
