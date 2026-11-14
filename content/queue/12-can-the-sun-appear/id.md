---
title: Mungkinkah matahari muncul?
description: Apa yang terjadi saat kami membiarkan pemain AI memainkan Sunmeld berulang kali: batu tertinggi hampir tidak pernah muncul, dan solusinya ada di aturan, bukan di AI.
slug: can-the-sun-appear
lang: id
category: devlog
keywords: Sunmeld, keseimbangan, AI, pengujian, desain game, jurnal
translation_of: en
---
Sunmeld masih dalam pengembangan untuk iOS dan Android. Catatan ini tentang masalah yang baru kami temukan karena kami tidak mempercayai perasaan kami sendiri terhadap game ini.

## Membiarkan AI bermain sampai selesai

Di awal, aturannya hanyalah prototipe cepat. Sebelum meminta siapa pun mencobanya, kami membiarkan pemain AI memainkan game ini berkali-kali melawan satu sama lain, dengan kondisi awal yang sama setiap kali agar hasilnya bisa diulang. Kami mencatat seberapa sering game berakhir karena meluap, seberapa sering pemain pertama menang, dan seberapa sering ada yang berhasil membuat batu tertinggi, yaitu matahari.

## Matahari tidak pernah datang

Dengan aturan prototipe, tidak ada yang pernah membuat matahari. Bukan AI yang mudah, bukan pula yang tersulit. Awalnya ini tampak seperti masalah AI, jadi kami memeriksa AI-nya. Lalu kami menghitungnya.

Setiap penggabungan menyatukan dua batu menjadi satu batu tahap berikutnya, sehingga matahari menyimpan banyak "volume batu". Batu yang jatuh ke toples adalah batu kecil. Dalam jumlah jatuhan yang diizinkan satu game, total volume yang bisa masuk ke toples jauh di bawah yang dibutuhkan satu matahari. Sehebat apa pun kemampuannya, tidak ada yang bisa membangun sesuatu jika aturannya tidak menyediakan bahan yang cukup. Ini masalah aturan, bukan masalah AI.

## Yang kami ubah

Kami membentuk ulang tangga tahap dan ukuran toples, lalu memberi setiap pemain jatah jatuhan yang sesuai dengan tangga yang baru. Setelah itu, game AI yang sama menghasilkan matahari, lebih sering oleh AI yang lebih kuat, dan lebih sedikit game yang berakhir karena meluap. Matahari menjadi langka tetapi mungkin dibuat, dan itulah yang kami inginkan dari tahap terakhir.

## Kejutan kedua: jam membidik

Hasil uji juga menunjukkan bahwa game yang dimainkan secara real time lebih sering berakhir karena meluap daripada game yang sama yang dimainkan seketika. Ini bukan bug pada AI. Jam luapan terus berjalan saat pemain masih membidik, sehingga pemain yang baru saja menjatuhkan batu ke toples yang padat bisa kalah selagi pihak lain berpikir. Sekarang jam bahaya berhenti menunggu selama pemain membidik.

## Mengapa kami menceritakan ini

Bermain uji secara manual akan butuh waktu lama untuk menyadari bahwa matahari tidak terjangkau. Beberapa baris hitungan dan banyak game otomatis menemukannya dalam satu sore. Belum ada tanggal rilis. Kalau ada kabar, akan muncul di sini.
