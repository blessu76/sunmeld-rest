---
title: La marque « nouveau record » après une partie d'entraînement
description: Quand l'écran de résultat affiche un nouveau record, quels records comptent et comment la marque apparaît.
slug: new-record
lang: fr
category: devlog
keywords: Sunmeld, nouveau record, résultat, série, entraînement, journal
translation_of: en
published: 2026-11-25T14:30+09:00
---
Sunmeld est toujours en développement pour iOS et Android. Cette note parle d'une petite marque sur l'écran de résultat, qui apparaît quand une partie d'entraînement établit un nouveau record.

## Pourquoi une marque sur le résultat

Un record n'est utile que si on le remarque. Avant ce changement, un meilleur score ou la plus longue série de victoires pouvait progresser sans aucun signe sur l'écran de résultat. Nous avons donc ajouté une ligne au-dessus du résumé, « Nouveau record », suivie des records établis par cette partie.

## Seul ce qui a monté est affiché

La ligne ne liste que les records qui ont augmenté dans cette partie : le meilleur score en difficulté difficile et la plus longue série de victoires. Si rien n'a augmenté, aucune ligne n'apparaît. Une première victoire en difficulté difficile compte aussi comme nouveau record.

## Les séries commencent à deux

Une série n'est affichée que si la plus longue série vaut au moins deux. Sinon, chaque première victoire afficherait la marque, et elle ne voudrait rien dire.

## Seulement les parties d'entraînement

Les parties de ligue, le défi quotidien et le mode rush n'ajoutent rien au record d'entraînement, donc ils n'affichent pas non plus la marque. Appuyer sur « Rejouer » l'efface, pour qu'une ancienne marque ne passe pas à la partie suivante.

## Comment elle apparaît

La marque grandit d'une taille un peu plus petite jusqu'à sa taille normale. Si le mouvement réduit est activé dans le système ou dans l'application, elle apparaît directement à sa taille normale, sans animation. Elle utilise le même style d'étiquette que la marque « nouveau meilleur » dans l'empilement en solo et dans le rush.

## Ce que nous n'avons pas encore vérifié

Nous n'avons pas encore vu comment la marque se présente sur un vrai appareil, ni comment un lecteur d'écran la lit. Sur un très petit écran, il faudra peut-être faire défiler un peu plus pour atteindre les boutons. Il n'y a pas encore de date de sortie.

## FAQ

### La marque apparaît-elle dans les parties de ligue ?

Non. Les parties de ligue, le défi quotidien et le rush ne l'affichent pas.

### Qu'est-ce qui compte comme nouveau record ?

Un meilleur score plus élevé en difficulté difficile, ou une série de victoires plus longue. Une première victoire en difficulté difficile compte aussi.

### Pourquoi une série demande-t-elle deux victoires ?

Une série d'une seule victoire correspondrait à chaque première victoire. Commencer à deux garde la marque significative.

### Y a-t-il une date de sortie ?

Pas encore. Aucune date n'a été fixée.
