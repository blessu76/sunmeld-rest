---
title: Progress stays on the phone — and can sync across your devices
description: How Sunmeld saves your game progress locally, and what happens when you play on another device with the same Apple account.
slug: progress-stays-on-phone
lang: en
category: devlog
keywords: Sunmeld, progress, save, iCloud, sync, storage
copy_review: iris 2026-11-15
---
Sunmeld is still in development for iOS and Android. This note is about how your game progress is saved and shared across your devices.

## Where your progress lives

Your progress — the stars you have earned, the records you have set, the leagues you have played, and your nickname — is saved on your phone first. That is the source of truth. We also send a copy to iCloud so it can travel with you if you play on another device.

## Playing on another device

If you play Sunmeld on another device with the same Apple account, the progress from both devices gets merged. Whenever you open the game or come back to it, the app checks iCloud for newer progress and brings it in. The merge rule is simple: for each piece of progress like a record or a league level, we keep the one that is further along. We do not add them together. If one device has cleared league 2 and another has cleared league 1, the device with league 1 gets updated to league 2.

## How fast devices sync

The sync between your devices takes time that Apple controls, usually a few seconds to a few minutes. You may have to wait for a moment or come back to the game after a little while to see the other device's progress.

## Settings and nickname

Your settings — the theme, the language and the sounds you turned on or off — sync across your devices too. Your nickname follows its own rule: if you change it on two devices, the most recent change wins, and a device that has no nickname never erases one that does.

## Why this matters

The phone is still the device you hold. Your progress is there first, safe from internet problems. If iCloud goes down or you do not have a connection, the game still works. Sync is there for players who want to pick up where they left off on a different device without losing any progress.

## FAQ

### Where is my progress saved?

Your progress is saved on your phone first. A copy is also sent to iCloud so it can sync to your other devices.

### What happens if I play on two devices at the same time?

When you come back to the game on either device, the app checks iCloud for newer progress and merges what it finds. The merge keeps the progress that is further along for each record, league, or star count.

### How long does it take for progress to sync between devices?

Syncing takes time that Apple controls, usually a few seconds to a few minutes. You may have to wait a moment or come back to the game after a while to see the other device's progress.

### What if iCloud is down or I have no connection?

The game works fine without a connection. Your progress stays on your phone. The sync to iCloud will catch up when you are online again.
