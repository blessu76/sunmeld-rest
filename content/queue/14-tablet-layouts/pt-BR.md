---
title: Uma tela própria para tablets
description: Por que o Sunmeld no tablet não é só a tela do celular esticada, e como conferimos muitos tamanhos de tela.
slug: tablet-layouts
lang: pt-BR
category: devlog
keywords: Sunmeld, iPad, layout, tamanho de tela, testes, diário
translation_of: en
---
O Sunmeld ainda está em desenvolvimento para iOS e Android. Esta nota fala do que acontece quando o mesmo jogo encontra uma tela muito maior.

## A primeira tentativa: um celular no meio

No início, num tablet o jogo simplesmente mostrava a tela do celular numa coluna estreita no meio. Tudo funcionava, mas a maior parte da tela ficava vazia. Ao virar o tablet de lado, era uma tela de celular esticada. Dava para testar o jogo, mas não para jogá-lo.

## Dois layouts, não um

Agora desenhamos os tablets em dois layouts separados, retrato e paisagem. No retrato, o pote fica maior, com o oponente em cima e você embaixo. Na paisagem, o oponente fica à esquerda, o pote no meio e você à direita. A tela de resultado põe a imagem de um lado e a pontuação e os botões do outro. Os celulares mantêm a tela própria de sempre. Escolhemos o layout pela largura da janela, não pelo nome do aparelho.

## Conferindo tamanhos sem uma gaveta cheia de aparelhos

Não temos como segurar todos os tablets nas mãos, então o layout é conferido por testes automáticos que desenham as telas em vários tamanhos de celular e tablet, em retrato e paisagem, e falham se algo transbordar ou se um layout inesperado for escolhido. As mesmas verificações rodam para cada um dos 12 idiomas, já que uma palavra longa num idioma pode quebrar um layout que parece bom em outro. Também guardamos algumas capturas reais de simuladores de tablet para olhar com os nossos próprios olhos.

## Uma pequena armadilha nas ferramentas

Uma surpresa veio das ferramentas de captura de tela. Num sistema de tablet mais novo, o simulador pode abrir um app em paisagem numa janela em vez de girar o aparelho, e a imagem capturada saía de lado. Agora desenhamos a tela girada de propósito para essas capturas e viramos o arquivo de volta.

## O que ainda não foi conferido

Ainda não vimos uma partida ser girada no meio, num tablet real, e janelas tão estreitas quanto um celular voltam ao layout de celular, que também ainda não examinamos de perto. Avisaremos aqui quando isso mudar. Ainda não há data de lançamento.

## Perguntas frequentes

### O tablet tem um layout próprio?

Tem. Tablets usam layouts separados em retrato e paisagem, escolhidos pela largura da janela e não pelo nome do aparelho. Celulares mantêm a própria tela.

### Como são testados tantos tamanhos de tela?

Testes automáticos desenham as telas em vários tamanhos de celular e tablet, em retrato e paisagem, para cada um dos 12 idiomas.

### Já foi testado girar durante uma partida em um tablet real?

Ainda não. Ainda não vimos uma partida ser girada no meio do jogo em um tablet real.

### Existe data de lançamento?

Não. Ainda não há data de lançamento.
