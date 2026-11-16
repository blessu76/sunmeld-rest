---
title: Taşları bir oyun motoruna taşımak
description: Sunmeld'in düşen taşlarının ve diğer hareketli parçalarının neden artık bir oyun motorunda çalıştığı ve bunu nasıl kontrol ettiğimiz.
slug: stones-on-a-game-engine
lang: tr
category: devlog
keywords: Sunmeld, Flame, motor, animasyon, performans, günlük
translation_of: en
---
Sunmeld, iOS ve Android için hâlâ geliştirme aşamasında. Bu not, oyunun hareketli parçalarının nasıl çizildiği hakkında.

## Önce her hareketi listelemek

Bir şeyi değiştirmeden önce oyundaki her hareketi yazdık: düşüp çarpışan taşlar, taşlar birleşirken parlama, beliren puan, uyarı çizgisi, nişan çizgisi ve puan ile süreyi gösteren üst çubuk. Her biri için her karede ekrana ne kadar iş yüklediğini sorduk. Bazıları hafifti. Diğerleri pahalıydı; örneğin bir taşı her karede gradyan ve yumuşak parlamayla yeniden çizmek gibi.

## Bir kez çiz, çok kez hareket ettir

Seçtiğimiz motor, Flutter üzerinde çalışan bir oyun motoru olan Flame. Taşlar ve cam artık birer görsel olarak bir kez çiziliyor ve her karede yerleştiriliyor. Birleşme parlaması, üzerine renk eklenmiş hazır bir yumuşak şekil. Puan yazısı önceden hazırlanıyor. Kurallar değişmedi: düşmeyi ve birleşmeyi aynı fizik yönetiyor.

## Bilgisayarda kontrol edildi, telefonda henüz değil

Mac'te profil modunda ölçüm yaptık ve kareler kendi bütçesi içinde kaldı. Bu bir bilgisayar, sizin telefonunuz değil. Sonucu henüz tam yenileme hızında gerçek bir iPhone ya da Android'de kontrol etmedik; bu yüzden gerçek cihazlardaki akıcılık hâlâ açık.

## Neden motor

Flutter'ın kendi çizim araçları da bunu yapabilirdi. Yan yana bir karşılaştırma testi yapmadık, bu yüzden motorun daha hızlı olduğunu iddia etmiyoruz. Onu seçmemizin nedeni, hareketli parçaların artık tek bir döngüde çalışması; oyun büyüdükçe akıcılığı korumak daha kolay.

## Sırada ne var

Son adım, yüksek yenileme hızlı gerçek cihazlarda hissi kontrol etmek ve küçük ekranlara yeniden bakmak. Henüz bir çıkış tarihi yok.

## Sık sorulan sorular

### Oyun oynanışı değişti mi?

Hayır. Kurallar ve fizik korundu. Yalnızca hareketli parçaların çizimi ve zamanlaması değişti.

### Neden bir oyun motoru kullanılıyor?

Artık her hareketli parça tek bir döngüde çalışıyor; bu yüzden oyun her küçük hareket için tüm ekranı yeniden kurmak zorunda kalmıyor.

### Telefonda test edildi mi?

Şimdiye kadar bilgisayarda ölçüldü. Gerçek bir telefondaki test henüz yapılmadı.
