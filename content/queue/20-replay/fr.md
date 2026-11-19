---
title: Revoir une partie terminée, coup par coup
description: Comment fonctionne le replay d'une partie terminée de Sunmeld et comment nous avons vérifié qu'il se rejoue à l'identique.
slug: replay
lang: fr
category: devlog
keywords: Sunmeld, replay, revoir, partie, journal
translation_of: en
---
Sunmeld est toujours en développement pour iOS et Android. Cette note parle d'une fonction qui permet de revoir une partie terminée, coup par coup.

## Pourquoi revoir

Quand une partie est finie, on se demande pourquoi on l'a perdue. On sait que la dernière pierre a débordé, mais on se souvient mal de l'endroit où tout a commencé à basculer. Nous avons donc ajouté « Revoir » à l'écran de résultat.

## On note les coups, pas une vidéo

La partie n'est pas enregistrée en vidéo. Nous notons seulement ce qu'il faut pour la reconstruire : la valeur aléatoire du départ, qui a joué en premier, et pour chaque pierre lâchée, à quel pas elle est tombée, où elle a été posée et de quel type elle était. Une pierre tombée toute seule quand le temps s'est écoulé est notée de la même façon.

## Réinjecté au même pas

Quand tu appuies sur « Revoir », les coups enregistrés sont réinjectés dans le moteur du jeu aux mêmes pas. La même entrée donne le même résultat. Il faut que non seulement le score, mais aussi la position et le niveau de chaque pierre coïncident, et un test automatique le fige. Les tests couvrent les pierres tombées après un délai dépassé, les pierres spéciales, une partie commencée par l'adversaire et la relecture d'un enregistrement sauvegardé.

## Comment regarder

Il y a lecture et pause, recommencer et coup suivant, et tu peux passer d'une vitesse plus lente à une plus rapide. Si la réduction des animations est activée dans le système ou dans l'app, le replay démarre en pause et sans effets lumineux. Tu peux alors avancer coup par coup avec « Coup suivant ».

## Limites pour l'instant

Seules les parties contre les adversaires IA peuvent être rejouées. L'empilement en solo et les parties d'entraînement n'en font pas partie. Seule la dernière partie peut être revue, et l'unique accès est l'écran de résultat. Le mouvement de visée de l'IA n'est pas redessiné ; la pierre va directement là où elle est tombée. Le résultat de la chute est le même.

## Ce que nous n'avons pas encore vérifié

Nous n'avons pas vérifié la sensation sur un vrai appareil ni le rendu avec un lecteur d'écran. Nous ne savons pas non plus quelle taille l'enregistrement atteint pour une très longue partie. Si cela change, nous le noterons ici. Il n'y a pas encore de date de sortie.

## Questions fréquentes

### Puis-je revoir une partie précédente ?

Tu peux revoir la dernière partie terminée contre un adversaire IA depuis l'écran de résultat.

### Le replay peut-il donner un résultat différent ?

Non. Les coups enregistrés sont réinjectés aux mêmes pas, et des tests vérifient que le score et la position de chaque pierre coïncident.

### Puis-je aussi rejouer l'empilement en solo ?

Pas encore. Pour l'instant, seules les parties contre les adversaires IA sont prises en charge.

### Y a-t-il une date de sortie ?

Pas encore. Aucune date de sortie n'a été fixée.
