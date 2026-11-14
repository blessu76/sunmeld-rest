---
title: Un seul ciel nocturne, deux apparences
description: Comment l'apparence de Sunmeld a été refaite, et pourquoi le bocal reste sombre même quand tu choisis le thème clair.
slug: two-looks-one-night-sky
lang: fr
category: devlog
keywords: Sunmeld, design, thème, mode sombre, journal
translation_of: en
---
Sunmeld est toujours en développement pour iOS et Android. Cette note parle de la façon dont le jeu a trouvé son apparence, et d'un choix que nous avons fait exprès.

## Recommencer une fois

La première version des écrans ne faisait pas fini. Ça fonctionnait, mais on aurait dit un prototype. Nous sommes donc revenus aux maquettes et avons reconstruit de zéro l'écran d'accueil, l'écran de jeu et les écrans de résultat. Les pierres sont devenues des corps célestes qui rayonnent, un fin anneau marque une fusion, et le score fait un petit bond quand il monte. Les règles et le moteur n'ont pas été touchés. Seule l'apparence a changé.

## Sombre et clair, à la demande

Ensuite, nous avons ajouté un choix de thème dans les réglages : suivre le système, sombre ou clair. L'apparence sombre est un ciel nocturne profond parsemé d'étoiles. L'apparence claire est une aube douce, aux couleurs pastel et aux cartes crème. Si tu choisis « suivre le système », le jeu change avec ton téléphone, même quand une feuille est ouverte.

## Le bocal reste sombre

Le bocal est la seule chose qui ne change pas avec le thème. Même dans le thème clair, il garde sa couleur de nuit. Pour deux raisons. Les pierres, avec leur halo, se lisent mieux sur un ciel sombre. Et un plateau qui a le même aspect dans les deux thèmes, c'est un même jeu qui se lit de la même façon pour tout le monde, quel que soit le thème choisi.

## Les petits détails à régler

Le texte sur les boutons dorés et roses avait besoin de sa propre encre sombre pour rester lisible. La couleur de l'écran de lancement doit correspondre au thème avant que l'app puisse lire ton réglage ; elle suit donc uniquement le système. C'est une limite du téléphone, pas un choix. Nous gardons aussi un test qui vérifie que les thèmes sombre et clair définissent exactement le même ensemble de couleurs, pour que l'un ne manque pas d'une couleur que l'autre a.

## La suite

Nous continuons de vérifier l'aspect des écrans en petite taille. Il n'y a pas encore de date de sortie. Quand il y aura du nouveau, cela apparaîtra ici.

## Questions fréquentes

### Pourquoi la cuve reste-t-elle sombre en thème clair ?

Les pierres avec leur halo se lisent mieux sur un ciel sombre. Un plateau identique dans les deux thèmes se lit aussi de la même façon pour tout le monde.

### Quels thèmes peut-on choisir ?

Dans les réglages, vous pouvez choisir suivre le système, sombre ou clair.

### Le jeu suit-il le thème de mon téléphone ?

Oui, si vous choisissez suivre le système. Le jeu change avec le téléphone, même lorsqu'une feuille est ouverte.

### Les règles ont-elles changé avec le nouveau style ?

Non. Les règles et le moteur n'ont pas été touchés. Seul l'aspect a changé.
