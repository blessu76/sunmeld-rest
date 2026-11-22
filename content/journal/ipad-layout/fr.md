---
title: Que faire de la place en plus sur un grand écran
description: Comment la disposition iPad de Sunmeld reconstruit l'écran d'accueil, les feuilles et la taille du texte au lieu d'étirer l'écran du téléphone.
slug: ipad-layout
lang: fr
category: devlog
keywords: Sunmeld, iPad, écran d'accueil, paysage, disposition, journal
translation_of: en
published: 2026-11-22T15:45+09:00
---
Sunmeld est toujours en développement pour iOS et Android. Cette note raconte comment l'écran d'accueil et les feuilles ont été refaits pour le grand écran de l'iPad.

## Étirer laisse du vide

Agrandir l'écran du téléphone grossit les pierres mais laisse beaucoup de vide autour. Plutôt que de l'étirer, nous nous sommes demandé ce qui doit venir en premier sur un grand écran. L'écran du téléphone n'a pas été touché.

## Portrait : une colonne centrée

En portrait, l'écran d'accueil de l'iPad est une seule colonne centrée. L'ordre est le même que sur le téléphone, donc il paraît familier. La grande image prend la hauteur qui reste dans la colonne. La largeur de la colonne suit la taille de l'écran.

## Paysage : l'image à gauche, les actions à droite

Tourné sur le côté, l'écran d'accueil se divise en deux. À gauche, la grande image et la présentation de ton adversaire. La colonne étroite de droite contient, de haut en bas, l'en-tête, la ligue, le défi du jour, le départ et le menu. Les trois cases de la ligue sont côte à côte sur un téléphone, mais empilées ici. Les yeux vont à l'image ; les mains travaillent à droite.

## Les feuilles se rassemblent au centre

Les feuilles comme les réglages, l'échelle et les règles ne s'étalent pas sur tout l'écran. Elles restent au centre, avec une largeur fixée. La ligue et la personnalisation utilisent une colonne plus large, et les cartes pour les nouveaux joueurs une colonne plus étroite encore. Des lignes de texte qui s'étirent sans fin sur un grand écran sont pénibles à lire.

## Le texte est un peu plus grand

Sur iPad, le texte est un peu plus grand. Sur téléphone, il reste comme avant. L'écran est plus loin des yeux, et la même taille paraissait petite.

## L'orientation dépend de l'appareil

L'iPad accepte les quatre orientations ; le téléphone reste en portrait. La disposition choisie dépend de la largeur de la fenêtre, pas du nom de l'appareil.

## Ce que nous n'avons pas encore vérifié

Nous n'avons pas encore vu si le jeu garde son état quand on tourne un vrai iPad en pleine partie. Même chose pour une fenêtre aussi étroite qu'un téléphone. Si cela change, nous le noterons ici. Il n'y a pas encore de date de sortie.

## Questions fréquentes

### L'écran de l'iPad est-il simplement celui du téléphone étiré ?

Non. Le portrait et le paysage ont chacun leur propre disposition. L'écran du téléphone n'a pas changé.

### Le texte change-t-il sur iPad ?

Il est un peu plus grand. Sur téléphone, il reste le même.

### L'écran change-t-il quand je tourne l'iPad ?

Oui. Le portrait et le paysage ont des dispositions différentes. Tourner en pleine partie n'a pas encore été vérifié sur un vrai appareil.

### Y a-t-il une date de sortie ?

Pas encore. Aucune date de sortie n'a été fixée.
