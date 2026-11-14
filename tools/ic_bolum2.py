# -*- coding: utf-8 -*-
"""Oturum 5–8: Riskler (uyku ve dikkat, beden, oyun, çevrimiçi zarar)."""
from ic_ortak import S

OTURUMLAR_2 = [
    # ------------------------------------------------------------------ 5
    dict(
        no=5, kesim="r", kisa="Uyku ve dikkat",
        baslik="Uyku ve dikkat: en tutarlı bulgu ile en çok abartılan bulgu",
        slogan="Uykuda kanıt tutarlı, çözüm basit. Dikkatte ilişki var, yönü hâlâ tartışmalı.",
        bakis=("Dijital medyanın sağlıkla ilişkisinde en tutarlı bulgu uykuyla ilgilidir ve en ucuz müdahale de buradadır. ‘Dikkati "
               "bozuyor’ iddiası ise kamuoyunda çok daha kesin konuşulur, oysa kanıtı daha zayıftır. Bu oturum ikisini yan yana koyuyor."),
        sorun=[
            "Hastanızın telefonu gece nerede duruyor? Bunu en son ne zaman sordunuz?",
            "‘Dikkati dağıldı’ diyen ailede DEHB’yi, uykusuzluğu ve alışkanlığı birbirinden nasıl ayırıyorsunuz?",
            "Kısa videoların dikkati bozduğuna inanıyor musunuz? Sizi hangi tür kanıt ikna eder?",
        ],
        fikirler=[
            ("Yatakta cihaz: en tutarlı ilişki",
             "20 çalışmayı ve 125.198 çocuğu kapsayan meta-analizde yatmadan önce taşınabilir cihaz kullanımı yetersiz uyku süresi "
             "(OR 2,17), kötü uyku kalitesi (OR 1,46) ve gündüz aşırı uykululuk (OR 2,72) ile ilişkiliydi [@carter2016]."),
            ("Kullanılmasa bile odada olması yetiyor",
             "Aynı meta-analizde gece cihaza erişimi olan ama kullanmadığını bildiren çocuklarda da yetersiz uyku (OR 1,79) ve gündüz "
             "uykululuk (OR 2,27) daha sıktı [@carter2016]."),
            ("Etki günlük ölçekte küçük, ama birikiyor",
             "21 kohortu (548.338 kişi) birleştiren meta-analizde günde her ek saat ekran, toplam uykuyu yaklaşık 3–5 dakika kısaltıyordu; "
             "kısa uyku olasılığı artmıştı (OR 1,25) [@he2025]. Aynı çocuğun günlerini karşılaştıran çalışmaların meta-analizinde "
             "(25 çalışma, 4562 genç) ekranın arttığı günlerde yalnızca uykuya geçiş saati biraz gecikiyordu (r=0,08); toplam uyku "
             "süresi ve verimliliği değişmiyordu. Yatağa girdikten sonraki kullanım ise öznel uyku kalitesiyle daha güçlü ilişkiliydi "
             "[@bourke2026]."),
            ("Ok iki yöne de gidiyor",
             "Uykusu bir hafta boyunca birer saat kısaltılan çocuklar, giyilebilir kamerayla ölçüldüğünde okul sonrası saatlerde ekran "
             "süresi artmış göründü; ebeveynler de daha uzun kullanım bildirdi (çapraz tasarımlı randomize çalışma, 49 çocuk) "
             "[@jackson2025]. Ekran uykuyu, uykusuzluk ekranı besliyor."),
            ("Uzman uzlaşısı içerik ve davranışı işaret ediyor",
             "Ulusal Uyku Vakfı’nın paneli üç önermede uzlaştı: ekran kullanımı çocuk ve ergenlerde uyku sağlığını bozar; uyku öncesi "
             "izlenen içeriğin niteliği önemlidir; davranışsal stratejiler olumsuz etkiyi azaltabilir. On önermenin yalnızca beşinde "
             "uzlaşı sağlanabildi [@hartstein2024]."),
            ("Dikkat: ilişki var, küçük ve belirli bir kullanım biçimine özgü",
             "2587 ergenin iki yıl izlendiği çalışmada başlangıçta sık yapılan her ek dijital etkinlik, sonradan DEHB belirtisi görülme "
             "olasılığını biraz artırdı (OR 1,11); hiçbir etkinliği sık yapmayanlarda belirti oranı %4,6, yedi etkinliği sık yapanlarda "
             "%9,5 idi [@ra2018]. ABCD kohortunda sosyal medya süresi dikkatsizlik belirtilerinde yıllar içinde küçük bir artışla "
             "ilişkiliydi (dört yılda toplam β=0,15); oyun ve video izleme ilişkili değildi, genetik yatkınlık sonucu değiştirmedi ve "
             "dikkatsizlik sonraki sosyal medya kullanımını öngörmedi [@nivins2026]. Sorunlu sosyal medya kullanımı da izleyen yıl "
             "DEHB belirtilerinde hafif artışla birlikteydi (β=0,08) [@nagata2026]."),
            ("Yaş önemli: okul öncesinde ilişki daha güçlü",
             "Aşırı ekran süresi ile DEHB arasındaki ilişkiyi birleştiren meta-analizde genel OR 1,56 idi; okul öncesinde 2,40, okul "
             "çağı ve sonrasında 1,16. Çalışmalar arası heterojenlik çok yüksekti [@zhao2026]."),
            ("DEHB’li çocuk da daha çok ekran kullanıyor",
             "22 çalışmanın meta-analizine göre DEHB’li çocuk ve ergenlerin hafta içi iki saatin üzerinde ekran kullanma olasılığı "
             "daha yüksek; kanıtın kesinliği düşük ya da çok düşük [@goncalves2026]. İlişkinin bir bölümü buradan geliyor olabilir."),
            ("Erişkinlerde bir deney: bağlantıyı kesmek dikkati düzeltiyor",
             "Telefonlarında mobil interneti iki hafta kapatan erişkinlerde sürdürülen dikkat nesnel testle iyileşti; katılımcıların "
             "%91’i dikkat, ruh sağlığı ya da iyi oluş ölçütlerinden en az birinde düzeldi [@castelo2025]. Ergenlerde benzer bir deney "
             "henüz yok."),
        ],
        klinik=[
            "Her ergene üç soru: Telefon gece nerede duruyor? Yatağa girdikten sonra ne kadar bakıyorsun? Gece bildirim gelince uyanıyor musun?",
            "Tek bir kural önerecekseniz bu olsun: şarj yeri yatak odasının dışında. Kullanılmasa bile odada cihaz bulunması yetersiz uykuyla ilişkili [@carter2016]. Çalar saat gerekçesine karşı aileye ucuz bir masa saati önerin.",
            "Uykusuzluk yakınmasında önce gece kullanımını düşünün; duygudurum ya da uyku bozukluğu tanısından önce bir-iki haftalık uyku ve ekran günlüğü isteyin.",
            "Döngüyü iki ucundan kırın: uykusuz çocuk ertesi gün ekrana daha çok yönelir [@jackson2025]. Yalnızca ekranı kısıtlamak yerine yatış ve kalkış saatini de sabitleyin.",
            "Dikkat yakınmasında sırayı koruyun: önce uyku, sonra duygudurum ve kaygı, sonra DEHB. Ekran yüzünden uykusuz kalmak DEHB’yi taklit eder; ekran başında saatlerce kalabilmek de DEHB’yi dışlamaz.",
            "DEHB tanılı ergende sosyal medya ve oyunun işlevini sorun. Bu grup hem daha çok kullanıyor hem de sorunlu kullanıma daha yatkın [@goncalves2026] [@ho2014].",
            "TR TÜİK araştırmasında çocukların %17,2’si ekran yüzünden daha az uyuduğunu kendisi bildiriyor [@tuik2024]. Soruyu doğrudan çocuğa sormak, ebeveynden farklı bir yanıt getirebilir.",
            "TR Yönetmelik, 15–17 yaş hesapları için platformları ebeveynin kullanım süresini izleyip sınırlayabileceği araçlar sunmakla yükümlü kılıyor [@yonetmelik2026]. Gece saatleri için bu araçlar kullanılabilir; yine de en basit çözüm cihazın odadan çıkmasıdır.",
        ],
        kitaplar=[
            ("williams", "Ayırıcı tanı örneklerinde yazarlar, haftalardır çok az uyuyan bir ergende ilk akla gelmesi gereken "
                         "açıklamalardan birinin gece sosyal medya kullanımı olduğunu belirtir [@williams2025]. Nadir tanılara geçmeden "
                         "önce sık olanı sormak gerekir."),
            ("iacapap", "DEHB bölümü, yapılandırılmış ve çekici görevlerde belirtilerin gizlenebildiğini, sıkıcı ve uzun görevlerde "
                        "ortaya çıktığını anlatır [@iacapap2]. Ekran, belirtinin en az görüldüğü ortamdır; tanı için en zayıf gözlem yeridir."),
            ("lewis", "DEHB bölümünün tedavi tablosunda oyun temelli bir dijital tedavi, kanıt düzeyi belirtilen seçenekler arasında "
                      "yer alır [@lewis6]. Aynı ekran dikkat için hem yakınma konusu hem tedavi aracı olabiliyor; ayrıntı Oturum 13’te."),
        ],
        tartisma=[
            ("Işık mı, içerik mi, yer değiştirme mi?",
             "Uzlaşı paneli içeriğe ve davranışa işaret etti; oylanan on önermenin beşinde görüş birliği sağlanamadı "
             "[@hartstein2024]. Kişi-içi veride etki uyku süresinde değil, uykuya geçiş saatinde görülüyor [@bourke2026]; bu, ekranın "
             "uykunun yerini aldığı açıklamasıyla uyumlu. Mekanizma tartışması sürerken pratik öneri değişmiyor."),
            ("Kısa video dikkati bozuyor mu?",
             "Kesitsel ilişki orta büyüklükte (r=−0,38) [@nguyen2025]. Boylamsal bulgular çok daha küçük, ama yön sosyal medyadan "
             "dikkate doğru ve oyunla televizyonda aynı ilişki yok [@nivins2026] [@nagata2026]. Bu, ‘ekran’ın değil, belirli bir "
             "kullanım biçiminin sorun olabileceğini düşündürüyor. Ergenlerde nedenselliği sınayan bir deney henüz yapılmadı; "
             "‘kalıcı dikkat hasarı’ iddiasını destekleyen veri yok."),
            ("Okul öncesi ayrı bir konu mu?",
             "İlişki en güçlü okul öncesinde [@zhao2026]. İki yaşındaki daha uzun ekran süresi üç yaşındaki gelişim taramasında daha "
             "düşük puanları öngördü [@madigan2019]; süre arttıkça dil becerileri azalırken birlikte izleme ve eğitsel içerik daha iyi "
             "dil becerisiyle ilişkiliydi [@madigan2020]. Ebeveynin çocuğun yanında kendi cihazını kullanması da küçük çocuklarda "
             "biliş ve davranışla ilişkili bulundu [@toledo2025]. Bu rehberin odağı ergenlik; ancak ergen hastanın küçük kardeşleri "
             "için aileyle ayrı bir konuşma yapılabilir."),
        ],
        sorular=[
            S("On beş yaşındaki Selin iki aydır derslerde uyukluyor, dikkati dağınık, sabahları kalkamıyor. Annesi ‘DEHB olabilir mi?’ diye soruyor. Telefonun yastığın altında durduğu ve Selin’in gece bildirimlerle uyandığı öğreniliyor. İlk adım hangisidir?",
              ["Uyarıcı ilaç başlamak",
               "Telefonu iki hafta yatak odasının dışında şarj etmek, uyku günlüğü tutmak ve dikkat yakınmasını sonra yeniden değerlendirmek",
               "Doğrudan uyku laboratuvarına yönlendirmek",
               "DEHB ölçeği verip puana göre tanı koymak"], 1,
              "Belirtiler iki aydır var ve uyku bozulmasıyla aynı zamanda başlamış; DEHB belirtileri ise çocukluktan beri sürer. Yatakta cihaz kullanımı yetersiz uyku ve gündüz uykululukla tutarlı biçimde ilişkilidir [@carter2016]. Önce düzeltilebilir olanı düzeltin."),
            S("Bir baba ‘Telefonu odasında duruyor ama gece kullanmıyor, kontrol ettim’ diyor. Meta-analiz verisi ne söyler?",
              ["Kullanılmıyorsa uykuyu etkilemez",
               "Kullanılmasa bile yatak odasında cihaz bulunması yetersiz uyku ve gündüz uykululukla ilişkilidir; şarj yerini odanın dışına almak yine önerilir",
               "Ekran filtresi kullanmak yeterlidir",
               "Bu ilişki yalnızca kızlarda geçerlidir"], 1,
              "Erişimi olup kullanmadığını bildirenlerde de yetersiz uyku daha sık (OR 1,79) [@carter2016]. Olası açıklamalar bildirimle uyanma, kullanımın eksik bildirilmesi ve beklenti; hangisi olursa olsun çözüm aynıdır."),
            S("Bir öğretmen eğitiminde ‘Kısa videolar çocukların dikkat süresini kalıcı olarak kısaltıyor; meta-analiz kanıtladı’ deniyor. En doğru düzeltme hangisidir?",
              ["İfade doğrudur; korelasyon nedenselliği gösterir",
               "Meta-analiz orta düzeyde bir ilişki buldu; çalışmaların çoğu kesitsel olduğundan dikkati zayıf olanların kısa videoya yönelmesi de aynı sonucu verir; kalıcılık gösterilmedi",
               "Hiçbir ilişki bulunmadı",
               "İlişki yalnızca erişkinlerde gösterildi"], 1,
              "İlişki gerçek, yorum aşırı [@nguyen2025]. Boylamsal çalışmalar sosyal medyadan dikkate doğru küçük bir etki düşündürüyor [@nivins2026], ancak ‘kalıcı kısalma’ ölçülmüş bir sonuç değil."),
        ],
        akilda="Tek bir öneri verecekseniz: telefon gece yatak odasının dışında şarj olsun. Kanıtı en tutarlı, maliyeti en düşük öneri budur.",
    ),
    # ------------------------------------------------------------------ 6
    dict(
        no=6, kesim="r", kisa="Beden ve karşılaştırma",
        baslik="Beden ve karşılaştırma: süre değil, içerik ve kıyas",
        slogan="Bedeni etkileyen ekranda geçen saat değil; neye bakıldığı ve kiminle kıyaslandığı.",
        bakis=("Beden imajı ve yeme bozuklukları, sosyal medya tartışmasında nedenselliğe ilişkin deneysel kanıtın en çok biriktiği "
               "alandır. Bulgular aynı yeri gösteriyor: belirleyici olan kullanım süresi değil, görünüş odaklı içerik ve kendini "
               "başkalarıyla karşılaştırma eğilimi."),
        sorun=[
            "Hastanızın akışında ne var? Hiç birlikte baktınız mı?",
            "Yeme bozukluğu olan bir ergene ‘sosyal medyayı bırak’ demek mi daha gerçekçi, akışını değiştirmek mi?",
            "Erkek ergenlerde görünüş kaygısını (kas, boy, cilt) ne sıklıkta soruyorsunuz?",
        ],
        fikirler=[
            ("Asıl değişken karşılaştırma",
             "83 çalışmayı (55.440 kişi) birleştiren meta-analizde çevrimiçi sosyal karşılaştırma eğilimi beden imajı kaygısıyla r=0,45, "
             "yeme bozukluğu belirtileriyle r=0,36 ilişkiliydi [@bonfanti2024]. Bu, alanın genelindeki süre-depresyon ilişkisinden "
             "(r≈0,1) birkaç kat büyük."),
            ("Süre tek başına zayıf bir gösterge",
             "Kısa video kullanımını inceleyen meta-analizde kullanım miktarı beden imajı ve benlik saygısıyla ilişkili bulunmadı; "
             "yazarlar bunu platformlardaki içerik çeşitliliğine bağladı [@nguyen2025]."),
            ("İçeriğin etkisi deneyle gösterildi",
             "20 deneyi (3603 genç kadın) birleştiren meta-analizde ideal beden içeriğine bakmak beden memnuniyetini düşürdü (d=−0,29). "
             "Etki video temelli platformlarda daha büyüktü (TikTok d=−0,45; Instagram görselleri d=−0,25). Bedeni olumlayan içerik ise "
             "memnuniyeti biraz artırdı (d=0,20) [@zhang2025b]."),
            ("Kısa ara, kısa vadede işe yarıyor",
             "Bir hafta ara veren genç kadınlarda beden memnuniyeti ve benlik saygısı kontrol grubuna göre daha yüksekti (66 katılımcı) "
             "[@smith2024]. Duygusal sıkıntısı olan 17–25 yaş gençlerde kullanımı üç hafta boyunca günde bir saatle sınırlamak görünüş "
             "ve kiloyla ilgili benlik saygısını iyileştirdi (220 katılımcı) [@thai2024]. Üniversite öğrencilerinde bir haftalık ara, "
             "yeme bozukluğu belirtilerinde azalmayla sonuçlandı; ancak katılımcıların yaklaşık dörtte biri çalışmayı bıraktığı ya da "
             "kurala uymadığı için analiz dışı kaldı [@dondzilo2023]."),
            ("Akışı temizlemek bırakmaktan daha gerçekçi olabilir",
             "17–35 yaş 175 kadının rastgele atandığı çalışmada üç strateji denendi: tümüyle ara vermek, günde 30 dakikayla sınırlamak "
             "ve görünüş odaklı hesapları akıştan çıkarmak. Üçünde de görünüş memnuniyeti bir haftada arttı; akış temizliği en umut "
             "verici seçenek olarak öne çıktı [@seekis2025]."),
            ("Zincirin halkaları",
             "On dört yaşındaki 10.904 ergende yoğun sosyal medya kullanımı; çevrimiçi taciz, kötü uyku, düşük benlik saygısı ve kötü "
             "beden imajıyla, bunlar da depresif belirtilerle ilişkiliydi. Günde beş saat ve üzeri kullananlarda kilosundan memnun "
             "olmama olasılığı %31 daha yüksekti [@kelly2018]."),
            ("Akışta ticari bir katman da var",
             "ABD’de 8–17 yaş 1011 gencin ekran kayıtlarında yılda ortanca 3883 yiyecek-içecek pazarlaması görüldü (ergenlerde "
             "10.107). Gösterimlerin %82,6’sı sosyal medyadaydı ve restoran dışı ürünlerin %91,6’sı beslenme ölçütlerini karşılamıyordu "
             "[@powell2026]."),
            ("Erkekler veri setlerinde eksik",
             "2026’da iki sözlüğün yılın sözcüğü seçimleri görünüş yarışına ilişkindi: *maxxing* ve *mogging* [@dictionary2026] "
             "[@collins2026]. Deneysel çalışmalar ise neredeyse yalnızca genç kadınlarla yapıldı [@zhang2025b]. Erkek ergenlerde "
             "görünüş baskısının etkisi konusunda elimizdeki veri, kültürdeki görünürlüğünün gerisinde."),
        ],
        klinik=[
            "Akışa birlikte bakın. ‘Bana keşfet sayfanı gösterir misin?’ sorusu süre sorusundan daha çok şey söyler; görünüş, diyet ve egzersiz içeriğinin payına bakın.",
            "Karşılaştırmayı doğrudan sorun: ‘Baktıktan sonra kendini nasıl hissediyorsun? Kendini en çok kimlerle kıyaslıyorsun?’",
            "Yeme bozukluğu tedavisinde sosyal medyayı plana yazın: tetikleyici hesapları takipten çıkarmak, ‘ilgilenmiyorum’ işaretlemek ve arama geçmişini temizlemek somut ev ödevleridir [@seekis2025].",
            "Tümüyle bırakmayı kısa süreli bir deneme olarak önerin. Çalışmalar bir ile üç hafta sürdü ve çoğu genç erişkin kadınlarla yapıldı [@smith2024] [@thai2024]; uzun vadeli etkiyi bilmiyoruz.",
            "Erkek ergenlerde kas, boy ve cilt kaygısını; takviye, ‘kür’ ve ilaç kullanımını sorun. Görünüş baskısı kızlara özgü değildir.",
            "Bedeni olumlayan içerik yararlı olabilir, ama o da görünüşü merkezde tutar. Hedef, akışta görünüş dışı ilgi alanlarının payını artırmaktır [@zhang2025b].",
            "TR Türkiye’de çocukların en çok kullandığı platform YouTube; ardından Instagram ve TikTok geliyor [@tuik2024]. Görünüş içeriğine maruz kalmayı sorarken üçünü de sorun.",
            "TR 15–17 yaş hesaplarında davranışa göre kişiselleştirme ve kişiselleştirilmiş ticari reklam 1 Kasım 2026’dan beri yasak [@yonetmelik2026]. Uygulamanın akışları gerçekte nasıl değiştirdiği henüz bilinmiyor; hastanızın akışına bakmak bunu da gösterir.",
        ],
        kitaplar=[
            ("lewis", "Yeme bozuklukları bölümü sosyal medyayı risk bağlamının parçası olarak ele alır ve platformların içerik "
                      "önerilerine ilişkin sivil toplum raporlarına yer verir [@lewis6]."),
            ("rutter", "Yedinci baskıya beden dismorfik bozukluğu için ayrı bir bölüm eklenmiştir [@rutter7]. Görünüş kaygısının klinik "
                       "ucunu ayrıca tanımak gerekir."),
            ("haidt", "Haidt, sosyal medyanın kızları başlıca görsel karşılaştırma ve ilişkisel saldırganlık yoluyla, erkekleri ise oyun "
                      "ve geri çekilme yoluyla etkilediğini öne sürer [@haidt2024]. Bu oturumdaki deneysel bulgular ilk yarıyı kısmen "
                      "destekliyor; ikinci yarı için veri daha az."),
        ],
        tartisma=[
            ("Süre önemsiz, içerik önemli: çelişki mi?",
             "Kullanım miktarı beden imajıyla ilişkili değil [@nguyen2025], ama ideal beden içeriğine bakmak memnuniyeti düşürüyor "
             "[@zhang2025b]. İki bulgu birbirini tamamlıyor: saat, akışta ne olduğunu söylemez. Öte yandan deneyler dakikalar süren "
             "maruziyetten hemen sonraki memnuniyeti ölçüyor; aylar içindeki birikimli etki bilinmiyor."),
            ("Deneyler kimi temsil ediyor?",
             "Katılımcıların çoğu üniversite çağındaki kadınlar; ergenler ve erkekler az. Süreler bir ile üç hafta arasında, etkin "
             "kontrol grubu çoğunlukla yok ve çalışmayı bırakanların oranı yüksek olabiliyor [@dondzilo2023] [@smith2024]. Bulguları "
             "on dört yaşındaki bir hastaya aktarırken bu boşluk akılda tutulmalı."),
            ("Platform üzerinden müdahale çözüm mü?",
             "Görsel platformları kullanarak beden imajını iyileştirmeyi amaçlayan müdahalelerin sistematik derlemesi mütevazı yararlar "
             "bildirdi; biçim ve süre çalışmadan çalışmaya çok değişiyor [@copez2026]. Sorunu üreten ortamın içinden çözüm üretmek "
             "mümkün görünüyor, ama etki küçük."),
        ],
        sorular=[
            S("On altı yaşındaki İpek anoreksiya nervoza nedeniyle izleniyor ve sosyal medyayı günde ‘yalnızca bir saat’ kullandığını söylüyor. Bu bilgiye ilişkin en doğru değerlendirme hangisidir?",
              ["Süre kısa olduğundan risk yoktur",
               "Süre az bilgi verir; akışın içeriği ve karşılaştırma eğilimi değerlendirilmelidir",
               "Sosyal medya anoreksiyanın nedenidir",
               "Konu tedaviyle ilgili değildir"], 1,
              "Beden imajıyla ilişkili olan süre değil, karşılaştırma eğilimi (r=0,45) ve görünüş odaklı içeriktir [@bonfanti2024] [@nguyen2025]. Bir saatlik diyet içeriği, beş saatlik müzik videosundan daha çok şey değiştirebilir."),
            S("İpek hesaplarını kapatmayı reddediyor. Kanıta göre denenebilecek ara çözüm hangisidir?",
              ["Hesapları ailesine zorla kapattırmak",
               "Görünüş ve diyet odaklı hesapları akıştan birlikte çıkarmak ve bir hafta sonra nasıl hissettiğini değerlendirmek",
               "Yalnızca bedeni olumlayan hesapları takip ettirmek",
               "Konuyu gündemden çıkarmak"], 1,
              "Akış temizliği, tümüyle ara vermek ve süre sınırı kadar yararlı göründü ve sürdürülmesi daha kolay [@seekis2025]. Bedeni olumlayan içerik de görünüşü merkezde tutar; yalnızca ona yönelmek hedefi daraltır."),
            S("On beş yaşındaki Emre son altı ayda protein tozu, ‘çene hattı’ egzersizleri ve görünüş puanlama forumlarıyla ilgilenmeye başlamış; aynada uzun süre geçiriyor ve fotoğraf çekilmekten kaçınıyor. İlk klinik adım hangisidir?",
              ["Ergenlikte olağandır; sorgulamaya gerek yoktur",
               "Görünüş kaygısını, karşılaştırmayı, takviye ya da ilaç kullanımını ve işlev kaybını ayrıntılı sormak; beden dismorfik bozukluğu açısından değerlendirmek",
               "Yeme bozukluğu ve görünüş kaygısı yalnızca kızlarda görülür",
               "Sosyal medyayı yasaklamak yeterlidir"], 1,
              "Aynada uzun süre geçirme ve fotoğraftan kaçınma, olağan ilginin ötesine geçildiğini düşündürür. Erkek ergenlerde görünüş kaygısı kas ve yüz hatlarına odaklanabilir ve gözden kaçar. Çevrimiçi topluluklar kaygıyı besleyebilir; değerlendirme önce belirtiyi ve işlevi sormakla başlar."),
        ],
        akilda="Bedeni etkileyen saat değil, kıyastır. Süreyi değil akışı sorun; bırakmak mümkün değilse akışı birlikte değiştirin.",
    ),
    # ------------------------------------------------------------------ 7
    dict(
        no=7, kesim="r", kisa="Oyun",
        baslik="Oyun: çoğunluk için hobi, azınlık için bozukluk",
        slogan="Tanı süreyle konmaz; bırakamama, her şeyin önüne geçme ve zarara karşın sürdürme üçlüsüyle konur.",
        bakis=("Dijital oyun çocukların dörtte üçünün yaptığı bir etkinlik; oyun bozukluğu ise ICD-11’de tanımlı, görece seyrek bir "
               "tablo. Bu oturum ikisini ayırmanın ölçütlerini, eş tanıların ağırlığını ve tedavi kanıtının bugünkü durumunu ele alıyor."),
        sorun=[
            "Günde beş saat oynayan ama dersleri ve arkadaşlıkları yerinde olan bir ergen ile günde iki saat oynayıp okulu bırakan bir ergen: hangisi tanı alır?",
            "Oyunun o çocuk için işlevi ne: başarı duygusu, aidiyet, kaçış?",
            "Oyun içi harcamayı ve bahsi soruyor musunuz?",
        ],
        fikirler=[
            ("ICD-11 tanımı üç ayaklıdır",
             "Oyun bozukluğu (6C51) üç özellikle tanımlanır: oyun üzerinde denetimin bozulması, oyunun diğer ilgi ve günlük "
             "etkinliklerin önüne geçmesi ve olumsuz sonuçlara karşın sürdürülmesi ya da artması. Tanı için belirgin işlev kaybı ve "
             "genellikle en az 12 aylık bir süreklilik aranır [@icd11]. Tanımda saat cinsinden bir ölçüt yoktur."),
            ("Yaygınlık, kullanılan ölçeğe bağlı",
             "53 çalışmayı (226.247 kişi, 17 ülke) birleştiren meta-analizde yaygınlık %3,05 bulundu; yalnızca daha sıkı örnekleme "
             "yöntemi kullanan çalışmalar alındığında %1,96. Tahminlerdeki değişkenliğin %77’sini tarama aracının seçimi açıkladı; "
             "erkek/kız oranı yaklaşık 2,5’e 1 idi [@stevens2021]."),
            ("Çoğu oyuncuda süre ile iyi oluş arasında anlamlı bir bağ yok",
             "Oyun şirketlerinden alınan kayıtlı oyun süreleriyle yapılan çalışmada süre ile iyi oluş arasında küçük ve olumlu bir "
             "ilişki bulundu [@johannes2021]. 38.935 oyuncunun altı haftalık verisinde oyun süresinin iyi oluşu etkilediğine dair "
             "kanıt yok denecek kadar azdı; belirleyici olan sürenin kendisi değil, oynama güdüsüydü [@vuorre2022]. Oyunun bilişsel, "
             "güdüsel, duygusal ve sosyal yararlarını özetleyen derleme hâlâ geçerli bir karşı ağırlıktır [@granic2014]."),
            ("Eş tanı kural gibidir",
             "İnternet bağımlılığı çalışmalarının meta-analizinde alkol kötüye kullanımı (OR 3,05), DEHB (OR 2,85), depresyon (OR 2,77) "
             "ve kaygı (OR 2,70) ile ilişki saptandı [@ho2014]. Sistematik derlemede en tutarlı ilişkiler depresyon ve DEHB belirtileriyle "
             "bulundu [@carli2013]."),
            ("Aile hem risk hem koruyucu",
             "64 çalışmanın derlemesinde ebeveynin çocuğun oyun dünyasına ilişkin bilgisi ve olumlu ebeveynlik koruyucu; olumsuz "
             "ebeveynlik ve aile içi uyumsuzluk risk etkeniydi. Kısıtlayıcı kuralların etkisine ilişkin sonuçlar tutarsızdı "
             "[@petrescu2025]."),
            ("Rastgele ödüllü satın almalar kumara benziyor",
             "7422 oyuncuyla yapılan ankette ganimet kutularına harcanan para ile sorunlu kumar şiddeti arasında ilişki bulundu; "
             "diğer oyun içi satın almalarla ilişki belirgin biçimde daha zayıftı [@zendle2018]. Yön bilinmiyor: kutular kumara mı "
             "götürüyor, yoksa kumara yatkın olanlar mı kutulara yöneliyor?"),
            ("Tedavi: bilişsel davranışçı yaklaşım umut verici, kanıt kalitesi sınırlı",
             "21 kontrollü çalışmanın (1360 katılımcı) meta-analizinde tedaviler oyun bozukluğu belirtilerini (g=1,38) ve oyun süresini "
             "(g=0,90) azalttı; kazanım 90 günlük izlemde sürdü ve ergenlerde daha büyüktü. Heterojenlik yüksekti; ilaç tedavisi için "
             "kanıt yetersizdi [@harpas2025]. Önceki derlemeler tedavi sonrası kazanımın izlemde sürmediğini ve çalışmaların raporlama "
             "kalitesinin düşük olduğunu bildirmişti [@stevens2019] [@king2017]. Programlarda en sık yer alan bileşenler duygu "
             "düzenleme becerileri, psikoeğitim ve bilişsel yeniden yapılandırmadır [@radunz2026]."),
            ("Önleme, riskli gruba yöneldiğinde işe yarıyor",
             "Almanya’da 44 okulda 1793 öğrenciyle yapılan randomize çalışmada bilişsel davranışçı temelli dört oturumluk program, "
             "tüm örneklemde medya okuryazarlığı programından farklı değildi; yalnızca başlangıçta yüksek riskli olan 205 ergende "
             "on iki ay sonra belirtiler daha düşüktü (d=−0,30) [@lindenberg2026]."),
        ],
        klinik=[
            "Üç soruyla tarayın: Bırakmak istediğinde bırakabiliyor musun? Oyun yüzünden bıraktığın şeyler oldu mu? Sorun çıkardığını bildiğin hâlde sürdürüyor musun? Ardından işlev kaybını ve ne kadar zamandır sürdüğünü sorun [@icd11].",
            "Oyunun işlevini bulun: başarı duygusu, arkadaş grubu, kaçış ya da can sıkıntısı. Plan, bu işlevin yerine ne konacağını söylemeli.",
            "Eş tanıyı arayın: DEHB, depresyon ve kaygı oyun sorununun arkasında sık bulunur [@ho2014]. Eş tanı tedavi edilmeden oyun süresini kısıtlamak çoğu kez sonuç vermez.",
            "Oyun içi harcamayı ve ganimet kutularını sorun; ailenin kart bilgisinin hesapta kayıtlı olup olmadığını öğrenin [@zendle2018].",
            "Aileye yasaktan önce ilgi önerin: çocuğun oynadığı oyunu bilmek ve arada birlikte oynamak, koruyucu etkenler arasında sayılan ebeveyn bilgisinin somut hâlidir [@petrescu2025].",
            "Okuldan çekilmiş ergende sıralamaya dikkat edin: önce gün-gece düzeni ve okula dönüş planı, sonra oyun süresi. Oyunu bir gecede kesmek çoğu kez çatışmayı büyütür.",
            "TR Türkiye’de düzenli oyun oynayan 6–15 yaş çocukların %40,1’i planladığından uzun oynadığını söylüyor [@tuik2024]. Bu sıklıkta bir bildirimin tek başına tanı değeri yoktur; ICD-11 eşiği işlev kaybı ve süreklilik ister.",
            "TR Bingöl’de 866 lise öğrencisinde sorunlu internet kullanımı %14,3, oyun bozukluğu %0,9 bulundu [@zeyrek2026]. İki sayı arasındaki fark, ‘internet bağımlılığı’ ölçeklerinin ne kadar geniş bir alanı taradığını gösterir.",
            "TR İstanbul’da 6116 ergenin %12,4’ü çevrimiçi bahis oynadığını bildirdi; sorunlu kullanıcıların yaklaşık dörtte biri 10–12 yaşında başlamıştı [@aricak2019]. Oyun öyküsünde bahsi ve şans oyunlarını ayrıca sorun.",
            "TR 7578 sayılı Kanun oyun platformlarına yaş derecelendirmesi yapma ve ebeveyn kontrol aracı sunma (hesap ayarları, ücretli işlemler için ebeveyn onayı) yükümlülüğü getirdi; hükümler 1 Kasım 2026’da yürürlüğe girdi, ayrıntılar BTK yönetmeliğine bırakıldı [@kanun7578].",
            "TR Yeşilay Danışmanlık Merkezleri (YEDAM, 115) teknoloji bağımlılığı için de ücretsiz psikososyal destek sunuyor [@yedam]; hastanenizde yapılandırılmış bir program yoksa yönlendirme seçeneği olarak bilinmeli.",
        ],
        kitaplar=[
            ("williams", "Formülasyon bölümündeki bir örnek, ergenin oyun isteğini ailenin gelecek kaygısıyla; düzenli uyku ihtiyacını "
                         "oyundan alınan keyifle yan yana yazar [@williams2025]. İki tarafın ihtiyacını aynı sayfada görmek pazarlığın "
                         "ön koşuludur."),
            ("iacapap", "2.0 sürümünde sorunlu internet kullanımı ve diğer davranışsal bağımlılıklar için ayrı bölümler vardır; internet "
                        "bağımlılığı ölçeklerinin Türkçe sürümlerinin bulunduğu not edilir [@iacapap2]. Bu bölümler notlarımızda henüz "
                        "ayrıntılı işlenmedi."),
            ("lewis", "DEHB bölümü oyun temelli dijital tedaviyi kanıt tablosuna almıştır [@lewis6]. ‘Oyun’ sözcüğü tek başına risk "
                      "anlamına gelmez."),
        ],
        tartisma=[
            ("Oyun bozukluğu bir tanı olmalı mıydı?",
             "Tanı önerildiğinde 26 araştırmacı açık bir tartışma yazısıyla karşı çıktı: araştırma tabanı zayıftı, ölçütler madde "
             "kullanımı ve kumardan uyarlanmıştı, ahlaki panik ve yanlış pozitif tanı riski vardı [@aarseth2017]. Savunanlara göre "
             "tanı, yardım arayan gerçek bir grubu görünür kılıyor ve yaygınlığı başka bozukluklarla karşılaştırılabilir düzeyde "
             "[@stevens2021]. DSM-5 ise ‘internet oyun oynama bozukluğu’nu hâlâ ileri araştırma gerektiren durumlar arasında tutuyor "
             "[@king2017]."),
            ("Şiddet içerikli oyunlar saldırganlığı artırır mı?",
             "Erişkinlerin iki ay boyunca her gün şiddet içerikli bir oyun oynadığı randomize çalışmada saldırganlık, empati, "
             "dürtüsellik ve duygudurum ölçümlerinde ne oyun sonrasında ne de iki ay sonra değişiklik saptandı [@kuhn2019]. Çalışma "
             "erişkinlerle yapıldı; ergenlerde aynı nitelikte bir deney yok ve bulgu doğrudan genellenemez."),
            ("Kısıtlamak mı, ilgilenmek mi?",
             "Kısıtlayıcı kuralların etkisine ilişkin bulgular tutarsız; ebeveynin bilgisi ve sıcak ilişki ise tutarlı biçimde "
             "koruyucu [@petrescu2025]. Evrensel önleme programları da yalnızca riskli grupta etkili [@lindenberg2026]. Veri, "
             "herkese aynı kuralı koymaktan çok riskli çocuğu erken tanımayı destekliyor."),
        ],
        sorular=[
            S("On altı yaşındaki Barış hafta içi günde dört-beş saat çevrimiçi oyun oynuyor. Notları iyi, basketbol antrenmanlarına gidiyor, arkadaşlarıyla yüz yüze görüşüyor ve istendiğinde bırakabiliyor. Annesi ‘oyun bağımlısı’ olduğunu düşünüyor. ICD-11’e göre değerlendirme nedir?",
              ["Oyun bozukluğu; süre yeterlidir",
               "Tanı ölçütleri karşılanmıyor: denetim kaybı, öncelik değişimi ve işlev kaybı yok",
               "Tanı için sürenin altı saati geçmesi gerekir",
               "Aile bildirimi tanı için yeterlidir"], 1,
              "ICD-11 tanımında süre ölçütü yoktur; denetim kaybı, oyunun diğer etkinliklerin önüne geçmesi, zarara karşın sürdürme ve işlev kaybı aranır [@icd11]. Barış’ta yoğun ama sorunsuz kullanım var. Annenin kaygısı yine de ciddiye alınmalı: kaygının kaynağını sorun."),
            S("On beş yaşındaki Onur sekiz aydır okula gitmiyor; gece boyunca oynuyor, gündüz uyuyor. Görüşmede dikkat sorunlarının ilkokuldan beri sürdüğü ve son bir yılda arkadaş grubundan dışlandığı öğreniliyor. Planın ilk adımı hangisidir?",
              ["Evdeki interneti kestirmek",
               "Eş tanıları değerlendirip tedavi etmek; gün-gece düzeni ve okula dönüş için basamaklı plan yapmak; oyunu bu planın içinde ele almak",
               "Yalnızca oyun süresini günde bir saate indirmek",
               "Doğrudan yatış planlamak"], 1,
              "Oyun sorununa DEHB, depresyon ve kaygı sık eşlik eder [@ho2014]. Onur’da oyun hem dışlanmadan kaçış hem de dikkat sorunlarının kolay ödül bulduğu alan olabilir. Bilişsel davranışçı programlar ergenlerde etkili görünüyor [@harpas2025], ancak altta yatan sorun ele alınmadan süre kısıtlaması kalıcı olmaz."),
            S("On üç yaşındaki Deniz’in babası kart ekstresinde oyun içi ‘sandık’ satın almalarını fark ediyor. Bu bulgunun önemi nedir?",
              ["Önemsizdir; bütün oyuncular yapar",
               "Rastgele ödül içeren satın almalar kumara benzer bir düzenektir; harcama örüntüsü, denetim kaybı ve bahis davranışı ayrıca sorulmalı, kart bilgisi hesaptan kaldırılmalıdır",
               "Tek başına oyun bozukluğu tanısı koydurur",
               "Tıbbi açıdan ilgisizdir"], 1,
              "Ganimet kutusu harcaması sorunlu kumar şiddetiyle ilişkili bulundu [@zendle2018]. Türkiye’de oyun platformları ücretli işlemleri ebeveyn onayına bağlayan araçlar sunmakla yükümlü [@kanun7578]; aileye bu ayarı birlikte açmayı önerin."),
        ],
        akilda="Oyun bozukluğu süreyle değil üçlüyle tanınır: bırakamama, her şeyin önüne geçme ve zarara karşın sürdürme. Arkasında çoğu kez tedavi edilebilir bir eş tanı vardır.",
    ),
    # ------------------------------------------------------------------ 8
    dict(
        no=8, kesim="r", kisa="Çevrimiçi zarar",
        baslik="Çevrimiçi zarar: zorbalık, cinsel istismar ve şantaj",
        slogan="Fail çoğu kez yabancı değil, tanıdık. Çocuğu susturan çoğu kez utanç ve ceza korkusu.",
        bakis=("Ekran süresi tartışmasının gölgesinde kalan, ama bireysel düzeyde en ağır sonuçları doğuran başlık çevrimiçi "
               "mağduriyettir. Bu oturum siber zorbalığı, görüntü temelli cinsel istismarı, cinsel şantajı ve medya yoluyla bulaşan "
               "sıkıntıyı ele alıyor; odak, çocuğun bunu size anlatabilmesinin koşulları."),
        sorun=[
            "Bir ergen çıplak fotoğrafının yayıldığını söylese ilk cümleniz ne olurdu?",
            "Ailelere ‘yabancılarla konuşmasın’ demek yeterli mi?",
            "Çocuk, anlatırsa telefonunun elinden alınacağını düşünüyorsa ne olur?",
        ],
        fikirler=[
            ("Siber zorbalık kendine zarar ve intihar davranışıyla ilişkili",
             "Meta-analizde siber zorbalık mağdurlarında kendine zarar (OR 2,35), intihar düşüncesi (OR 2,15) ve intihar girişimi "
             "(OR 2,57) mağdur olmayanlara göre daha sıktı. Zorbalık yapanlarda da intihar düşüncesi ve davranışı hafifçe artmıştı "
             "(OR 1,2 dolayında) [@john2018]."),
            ("Cinsel içerikli mesajlaşma yaygın; asıl sorun rızasız iletim",
             "39 çalışmanın (110.380 genç, ortalama yaş 15) meta-analizinde gençlerin %14,8’i cinsel içerikli mesaj göndermiş, %27,4’ü "
             "almıştı; %12,0’ı aldığı içeriği rıza olmadan başkasına iletmiş, %8,4’ünün kendi içeriği rızası dışında iletilmişti "
             "[@madigan2018]. 2016 sonrası çalışmaları kapsayan güncellemede oranlar benzer düzeyde kaldı (gönderme %19,3, alma %34,8, "
             "rızasız iletme %14,5) [@mori2022]."),
            ("Çevrimiçi cinsel istismar sık ve fail çoğu kez tanıdık",
             "ABD’de 2639 genç erişkinle yapılan ulusal ankette katılımcıların %15,6’sı 18 yaşından önce çevrimiçi cinsel istismarın "
             "bir biçimini yaşadığını bildirdi: görüntü temelli cinsel istismar %11,0, yetişkin tarafından çevrimiçi kandırma %5,4, "
             "cinsel şantaj %3,5. Faillerin çoğu yabancı değil; flört edilen kişi, arkadaş ya da tanıdıktı. En riskli yaş aralığı "
             "13–17 idi [@finkelhor2022]."),
            ("Kandırma girişimi sıradanlaşmış",
             "Avustralya’da 10–17 yaş 304 gencin %66’sı kandırma (grooming) ile ilişkili bir iletişim, %31’i cinsel talep yaşadığını "
             "bildirdi. Çoğu karşısındakinin çocuk olduğunu düşünmüştü ve ya hiçbir şey yapmamış ya da kişiyi engellemişti. Gizlilik "
             "ayarları ve ebeveyn arabuluculuğu gibi güvenlik önlemleri ile bu deneyimler arasında ilişki bulunmadı [@logos2026]."),
            ("Cinsel şantaj intihar riskiyle birlikte gidiyor",
             "ABD’de 13–17 yaş 3416 öğrencinin yaklaşık %15’i cinsel şantajın hedefi olmuştu; bu deneyim intihar düşüncesi ve "
             "davranışıyla ilişkiliydi ve failin çevrimdışı tanınan biri olup olmaması sonucu değiştirmiyordu [@patchin2026]. Kapsam "
             "derlemesine göre failler çoğu kez partner ya da tanıdık; bildirim ve yardım arama oranı ise utanç, korku ve kurumlara "
             "güvensizlik nedeniyle çok düşük [@ray2025]."),
            ("Neden anlatmıyorlar?",
             "18 yaşından önce görüntü temelli cinsel istismar yaşayıp bunu kimseye söylememiş 1551 kişi, susma nedeni olarak en sık "
             "aileyle başının derde gireceği korkusunu (%53,9), utancı (%52,9) ve kendi başına çözebileceği inancını (%45,2) gösterdi "
             "[@mitchell2025]."),
            ("Yapay zekâyla üretilen cinsel görüntüler okullara ulaştı",
             "İngiltere’de okullarda yapılan nitel çalışmada öğretmenlerin bir bölümü bu teknolojinin ne kadar kolay kullanıldığını "
             "hafife alıyordu; yapay görüntülerin rızasız paylaşılan gerçek görüntülerle aynı ciddiyette ele alınması gerektiği "
             "konusunda okullar arasında tutarlılık yoktu. Öğrenciler konuda hiç eğitim almadıklarını söyledi [@ringrose2026]."),
            ("Sonuçlar ağır ve okul yaşamına uzanıyor",
             "10–24 yaş grubundaki 12 çalışmanın derlemesinde görüntü temelli cinsel istismarın ardından korku, kaygı, depresyon ve "
             "intihar düşüncesi; akran zorbalığı, dışlanma ve mağdurun suçlanması; okul değiştirme bildirildi [@hellevik2025]."),
            ("Sıkıntı ekrandan da bulaşır",
             "Boston Maratonu saldırısından sonraki hafta günde altı saat ve üzeri olayla ilgili yayın izleyenlerde akut stres "
             "belirtileri, olay yerinde bulunanlardan yüksekti [@holman2014]. Bir intiharı konu alan dizinin yayımlanmasını izleyen "
             "ay ABD’de 10–17 yaş grubunda intihar oranı %29 arttı; artış erkeklerde belirgindi [@bridge2020]. İkinci bir analiz "
             "10–19 yaşta üç ay süren bir artış buldu [@niederkrotenthaler2019]. Aynı araştırma çizgisi koruyucu yönü de gösterdi: "
             "kriz anında başka bir yol bulan kişilerin öyküleri intihar oranlarındaki düşüşle ilişkiliydi [@niederkrotenthaler2010]."),
        ],
        klinik=[
            "İlk cümleniz suçlamasız olsun: ‘Bunu anlatman zordu. Suç senin değil; birlikte çözeceğiz.’ Çocukların yarısından fazlası aileden çekindiği ya da utandığı için susuyor [@mitchell2025].",
            "Aileye, ilk tepkinin telefonu almak olmaması gerektiğini önceden anlatın. Ceza beklentisi bir sonraki olayın gizlenmesine yol açar.",
            "Cinsel şantajda dört adım: ödeme yapmamak ve yeni görüntü göndermemek; konuşmayı silmeden ekran görüntüsü almak; hesabı platforma bildirip engellemek; güvenilen bir yetişkine ve yetkili birimlere başvurmak. İntihar riskini mutlaka değerlendirin [@patchin2026].",
            "Görüntü yayıldıysa kaldırma yollarını bilin. 18 yaşından önce çekilmiş görüntüler için NCMEC’in Take It Down hizmeti, görüntünün kendisini değil sayısal özetini kullanarak katılımcı platformlarda yayılımı durdurmayı amaçlar [@takeitdown].",
            "Güvenlik konuşmasını ‘yabancı tehlikesi’ne daraltmayın: fail çoğu kez flört edilen kişi, arkadaş ya da tanıdıktır [@finkelhor2022]. Rızayı, baskıyı ve görüntünün başkasına iletilmesini konuşun.",
            "Siber zorbalık öyküsünde hem mağduriyeti hem zorbalık yapmayı sorun; ikisinde de intihar düşüncesi daha sık [@john2018].",
            "Sarsıcı bir olayın ardından haber ve video izleme süresini sorun. Saatlerce yinelenen izleme akut stres belirtilerini uzatabilir [@holman2014].",
            "TR Yasa dışı içerik için ihbarweb.org.tr üzerinden bildirim yapılabilir; internetle ilgili sorunlarda BTK’nın ALO 141 İnternet Bilgi Destek Hattı vardır [@btk2026]. Çocuk koruma gerektiren durumlarda ALO 183 Sosyal Destek Hattı, acil durumda 112 aranır.",
            "TR Çocuğun cinsel istismarı şüphesinde sağlık çalışanının bildirim yükümlülüğü çevrimiçi istismarı da kapsar. Kurumunuzun çocuk koruma birimini ve Çocuk İzlem Merkezi yolunu izleyin; kanıt niteliğindeki görüntüleri kendi cihazınıza aktarmayın.",
            "TR 1 Kasım 2026’dan beri 15–17 yaş hesapları varsayılan olarak gizli; yalnızca çocuğun takip ettiği hesaplar mesaj gönderebiliyor ve rehber eşleştirmesi yasak [@yonetmelik2026]. Bu kurallar yabancı kaynaklı teması azaltmayı hedefler; tanıdık kaynaklı riski değiştirmez.",
        ],
        kitaplar=[
            ("lewis", "Epidemiyoloji bölümü kurgusal intihar anlatımının gerçek dünyadaki etkisini bir dizi örneği üzerinden işler; "
                      "azınlık gençliği bölümü ise şiddet içeren videoların yinelenen izlenmesini travmatik medya maruziyeti olarak "
                      "ele alır [@lewis6]."),
            ("williams", "Kitabın zor görüşmelere ilişkin ilkesi burada da geçerlidir: önce duyguyu karşılamak, sonra bilgi toplamak "
                         "[@williams2025]. İfşa anında sorulan ‘neden gönderdin?’ sorusu görüşmeyi kapatır."),
            ("rutter", "Yedinci baskı salgın, savaş ve afet gibi halk sağlığı olaylarının çocuk ruh sağlığına etkisine ayrı bir bölüm "
                       "ayırmıştır [@rutter7]. Bu olayların çocuklara büyük ölçüde ekrandan ulaştığı düşünülürse medya maruziyeti "
                       "öykünün parçasıdır."),
        ],
        tartisma=[
            ("Güvenlik ayarları koruyor mu?",
             "Avustralya çalışmasında gizlilik ayarı ve ebeveyn arabuluculuğu kandırma girişimleriyle ilişkili bulunmadı [@logos2026]. "
             "Mevzuat ise korumayı büyük ölçüde varsayılan ayarlara dayandırıyor [@yonetmelik2026]. Failin çoğu kez tanıdık olduğu "
             "düşünülürse [@finkelhor2022] teknik önlem gerekli, ama yetersiz görünüyor; rıza ve ilişki eğitimi ayrıca gerekiyor."),
            ("Yaygınlık rakamları neden bu kadar farklı?",
             "Cinsel şantaj için derleme %0,7–5,0 aralığı verirken [@ray2025], 2026 tarihli ABD anketi yaklaşık %15 buldu "
             "[@patchin2026]. Fark tanımdan (tehdit mi, gerçekleşen eylem mi), sorulan dönemden ve örneklemden doğabilir; son "
             "yıllarda gerçek bir artış da olasıdır. Bir oranı aktarırken neyin sayıldığını söylemek gerekir."),
            ("Ebeveyn izlemi mi, mahremiyet mi?",
             "Çocukları susturan başlıca etken ceza korkusu [@mitchell2025]; gizli izleme ortaya çıktığında bu korkuyu büyütür. "
             "Türkiye’deki yönetmelik ebeveyn kontrol araçlarının etkinleştirildiğinde çocuğa açıkça bildirilmesini ve çocuğun "
             "mahremiyetini orantısız biçimde ortadan kaldırmayacak, gözetimden çok iletişim esasına dayanacak biçimde tasarlanmasını "
             "şart koşuyor [@yonetmelik2026]. Bu ilke klinik öneriyle örtüşüyor: izleme açık olmalı, gerekçesi konuşulmalı."),
        ],
        sorular=[
            S("On dört yaşındaki Yağmur, eski erkek arkadaşının kendisine ait çıplak bir fotoğrafı sınıf grubuna gönderdiğini ağlayarak anlatıyor ve ‘Annem öğrenirse telefonumu alır’ diyor. En uygun ilk yanıt hangisidir?",
              ["‘O fotoğrafı neden gönderdin?’",
               "‘Bunu anlatman cesaret istedi; suç senin değil. Şimdi güvende olman ve fotoğrafın yayılmasını durdurmak için neler yapabileceğimize bakalım.’",
               "‘Bunu annenle konuşmalısın; benim alanım değil.’",
               "Yanıt vermeden bildirim formunu doldurmak"], 1,
              "Çocukların susma nedenlerinin başında aileden çekinme ve utanç gelir [@mitchell2025]. Önce duygu karşılanır, sonra güvenlik ve kaldırma adımları, intihar riski ve bildirim süreci ele alınır. Bildirim yükümlülüğü sürer; nasıl yapılacağı çocuğa açıklanır."),
            S("On altı yaşındaki Kaan, çevrimiçi tanıştığı birine görüntü gönderdikten sonra para istendiğini, ödemezse görüntünün ailesine gönderileceğinin söylendiğini anlatıyor. Aşağıdakilerden hangisi önerilmez?",
              ["Konuşmanın ekran görüntülerini saklamak",
               "İstenen parayı ödeyip konuyu kapatmak",
               "Hesabı platforma bildirmek ve engellemek",
               "İntihar düşüncesini sormak"], 1,
              "Ödeme tehdidi sona erdirmez, çoğu kez yeni talepleri getirir. Kanıtı saklamak, hesabı bildirmek, bir yetişkini ve yetkili birimleri devreye sokmak önerilir. Cinsel şantaj intihar düşüncesi ve davranışıyla ilişkili olduğundan risk değerlendirmesi atlanmamalı [@patchin2026]."),
            S("Bir veli toplantısında ‘Çocuğunuzu çevrimiçi istismardan korumak için tanımadığı kişilerle konuşmasını yasaklayın, yeter’ deniyor. Veriye göre bu önerinin eksiği nedir?",
              ["Eksiği yoktur; failler yabancıdır",
               "Çevrimiçi cinsel istismarda fail çoğu kez flört edilen kişi, arkadaş ya da tanıdıktır; koruma rıza, baskı ve görüntü paylaşımı konularını da kapsamalıdır",
               "Çevrimiçi istismar çok seyrek olduğundan öneri gereksizdir",
               "Yalnızca erkek çocuklar risk altındadır"], 1,
              "Ulusal ankette faillerin çoğu yabancı değildi [@finkelhor2022]. ‘Yabancı tehlikesi’ çerçevesi, en sık görülen senaryoyu, yani bir ilişki içinde paylaşılan görüntünün sonradan kötüye kullanılmasını dışarıda bırakır."),
        ],
        akilda="Çocuğun anlatmasını sağlayan şey gözetim değil, cezalandırılmayacağını bilmesidir. İlk cümleniz, bir sonraki ifşanın olup olmayacağını belirler.",
    ),
]
