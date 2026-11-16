---
title: Déplacer les pierres sur un moteur de jeu
description: Pourquoi les pierres qui tombent et les autres éléments mobiles de Sunmeld tournent désormais sur un moteur de jeu, et comment nous les avons vérifiés.
slug: stones-on-a-game-engine
lang: fr
category: devlog
keywords: Sunmeld, Flame, moteur, animation, performance, journal
translation_of: en
---
Sunmeld est toujours en développement pour iOS et Android. Cette note explique comment les éléments mobiles du jeu sont dessinés.

## D'abord, lister chaque mouvement

Avant de rien changer, nous avons noté chaque mouvement du jeu : les pierres qui tombent et se heurtent, la lueur lors d'une fusion, le score qui apparaît, la ligne d'alerte, la ligne de visée et la barre du haut avec le score et le temps. Pour chacun, nous nous sommes demandé combien de travail il imposait à l'écran à chaque image. Certains étaient peu coûteux. D'autres étaient lourds, comme dessiner une pierre avec un dégradé et une lueur douce à chaque image.

## Dessiner une fois, bouger souvent

Le moteur choisi est Flame, un moteur de jeu qui fonctionne sur Flutter. Les pierres et le verre sont désormais dessinés une fois sous forme d'images, puis placés à chaque image. La lueur de fusion est une forme douce toute prête, sur laquelle on applique une couleur. Le texte du score est préparé à l'avance. Les règles n'ont pas changé : la même physique gère la chute et la fusion.

## Vérifié sur ordinateur, pas encore sur téléphone

Nous avons mesuré sur un Mac en mode profil, et les images sont restées dans leur budget de temps. C'est un ordinateur, pas ton téléphone. Nous n'avons pas encore vérifié le résultat sur un iPhone ou un Android réel à sa pleine fréquence de rafraîchissement, donc la fluidité sur les vrais appareils reste à confirmer.

## Pourquoi ce moteur

Les outils de dessin de Flutter pourraient aussi le faire. Nous n'avons pas fait de test comparatif côte à côte, donc nous ne prétendons pas que le moteur est plus rapide. Nous l'avons choisi parce que tous les éléments mobiles tournent désormais dans une même boucle, ce qui facilite la fluidité à mesure que le jeu grandit.

## La suite

La dernière étape est de vérifier la sensation sur de vrais appareils à haute fréquence de rafraîchissement, puis de revoir les petits écrans. Il n'y a pas encore de date de sortie.

## Questions fréquentes

### La façon de jouer a-t-elle changé ?

Non. Les règles et la physique sont restées identiques. Seuls le dessin et le timing des éléments mobiles ont changé.

### Pourquoi utiliser un moteur de jeu ?

Chaque élément mobile tourne désormais dans une même boucle, donc le jeu n'a pas à reconstruire tout l'écran pour chaque petit mouvement.

### A-t-il été testé sur un téléphone ?

Pour l'instant, il a été mesuré sur un ordinateur. Le test sur un vrai téléphone reste à venir.
