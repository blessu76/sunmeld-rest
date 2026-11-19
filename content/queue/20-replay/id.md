---
title: Menonton ulang permainan yang selesai, satu langkah demi satu
description: Bagaimana ulangan permainan Sunmeld yang telah selesai bekerja dan bagaimana kami memastikan hasilnya diputar sama persis.
slug: replay
lang: id
category: devlog
keywords: Sunmeld, ulangan, tonton ulang, permainan, jurnal
translation_of: en
---
Sunmeld masih dalam pengembangan untuk iOS dan Android. Catatan ini membahas fitur yang memungkinkan kamu menonton ulang permainan yang sudah selesai, satu langkah demi satu.

## Mengapa ingin menonton ulang

Setelah permainan selesai, orang bertanya-tanya mengapa kalah. Kamu tahu batu terakhir meluap, tetapi sulit mengingat di mana semuanya mulai miring. Karena itu kami menambahkan "Tonton ulang" di layar hasil.

## Kami mencatat langkah, bukan video

Permainan tidak direkam sebagai video. Kami hanya mencatat apa yang dibutuhkan untuk membangunnya kembali: nilai acak saat permainan dimulai, siapa yang main lebih dulu, dan untuk setiap batu yang dijatuhkan: pada langkah ke berapa, di mana ditempatkan, dan jenis batunya. Batu yang jatuh sendiri saat waktu habis dicatat dengan cara yang sama.

## Dimasukkan kembali pada langkah yang sama

Saat kamu menekan "Tonton ulang", langkah yang tersimpan dimasukkan kembali ke mesin permainan pada langkah yang sama. Masukan yang sama menghasilkan hasil yang sama. Bukan hanya skor, posisi dan tahap setiap batu juga harus sama, dan pengujian otomatis mengunci hal itu. Pengujiannya mencakup batu yang jatuh karena waktu habis, batu khusus, permainan yang dimulai lawan, dan catatan tersimpan yang dibaca kembali.

## Cara menontonnya

Ada putar dan jeda, ulang dari awal, dan langkah berikutnya, serta kecepatan bisa diganti antara lebih lambat dan lebih cepat. Jika kurangi gerakan aktif di sistem atau di aplikasi, ulangan dimulai dalam keadaan berhenti dan tanpa efek cahaya. Lalu kamu bisa maju satu langkah demi satu dengan "Langkah berikutnya".

## Batasan untuk saat ini

Hanya permainan melawan AI yang bisa diulang. Menumpuk sendiri dan permainan latihan tidak termasuk. Hanya permainan terakhir yang bisa ditonton, dan satu-satunya jalan masuk adalah layar hasil. Gerakan membidik AI tidak digambar ulang; batu langsung menuju tempat jatuhnya. Hasil jatuhnya sama.

## Yang belum kami periksa

Kami belum memeriksa rasanya di perangkat sungguhan atau bunyinya dengan pembaca layar. Kami juga belum tahu seberapa besar catatan untuk permainan yang sangat panjang. Jika ada perubahan, kami akan mencatatnya di sini. Belum ada tanggal rilis.

## Pertanyaan umum

### Bisakah saya menonton ulang permainan sebelumnya?

Kamu bisa menonton ulang permainan terakhir yang selesai melawan AI dari layar hasil.

### Apakah ulangan bisa berbeda hasilnya?

Tidak. Langkah yang tersimpan dimasukkan kembali pada langkah yang sama, dan pengujian memeriksa bahwa skor serta posisi setiap batu sama.

### Bisakah menumpuk sendiri juga diulang?

Belum. Untuk saat ini hanya permainan melawan AI yang didukung.

### Apakah sudah ada tanggal rilis?

Belum. Tanggal rilis belum ditetapkan.
