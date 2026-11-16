---
title: Tombol suara yang tidak melakukan apa-apa
description: Mengapa pengaturan suara Sunmeld sempat diam, dan apa yang kami tambahkan agar bunyi penggabungan bisa terdengar.
slug: sound-that-was-silent
lang: id
category: devlog
keywords: Sunmeld, suara, audio, pengaturan, mode senyap, jurnal
translation_of: en
---
Sunmeld masih dalam pengembangan untuk iOS dan Android. Catatan ini membahas pengaturan yang ada tetapi tidak bisa berbuat apa-apa.

## Tombolnya ada, suaranya tidak

Layar pengaturan punya tombol suara, dan pilihanmu tersimpan dengan benar. Game memeriksanya setiap kali batu jatuh atau bergabung. Tetapi bagian yang seharusnya memutar suara hanyalah placeholder kosong. Kami sengaja membiarkannya begitu, karena berkas suara dan lisensinya belum diputuskan. Tombolnya sendiri tidak pernah rusak. Yang belum ada adalah suaranya.

## Membuat suaranya sendiri

Daripada menunggu lisensi, kami membuat suaranya sendiri. Ada enam belas efek pendek untuk hal seperti mendarat, bergabung, rantai, dan peringatan luapan. Semuanya dibuat oleh skrip kecil yang tidak memakai angka acak, jadi menjalankannya dua kali menghasilkan berkas yang sama. Totalnya sekitar 220 KB.

## Senyap saat ponselmu senyap

Game sudah diatur untuk menghormati tombol senyap di iPhone, dan tidak menghentikan musik dari aplikasi lain yang sedang diputar. Di Android, suara diputar sebagai suara game dan tidak mengambil fokus audio. Jika suara gagal diputar, ronde tetap berjalan seperti biasa.

## Yang belum kami dengar

Suaranya sudah tersambung dan aplikasinya bisa dibangun dengan suara itu. Tetapi kami belum mendengarkannya di iPhone sungguhan, di ruangan sungguhan, pada volume normal. Nada dan kerasnya mungkin perlu diperbaiki lagi. Jika begitu, berkas suara bisa diganti dengan yang memiliki nama sama.

## Pertanyaan umum

### Mengapa dulu tidak ada suara?

Keluaran suaranya berupa placeholder senyap. Berkas suara dan bagian audio aplikasi baru ditambahkan belakangan ini.

### Apakah game menghormati tombol senyap di iPhone?

Begitulah pengaturannya. Kami belum memeriksanya di perangkat sungguhan, dan kami akan memberi kabar setelah itu.

### Bisakah saya mematikan suaranya?

Bisa. Tombol suara di pengaturan mengendalikan efek. Saat dimatikan, game tidak memutar apa pun.
