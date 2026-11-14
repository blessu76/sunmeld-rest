---
title: O sol poderia mesmo aparecer?
description: O que aconteceu quando deixamos jogadores de IA jogarem Sunmeld sem parar: a pedra mais alta quase nunca apareceu, e a solução estava nas regras, não na IA.
slug: can-the-sun-appear
lang: pt-BR
category: devlog
keywords: Sunmeld, equilíbrio, IA, testes, design de jogos, diário
translation_of: en
---
O Sunmeld ainda está em desenvolvimento para iOS e Android. Esta nota fala de um problema que só encontramos porque não confiamos na nossa própria sensação do jogo.

## Deixando as IAs jogarem até o fim

No começo, as regras eram um protótipo rápido. Antes de pedir a alguém que as testasse, deixamos jogadores de IA jogarem muitas partidas uns contra os outros, sempre com as mesmas condições iniciais, para que um resultado pudesse ser repetido. Medimos com que frequência uma partida terminava por transbordamento, com que frequência o primeiro jogador vencia e com que frequência alguém fazia a pedra mais alta, o sol.

## O sol nunca veio

Nas regras do protótipo, ninguém jamais fez um sol. Nem a IA fácil, nem a mais difícil. De início parecia um problema da IA, então olhamos para a IA. Depois fizemos as contas.

Cada fusão combina duas pedras numa do estágio seguinte, então o sol reúne muito "volume de pedra". As pedras que caem no pote são pequenas. Dentro do número de jogadas que uma partida permitia, o volume total que poderia entrar no pote ficava bem abaixo do que um sol exige. Nenhuma habilidade constrói algo para o qual as regras não dão material suficiente. Era um problema das regras, não da IA.

## O que mudamos

Remodelamos a escada de estágios e o tamanho do pote, e demos a cada jogador um orçamento de jogadas compatível com a nova escada. Depois disso, as mesmas partidas de IA passaram a produzir sóis, mais vezes com as IAs mais fortes, e menos partidas terminaram em transbordamento. O sol ficou raro, mas possível, que é o que queríamos de um estágio final.

## Uma segunda surpresa: o relógio da mira

Os testes também mostraram que uma partida jogada em tempo real terminava por transbordamento com mais frequência do que a mesma partida jogada instantaneamente. Não era um erro da IA. O relógio do transbordamento continuava correndo enquanto o jogador ainda mirava, então quem tinha acabado de soltar uma pedra num pote cheio podia perder enquanto o outro lado pensava. Agora o relógio de perigo espera enquanto o jogador mira.

## Por que contamos isso

Testar à mão levaria muito tempo para notar que o sol estava fora de alcance. Algumas linhas de aritmética e muitas partidas automáticas encontraram o problema numa tarde. Ainda não há data de lançamento. Quando houver novidades, elas aparecerão aqui.

## Perguntas frequentes

### A pedra mais alta pode mesmo ser alcançada?

Pode. Depois de reformular as regras, os mesmos jogos de teste com IA passaram a produzir sóis, ainda que raramente. Esse era o objetivo para um estágio final.

### O problema era a IA?

Não. O problema estava nas regras. O sol precisa de mais volume de pedra do que as quedas permitidas em uma partida conseguiam trazer para a cuba.

### O relógio de perigo continua correndo enquanto eu miro?

Não. O relógio de transbordamento agora espera enquanto um jogador mira.

### Existe data de lançamento?

Não. Ainda não há data de lançamento.
