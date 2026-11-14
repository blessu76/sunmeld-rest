---
title: Una pantalla propia para tabletas
description: Por qué Sunmeld en una tableta no es solo la pantalla del teléfono estirada, y cómo comprobamos muchos tamaños de pantalla.
slug: tablet-layouts
lang: es
category: devlog
keywords: Sunmeld, iPad, diseño, tamaño de pantalla, pruebas, diario
translation_of: en
---
Sunmeld sigue en desarrollo para iOS y Android. Esta nota trata de qué pasa cuando el mismo juego se encuentra con una pantalla mucho más grande.

## El primer intento: un teléfono en el centro

Al principio, en una tableta el juego mostraba sin más la pantalla del teléfono en una columna estrecha en el centro. Todo funcionaba, pero la mayor parte de la pantalla estaba vacía. Si girabas la tableta, era una pantalla de teléfono estirada a lo ancho. Eso servía para probar el juego y no servía para jugarlo.

## Dos diseños, no uno

Ahora dibujamos las tabletas con dos diseños separados, vertical y horizontal. En vertical, el tarro es más grande, con tu rival arriba y tú abajo. En horizontal, tu rival queda a la izquierda, el tarro en el centro y tú a la derecha. La pantalla de resultado pone la imagen en un lado y la puntuación y los botones en el otro. Los teléfonos conservan su propia pantalla, como antes. Elegimos el diseño según el ancho de la ventana, no según el nombre del dispositivo.

## Comprobar tamaños sin un cajón lleno de dispositivos

No podemos tener en la mano todas las tabletas, así que el diseño lo comprueban pruebas automáticas que dibujan las pantallas en varios tamaños de teléfono y tableta, en vertical y en horizontal, y fallan si algo se desborda o si se elige un diseño que no esperábamos. Las mismas comprobaciones se ejecutan para cada uno de los 12 idiomas, porque una palabra larga en un idioma puede romper un diseño que se ve bien en otro. También guardamos algunas capturas reales de simuladores de tableta para mirarlas con nuestros propios ojos.

## Una pequeña trampa en las herramientas

Una sorpresa estuvo en las herramientas de captura. En un sistema de tableta más reciente, el simulador puede abrir una app horizontal en una ventana en lugar de girar el dispositivo, y la imagen capturada salía de lado. Ahora dibujamos la pantalla girada a propósito para esas capturas y devolvemos el archivo a su posición vertical.

## Lo que aún no está comprobado

Todavía no hemos visto cómo se gira una partida a medias en una tableta real, y las ventanas tan estrechas como un teléfono vuelven al diseño de teléfono, que tampoco hemos mirado de cerca. Lo diremos aquí cuando cambie. Todavía no hay fecha de lanzamiento.

## Preguntas frecuentes

### ¿Una tableta tiene su propio diseño?

Sí. Las tabletas usan diseños separados en vertical y horizontal, elegidos según el ancho de la ventana y no por el nombre del dispositivo. Los teléfonos mantienen su propia pantalla.

### ¿Cómo se comprueban tantos tamaños de pantalla?

Pruebas automáticas dibujan las pantallas en varios tamaños de teléfono y tableta, en vertical y horizontal, para cada uno de los 12 idiomas.

### ¿Se ha probado girar el dispositivo durante una partida en una tableta real?

Todavía no. Aún no hemos visto una partida girarse a mitad de juego en una tableta real.

### ¿Hay fecha de lanzamiento?

No. Todavía no hay fecha de lanzamiento.
