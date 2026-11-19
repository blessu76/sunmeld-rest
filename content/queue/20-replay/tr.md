---
title: Biten bir oyunu yeniden izlemek, hamle hamle
description: Sunmeld'de biten bir oyunun tekrarının nasıl çalıştığı ve aynı şekilde oynadığını nasıl denetlediğimiz.
slug: replay
lang: tr
category: devlog
keywords: Sunmeld, tekrar, yeniden izle, oyun, günlük
translation_of: en
---
Sunmeld, iOS ve Android için hâlâ geliştirme aşamasında. Bu not, biten bir oyunu hamle hamle yeniden izlemenizi sağlayan bir özellik hakkında.

## Neden yeniden izlemek

Oyun bitince insan neden kaybettiğini merak ediyor. Son taşın taştığını biliyorsun ama işlerin nerede ters gitmeye başladığını hatırlamak daha zor. Bu yüzden sonuç ekranına "Yeniden izle" ekledik.

## Video değil, hamleleri kaydediyoruz

Oyun video olarak kaydedilmez. Yalnızca onu yeniden kurmak için gerekeni kaydediyoruz: oyunun başladığı rastgele değer, kimin önce oynadığı ve bırakılan her taş için hangi adımda düştüğü, nereye konduğu ve ne tür bir taş olduğu. Süre dolunca kendiliğinden düşen taş da aynı şekilde kaydedilir.

## Aynı adımda geri verilir

"Yeniden izle"ye bastığında, kaydedilen hamleler oyun motoruna aynı adımlarda geri verilir. Aynı girdi aynı sonucu verir. Yalnızca puan değil, her taşın konumu ve aşaması da aynı olmalı ve bunu otomatik bir test sabitler. Testler, süre aşımıyla düşen taşları, özel taşları, rakibin başladığı bir oyunu ve kaydedilmiş bir kaydın geri okunmasını içerir.

## Nasıl izlenir

Oynat ve duraklat, baştan başla ve sonraki hamle var; hız daha yavaş ile daha hızlı arasında değiştirilebilir. Sistemde veya uygulamada hareketi azalt açıksa tekrar duraklatılmış olarak ve parlama efektleri olmadan başlar. O zaman "Sonraki hamle" ile hamle hamle ilerleyebilirsin.

## Şimdilik sınırlar

Yalnızca yapay zekâ rakiplere karşı oynanan oyunlar tekrar izlenebilir. Tek başına istifleme ve alıştırma oyunları dahil değil. Yalnızca en son oyun izlenebilir ve tek giriş yolu sonuç ekranıdır. Yapay zekânın nişan alma hareketi yeniden çizilmez; taş doğrudan düştüğü yere gider. Düşüşün sonucu aynıdır.

## Henüz denetlemediğimiz şeyler

Gerçek bir cihazda nasıl hissettirdiğini ya da ekran okuyucuyla nasıl duyulduğunu henüz denetlemedik. Çok uzun bir oyunda kaydın ne kadar büyüdüğünü de henüz bilmiyoruz. Bu değişirse buraya yazarız. Henüz çıkış tarihi yok.

## Sık sorulan sorular

### Önceki bir oyunu yeniden izleyebilir miyim?

Sonuç ekranından, yapay zekâ rakibe karşı en son biten oyunu yeniden izleyebilirsin.

### Tekrar farklı sonuçlanabilir mi?

Hayır. Kaydedilen hamleler aynı adımlarda geri verilir ve testler puanın ve her taşın konumunun aynı olduğunu denetler.

### Tek başına istiflemeyi de tekrar izleyebilir miyim?

Henüz değil. Şimdilik yalnızca yapay zekâ rakiplere karşı oyunlar destekleniyor.

### Çıkış tarihi var mı?

Henüz yok. Çıkış tarihi belirlenmedi.
