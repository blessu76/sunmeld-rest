---
title: Memindahkan batu ke mesin game
description: Mengapa batu yang jatuh dan bagian bergerak lain di Sunmeld sekarang berjalan di mesin game, dan bagaimana kami memeriksanya.
slug: stones-on-a-game-engine
lang: id
category: devlog
keywords: Sunmeld, Flame, mesin, animasi, performa, jurnal
translation_of: en
---
Sunmeld masih dalam pengembangan untuk iOS dan Android. Catatan ini membahas cara bagian-bagian bergerak dalam game digambar.

## Mendaftar setiap gerakan dulu

Sebelum mengubah apa pun, kami mencatat setiap gerakan dalam game: batu yang jatuh dan saling bertabrakan, kilau saat batu bergabung, skor yang muncul, garis peringatan, garis bidik, dan bilah atas dengan skor dan waktu. Untuk tiap gerakan, kami bertanya seberapa besar kerjanya bagi layar di setiap bingkai. Ada yang ringan. Ada yang berat, seperti menggambar batu dengan gradasi dan kilau lembut berulang kali di setiap bingkai.

## Menggambar sekali, menggerakkan berkali-kali

Mesin yang kami pilih adalah Flame, mesin game yang berjalan di atas Flutter. Batu dan kaca sekarang digambar sekali sebagai gambar, lalu ditempatkan di setiap bingkai. Kilau penggabungan adalah bentuk lembut yang sudah jadi dengan warna di atasnya. Teks skor disiapkan lebih dulu. Aturannya tidak berubah: fisika yang sama mengurus jatuh dan bergabung.

## Diuji di komputer, belum di ponsel

Kami mengukur di Mac dalam mode profil, dan bingkainya tetap dalam anggaran waktunya. Itu komputer, bukan ponselmu. Hasilnya belum kami periksa di iPhone atau Android sungguhan pada kecepatan refresh penuh, jadi kelancaran di perangkat nyata masih terbuka.

## Mengapa mesinnya

Alat gambar Flutter sendiri juga bisa melakukannya. Kami tidak menjalankan uji perbandingan langsung, jadi kami tidak mengklaim mesin ini lebih cepat. Kami memilihnya karena semua bagian bergerak sekarang berjalan dalam satu loop, yang lebih mudah dijaga tetap lancar seiring game berkembang.

## Yang berikutnya

Langkah terakhir adalah memeriksa rasanya di perangkat sungguhan dengan refresh rate tinggi, dan melihat lagi layar kecil. Belum ada tanggal rilis.

## Pertanyaan umum

### Apakah cara bermain game berubah?

Tidak. Aturan dan fisikanya tetap. Yang berubah hanya cara menggambar dan waktu bagian-bagian yang bergerak.

### Mengapa memakai mesin game?

Setiap bagian yang bergerak sekarang berjalan dalam satu loop, jadi game tidak perlu membangun ulang seluruh layar untuk setiap gerakan kecil.

### Apakah sudah diuji di ponsel?

Sejauh ini diukur di komputer. Pengujian di ponsel sungguhan masih akan dilakukan.
