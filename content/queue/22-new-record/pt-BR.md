---
title: A marca de "novo recorde" depois de uma partida de treino
description: Quando a tela de resultado mostra um novo recorde, quais recordes contam e como a marca aparece.
slug: new-record
lang: pt-BR
category: devlog
keywords: Sunmeld, novo recorde, resultado, sequência, treino, diário
translation_of: en
---
O Sunmeld continua em desenvolvimento para iOS e Android. Esta nota fala de uma pequena marca na tela de resultado que aparece quando uma partida de treino estabelece um novo recorde.

## Por que uma marca no resultado

Um recorde só é útil se você percebe. Antes desta mudança, uma melhor pontuação ou a maior sequência de vitórias podia subir sem nenhum sinal na tela de resultado. Por isso acrescentamos uma linha acima do resumo com o texto "Novo recorde", seguida dos recordes que esta partida estabeleceu.

## Só o que subiu é mostrado

A linha lista apenas os recordes que subiram nesta partida: a melhor pontuação no nível difícil e a maior sequência de vitórias. Se nada subiu, nenhuma linha aparece. Uma primeira vitória no nível difícil também conta como novo recorde.

## Sequências começam em dois

Uma sequência só é mostrada quando a maior sequência tem pelo menos dois. Caso contrário, cada primeira vitória traria a marca, e ela não diria nada.

## Só partidas de treino

Partidas de liga, o desafio diário e o modo rush não somam ao recorde de treino, então também não mostram a marca. Tocar em "Jogar de novo" a limpa, para que uma marca antiga não passe para a próxima partida.

## Como aparece

A marca cresce de um tamanho um pouco menor até o tamanho normal. Quando o movimento reduzido está ativado no sistema ou no app, ela aparece direto no tamanho normal, sem movimento. Usa o mesmo estilo de etiqueta da marca "novo melhor" no empilhamento solo e no rush.

## O que ainda não verificamos

Ainda não vimos como a marca fica em um aparelho de verdade, nem como um leitor de tela a lê. Em uma tela muito pequena, pode ser preciso rolar um pouco mais para chegar aos botões. Ainda não há data de lançamento.

## Perguntas frequentes

### A marca aparece nas partidas de liga?

Não. Partidas de liga, o desafio diário e o rush não a mostram.

### O que conta como novo recorde?

Uma melhor pontuação mais alta no nível difícil, ou uma sequência de vitórias mais longa. Uma primeira vitória no nível difícil também conta.

### Por que uma sequência precisa de duas vitórias?

Uma sequência de uma vitória seria toda primeira vitória. Começar em duas mantém a marca significativa.

### Há data de lançamento?

Ainda não. Nenhuma data foi definida.
