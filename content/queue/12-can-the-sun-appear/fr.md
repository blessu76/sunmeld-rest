---
title: Le soleil pourrait-il un jour apparaître ?
description: Ce qui s'est passé quand nous avons laissé des joueurs IA jouer à Sunmeld encore et encore : la pierre la plus haute n'apparaissait presque jamais, et la solution était dans les règles, pas dans l'IA.
slug: can-the-sun-appear
lang: fr
category: devlog
keywords: Sunmeld, équilibrage, IA, tests, game design, journal
translation_of: en
---
Sunmeld est toujours en développement pour iOS et Android. Cette note parle d'un problème que nous n'avons trouvé que parce que nous ne faisions pas confiance à notre propre ressenti du jeu.

## Laisser les IA jouer jusqu'au bout

Au début, les règles n'étaient qu'un prototype rapide. Avant de demander à quiconque de les essayer, nous avons fait jouer des joueurs IA de nombreuses fois les uns contre les autres, avec les mêmes conditions de départ à chaque fois pour qu'un résultat soit reproductible. Nous avons relevé à quelle fréquence une partie se terminait par un débordement, à quelle fréquence le premier joueur gagnait, et à quelle fréquence quelqu'un faisait la pierre la plus haute, le soleil.

## Le soleil n'est jamais venu

Avec les règles du prototype, personne n'a jamais fait de soleil. Ni l'IA facile, ni la plus forte. Au début, cela ressemblait à un problème d'IA, alors nous avons regardé l'IA. Puis nous avons fait le calcul.

Chaque fusion combine deux pierres en une du stade suivant : le soleil représente donc beaucoup de « volume de pierre ». Les pierres qui tombent dans le bocal sont petites. Sur le nombre de lâchers qu'une partie permettait, le volume total qui pouvait entrer dans le bocal était bien en dessous de ce qu'il faut pour un soleil. Aucune habileté ne construit ce pour quoi les règles ne donnent pas assez de matière. C'était un problème de règles, pas d'IA.

## Ce que nous avons changé

Nous avons remodelé l'échelle des stades et la taille du bocal, et donné à chaque joueur un budget de lâchers adapté à la nouvelle échelle. Ensuite, les mêmes parties d'IA ont produit des soleils, plus souvent avec les IA les plus fortes, et moins de parties se sont terminées par un débordement. Le soleil est devenu rare mais possible, ce que nous voulions d'un stade final.

## Une seconde surprise : l'horloge de visée

Les tests ont aussi montré qu'une partie jouée en temps réel se terminait plus souvent par un débordement que la même partie jouée instantanément. Ce n'était pas un bug de l'IA. L'horloge de débordement continuait de tourner pendant qu'un joueur visait encore : celui qui venait de lâcher une pierre dans un bocal bien rempli pouvait perdre pendant que l'autre réfléchissait. Désormais, l'horloge de danger attend pendant qu'un joueur vise.

## Pourquoi nous te le racontons

Tester à la main aurait mis longtemps à remarquer que le soleil était hors de portée. Quelques lignes de calcul et beaucoup de parties automatiques l'ont trouvé en un après-midi. Il n'y a pas encore de date de sortie. Quand il y aura du nouveau, cela apparaîtra ici.
