---
title: ¿Podría aparecer alguna vez el sol?
description: Qué pasó cuando dejamos que jugadores de IA jugaran a Sunmeld una y otra vez: la piedra máxima casi nunca aparecía, y la solución estaba en las reglas, no en la IA.
slug: can-the-sun-appear
lang: es
category: devlog
keywords: Sunmeld, equilibrio, IA, pruebas, diseño de juegos, diario
translation_of: en
---
Sunmeld sigue en desarrollo para iOS y Android. Esta nota trata de un problema que solo encontramos porque no nos fiamos de nuestra propia intuición sobre el juego.

## Dejar que las IA jueguen hasta el final

Al principio, las reglas eran un prototipo rápido. Antes de pedir a nadie que las probara, hicimos que jugadores de IA jugaran muchas partidas entre sí, con las mismas condiciones iniciales cada vez para que el resultado se pudiera repetir. Medimos cuántas partidas terminaban por desbordamiento, cuántas ganaba quien empezaba y cuántas veces alguien conseguía la piedra más alta, el sol.

## El sol nunca llegó

Con las reglas del prototipo, nadie hizo nunca un sol. Ni la IA fácil ni la más difícil. Al principio parecía un problema de la IA, así que miramos la IA. Después hicimos la cuenta.

Cada fusión combina dos piedras en una del siguiente nivel, así que el sol encierra mucho «volumen de piedra». Las piedras que caen en el tarro son pequeñas. Con el número de caídas que permitía una partida, el volumen total que podía entrar en el tarro quedaba muy por debajo de lo que necesita un solo sol. Ninguna habilidad puede construir algo para lo que las reglas no dan material suficiente. Era un problema de reglas, no de IA.

## Qué cambiamos

Rediseñamos la escalera de niveles y el tamaño del tarro, y dimos a cada jugador un presupuesto de caídas acorde con la nueva escalera. Después, las mismas partidas de IA produjeron soles, más a menudo con las IA más fuertes, y menos partidas terminaron por desbordamiento. El sol pasó a ser raro pero posible, que es lo que queríamos de un nivel final.

## Una segunda sorpresa: el reloj de apuntar

Las pruebas también mostraron que una partida jugada en tiempo real terminaba por desbordamiento más a menudo que la misma partida jugada al instante. No era un fallo de la IA. El reloj del desbordamiento seguía corriendo mientras un jugador apuntaba, así que quien acababa de soltar una piedra en un tarro lleno podía perder mientras el otro pensaba. Ahora el reloj de peligro espera mientras un jugador apunta.

## Por qué te lo contamos

Probar a mano habría tardado mucho en descubrir que el sol estaba fuera de alcance. Unas líneas de aritmética y muchas partidas automáticas lo encontraron en una tarde. Todavía no hay fecha de lanzamiento. Cuando haya novedades, aparecerán aquí.

## Preguntas frecuentes

### ¿Se puede llegar de verdad a la piedra más alta?

Sí. Después de rediseñar las reglas, los mismos juegos de prueba con IA produjeron soles, aunque poco a menudo. Ese era el objetivo para una etapa final.

### ¿El problema era la IA?

No. El problema eran las reglas. El sol necesita más volumen de piedra del que los lanzamientos de una partida podían llevar a la tina.

### ¿El reloj de peligro sigue corriendo mientras apunto?

No. El reloj de desbordamiento ahora espera mientras un jugador apunta.

### ¿Hay fecha de lanzamiento?

No. Todavía no hay fecha de lanzamiento.
