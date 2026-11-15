---
title: La progression reste sur le téléphone — et peut se synchroniser entre tes appareils
description: Comment Sunmeld enregistre ta progression de jeu localement, et ce qui se passe lorsque tu joues sur un autre appareil avec le même compte Apple.
slug: progress-stays-on-phone
lang: fr
category: devlog
keywords: Sunmeld, progression, sauvegarde, iCloud, synchronisation
translation_of: en
---
Sunmeld est toujours en développement pour iOS et Android. Cette note parle de la manière dont ta progression de jeu est enregistrée et partagée entre tes appareils.

## Où vit ta progression

Ta progression — les étoiles que tu as gagnées, les records que tu as établis, les ligues auxquelles tu as joué et ton surnom — est d'abord enregistrée sur ton téléphone. C'est la source de la vérité. Nous envoyons également une copie à iCloud pour qu'elle puisse voyager avec toi si tu joues sur un autre appareil.

## Jouer sur un autre appareil

Si tu joues à Sunmeld sur un autre appareil avec le même compte Apple, la progression des deux appareils est fusionnée. Lorsque tu reviens au jeu sur un appareil ou que ton téléphone se réveille, l'application vérifie iCloud pour les progressions plus récentes et les récupère. La règle de fusion est simple : pour chaque élément de progression comme un record ou un niveau de ligue, nous gardons celui qui est le plus avancé. Nous ne les ajoutons pas. Si un appareil a atteint la ligue 2 et un autre seulement la ligue 1, l'appareil avec la ligue 1 sera mis à jour à la ligue 2.

## Vitesse de synchronisation entre appareils

La synchronisation entre tes appareils prend du temps que Apple contrôle, généralement quelques secondes à quelques minutes. Tu devras peut-être attendre un instant ou revenir au jeu après un moment pour voir la progression de l'autre appareil.

## Ce qui n'est pas encore synchronisé

Tes paramètres — le thème que tu as choisi, la langue que tu as sélectionnée et les sons que tu as activés ou désactivés — sont également synchronisés entre les appareils. Cependant, le surnom reçoit un traitement spécial : si tu changes ton surnom sur un appareil et que la version d'un autre appareil n'avait pas été vérifiée depuis un certain temps, le changement le plus récent gagne.

## Pourquoi c'est important

Le téléphone est toujours l'appareil que tu tiens. Ta progression y est d'abord, en sécurité face aux problèmes d'internet. Si iCloud s'arrête ou que tu n'as pas de connexion, le jeu fonctionne quand même bien. La synchronisation est optionnelle, pour les joueurs qui veulent continuer où ils se sont arrêtés sur un autre appareil sans perdre leur progression.

## Questions fréquentes

### Où ma progression est-elle enregistrée ?

Ta progression est d'abord enregistrée sur ton téléphone. Une copie est également envoyée à iCloud pour qu'elle puisse se synchroniser avec tes autres appareils.

### Que se passe-t-il si je joue sur deux appareils en même temps ?

Quand tu reviens à un appareil ou que l'application se réveille, elle vérifiera iCloud pour les progressions plus récentes et fusionnera ce qu'elle trouve. La fusion garde la progression qui est la plus avancée pour chaque record, ligue ou étoile.

### Combien de temps faut-il pour que la progression se synchronise entre les appareils ?

La synchronisation prend du temps que Apple contrôle, généralement quelques secondes à quelques minutes. Tu devras peut-être attendre un instant ou revenir au jeu après un moment.

### Que se passe-t-il si iCloud s'arrête ou que je n'ai pas de connexion ?

Le jeu fonctionne très bien sans connexion. Ta progression reste sur ton téléphone. La synchronisation avec iCloud se fera quand tu seras de nouveau en ligne.
