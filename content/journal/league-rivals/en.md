---
title: Who you beat in the league, one rival at a time
description: How the league now keeps a win and game count against each opponent, and how those counts are merged between your devices.
slug: league-rivals
lang: en
category: devlog
keywords: Sunmeld, league, record, rival, iCloud, journal
published: 2026-11-24T17:00+09:00
---
Sunmeld is still in development for iOS and Android. This note is about a new table in the league: how many games you have won and played against each opponent.

## Why a record per opponent

The league already keeps stars for your progress, but stars do not say how many games you played against someone. A player who has lost to the same rival again and again wants to see that plainly. So we added a small table to the record sheet, with one line for each opponent you have faced.

## Only the opponents you have met

The table lists only the rivals you have played at least once. Opponents you have not met yet are not listed, and locked opponents do not show their names either. If there is no game in the league yet, the section stays hidden.

## A loss counts too

A win adds one to both the wins and the games. A loss or a draw adds one to the games only.

## Old games are not added back

Stars do not tell how many games were played, so the table starts empty for progress saved before this change. We do not guess old numbers from the stars. The count starts from the first league game played in the new version.

## Two phones, one table

When your progress is merged from iCloud, each opponent's line is taken from the phone that has played more games against that opponent. If the games are equal, the line with more wins is kept. The numbers are not added together, so the same game is not counted twice. The result is the same whichever phone is merged first, and merging more than once gives the same answer.

## What we have not checked yet

We have not yet seen how the table looks on a real phone, or how a screen reader reads it in order. We have also not tested a real merge between two devices. If that changes, we'll note it here. There is no release date yet.

## FAQ

### Does the table list every opponent?

No. It lists only the opponents you have played at least once. Locked and unmet opponents are hidden.

### Does a loss count?

Yes. A loss adds one game to the table. A win adds one to the wins and one to the games.

### Will my old league games appear?

No. Earlier progress starts with an empty table, because the stars do not tell how many games were played.

### Is there a release date?

Not yet. No release date has been set.
