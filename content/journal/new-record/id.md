---
title: Tanda «rekor baru» setelah permainan latihan
description: Kapan layar hasil menampilkan rekor baru, rekor apa saja yang dihitung, dan bagaimana tanda itu muncul.
slug: new-record
lang: id
category: devlog
keywords: Sunmeld, rekor baru, hasil, rentetan menang, latihan, jurnal
translation_of: en
published: 2026-11-25T14:30+09:00
---
Sunmeld masih dalam pengembangan untuk iOS dan Android. Catatan ini membahas tanda kecil di layar hasil yang muncul ketika permainan latihan mencetak rekor baru.

## Mengapa ada tanda di layar hasil

Rekor hanya berguna jika kamu menyadarinya. Sebelum perubahan ini, skor terbaik atau rentetan menang terpanjang bisa naik tanpa tanda apa pun di layar hasil. Maka kami menambahkan satu baris di atas ringkasan yang bertuliskan «Rekor baru», diikuti rekor yang dicetak permainan ini.

## Hanya yang naik yang ditampilkan

Baris itu hanya memuat rekor yang naik dalam permainan ini: skor terbaik pada tingkat sulit dan rentetan menang terpanjang. Jika tidak ada yang naik, baris tidak muncul. Kemenangan pertama pada tingkat sulit juga dihitung sebagai rekor baru.

## Rentetan dimulai dari dua

Rentetan hanya ditampilkan jika rentetan terpanjang minimal dua. Kalau tidak, setiap kemenangan pertama akan memunculkan tanda, dan itu tidak memberi informasi apa pun.

## Hanya permainan latihan

Permainan liga, tantangan harian, dan mode rush tidak menambah rekor latihan, sehingga tanda ini juga tidak muncul di sana. Menekan «Main lagi» menghapusnya, agar tanda lama tidak terbawa ke permainan berikutnya.

## Tampilannya

Tanda membesar dari ukuran sedikit lebih kecil ke ukuran penuh. Jika gerakan dikurangi di sistem atau di aplikasi, tanda langsung muncul dalam ukuran penuh tanpa gerakan. Tanda ini memakai gaya label yang sama dengan tanda «skor terbaru» pada susun solo dan rush.

## Yang belum kami periksa

Kami belum melihat bagaimana tanda ini tampil di perangkat sungguhan, atau bagaimana pembaca layar membacanya. Di layar yang sangat kecil, mungkin perlu sedikit lebih banyak menggulir untuk mencapai tombol. Belum ada tanggal rilis.

## Pertanyaan yang sering diajukan

### Apakah tanda muncul di permainan liga?

Tidak. Permainan liga, tantangan harian, dan rush tidak menampilkannya.

### Apa yang dihitung sebagai rekor baru?

Skor terbaik yang lebih tinggi pada tingkat sulit, atau rentetan menang terbaik yang lebih panjang. Kemenangan pertama pada tingkat sulit juga dihitung.

### Mengapa rentetan perlu dua kemenangan?

Rentetan satu kemenangan berarti setiap kemenangan pertama. Mulai dari dua membuat tanda tetap bermakna.

### Apakah ada tanggal rilis?

Belum. Belum ada tanggal yang ditetapkan.
