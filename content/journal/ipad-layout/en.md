---
title: What to do with the extra room on a big screen
description: How Sunmeld's iPad layout rebuilds the home screen, the sheets and the text size instead of stretching the phone screen.
slug: ipad-layout
lang: en
category: devlog
keywords: Sunmeld, iPad, home screen, landscape, layout, journal
published: 2026-11-22T15:45+09:00
---
Sunmeld is still in development for iOS and Android. This note is about how the home screen and the sheets were rebuilt for the wide screen of an iPad.

## Stretching leaves it empty

Scaling the phone screen up makes the stones bigger but leaves a lot of empty space around them. So instead of stretching it, we asked what should come first on a big screen. The phone screen is untouched.

## Portrait: one centered column

Held upright, the iPad home screen is a single centered column. The order is the same as on the phone, so it feels familiar. The large picture takes whatever height is left in the column. The column's width follows the size of the screen.

## Landscape: picture on the left, actions on the right

Turned sideways, the home screen splits in two. The left side holds the large picture and an introduction to your opponent. The narrow column on the right holds the header line, the league, the daily challenge, start and the menu, from top to bottom. The league's three cells sit side by side on a phone but are stacked here. The eyes go to the picture; the hands work on the right.

## Sheets gather in the middle

Sheets such as settings, the ladder and how to play do not spread across the whole screen. They sit in the middle with a set width. The league and customization screens use a wider column, and the cards for first-time players are narrower still. Lines of text that run endlessly across a wide screen are hard to read.

## Text is a little larger

On iPad the text is shown slightly larger. On a phone it stays as it was. The screen is farther from your eyes, and the same size felt small.

## Orientation depends on the device

iPad allows all four orientations; the phone stays in portrait. Which layout is used depends on the width of the window, not on the device name.

## What we have not checked yet

We have not yet seen whether the game keeps its state when you turn a real iPad in the middle of a game. The same goes for a window as narrow as a phone. If that changes, we'll note it here. There is no release date yet.

## FAQ

### Is the iPad screen just a stretched phone screen?

No. Portrait and landscape each have their own layout. The phone screen has not changed.

### Does the text change on iPad?

It is shown a little larger. On a phone it stays the same.

### Does the screen change when I rotate the iPad?

Yes. Portrait and landscape have different layouts. Rotating in the middle of a game has not been checked on a real device yet.

### Is there a release date?

Not yet. No release date has been set.
