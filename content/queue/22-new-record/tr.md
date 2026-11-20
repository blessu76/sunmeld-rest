---
title: Alıştırma maçından sonra çıkan "yeni rekor" işareti
description: Sonuç ekranında yeni rekorun ne zaman görüneceğini, hangi rekorların sayıldığını ve işaretin nasıl belirdiğini anlatıyoruz.
slug: new-record
lang: tr
category: devlog
keywords: Sunmeld, yeni rekor, sonuç, seri, alıştırma, günlük
translation_of: en
---
Sunmeld hâlâ iOS ve Android için geliştiriliyor. Bu not, bir alıştırma maçı yeni bir rekor kırdığında sonuç ekranında çıkan küçük bir işaretle ilgili.

## Sonuçta neden bir işaret var

Bir rekorun faydası, onu fark etmenle olur. Bu değişiklikten önce en yüksek puan ya da en uzun galibiyet serisi artsa bile sonuç ekranında bunun hiçbir belirtisi yoktu. Bu yüzden özetin üstüne "Yeni rekor" yazan bir satır ekledik ve ardından bu maçta kırılan rekorları gösteriyoruz.

## Yalnızca artanlar gösterilir

Satır, yalnızca bu maçta artan rekorları listeler: zor ayarda en yüksek puan ve en uzun galibiyet serisi. Hiçbir şey artmadıysa satır çıkmaz. Zor ayarda ilk galibiyet de yeni rekor sayılır.

## Seriler ikiden başlar

Seri, yalnızca en uzun seri en az iki olduğunda gösterilir. Aksi halde her ilk galibiyette işaret çıkardı ve bir şey anlatmazdı.

## Yalnızca alıştırma maçları

Lig, günlük meydan okuma ve rush maçları alıştırma rekoruna eklenmez, dolayısıyla işaret de onlarda çıkmaz. "Tekrar oyna" düğmesine basmak işareti temizler, böylece eski bir işaret bir sonraki maça taşınmaz.

## Nasıl belirir

İşaret, biraz küçük bir boyuttan tam boyuta büyür. Sistemde ya da uygulamada hareketi azalt ayarı açıksa, işaret hareket etmeden doğrudan tam boyutta görünür. Tekli yığınlama ve rush'taki "yeni en iyi" işaretiyle aynı etiket stilini kullanır.

## Henüz kontrol etmediklerimiz

İşaretin gerçek bir cihazda nasıl göründüğünü ve ekran okuyucunun onu nasıl okuduğunu henüz görmedik. Çok küçük bir ekranda düğmelere ulaşmak için biraz daha kaydırmak gerekebilir. Henüz bir çıkış tarihi yok.

## Sık sorulan sorular

### İşaret lig maçlarında çıkar mı?

Hayır. Lig, günlük meydan okuma ve rush maçlarında gösterilmez.

### Neler yeni rekor sayılır?

Zor ayarda daha yüksek bir en iyi puan ya da daha uzun bir en iyi galibiyet serisi. Zor ayarda ilk galibiyet de sayılır.

### Seri neden iki galibiyet gerektirir?

Tek galibiyetlik bir seri, her ilk galibiyet olurdu. İkiden başlamak işaretin anlamını korur.

### Bir çıkış tarihi var mı?

Henüz yok. Bir tarih belirlenmedi.
