---
title: "Stealing Two Days in Huangshan Between Releases"
date: 2026-10-19
authors: [vonng]
summary: >
  A family road trip from Shanghai to southern Anhui—rice paddies at Tachuan Academy, hairy tofu in Hongcun, and shipping the Silo October security release and Oink v1.3's native photo gallery from the road.
tags: [Open Source, Essay, Travel]
---

Over the past couple of days, I drove from Shanghai through Hangzhou down to Huangshan. We spent this morning around Hongcun and checked into an inn at the foot of Mount Huangshan for the night—stealing two days away to show the family around and catch a breather.

Things really have been hectic lately. I have a batch of commercial contracts up for renewal, three slide decks to put together for November talks (one at Tsinghua University, one at the China Enterprise AI Conference, and another at PGConf.Asia), adaptation work lined up for next month's PostgreSQL 19 GA release, plus a dozen new fronts opened up by AI coding. All of it takes serious bandwidth.

Fortunately, with AI riding shotgun, as long as I have a laptop within reach, the wheels keep turning even when I am on the road. None of our open-source product lines have missed a beat on their release cadence. Over the last few days, I shipped updates to two projects along the way:

## Silo `20261018` Monthly Security Release

**[Silo](/en/db/long-live-silo/)**, the open-source object storage fork of MinIO that I maintain, shipped its `20261018` monthly release yesterday, focusing on security hardening and component synchronization:

- **Core security fixes**: The October security update patches vulnerabilities in **Object Lock**, **Admin Credentials**, and **JWK parsing**. If you rely on object storage for database backups—especially immutable backups against ransomware or accidental deletion—and compliance archiving, closing these low-level permission and locking gaps is non-negotiable.

- **Synchronized ecosystem artifacts**: The companion client `mcli 20261018`, the full-featured web management console `Console v2.4.2`, and the core library `silo-pkg 3.14.3` have all been built and updated in lockstep. By user request, the `KES` key management component is now officially part of the build and distribution pipeline as well.

- **Ready out of the box**: As usual, the release ships with prebuilt binaries, multi-arch container images (including Distroless variants), and native RPM / DEB / APK packages. It remains a drop-in replacement with full compatibility for existing `MINIO_*` environment variables, the S3 API, and on-disk data volumes—just swap the image or package for a smooth upgrade.

Project homepage & changelog: [Silo](https://silo.pgsty.com/)

![Silo 20261018 monthly security release announcement](silo-release.webp)

## Oink `v1.3`: Native Expo Photo Galleries

Alongside our storage layer, **[Oink](/en/ai/oink-intro/)**, the local-first Hugo theme framework that powers our entire documentation fleet, also reached `v1.3` over the past few days (with patch releases already up to `v1.3.2`). The headline update adds a native **Expo** photo gallery layout alongside the existing **Docs**, **Blog**, and **Book** archetypes:

![Oink 1.3 native Expo photo gallery](oink-expo.webp)

- **A directory is an album, zero boilerplate**: Following an engineering-first approach, a standard Hugo leaf bundle—an `index.md` plus a folder of images—is all it takes to make an album. Drop your photos into the directory and Oink renders the gallery automatically, without creating per-image pages or hand-writing piles of YAML.

- **Three layout modes and a full-resolution viewer**: Expo includes **Wall**, **Cards**, and **Seamless** layouts right out of the box and automatically remembers each reader's view preference. The built-in full-resolution viewer supports smooth continuous zoom, drag-to-pan inspection, GIF playback controls, touch gestures, and a full set of keyboard shortcuts (`Q`/`E` or arrow keys to switch photos, `K`/`J` to zoom, `F` to expand, and more).

- **Engineering polish across the board**: The build baseline has been upgraded to `Hugo Extended 0.166.0` and `Go 1.27`, accompanied by fixes for sidebar navigation scoping, Draw.io modal focus handling, code block interactions on landing pages, and full-book print aggregation (`Print`). All 36 sites we maintain are already running the latest release.

![Wildlife photo wall in an Oink Expo gallery](wildlife-gallery.webp)

Since I took plenty of good photos on this trip through southern Anhui, Oink's new gallery feature will come in handy as soon as I get back. Project homepage & live demo: [Oink](https://oink.pgsty.com/)

![Desert poplars and sand dunes in an Oink Expo gallery](desert-gallery.webp)

## Hongcun and Tachuan Academy

We woke up in Hongcun at Tachuan Academy, a wonderful boutique inn looking out over a beautiful stretch of rice paddies.

![featured.jpg](featured.jpg)

![Tachuan Academy inn by the stream](tachuan-inn.jpg)

![Rice paddies and trees beside Tachuan Academy](tachuan-fields.jpg)

There were also a few resident cats that weren't the least bit shy around people—one of them looked uncannily like, well...

For lunch we had two classic Anhui specialties: *chouguiyu* (fermented mandarin fish, famously pungent and tender) and *maodoufu* ("hairy tofu," pan-fried after fermenting under a coat of white mycelium). Both live up to their reputation.

![Anhui-style pan-fried hairy tofu](hairy-tofu.jpg)

After lunch we strolled around Hongcun. I have been to Huangshan several times, but this was my first time setting foot inside Hongcun itself. Honestly, as a top-tier 5A tourist attraction, it is wildly overrated. It felt thoroughly average—just another restored old town. The upkeep is decent enough, but turning it into a ticketed attraction feels completely redundant. The open countryside and the inn outside the village were far nicer.

![Ancient tree and tourists in Hongcun](hongcun-tree.jpg)

![Huizhou-style houses along the water in Hongcun](hongcun-houses.jpg)

![Stone inscription at the entrance to Hongcun](hongcun-sign.jpg)

Tonight we are staying at a guesthouse at the foot of Mount Huangshan. On previous trips I always stayed in Tangkou Town, but this time we booked near the East Gate, where the new Donghai Cableway and Donghai Scenic Area opened less than six months ago—a good excuse to check out the new route.

The mountain air really is something else; I have slept like a rock the past two nights. No need to turn this into an essay—just jotting down a few notes while stealing a break. Back to enjoying the scenery with the family. Tomorrow we push up Mount Huangshan and drive all the way back to Shanghai in a single day, and we'll take it from there.
