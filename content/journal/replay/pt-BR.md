---
title: Rever uma partida terminada, jogada por jogada
description: Como funciona o replay de uma partida terminada do Sunmeld e como verificamos que ele toca igual.
slug: replay
lang: pt-BR
category: devlog
keywords: Sunmeld, replay, rever, partida, diário
translation_of: en
published: 2026-11-23T18:00+09:00
---
O Sunmeld ainda está em desenvolvimento para iOS e Android. Esta nota trata de um recurso que permite rever uma partida terminada, jogada por jogada.

## Por que rever

Quando uma partida termina, a gente quer saber por que perdeu. Você sabe que a última pedra transbordou, mas é mais difícil lembrar onde tudo começou a virar. Por isso colocamos "Rever" na tela de resultado.

## Anotamos jogadas, não vídeo

A partida não é gravada em vídeo. Anotamos só o necessário para reconstruí-la: o valor aleatório com que começou, quem jogou primeiro e, para cada pedra solta, em que passo caiu, onde foi colocada e de que tipo era. Uma pedra que caiu sozinha quando o tempo acabou é anotada do mesmo jeito.

## Reenviado no mesmo passo

Ao tocar em "Rever", as jogadas guardadas são enviadas de novo ao motor do jogo nos mesmos passos. A mesma entrada dá o mesmo resultado. Não só a pontuação: a posição e o estágio de cada pedra precisam coincidir, e um teste automático fixa isso. Os testes incluem pedras caídas por tempo esgotado, pedras especiais, uma partida iniciada pelo oponente e a leitura de volta de um registro salvo.

## Como assistir

Há reproduzir e pausar, recomeçar e próxima jogada, e você pode alternar entre mais lento e mais rápido. Se "reduzir movimento" estiver ativado no sistema ou no app, o replay começa pausado e sem efeitos de brilho. Aí você avança jogada por jogada com "Próxima jogada".

## Limites por enquanto

Só partidas contra oponentes de IA podem ser repetidas. Empilhar sozinho e partidas de treino não entram. Só dá para ver a última partida, e a única entrada é a tela de resultado. O movimento de mira da IA não é redesenhado; a pedra vai direto ao lugar onde caiu. O resultado da queda é o mesmo.

## O que ainda não verificamos

Ainda não verificamos como é a sensação em um dispositivo real nem como soa com um leitor de tela. Também não sabemos o tamanho do registro numa partida muito longa. Se isso mudar, anotaremos aqui. Ainda não há data de lançamento.

## Perguntas frequentes

### Posso rever uma partida anterior?

Você pode rever, na tela de resultado, a última partida terminada contra um oponente de IA.

### O replay pode sair diferente?

Não. As jogadas guardadas são reenviadas nos mesmos passos, e testes verificam que a pontuação e a posição de cada pedra coincidem.

### Posso rever também o empilhar sozinho?

Ainda não. Por enquanto só há suporte a partidas contra oponentes de IA.

### Existe data de lançamento?

Ainda não. Nenhuma data de lançamento foi definida.
