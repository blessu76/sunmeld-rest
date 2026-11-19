---
title: A chave de som que não fazia nada
description: Por que a configuração de som do Sunmeld ficou muda por um tempo, e o que acrescentamos para que a fusão possa ser ouvida.
slug: sound-that-was-silent
lang: pt-BR
category: devlog
keywords: Sunmeld, som, áudio, configurações, modo silencioso, diário
translation_of: en
published: 2026-11-19T17:45+09:00
---
O Sunmeld ainda está em desenvolvimento para iOS e Android. Esta nota trata de uma configuração que existia, mas não conseguia fazer nada.

## A chave estava lá, o som não

A tela de configurações tinha uma chave de som, e ela salvava bem a sua escolha. O jogo a consultava toda vez que uma pedra caía ou se fundia. Mas a parte que deveria tocar o som era um espaço vazio. Deixamos assim de propósito, porque os arquivos de som e a licença ainda não estavam decididos. A chave em si nunca esteve quebrada. O que faltava era o som.

## Fizemos os sons nós mesmos

Em vez de esperar uma licença, criamos os sons por conta própria. São dezesseis efeitos curtos para coisas como pousar, fundir, as cadeias e o aviso de transbordamento. Eles são gerados por um pequeno script que não usa números aleatórios, então rodá-lo duas vezes dá os mesmos arquivos. No total, somam cerca de 220 KB.

## Silêncio quando seu celular está em silêncio

O jogo está configurado para respeitar a chave de silencioso no iPhone, e para não interromper a música de outro app que já esteja tocando. No Android, ele toca como som de jogo e não pega o foco de áudio. Se um som não conseguir tocar, a partida segue normalmente.

## O que ainda não ouvimos

Os sons estão ligados e o app compila com eles. Ainda não os ouvimos em um iPhone de verdade, em um ambiente de verdade, com volume normal. O timbre e o volume talvez precisem de mais um ajuste. Quando isso acontecer, basta trocar um arquivo de som por outro com o mesmo nome.

## Perguntas frequentes

### Por que antes não havia som?

A saída de som era um espaço silencioso. Os arquivos de som e a parte de áudio do app só foram adicionados recentemente.

### O jogo respeita a chave de silencioso no iPhone?

É assim que está configurado. Ainda não verificamos em um aparelho real; diremos mais quando fizermos isso.

### Posso desligar o som?

Sim. A chave de som nas configurações controla os efeitos. Quando está desligada, o jogo não toca nada.
