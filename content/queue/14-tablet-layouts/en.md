---
title: A screen of its own for tablets
description: Why Sunmeld on a tablet is not just the phone screen stretched, and how we check many screen sizes.
slug: tablet-layouts
lang: en
category: devlog
keywords: Sunmeld, iPad, layout, screen size, testing, journal
---
Sunmeld is still in development for iOS and Android. This note is about what happens when the same game meets a much bigger screen.

## The first attempt: a phone in the middle

At first, on a tablet the game simply showed the phone screen in a narrow column in the middle. Everything worked, but most of the screen was empty. Turn the tablet sideways and it was a phone screen pulled wide. That was fine for testing the game and not fine for playing it.

## Two layouts, not one

We now draw tablets in two separate layouts, portrait and landscape. In portrait, the tub gets bigger, with your opponent above and you below. In landscape, your opponent sits on the left, the tub in the middle and you on the right. The result screen puts the picture on one side and the score and buttons on the other. Phones keep their own screen as before. We pick the layout from the width of the window, not from the device name.

## Checking sizes without a drawer full of devices

We cannot hold every tablet in our hands, so the layout is checked by automatic tests that draw the screens at several phone and tablet sizes, portrait and landscape, and fail if anything overflows or if a layout is chosen that we did not expect. The same checks run for each of the 12 languages, since a long word in one language can break a layout that looks fine in another. We also keep a few real screenshots from tablet simulators to look at with our own eyes.

## A small trap in the tools

One surprise was in the screenshot tools. On a newer tablet system, the simulator can open a landscape app in a window instead of turning the device, so the captured picture came out sideways. We now draw the screen rotated on purpose for those shots, and turn the file back upright.

## What is not checked yet

We have not yet watched a game get rotated halfway through on a real tablet, and windows that are about as narrow as a phone fall back to the phone layout, which we have not looked at closely either. We will say so here when that changes. There is no release date yet.
