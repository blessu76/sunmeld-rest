---
title: Un écran à part pour les tablettes
description: Pourquoi Sunmeld sur tablette n'est pas simplement l'écran du téléphone étiré, et comment nous vérifions de nombreuses tailles d'écran.
slug: tablet-layouts
lang: fr
category: devlog
keywords: Sunmeld, iPad, mise en page, taille d'écran, tests, journal
translation_of: en
---
Sunmeld est toujours en développement pour iOS et Android. Cette note parle de ce qui se passe quand le même jeu rencontre un écran bien plus grand.

## Première tentative : un téléphone au milieu

Au début, sur tablette, le jeu affichait simplement l'écran du téléphone dans une colonne étroite au milieu. Tout fonctionnait, mais l'essentiel de l'écran était vide. En tournant la tablette sur le côté, on obtenait un écran de téléphone étiré. C'était bien pour tester le jeu, mais pas pour y jouer.

## Deux mises en page, pas une

Nous dessinons désormais les tablettes en deux mises en page distinctes, portrait et paysage. En portrait, le bocal est plus grand, avec ton adversaire en haut et toi en bas. En paysage, ton adversaire est à gauche, le bocal au milieu et toi à droite. L'écran de résultat place l'image d'un côté et le score et les boutons de l'autre. Les téléphones gardent leur propre écran, comme avant. Nous choisissons la mise en page d'après la largeur de la fenêtre, pas d'après le nom de l'appareil.

## Vérifier les tailles sans un tiroir plein d'appareils

Nous ne pouvons pas tenir toutes les tablettes entre nos mains : la mise en page est donc vérifiée par des tests automatiques qui dessinent les écrans à plusieurs tailles de téléphone et de tablette, en portrait et en paysage, et échouent si quelque chose déborde ou si une mise en page inattendue est choisie. Les mêmes vérifications tournent pour chacune des 12 langues, car un mot long dans une langue peut casser une mise en page qui semble correcte dans une autre. Nous gardons aussi quelques vraies captures de simulateurs de tablette pour les regarder de nos propres yeux.

## Un petit piège dans les outils

Une surprise est venue des outils de capture. Sur un système de tablette plus récent, le simulateur peut ouvrir une app en paysage dans une fenêtre au lieu de faire pivoter l'appareil, et l'image capturée sortait couchée. Nous dessinons maintenant l'écran pivoté exprès pour ces captures, puis nous remettons le fichier droit.

## Ce qui n'est pas encore vérifié

Nous n'avons pas encore vu une partie pivoter en plein milieu sur une vraie tablette, et les fenêtres à peu près aussi étroites qu'un téléphone retombent sur la mise en page téléphone, que nous n'avons pas non plus regardée de près. Nous le dirons ici quand cela changera. Il n'y a pas encore de date de sortie.

## Questions fréquentes

### Une tablette a-t-elle sa propre mise en page ?

Oui. Les tablettes utilisent des mises en page séparées en portrait et en paysage, choisies selon la largeur de la fenêtre et non le nom de l'appareil. Les téléphones gardent leur propre écran.

### Comment vérifie-t-on autant de tailles d'écran ?

Des tests automatiques dessinent les écrans à plusieurs tailles de téléphone et de tablette, en portrait et en paysage, pour chacune des 12 langues.

### La rotation en cours de partie a-t-elle été testée sur une vraie tablette ?

Pas encore. Nous n'avons pas encore vu une partie tourner en plein milieu sur une vraie tablette.

### Y a-t-il une date de sortie ?

Non. Il n'y a pas encore de date de sortie.
