---
title: Levar as pedras para um motor de jogo
description: Por que as pedras que caem e as outras partes em movimento do Sunmeld agora rodam em um motor de jogo, e como verificamos isso.
slug: stones-on-a-game-engine
lang: pt-BR
category: devlog
keywords: Sunmeld, Flame, motor, animação, desempenho, diário
translation_of: en
---
O Sunmeld ainda está em desenvolvimento para iOS e Android. Esta nota trata de como as partes em movimento do jogo são desenhadas.

## Primeiro, listar cada movimento

Antes de mudar qualquer coisa, anotamos cada movimento do jogo: pedras caindo e batendo, o brilho quando as pedras se fundem, a pontuação que aparece, a linha de aviso, a linha de mira e a barra superior com pontuação e tempo. Para cada um, perguntamos quanto trabalho ele exige da tela a cada quadro. Alguns eram baratos. Outros eram caros, como desenhar uma pedra com degradê e um brilho suave a cada quadro.

## Desenhar uma vez, mover muitas vezes

O motor escolhido é o Flame, um motor de jogos que roda sobre o Flutter. As pedras e o vidro agora são desenhados uma vez como imagens e posicionados a cada quadro. O brilho da fusão é uma forma suave já pronta com uma cor por cima. O texto da pontuação é preparado com antecedência. As regras não mudaram: a mesma física cuida da queda e da fusão.

## Verificado no computador, ainda não no celular

Medimos em um Mac no modo de perfil, e os quadros ficaram dentro do limite de tempo. Isso é um computador, não o seu celular. Ainda não verificamos o resultado em um iPhone ou Android de verdade, na taxa de atualização máxima, então a fluidez nos aparelhos reais continua em aberto.

## Por que o motor

As ferramentas de desenho do próprio Flutter também conseguiriam fazer isso. Não fizemos um teste lado a lado, então não afirmamos que o motor seja mais rápido. Escolhemos porque todas as partes em movimento agora rodam em um único laço, o que facilita manter a fluidez conforme o jogo cresce.

## O que vem a seguir

O último passo é checar a sensação em aparelhos reais com alta taxa de atualização, e revisar as telas pequenas. Ainda não há data de lançamento.

## Perguntas frequentes

### A forma de jogar mudou?

Não. As regras e a física foram mantidas. Mudaram apenas o desenho e o momento das partes em movimento.

### Por que usar um motor de jogo?

Agora todas as partes em movimento rodam em um único laço, então o jogo não precisa reconstruir a tela inteira a cada pequeno movimento.

### Já foi testado em celular?

Até agora foi medido em computador. O teste em um celular real ainda está por vir.
