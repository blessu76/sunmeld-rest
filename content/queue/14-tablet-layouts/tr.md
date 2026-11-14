---
title: Tabletler için ayrı bir ekran
description: Sunmeld'in tablette neden telefon ekranının yalnızca uzatılmış hali olmadığı ve birçok ekran boyutunu nasıl kontrol ettiğimiz.
slug: tablet-layouts
lang: tr
category: devlog
keywords: Sunmeld, iPad, yerleşim, ekran boyutu, test, günlük
translation_of: en
---
Sunmeld iOS ve Android için hâlâ geliştiriliyor. Bu not, aynı oyun çok daha büyük bir ekranla buluştuğunda ne olduğuyla ilgili.

## İlk deneme: ortada bir telefon

Başlangıçta tablette oyun, telefon ekranını ortada dar bir sütunda gösteriyordu. Her şey çalışıyordu ama ekranın çoğu boştu. Tableti yan çevirince ekran, genişçe çekilmiş bir telefon ekranı oluyordu. Oyunu denemek için yeterliydi, oynamak için değil.

## Tek değil, iki yerleşim

Artık tabletleri iki ayrı yerleşimle çiziyoruz: dikey ve yatay. Dikeyde kap daha büyük; rakibin üstte, sen altta yer alıyorsun. Yatayda rakibin solda, kap ortada, sen sağdasın. Sonuç ekranı resmi bir yana, skoru ve düğmeleri öbür yana koyuyor. Telefonlar eskisi gibi kendi ekranını koruyor. Yerleşimi cihazın adına göre değil, pencerenin genişliğine göre seçiyoruz.

## Çekmece dolusu cihaz olmadan boyutları kontrol etmek

Her tableti elimize alamayız; bu yüzden yerleşim, ekranları birkaç telefon ve tablet boyutunda, dikey ve yatay çizen otomatik testlerle kontrol ediliyor. Bir şey taşarsa ya da beklemediğimiz bir yerleşim seçilirse testler başarısız oluyor. Aynı kontroller 12 dilin her biri için de çalışıyor, çünkü bir dildeki uzun bir kelime, başka bir dilde iyi görünen bir yerleşimi bozabilir. Kendi gözlerimizle bakmak için tablet simülatörlerinden birkaç gerçek ekran görüntüsü de tutuyoruz.

## Araçlarda küçük bir tuzak

Bir sürpriz ekran görüntüsü araçlarındaydı. Daha yeni bir tablet sisteminde simülatör, cihazı döndürmek yerine yatay bir uygulamayı bir pencerede açabiliyor ve yakalanan görüntü yan çıkıyordu. Artık bu çekimler için ekranı bilerek döndürülmüş çiziyor, sonra dosyayı yeniden dik çeviriyoruz.

## Henüz kontrol edilmeyenler

Gerçek bir tablette oyunun yarıda döndürüldüğünü henüz izlemedik; telefon kadar dar pencereler de telefon yerleşimine geri dönüyor, ona da henüz yakından bakmadık. Bu değiştiğinde burada söyleyeceğiz. Henüz çıkış tarihi yok.
