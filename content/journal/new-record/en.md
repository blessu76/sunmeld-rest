---
title: A "new record" mark after a practice match
description: When the result screen shows a new record, which records count, and how the mark appears.
slug: new-record
lang: en
category: devlog
keywords: Sunmeld, new record, result, streak, practice, journal
published: 2026-11-25T14:30+09:00
---
Sunmeld is still in development for iOS and Android. This note is about a small mark on the result screen that shows when a practice match sets a new record.

## Why a mark on the result

A record is only useful if you notice it. Before this change, a best score or a longest win streak could go up with no sign on the result screen. So we added a line above the summary that reads "New record", followed by the records this match set.

## Only what went up is shown

The line lists only the records that rose in this match: the best score on the hard setting and the longest win streak. If nothing rose, no line appears. A first win on the hard setting also counts as a new record.

## Streaks start at two

A streak is shown only when the longest streak is at least two. Otherwise every first win would bring the mark, and it would tell you nothing.

## Only practice matches

League, daily challenge and rush games do not add to the practice record, so they do not show the mark either. Pressing "Play again" clears it, so an old mark is not carried into the next match.

## How it appears

The mark grows from a little smaller to its full size. When reduced motion is on in the system or in the app, it appears at full size without the movement. It uses the same tag style as the "new best" mark in solo stacking and rush.

## What we have not checked yet

We have not yet seen how the mark looks on a real device, or how a screen reader reads it. On a very small screen the result may need a little more scrolling to reach the buttons. There is no release date yet.

## FAQ

### Does the mark show in league games?

No. League, daily challenge and rush games do not show it.

### What counts as a new record?

A higher best score on the hard setting, or a longer best win streak. A first win on the hard setting also counts.

### Why does a streak need two wins?

A streak of one would be every first win. Starting at two keeps the mark meaningful.

### Is there a release date?

Not yet. No release date has been set.
