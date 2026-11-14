---
title: Could the sun ever appear?
description: What happened when we let AI players play Sunmeld over and over: the top stone almost never showed up, and the fix was in the rules, not the AI.
slug: can-the-sun-appear
lang: en
category: devlog
keywords: Sunmeld, balance, AI, testing, game design, journal
copy_review: iris 2026-11-14
---
Sunmeld is still in development for iOS and Android. This note is about a problem we only found because we did not trust our own feel for the game.

## Letting the AIs play it out

Early on, the rules were a quick prototype. Before asking anyone to try them, we let AI players play the game many times against each other, with the same starting conditions each time so that a result could be repeated. We tracked how often a game ended by overflow, how often the first player won, and how often anyone made the highest stone, the sun.

## The sun never came

In the prototype rules, nobody ever made a sun. Not the easy AI, not the hardest one. At first it looked like an AI problem, so we looked at the AI. Then we did the arithmetic instead.

Each merge combines two stones into one of the next stage, so the sun holds a lot of "stone volume". The stones that drop into the tub are small ones. Over the number of drops a game allowed, the total volume that could ever enter the tub was well below what one sun needs. No amount of skill can build something the rules do not give you enough material for. It was a rules problem, not an AI problem.

## What we changed

We reshaped the ladder and the size of the tub, and gave each player a drop budget that fits the new ladder. After that, the same AI games produced suns, more often for the stronger AIs, and fewer games ended by overflow. A sun became rare but possible, which is what we wanted from a final stage.

## A second surprise: the aiming clock

The test runs also showed that a game played in real time ended by overflow more often than the same game played instantly. It was not a bug in the AI. The overflow clock kept running while a player was still aiming, so whoever had just dropped a stone into a crowded tub could lose while the other side was thinking. Now the danger clock waits while a player aims.

## Why we tell you this

Playtesting by hand would have taken a long time to notice that the sun was out of reach. A few lines of arithmetic and a lot of automatic games found it in an afternoon. There is no release date yet. When there is news, it will show up here.

## FAQ

### Can the top stone really be reached?

Yes. After the rules were reshaped, the same AI test games produced suns, though rarely. That was the goal for a final stage.

### Was the problem the AI?

No. The problem was the rules. The sun needs more stone volume than the drops allowed in a game could ever bring into the tub.

### Does the danger clock still run while I aim?

No. The overflow clock now waits while a player is aiming.

### Is there a release date?

No. There is no release date yet.
