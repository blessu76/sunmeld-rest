---
title: One night sky, two looks
description: How Sunmeld's look was redone, and why the tub stays dark even when you choose the light theme.
slug: two-looks-one-night-sky
lang: en
category: devlog
keywords: Sunmeld, design, theme, dark mode, journal
---
Sunmeld is still in development for iOS and Android. This note is about how the game got its look, and about a choice we made on purpose.

## Starting over once

The first version of the screens did not feel finished. It worked, but it looked like a prototype. So we went back to the design sketches and rebuilt the home screen, the game screen and the result screens from the ground up. The stones became celestial bodies with a glow, a thin ring marks a merge, and the score bumps when it goes up. The rules and the engine were not touched. Only the look changed.

## Dark and light, on request

After that we added a theme choice in settings: follow the system, dark, or light. The dark look is a deep night sky with stars. The light look is a soft dawn with pastel colors and cream cards. If you pick "follow the system", the game switches with your phone, even while a sheet is open.

## The tub stays dark

The tub is the one thing that does not change with the theme. Even in the light theme, the tub keeps its night color. Two reasons. The stones, with their glow, read best against a dark sky. And a game board that looks the same in both themes means the same game reads the same way for everyone, whichever theme they picked.

## Small things we had to handle

Text on gold and pink buttons needed its own dark ink so it stays readable. The launch screen color has to match the theme before the app can read your setting, so it follows the system only. That is a limit of the phone, not a choice. We also keep a test that checks that the dark and light themes define exactly the same set of colors, so one cannot be missing a color the other has.

## What is next

We keep checking how screens look at small sizes. There is no release date yet. When there is news, it will show up here.
