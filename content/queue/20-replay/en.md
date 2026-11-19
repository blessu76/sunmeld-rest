---
title: Watching a finished game again, one move at a time
description: How the replay of a finished Sunmeld game works and how we checked that it plays back the same.
slug: replay
lang: en
category: devlog
keywords: Sunmeld, replay, rewatch, game, journal
---
Sunmeld is still in development for iOS and Android. This note is about a feature that lets you watch a finished game again, one move at a time.

## Why watch again

After a game ends you start asking why it was lost. You know the last stone overflowed, but it is harder to remember where things began to tip. So we added "Watch again" to the result screen.

## We write down moves, not video

The game is not recorded as video. We write down only what is needed to rebuild it: the random value the game started from, who played first, and for every dropped stone which step it came at, where it was placed and what kind of stone it was. A stone that dropped by itself when time ran out is written down the same way.

## Fed back in on the same step

When you press "Watch again", the saved moves are fed back into the game engine on the same steps. The same input gives the same result. Not only the score but also the position and stage of every stone has to match, and an automated test holds that fixed. The tests include stones dropped by a timeout, special stones, a game where the opponent started and a saved record being read back.

## How to watch

There are play and pause, restart and next move, and you can switch between slower and faster speeds. If reduced motion is on in the system or in the app, the replay starts paused and without the glow effects. Then you can step through one move at a time with "Next move".

## Limits for now

Only games against the AI opponents can be replayed. Solo stacking and practice games are not included. Only the most recent game can be watched, and the only way in is the result screen. The AI's aiming movement is not redrawn; the stone goes straight to where it fell. The outcome of the drop is the same.

## What we have not checked yet

We have not checked how it feels on a real device or how it sounds with a screen reader. We also do not yet know how large the record gets for a very long game. If that changes, we'll note it here. There is no release date yet.

## FAQ

### Can I watch a previous game again?

You can watch the most recently finished game against an AI opponent from the result screen.

### Can the replay come out differently?

No. The saved moves are fed back on the same steps, and tests check that the score and the position of every stone match.

### Can I replay solo stacking too?

Not yet. For now only games against the AI opponents are supported.

### Is there a release date?

Not yet. No release date has been set.
