---
title: L'interrupteur du son qui ne faisait rien
description: Pourquoi le réglage du son de Sunmeld est resté muet un moment, et ce que nous avons ajouté pour qu'une fusion puisse être entendue.
slug: sound-that-was-silent
lang: fr
category: devlog
keywords: Sunmeld, son, audio, réglages, mode silencieux, journal
translation_of: en
published: 2026-11-19T17:45+09:00
---
Sunmeld est toujours en développement pour iOS et Android. Cette note parle d'un réglage qui existait mais ne pouvait rien faire.

## L'interrupteur était là, le son non

L'écran des réglages avait un interrupteur de son, et il enregistrait bien ton choix. Le jeu le consultait à chaque fois qu'une pierre tombait ou fusionnait. Mais la partie censée jouer le son était un espace vide. Nous l'avions laissé ainsi exprès, parce que les fichiers sonores et leur licence n'étaient pas encore décidés. L'interrupteur lui-même n'a jamais été cassé. Ce qui manquait, c'était le son.

## Fabriquer nous-mêmes les sons

Plutôt que d'attendre une licence, nous avons créé les sons nous-mêmes. Il y a seize effets courts pour des choses comme la chute, la fusion, les enchaînements et l'alerte de débordement. Ils sont générés par un petit script sans nombres aléatoires, donc le lancer deux fois donne les mêmes fichiers. Ensemble, ils pèsent environ 220 Ko.

## Silencieux quand ton téléphone l'est

Le jeu est configuré pour respecter l'interrupteur silencieux sur iPhone, sans couper la musique d'une autre application déjà en cours. Sur Android, il joue comme un son de jeu et ne prend pas le focus audio. Si un son ne peut pas se lire, la manche continue normalement.

## Ce que nous n'avons pas encore entendu

Les sons sont branchés et l'application se compile avec eux. Nous ne les avons pas encore écoutés sur un vrai iPhone, dans une vraie pièce, à un volume normal. Le timbre et le volume devront peut-être être revus. Le cas échéant, un fichier sonore pourra être remplacé par un autre portant le même nom.

## Questions fréquentes

### Pourquoi n'y avait-il pas de son avant ?

La sortie sonore était un espace silencieux. Les fichiers sonores et la partie audio de l'application n'ont été ajoutés que récemment.

### Le jeu respecte-t-il l'interrupteur silencieux sur iPhone ?

C'est ainsi qu'il est configuré. Nous ne l'avons pas encore vérifié sur un appareil réel ; nous en dirons plus une fois que ce sera fait.

### Puis-je couper le son ?

Oui. L'interrupteur de son dans les réglages contrôle les effets. Quand il est coupé, le jeu ne joue rien.
