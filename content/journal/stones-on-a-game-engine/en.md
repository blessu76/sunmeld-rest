---
title: Moving the stones onto a game engine
description: Why Sunmeld's falling stones and other moving parts now run on a game engine, and how we checked them.
slug: stones-on-a-game-engine
lang: en
category: devlog
keywords: Sunmeld, Flame, engine, animation, performance, journal
published: 2026-11-20T16:00+09:00
---
Sunmeld is still in development for iOS and Android. This note is about how the moving parts of the game are drawn.

## Listing every movement first

Before changing anything, we wrote down every movement in the game: stones falling and bumping, the glow when stones merge, the score that pops up, the warning line, the aim line, and the top bar with score and timer. For each one we asked how much work it puts on the screen every frame. Some were cheap. Others were expensive, such as drawing a stone with a gradient and a soft glow again on every frame.

## Drawing once, moving many times

The engine we chose is Flame, a game engine that runs on Flutter. The stones and the glass are now drawn once as images and placed on each frame. The merge glow is a ready-made soft shape with a color laid on top. The score text is prepared ahead of time. The rules did not change: the same physics does the falling and the merging.

## Checked on a computer, not yet on a phone

We measured on a Mac in profile mode, and the frames stayed inside their budget. That is a computer, not your phone. We have not yet checked the result on a real iPhone or Android phone at its full refresh rate, so the smoothness on real devices is still open.

## Why the engine

Flutter's own drawing tools could do this too. We did not run a side-by-side test, so we do not claim that the engine is faster. We chose it because all the moving parts now run in one loop, which is easier to keep smooth as the game grows.

## What is next

The last step is to check the feel on real devices with high refresh rates, and to look at the small screens again. There is no release date yet.

## FAQ

### Did the way the game plays change?

No. The rules and the physics were kept. Only the drawing and the timing of the moving parts changed.

### Why use a game engine?

Every moving part now runs in one loop, so the game does not have to rebuild the whole screen for each small movement.

### Has it been tested on a phone?

So far it has been measured on a computer. The test on a real phone is still to come.
