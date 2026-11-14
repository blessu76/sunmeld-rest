---
title: Layar tersendiri untuk tablet
description: Mengapa Sunmeld di tablet bukan sekadar layar ponsel yang direntangkan, dan bagaimana kami memeriksa banyak ukuran layar.
slug: tablet-layouts
lang: id
category: devlog
keywords: Sunmeld, iPad, tata letak, ukuran layar, pengujian, jurnal
translation_of: en
---
Sunmeld masih dalam pengembangan untuk iOS dan Android. Catatan ini tentang apa yang terjadi saat game yang sama bertemu layar yang jauh lebih besar.

## Percobaan pertama: ponsel di tengah

Awalnya, di tablet game hanya menampilkan layar ponsel dalam kolom sempit di tengah. Semuanya berfungsi, tetapi sebagian besar layar kosong. Putar tablet ke samping dan hasilnya layar ponsel yang ditarik melebar. Itu cukup untuk menguji game, tetapi tidak cukup untuk memainkannya.

## Dua tata letak, bukan satu

Sekarang kami menggambar tablet dalam dua tata letak terpisah, potret dan lanskap. Dalam potret, toples menjadi lebih besar, dengan lawanmu di atas dan kamu di bawah. Dalam lanskap, lawanmu ada di kiri, toples di tengah, dan kamu di kanan. Layar hasil menaruh gambar di satu sisi dan skor serta tombol di sisi lain. Ponsel tetap memakai layarnya sendiri seperti sebelumnya. Kami memilih tata letak dari lebar jendela, bukan dari nama perangkat.

## Memeriksa ukuran tanpa selemari perangkat

Kami tidak bisa memegang setiap tablet, jadi tata letak diperiksa oleh tes otomatis yang menggambar layar pada beberapa ukuran ponsel dan tablet, potret dan lanskap, dan gagal jika ada yang meluap atau jika tata letak yang tidak kami duga terpilih. Pemeriksaan yang sama dijalankan untuk masing-masing dari 12 bahasa, karena satu kata panjang di suatu bahasa bisa merusak tata letak yang tampak baik di bahasa lain. Kami juga menyimpan beberapa tangkapan layar asli dari simulator tablet untuk dilihat dengan mata sendiri.

## Jebakan kecil pada alat

Satu kejutan ada pada alat tangkapan layar. Pada sistem tablet yang lebih baru, simulator bisa membuka aplikasi lanskap dalam sebuah jendela alih-alih memutar perangkat, sehingga gambar yang ditangkap keluar menyamping. Sekarang kami sengaja menggambar layar dalam keadaan terputar untuk tangkapan itu, lalu memutar file kembali tegak.

## Yang belum diperiksa

Kami belum melihat game diputar di tengah permainan pada tablet sungguhan, dan jendela yang sesempit ponsel kembali ke tata letak ponsel, yang juga belum kami periksa dengan saksama. Kami akan menyampaikannya di sini kalau itu berubah. Belum ada tanggal rilis.

## FAQ

### Apakah tablet mendapat tata letak sendiri?

Ya. Tablet memakai tata letak terpisah untuk potret dan lanskap, yang dipilih dari lebar jendela, bukan dari nama perangkat. Ponsel tetap memakai layarnya sendiri.

### Bagaimana banyak ukuran layar itu diperiksa?

Tes otomatis menggambar layar dalam beberapa ukuran ponsel dan tablet, potret dan lanskap, untuk setiap dari 12 bahasa.

### Apakah rotasi saat permainan sudah diuji di tablet sungguhan?

Belum. Kami belum melihat permainan diputar di tengah jalan pada tablet sungguhan.

### Apakah ada tanggal rilis?

Belum. Belum ada tanggal rilis.
