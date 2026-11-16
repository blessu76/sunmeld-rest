---
title: Hiçbir şey yapmayan ses anahtarı
description: Sunmeld'in ses ayarının bir süre sessiz kalmasının nedeni ve birleşmenin duyulabilmesi için neler eklediğimiz.
slug: sound-that-was-silent
lang: tr
category: devlog
keywords: Sunmeld, ses, ses efektleri, ayarlar, sessiz mod, günlük
translation_of: en
---
Sunmeld, iOS ve Android için hâlâ geliştirme aşamasında. Bu not, var olan ama hiçbir şey yapamayan bir ayar hakkında.

## Anahtar oradaydı, ses yoktu

Ayarlar ekranında bir ses anahtarı vardı ve seçtiğiniz değeri doğru kaydediyordu. Oyun, bir taş her indiğinde ya da birleştiğinde bu değere bakıyordu. Ama sesi çalması gereken kısım boş bir yer tutucuydu. Ses dosyaları ve lisansları henüz belirlenmediği için bunu bilerek öyle bırakmıştık. Anahtarın kendisi hiç bozuk değildi. Eksik olan sesti.

## Sesleri kendimiz ürettik

Lisans beklemek yerine sesleri kendimiz ürettik. Bir taşın yere çarpması, birleşmesi, zincirleme birleşmeler ve taşma uyarısı gibi durumlar için on altı kısa efekt var. Rastgele sayı kullanmayan küçük bir betikle üretiliyorlar; bu yüzden betiği iki kez çalıştırmak aynı dosyaları verir. Hepsi birlikte yaklaşık 220 KB.

## Telefonunuz sessizse oyun da sessiz

Oyun, iPhone'da sessiz anahtarına uyacak ve zaten çalan başka bir uygulamanın müziğini kesmeyecek şekilde ayarlandı. Android'de oyun sesi olarak çalar ve ses odağını almaz. Bir ses çalınamazsa tur normal şekilde devam eder.

## Henüz duymadıklarımız

Sesler bağlandı ve uygulama bu seslerle derlenebiliyor. Ancak onları henüz gerçek bir iPhone'da, gerçek bir odada, normal ses düzeyinde dinlemedik. Ton ve ses seviyesi bir kez daha ayarlanmaya ihtiyaç duyabilir. O zaman aynı adı taşıyan bir ses dosyası değiştirilebilir.

## Sık sorulan sorular

### Daha önce neden ses yoktu?

Ses çıkışı sessiz bir yer tutucuydu. Ses dosyaları ve uygulamanın ses bölümü yakın zamanda eklendi.

### Oyun iPhone'da sessiz anahtarına uyuyor mu?

Öyle ayarlandı. Henüz gerçek bir cihazda kontrol etmedik; bunu yaptığımızda daha fazla bilgi vereceğiz.

### Sesi kapatabilir miyim?

Evet. Ayarlardaki ses anahtarı efektleri kontrol eder. Kapalıyken oyun hiçbir şey çalmaz.
