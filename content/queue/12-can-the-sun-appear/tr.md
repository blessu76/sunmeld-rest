---
title: Güneş hiç ortaya çıkabilir mi?
description: Yapay zekâ oyuncuların Sunmeld'i defalarca oynamasına izin verince ne oldu: en büyük taş neredeyse hiç görünmedi ve çözüm yapay zekâda değil, kurallardaydı.
slug: can-the-sun-appear
lang: tr
category: devlog
keywords: Sunmeld, denge, yapay zekâ, test, oyun tasarımı, günlük
translation_of: en
---
Sunmeld iOS ve Android için hâlâ geliştiriliyor. Bu not, yalnızca oyun hakkındaki kendi hissimize güvenmediğimiz için fark ettiğimiz bir sorunla ilgili.

## Yapay zekâların sonuna kadar oynamasına izin vermek

Başlangıçta kurallar hızlıca hazırlanmış bir prototipti. Kimseden denemesini istemeden önce, yapay zekâ oyuncuların birbirine karşı çok sayıda oyun oynamasını sağladık. Sonucun tekrarlanabilmesi için her seferinde aynı başlangıç koşullarını kullandık. Bir oyunun kaç kez taşmayla bittiğini, ilk oynayanın kaç kez kazandığını ve en yüksek taşı, yani güneşi, kimin kaç kez yapabildiğini takip ettik.

## Güneş hiç gelmedi

Prototip kurallarında kimse güneş yapamadı. Ne kolay yapay zekâ, ne de en zor olanı. İlk bakışta bu bir yapay zekâ sorunu gibi göründü, biz de yapay zekâya baktık. Sonra bunun yerine hesap yaptık.

Her birleşme iki taşı bir sonraki aşamadaki tek bir taşa dönüştürür, yani güneş çok fazla "taş hacmi" taşır. Kaba düşen taşlar ise küçük olanlar. Bir oyunun izin verdiği bırakma sayısı boyunca kaba girebilecek toplam hacim, tek bir güneşin gerektirdiğinin çok altındaydı. Kuralların yeterli malzeme vermediği bir şeyi hiçbir beceri inşa edemez. Bu bir kural sorunuydu, yapay zekâ sorunu değil.

## Ne değiştirdik

Aşama basamaklarını ve kabın boyutunu yeniden şekillendirdik, her oyuncuya da yeni basamaklara uygun bir bırakma bütçesi verdik. Bundan sonra aynı yapay zekâ oyunları güneş üretti, güçlü yapay zekâlarda daha sık, ve daha az oyun taşmayla bitti. Güneş nadir ama mümkün hale geldi; son aşamadan istediğimiz de buydu.

## İkinci bir sürpriz: nişan alma saati

Test çalışmaları, gerçek zamanlı oynanan bir oyunun taşmayla, aynı oyunun anında oynanmasına göre daha sık bittiğini de gösterdi. Bu yapay zekâdaki bir hata değildi. Bir oyuncu hâlâ nişan alırken taşma saati işlemeye devam ediyordu; bu yüzden kalabalık bir kaba yeni taş bırakan kişi, karşı taraf düşünürken kaybedebiliyordu. Artık tehlike saati, oyuncu nişan alırken bekliyor.

## Bunu neden anlatıyoruz

Elle oyun testi yapsaydık güneşin erişilmez olduğunu fark etmemiz çok uzun sürerdi. Birkaç satır hesap ve çok sayıda otomatik oyun bunu bir öğleden sonrada buldu. Henüz çıkış tarihi yok. Haber olduğunda burada görünecek.
