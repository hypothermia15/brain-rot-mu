# -*- coding: utf-8 -*-
"""Oturum 1–4: Manzara ve Kanıt. Sayıların tümü kaynakçadaki birincil kaynaktan ya da PubMed özetinden doğrulanmıştır."""
from ic_ortak import S

OTURUMLAR_1 = [
    # ------------------------------------------------------------------ 1
    dict(
        no=1, kesim="m", kisa="Sayılar ve sözcükler",
        baslik="Sayılar ve sözcükler: gençler çevrimiçinde ne kadar, nerede?",
        slogan="Neredeyse herkes çevrimiçi. Ayırt edici soru artık ‘kullanıyor mu?’ değil, ‘ne için ve neyin yerine?’",
        bakis=("Oxford sözlükleri 2024’te yılın sözcüğü olarak *brain rot*’u seçti [@oup2024]; izleyen iki yılda öne çıkan sözcüklerin "
               "çoğu da çevrimiçi yaşamdan geldi. Bu oturum tartışmanın zeminini kuruyor: Türkiye’de ve dünyada çocuklar ve ergenler "
               "interneti, sosyal medyayı, oyunu ve sohbet botlarını ne ölçüde kullanıyor; bu sayılar neyi söylüyor, neyi söylemiyor?"),
        sorun=[
            "Polikliniğinizde gördüğünüz çocukların kaçının yalnızca kendisinin kullandığı bir telefonu var? Tahmininizi aşağıdaki TÜİK verisiyle karşılaştırın.",
            "‘Ekran süresi’ dediğinizde ödevi, oyunu, mesajlaşmayı ve kısa video akışını aynı kefeye mi koyuyorsunuz?",
            "Bir aile ‘çok kullanıyor’ dediğinde hangi sayıyı ve hangi karşılaştırmayı kastediyor?",
        ],
        cizelge=("Yılın sözcükleri, 2024–2026", [
            ("2024 · Oxford", "**brain rot**: değersiz sayılan çevrimiçi içeriğin aşırı tüketimine bağlanan zihinsel körelme ve o içeriğin kendisi. Sözcüğün ilk kayıtlı kullanımı 1854’e uzanıyor [@oup2024]."),
            ("2025 · Oxford", "**rage bait**: öfke uyandırarak etkileşim toplamak için üretilen içerik [@oup2025]."),
            ("2025 · Cambridge", "**parasocial**: tanımadığı bir ünlüyle, giderek de bir yapay zekâyla kurulan tek yönlü yakınlık [@cambridge2025]."),
            ("2025 · Collins", "**vibe coding**: yapay zekâya gündelik dille yazılım yazdırmak [@popsci2025]."),
            ("2025 · Dictionary.com", "**67**: sabit bir anlamı olmayan, ortaokul çağında yayılan şaka sözcüğü [@dictionary2025]."),
            ("2026 · Dictionary.com", "**maxxing**: yaşamın bir yönünü sonuna kadar ‘iyileştirme’ uğraşı; en bilinen biçimi görünüşe odaklı *looksmaxxing* [@dictionary2026]."),
            ("2026 · Collins", "**mogging**: birini ya da bir şeyi gölgede bırakmak; kökeni çevrimiçi erkeklik forumları [@collins2026]."),
        ]),
        fikirler=[
            ("Çevrimiçi olmak istisna değil, norm",
             "TÜİK’in 2024 araştırmasına göre Türkiye’de 6–15 yaş çocukların %91,3’ü internet kullanıyor (2021’de %82,7); %66,1’i sosyal "
             "medya kullanıyor [@tuik2024]. Bu ölçekte bir davranışta ‘kullanan’ ile ‘kullanmayan’ı karşılaştırmak artık pek bilgi vermez."),
            ("Küçük yaş grubu da tablonun içinde",
             "Sosyal medya kullanımı 6–10 yaşta %53,5, 11–15 yaşta %79,0. TÜİK’in tanımı YouTube’u da kapsıyor: sosyal medya kullanan "
             "çocukların %96,3’ü YouTube, %41,5’i Instagram, %26,2’si TikTok kullanıyor [@tuik2024]. ‘İlkokul çocuklarının yarısı sosyal "
             "medyada’ cümlesi bu ayrıntıyla birlikte okunmalı."),
            ("Kendi cihazı olan çocuk artık azınlık değil",
             "Çocukların %76,1’i cep telefonu kullanıyor; %43,9’unun yalnızca kendisinin kullandığı bir telefonu var (2021’de %39,0) "
             "[@tuik2024]."),
            ("Yoğunluk yaşla artıyor",
             "Hafta içi günde iki saat ya da daha uzun internet kullananların oranı 6–10 yaşta %30,6, 11–15 yaşta %54,4. 11–15 yaş "
             "telefon kullanıcılarının %42,8’i telefonunu en az yarım saatte bir kontrol ediyor [@tuik2024]. ABD’de 13–17 yaş ergenlerin "
             "yaklaşık onda dördü neredeyse sürekli çevrimiçi olduğunu söylüyor; TikTok’u her gün kullananların oranı %61 [@pew2025]."),
            ("Sorunlu kullanım azınlıkta, ama artıyor",
             "44 ülkeyi kapsayan HBSC araştırmasında sorunlu sosyal medya kullanımı 2018’de %7 iken 2022’de %11’e çıktı (kızlarda %13, "
             "erkeklerde %9). Sorunlu oyun riski taşıyanların oranı %12 (erkeklerde %16, kızlarda %7) [@hbsc2024]."),
            ("Oyun yaygın; zorlanmayı çocuklar kendileri söylüyor",
             "Türkiye’de 6–15 yaş çocukların %74,0’ü dijital oyun oynuyor (erkeklerde %82,8, kızlarda %64,8). Düzenli oynayanların %40,1’i "
             "planladığından uzun oynadığını, %35,6’sı sorumluluklarını aksattığını, %23,4’ü oynamadığında huzursuz ve mutsuz hissettiğini "
             "bildiriyor [@tuik2024]. Bunlar tanı ölçütü değil, öz-bildirim maddeleridir; yine de görüşmede sorulacak soruları gösterir."),
            ("Yeni katman: sohbet botları",
             "ABD’de ergenlerin %64’ü bir yapay zekâ sohbet botu kullanmış; yaklaşık onda üçü her gün kullanıyor [@pew2025]. Bu başlık "
             "Oturum 10’da ayrıca ele alınıyor."),
            ("Sayıların çoğu öz-bildirim",
             "Kayıtlı kullanım ile öz-bildirim yalnızca orta düzeyde örtüşüyor; sorunlu kullanım ölçekleri kayıtlarla daha da zayıf "
             "ilişkili [@parry2021]. Küçük çocuklarda ebeveynlerin çoğu çocuğunun kullanımını ya az ya da fazla tahmin ediyor "
             "[@radesky2020]."),
        ],
        klinik=[
            "Süreyi sormadan önce cihazın kendi sayacını isteyin. Telefonun ekran süresi raporuna ergenle birlikte bakmak tahmin hatasını da pazarlığı da azaltır.",
            "‘Sosyal medya’ sorusunu platform platform sorun. YouTube’da video izlemek, anlık mesajlaşmak ve kısa video akışında gezinmek aynı deneyim değildir.",
            "Beklentinizi yaşa göre ayarlayın: 11 yaşından sonra yoğun kullanım istatistiksel olarak sıradandır. Sıradan olması zararsız olduğunu göstermez, tek başına patoloji de sayılmaz.",
            "Sıklığı da sorun: ‘Telefonuna ne kadar arayla bakıyorsun?’ sorusu, toplam süreden farklı bir şeyi, alışkanlık hâline gelmiş kontrolü yakalar.",
            "TR Türkiye’de 6–15 yaş çocukların %43,9’unun kendine ait telefonu var; ‘telefonu ne zaman alalım?’ sorusu çoğu aile için çoktan yanıtlanmış durumda. Görüşmeyi ‘almak ya da almamak’tan ‘nasıl kullanılacağına’ taşıyın [@tuik2024].",
            "TR TÜİK’e göre çocukların %34,4’ü ekran yüzünden daha az kitap okuduğunu, %33,3’ü daha az ders çalıştığını, %25,5’i ailesiyle daha az vakit geçirdiğini, %17,2’si daha az uyuduğunu kendisi söylüyor [@tuik2024]. Bu başlıklar aileyle ortak hedef belirlemek için hazır bir giriş sağlar.",
            "TR Ulusal veri 6–15 yaşı kapsıyor; 16–17 yaş için aynı ayrıntıda resmî veri yok. Lise çağındaki hastada bireysel öyküye daha çok yaslanmak gerekir.",
        ],
        kitaplar=[
            ("lewis", "Altıncı baskının yeni epidemiyoloji bölümü, hastalık sıklığını yalnızca ölçeklerle değil, toplumun kendini nasıl "
                      "tanımladığıyla birlikte ele alır ve sosyal medyanın tanı etiketlerinin yayılmasındaki rolüne ayrı yer verir. "
                      "Değerlendirme bölümünde medya kullanımı, gelişim öyküsünün olağan başlıklarından biri hâline gelmiştir [@lewis6]."),
            ("iacapap", "Değerlendirme bölümü çocukluğun kendine özgü bir kültür olduğunu, bu kültürün artık oyunlar ve ekranlarla "
                        "birlikte düşünülmesi gerektiğini vurgular [@iacapap2]."),
            ("rutter", "Yedinci baskıya eklenen yeni bölümlerden biri dijital teknolojinin değerlendirme ve tedavideki yerine ayrılmıştır "
                       "[@rutter7]. Ders kitaplarının üçü de konuyu artık ek bir merak alanı olarak değil, çekirdek içerik olarak ele alıyor."),
        ],
        tartisma=[
            ("‘Sosyal medya’ ölçülebilir bir maruziyet mi?",
             "TÜİK’in oranı YouTube’u içeriyor; Pew platformları ayrı ayrı soruyor; HBSC süreyi değil, sorunlu kullanım belirtilerini "
             "ölçüyor [@tuik2024] [@pew2025] [@hbsc2024]. Aynı sözcük üç farklı şeyi adlandırdığında ülkeler ve yıllar arasındaki "
             "karşılaştırmalar yanıltabilir. Kayıtlı veri kullanan çalışmalar hâlâ azınlıkta [@parry2021]."),
            ("Artış gerçek mi, ölçüm mü?",
             "Sorunlu kullanımın %7’den %11’e çıkışı pandemi dönemini kapsıyor [@hbsc2024]. Artışın ne kadarının kalıcı olduğu, ne kadarının "
             "o yılların olağanüstü koşullarını yansıttığı tek bir ölçümle söylenemez; izleyen araştırma turları bunu gösterecek."),
        ],
        sorular=[
            S("On üç yaşındaki Defne’nin annesi ‘Günde en fazla bir saat telefona bakıyor’ diyor; Defne omuz silkiyor. Görüşmenin bu noktasında en yararlı adım hangisidir?",
              ["Annenin bildirimini esas alıp konuyu kapatmak",
               "Defne’nin onayıyla telefonun ekran süresi raporuna birlikte bakmak",
               "Bir bağımlılık ölçeği verip kararı puana bırakmak",
               "Kullanımın az olduğunu varsayıp uyku öyküsüne geçmek"], 1,
              "Öz-bildirim ve ebeveyn bildirimi kayıtlı kullanımla yalnızca orta düzeyde örtüşür [@parry2021] [@radesky2020]. Cihazın kendi kaydına birlikte bakmak hem daha doğru veri verir hem de ergeni sürecin ortağı yapar. Ölçek puanı öykünün yerini tutmaz."),
            S("Bir okul toplantısında ‘TÜİK’e göre çocukların %66’sı sosyal medya bağımlısı’ deniyor. En doğru düzeltme hangisidir?",
              ["Oran doğrudur, ancak yalnızca 11–15 yaş için geçerlidir",
               "%66,1, sosyal medya kullanan 6–15 yaş çocukların oranıdır; kullanım bağımlılık anlamına gelmez ve bu oran YouTube’u da içerir",
               "TÜİK bağımlılık oranını %11 bulmuştur",
               "TÜİK yalnızca oyun süresini ölçmüştür"], 1,
              "TÜİK kullanım oranını bildirir, tanı koymaz [@tuik2024]. %11 değeri, 44 ülkeyi kapsayan HBSC araştırmasındaki sorunlu sosyal medya kullanımı oranıdır ve Türkiye’ye özgü değildir [@hbsc2024]. Ayrıntı için <a href=\"#/oturum-1/fikirler\">ana fikirler</a>."),
            S("HBSC verisinde sorunlu sosyal medya kullanımı kızlarda, sorunlu oyun riski erkeklerde daha sık. Bu örüntünün görüşmeye yansıması ne olmalıdır?",
              ["Erkeklerde sosyal medyayı, kızlarda oyunu sormaya gerek yoktur",
               "Her ergende ikisi de sorulur; olasılıkların farklı olduğu akılda tutulur",
               "Kızlarda tablo her zaman daha ağır seyreder",
               "Fark ölçüm hatasından ibarettir"], 1,
              "Oranlar farklıdır ama örtüşür: kızların %7’si sorunlu oyun riski taşır, erkeklerin %9’unda sorunlu sosyal medya kullanımı vardır [@hbsc2024]. Tarama sorularını cinsiyete göre daraltmak bu çocukları kaçırır."),
        ],
        akilda="Neredeyse herkes çevrimiçi; bu yüzden ‘kullanıyor mu?’ sorusu ayırt etmez. Ayırt eden; ne için kullandığı, neyin yerine geçtiği ve bırakabilip bırakamadığıdır.",
    ),
    # ------------------------------------------------------------------ 2
    dict(
        no=2, kesim="m", kisa="Ergen beyni ve tasarım",
        baslik="Ergen beyni ve tasarım: geç olgunlaşan fren, özenle tasarlanmış gaz",
        slogan="Ödüle ve akrana duyarlı bir beyin, dikkati tutmak üzere tasarlanmış bir ürünle karşılaşıyor.",
        bakis=("Ergenlikte ödül ve sosyal değerlendirme sistemleri erken, denetim sistemleri geç olgunlaşır. Platformların iş modeli "
               "ise kullanım süresini uzatmaya dayanır. Bu oturum iki tarafı birlikte ele alıyor: gelişimsel duyarlılık ne demek, "
               "‘bağımlılık yapıcı tasarım’ derken hangi özellikler kastediliyor ve nörogörüntüleme bulguları bunun ne kadarını gösteriyor?"),
        sorun=[
            "Ailelere ‘ergen beyni henüz gelişmedi’ derken neyi kastediyorsunuz: yapamaz mı, zorlanır mı, bağlama mı bağlı?",
            "Kendi telefonunuzda sizi en çok tutan özellik hangisi: bildirim, sonsuz akış, otomatik oynatma?",
            "Bir görüntüleme çalışması ‘fark’ bildirdiğinde bunu ‘hasar’ diye okumamak için hangi soruları sorarsınız?",
        ],
        fikirler=[
            ("Olgunlaşma takvimi eşit değil",
             "Ergenlikte ödüle ve sosyoduygusal bağlama duyarlılık artarken dürtü denetimi görece olgunlaşmamıştır; riskli davranıştaki "
             "artış bu dengesizlikle açıklanır [@casey2008]. On bir ülkeden 5227 kişilik bir çalışmada mantıksal akıl yürütme 16 yaş "
             "dolayında erişkin düzeyine ulaşırken, heyecanlı ve riskli durumlarda kendini tutabilme 18 yaşından sonra da gelişmeyi "
             "sürdürüyordu [@icenogle2019]. 101.457 kişinin MR verisinden çıkarılan büyüme eğrileri de beyin yapısındaki değişimin "
             "yaşam boyu sürdüğünü gösterir [@bethlehem2022]."),
            ("Beğeni, akran etkisinin sayıya dökülmüş hâlidir",
             "Instagram’a benzeyen bir görev sırasında fMRI çekilen ergenler, çok beğeni almış gibi gösterilen fotoğrafları daha çok "
             "beğendi; bu fotoğraflara bakarken ödülle ilişkili bölgelerde etkinlik arttı, riskli davranış içeren fotoğraflarda ise "
             "bilişsel kontrol ağının etkinliği azaldı [@sherman2016]."),
            ("Belirsiz ödül kesin ödülden daha çok bağlar",
             "Maymunlarda dopamin nöronlarının, ödül olasılığı yarı yarıya olduğunda, yani belirsizlik en yüksekken, ödül anına dek "
             "giderek artan bir yanıt verdiği gösterildi [@fiorillo2003]. Akışı yenilemek ya da bildirim beklemek aynı ‘belki’ye "
             "dayanır; uygulama tasarımı yazınında bu benzerlik açıkça tartışılır [@montag2019]."),
            ("Tutma özellikleri sayılabilir",
             "Avrupa Komisyonu 2026’da TikTok ve Meta hakkındaki ön bulgularında dört özelliği adıyla andı: sonsuz kaydırma, otomatik "
             "oynatma, anlık bildirimler ve kişiye göre ayarlanan öneri sistemi [@ab2026tiktok] [@ab2026meta]. ‘Bağımlılık yapıcı "
             "tasarım’ soyut bir suçlama değil, tek tek açılıp kapatılabilen ayarların toplamıdır."),
            ("Alışkanlık beyin gelişimiyle birlikte ilerler; yönü belirsiz",
             "169 ergenin üç yıl izlendiği bir fMRI çalışmasında, 12 yaşında sosyal medyayı alışkanlık hâlinde kontrol edenlerle "
             "etmeyenlerin sosyal ödül ve ceza beklentisine nöral duyarlılığı zıt yönlerde değişti: ilk grupta arttı, ikincide azaldı "
             "[@maza2023]. Çalışma gözlemseldir; kontrol alışkanlığının mı beyni değiştirdiği, yoksa farklı gelişen beyinlerin mi daha "
             "çok kontrol ettiği söylenemez."),
            ("‘Beyin çürümesi’ bir mecazdır",
             "71 çalışmayı kapsayan bir meta-analizde kısa video kullanımı dikkatle (r=−0,38) ve ketleyici denetimle (r=−0,41) orta "
             "düzeyde olumsuz ilişkiliydi [@nguyen2025]. Çalışmaların çoğu kesitsel olduğundan ters yön, yani dikkati zaten zayıf "
             "olanların kısa videoya yönelmesi dışlanmış değildir. Beyin çürümez; neyi tekrar ederse onda ustalaşır. Soru, hangi "
             "becerinin tekrar edildiğidir."),
            ("Beklenti algıyı bile biçimler",
             "Bir hastanede çalışan 169 sağlık çalışanının %68’i, cihazı titreşmediği hâlde titreşim hissettiğini bildirdi [@rothberg2010]. "
             "Erişkinlerde ve tıp ortamında yapılmış bu küçük çalışma, bildirim beklentisinin ne kadar kolay öğrenildiğini gösterir."),
        ],
        klinik=[
            "Aileye ‘irade zayıflığı’ yerine dengesiz bir yarış anlatın: bir yanda geç olgunlaşan fren, öte yanda çok sayıda mühendisin tasarladığı gaz pedalı. Sorumluluğu çocuktan ürüne kaydırmak savunmayı azaltır.",
            "Müdahaleyi tasarım özelliğine yöneltin. Bildirimleri kapatmak ya da günde birkaç kez toplu almak, otomatik oynatmayı kapatmak süre pazarlığından daha uygulanabilir hedeflerdir; erişkinlerle yapılan bir saha deneyinde bildirimleri toplu almak dikkat ve duygudurumu iyileştirdi [@fitz2019].",
            "Ergenin bilişsel kapasitesini küçümsemeyin: 16 yaşındaki bir genç riskleri bilir, zorlandığı yer heyecanlı olduğu ve akranlarının izlediği anlardır [@icenogle2019]. Kuralları sakin bir zamanda birlikte yazın.",
            "Görüntüleme haberlerini aileye aktarırken ‘ilişki’, ‘fark’ ve ‘hasar’ sözcüklerini ayırın. Eldeki çalışmalar birlikte değişimi gösteriyor; sosyal medyanın ergen beyninde kalıcı hasar yaptığını gösteren bir çalışma yok [@maza2023].",
            "Kendi telefonunuzu görüşme odasında görünmez kılın. Tasarımın gücünü anlattığınız görüşmede bildirime bakmak, söylediklerinizi boşa çıkarır.",
            "TR Türkiye’de 1 Kasım 2026’dan beri 15–17 yaş hesaplarında içeriğin kaydırma ile ya da kendiliğinden ardışık sunulması, canlı yayın açma ve davranışa göre kişiselleştirme yasak [@yonetmelik2026]. Bu oturumda sayılan tasarım özelliklerinin bir bölümü doğrudan mevzuatın hedefi; ayrıntı Oturum 11’de.",
            "TR TÜİK verisinde 11–15 yaş telefon kullanıcılarının %42,8’i telefonunu en az yarım saatte bir kontrol ediyor [@tuik2024]. ‘Alışkanlık hâlinde kontrol’ kavramının yerel karşılığı budur.",
        ],
        kitaplar=[
            ("williams", "İkna üzerine bölümde yazarlar en başarılı ikna sistemlerinin birkaç yöntemi birlikte kullandığını söyler ve "
                         "örnekleri arasında reklamcılıkla birlikte bilgisayar oyunlarını sayar [@williams2025]. Ürünü bir ikna sistemi "
                         "olarak görmek, çocuğu suçlamadan konuşmanın yolunu açar."),
            ("williams", "Aynı kitap DEHB’de ‘hiperfokus’ iddiasına mesafeli durur ve bu izlenimin çoğu kez oyun seven çocuklardan "
                         "doğduğunu düşündürür [@williams2025]. Ekranda saatlerce kalabilmek dikkatin sağlam olduğunu göstermez."),
            ("iacapap", "DEHB bölümü aynı noktayı klinik bir kural olarak yazar: bilgisayar oyununa odaklanabilmek DEHB’yi dışlamaz; "
                        "güdülenme ve görevin çekiciliği belirtilerin görünürlüğünü değiştirir [@iacapap2]."),
            ("notlar", "Davranışın biyolojisi notlarımızda dopaminin ödülün kendisinden çok beklentisini ve belirsizliğini kodladığı "
                       "fikri ayrıntılı işlenmişti [@fiorillo2003]. ‘Belki’ sözcüğünün gücü burada da iş başında."),
        ],
        tartisma=[
            ("‘Bağımlılık’ sözcüğü yerinde mi?",
             "Düzenleyici kurumlar ‘bağımlılık yapıcı tasarım’ ifadesini kullanıyor [@ab2026tiktok]. ICD-11 ise davranışsal bağımlılık "
             "olarak yalnızca kumar ve oyun bozukluğunu tanımlar; sosyal medya için bir tanı yoktur [@icd11]. Oyun bozukluğu tanısı "
             "önerildiğinde bir grup araştırmacı, gündelik bir etkinliğin hastalık sayılmasının yanlış pozitif tanılara ve damgalamaya "
             "yol açabileceği uyarısını yapmıştı [@aarseth2017]. Güncel bir derleme davranışsal bağımlılıkları keskin eşiklerle değil, "
             "bir süreklilik içinde ele almayı öneriyor [@park2026]."),
            ("Görüntüleme bulguları ne söylüyor, ne söylemiyor?",
             "Maza ve arkadaşlarının çalışması tek bölgeden 169 ergeni ve öz-bildirimle ölçülen kontrol sıklığını içeriyor [@maza2023]. "
             "ABCD kohortunda ekran süresi ile DEHB belirtileri ve kortikal kalınlık arasında bildirilen ilişkiler çok küçük (β≈0,03) "
             "[@shou2025]. Küçük ve gözlemsel ilişkilerden ‘sosyal medya beyni değiştiriyor’ sonucuna geçmek, verinin taşıyabileceğinden "
             "ağır bir yüktür."),
            ("Duyarlılık yaşla mı, hazır oluşla mı ölçülmeli?",
             "Boylamsal veride sosyal medya kullanımının yaşam doyumuyla ilişkisi kızlarda 11–13, erkeklerde 14–15 yaşlarında ve her iki "
             "cinsiyette 19 yaşında daha belirgin [@orben2022]. Mevzuat ise tek bir yaş eşiği kullanıyor [@kanun7578]. 2026’da "
             "yayımlanan bir görüş yazısı, ölçüt olarak yaş yerine gelişimsel hazır oluşu öneriyor [@zhangq2026]. Klinikte ikisi de "
             "gerekir: yasal eşik değişmez, hazır oluş çocuktan çocuğa değişir."),
        ],
        sorular=[
            S("On dört yaşındaki Kerem ‘Sınav haftasında oynamamam gerektiğini biliyorum, ama arkadaşlar çevrimiçi olunca duramıyorum’ diyor. Bu tabloyu en iyi hangi gelişimsel ilke açıklar?",
              ["Riskleri anlayacak bilişsel kapasitesi henüz yoktur",
               "Bilişsel kapasitesi yeterlidir; zorlandığı yer akran ve heyecan içeren bağlamlarda öz-denetimdir",
               "Kurala bilerek karşı gelmektedir",
               "Zihinsel yetersizlik düşünülmelidir"], 1,
              "Mantıksal akıl yürütme ergenliğin ortasında erişkin düzeyine yaklaşır; heyecanlı ve akranların bulunduğu durumlarda kendini tutabilme daha geç olgunlaşır [@icenogle2019] [@casey2008]. Bu yüzden kural koymak yetmez, kuralın çiğneneceği anın koşullarını değiştirmek gerekir."),
            S("Bir anne ‘Sosyal medya çocukların beynini değiştiriyormuş, MR’da çıkmış’ diyor. En doğru yanıt hangisidir?",
              ["Evet, kalıcı hasar kanıtlandı",
               "Çalışmalar kullanım alışkanlığı ile beyin gelişimi arasında küçük ilişkiler bildiriyor; bunlar gözlemseldir, hangisinin neden olduğu bilinmiyor ve kalıcı hasar gösterilmiş değil",
               "Emin olmak için çocuğa MR çekilmesi gerekir",
               "Bu konuda hiç araştırma yapılmadı"], 1,
              "En çok anılan çalışma 169 ergende, kontrol alışkanlığı olanlarla olmayanların nöral duyarlılığının farklı seyrettiğini gösterdi; neden-sonuç yönü belirlenemedi [@maza2023]. Bireysel bir çocuk için görüntülemenin tanısal değeri yoktur."),
            S("On beş yaşındaki Elif’in ailesi günlük süreyi bir saatle sınırlamayı denedi; her akşam kavga çıktı. Tasarım bilgisine dayanan ilk öneri hangisi olabilir?",
              ["Telefonu tümüyle elinden almak",
               "Bildirimleri kapatıp günde birkaç kez toplu bakmayı ve otomatik oynatmayı kapatmayı birlikte denemek; iki hafta sonra değerlendirmek",
               "Süre sınırını yarım saate indirmek",
               "Kendiliğinden geçmesini beklemek"], 1,
              "Süre sınırı her gün yeniden pazarlık gerektirir; ayar değişikliği bir kez yapılır. Bildirimleri toplu almanın yararı erişkinlerde bir saha deneyinde gösterildi [@fitz2019]; ergenlere uyarlanması akla yatkın, ancak bu yaş grubunda sınanmış değil. Öneriyi bir deneme olarak sunun."),
        ],
        akilda="Sorun çocuğun iradesinde aranırsa çatışma büyür. Tasarımda aranırsa değiştirilebilecek ayarlar bulunur: bildirim, otomatik oynatma, sonsuz akış.",
    ),
    # ------------------------------------------------------------------ 3
    dict(
        no=3, kesim="k", kisa="Kaygılı kuşak mı, panik mi?",
        baslik="Kaygılı kuşak mı, ahlaki panik mi? Büyük tartışmayı okumak",
        slogan="İki taraf da aynı verilere bakıyor. Ayrıldıkları yer, küçük bir ilişkinin nasıl yorumlanacağı.",
        bakis=("Haidt, 2010’ların başında çocukluğun ‘yeniden kablolandığını’ ve bunun ergen ruh sağlığındaki bozulmanın başlıca "
               "nedeni olduğunu savunuyor [@haidt2024]. Odgers ise eldeki kanıtın bu kadar güçlü bir nedensel iddiayı taşımadığını, "
               "asıl nedenlerin başka yerde aranması gerektiğini söylüyor [@odgers2024]. Bu oturum iki tezin dayandığı kanıt türlerini "
               "tek tek ayırıyor."),
        sorun=[
            "Bu tartışmada hangi tarafa yakınsınız ve bu yakınlık neye dayanıyor: kendi hastalarınıza mı, zaman eğilimlerine mi, deneylere mi?",
            "r=0,10 büyüklüğünde bir ilişki sizce klinikte önemli mi? Toplum düzeyinde önemli mi?",
            "‘Nedensellik kanıtlanmadı’ ile ‘zararsız’ arasındaki farkı bir aileye nasıl anlatırsınız?",
        ],
        fikirler=[
            ("Kesitsel ilişki var, ama küçük",
             "Üç büyük veri setinde (toplam 355.358 ergen) dijital teknoloji kullanımı iyi oluştaki değişkenliğin en çok %0,4’ünü "
             "açıkladı; yazarlar aynı verilerde patates yemenin benzer büyüklükte bir ilişki gösterdiğini not etti [@orben2019]. 102 "
             "meta-analizi birleştiren şemsiye derlemede sosyal medya ile depresyon arasındaki ilişki r=0,12 idi ve meta-analizlerin "
             "95’inde yanlılık riski orta ya da yüksekti [@sanders2024]. Derlemelerin çoğu ilişkiyi ‘zayıf’ ya da ‘tutarsız’ diye "
             "niteliyor [@valkenburg2022]."),
            ("Aynı küçük sayı iki türlü okunuyor",
             "Üç anketin (221.096 ergen) yeniden analizinde, günde beş saat ve üzeri kullananlar bir saatten az kullananlara göre "
             "mutsuzluk, düşük iyi oluş ve intihar risk etkenlerini %48 ile %171 arasında daha sık bildirdi; yazarlar ‘açıklanan "
             "varyans’ ölçüsünün pratik etkiyi küçük gösterdiğini savundu [@twenge2019]. İki okumayı kendi gözünüzle karşılaştırmak "
             "için <a href=\"#/etki\">etki büyüklüğü çeviriciyi</a> kullanabilirsiniz."),
            ("Boylamsal ilişki daha da küçük",
             "Yalnızca boylamsal ve deneysel çalışmaları alan 2026 tarihli bir meta-analizde (10–24 yaş, 37 çalışma) sosyal medya "
             "kullanımı depresyonla r=0,08, kaygıyla r=0,09 ilişkiliydi; yazarlara göre bu büyüklükte bir ilişkinin gençlik ruh sağlığı "
             "krizini açıklaması olası değil [@peachey2026]. ABCD kohortunda kişi-içi analizde kullanımı kendi ortalamasının üstüne "
             "çıkan çocukta ertesi yıl depresif belirtiler hafifçe daha yüksekti (β 0,07–0,09); ters yön saptanmadı [@nagata2025]. "
             "Britanya panelinde ise etkiler küçük, karşılıklı ve cinsiyete özgüydü [@orben2019pnas]."),
            ("Doğal deney ve randomize çalışmalar bir etki gösteriyor; çoğu erişkinde",
             "Facebook’un ABD üniversitelerine aşamalı girişini doğal deney olarak kullanan çalışma, platformun geldiği kampüslerde "
             "öğrencilerin ruh sağlığının kötüleştiğini buldu; yazarlar bunu olumsuz sosyal karşılaştırmaya bağladı [@braghieri2022]. "
             "Dört hafta Facebook’u kapatan erişkinlerde öznel iyi oluş arttı [@allcott2020]. Bir haftalık ara veren 154 erişkinde "
             "(ortalama yaş 29,6) iyi oluş, depresyon ve kaygı puanları kontrol grubuna göre iyileşti [@lambert2022]."),
            ("Deneylerin toplamı sıfırdan ayırt edilemiyor",
             "Sosyal medyadan uzak durma deneylerini birleştiren meta-analitik derlemede nedensel etkiye ilişkin kanıt istatistiksel "
             "olarak sıfırdan farksızdı; çalışmalar arası heterojenlik çok yüksekti ve katılımcıların araştırmacının beklentisini "
             "bilmesi başlı başına bir sorundu. Makale için sonradan bir düzeltme notu yayımlandı [@ferguson2025]."),
            ("Zaman eğilimi tek başına kanıt değil",
             "PISA verisinde okulda yalnızlık 2012–2018 arasında 37 ülkenin 36’sında arttı; akıllı telefon erişimi ve internet "
             "kullanımının yüksek olduğu yerlerde yalnızlık da yüksekti [@twenge2021]. Öte yandan teknoloji kullanımı ile ruh sağlığı "
             "arasındaki ilişkinin yıllar içinde güçlendiğine dair kanıt az [@vuorre2021] ve 72 ülkede Facebook’un yaygınlaşması iyi "
             "oluştaki bir düşüşle birlikte gitmedi [@vuorre2023]."),
            ("Ortak nedenler: genetik yatkınlık",
             "Norveç’te 23.790 ergenin verisinde hem günde 3–4 saat ve üzeri ekran kullanımı hem de çok az sosyal medya kullanımı "
             "psikiyatrik tanılarla ilişkiliydi; ilişkinin önemli bir bölümü ortak genetik etkenlere atfedilebildi [@frei2025]."),
            ("Kurumlar ne dedi?",
             "ABD Ulusal Akademileri’nin uzlaşı raporu, yazının sosyal medyanın toplum düzeyinde ergen sağlığını değiştirdiği sonucunu "
             "desteklemediğini; etkilerin küçük olduğunu ve kişiden kişiye değiştiğini bildirdi. Aynı rapor tasarım standartları, veri "
             "şeffaflığı, medya okuryazarlığı eğitimi ve hekim eğitimi önerdi [@nasem2024]. *Lancet*’in 2026 dizisi dijital medyanın "
             "olumsuz sonuçlarla daha tutarlı biçimde ilişkili olduğunu, nedensel temel belirsiz olsa da ihtiyatlı ve yapısal bir "
             "yanıt gerektiğini savundu [@holly2026]. Amerikan Pediatri Akademisi’nin 2026 politika bildirisi, konunun yalnızca ekran "
             "süresi sınırlarıyla ele alınamayacağını vurguladı [@aap2026]."),
        ],
        klinik=[
            "Aileye iki cümleyi birlikte söyleyin: ‘Toplum düzeyinde etki küçük görünüyor’ ve ‘Sizin çocuğunuz ortalama olmayabilir.’ Klinik karar ortalamaya göre değil, bu çocuğun öyküsüne göre verilir.",
            "Bir çalışmayı aktarırken tasarımını da söyleyin: kesitsel mi, boylamsal mı, deney mi; ergenlerle mi, üniversite öğrencileriyle mi yapılmış. Aileler başlığı duyar, tasarımı duymaz.",
            "Kendi yanlılığınızı hesaba katın: polikliniğe gelen çocuklar, sosyal medyayı sorunsuz kullanan çoğunluğu temsil etmez. Bu, klinisyeni karamsar yöne çeker.",
            "Belirsizlik, düşük maliyetli önlemleri ertelemek için gerekçe değildir. Telefonun gece odadan çıkması ya da bildirimlerin kapatılması için nedenselliğin kesinleşmesini beklemek gerekmez.",
            "‘Kanıt yok’ ile ‘etki yok’u ayırın. Ergenlerde iyi tasarlanmış randomize çalışma azdır; bu, sorunun yanıtlandığı değil, henüz iyi sorulmadığı anlamına gelir.",
            "TR Türkiye’de tartışma 2026’da mevzuata dönüştü; aileler artık ‘zararlı mı?’ yerine ‘yasak mı?’ diye soruyor. Yasal yaş sınırı ile klinik öneriyi ayrı tutun: kanun 15 yaşı çizdi, sizin öneriniz çocuğa göre değişir [@kanun7578].",
            "TR Türkiye’den yayınların çoğu kesitsel. Ülkedeki sorunlu internet kullanımı çalışmalarını birleştiren 2026 meta-analizi yalnızca kesitsel çalışmaları içerebildi; yazarları bulguların nedensellik göstermediğini açıkça belirtti [@kayir2026].",
        ],
        kitaplar=[
            ("haidt", "Kitabın çekirdek savı, çocukluğun oyun temelli olmaktan çıkıp telefon temelli hâle geldiği ve bunun ergen ruh "
                      "sağlığındaki bozulmanın ana nedeni olduğudur. Yazar dört toplumsal norm önerir: liseden önce akıllı telefon "
                      "olmaması, 16 yaşından önce sosyal medya olmaması, telefonsuz okul, daha çok bağımsızlık ve serbest oyun "
                      "[@haidt2024]. Bu bir tez kitabıdır; tezin sınanması bu oturumdaki çalışmaların işidir."),
            ("lewis", "Epidemiyoloji bölümü tartışmayı zarar-yarar ikiliği üzerinden değil, sosyal medyanın hastalık tanımını ve "
                      "kendini tanımlamayı nasıl değiştirdiği üzerinden kurar; olumlu ve olumsuz etkileri birlikte anar [@lewis6]."),
            ("iacapap", "Gelişim bölümü, dijital çağın tipik gelişim üzerindeki etkisine ilişkin kanıtı henüz kesin bulmaz [@iacapap2]."),
            ("rutter", "Kitabın genel yöntem dersi burada da geçerlidir: tek bir kesite değil, zaman içindeki seyre bakmak [@rutter7]. "
                       "Dijital teknolojiye ayrılan yeni bölüm notlarımızda henüz işlenmedi."),
        ],
        tartisma=[
            ("Küçük etki önemsiz midir?",
             "r=0,10 büyüklüğünde bir ilişki tek bir çocukta ayırt edilemez. Savunucularına göre nüfusun tamamında küçük bir kayma, "
             "uç dilimlerdeki çocuk sayısını belirgin biçimde değiştirebilir [@twenge2019] [@holly2026]. Karşı görüşe göre küçük "
             "ilişkiler ölçüm hatasına ve ortak nedenlere en açık olanlardır; bu büyüklükte bir ilişki üzerine politika kurmak erken "
             "olur [@orben2019]. İki görüş de aynı sayıya bakıyor."),
            ("İki 2026 meta-analizi, iki farklı sonuç",
             "Biri boylamsal ve deneysel çalışmaları alıp r=0,08 buldu [@peachey2026]. Diğeri on iki çalışmayı birleştirip r=0,31 "
             "bildirdi; heterojenlik çok yüksekti (I²≈%94) ve en güçlü ilişki ilkokul çağındaydı [@han2026]. Aynı yıl yayımlanan iki "
             "meta-analizin bu kadar ayrışması, sonucu çoğu zaman dahil etme ölçütlerinin ve tasarımın belirlediğini gösterir. Bir "
             "meta-analizi aktarırken hangi çalışmaları içerdiğini de söylemek gerekir."),
            ("İhtiyat ilkesi mi, kanıt eşiği mi?",
             "Bir yanda, nedensellik kesinleşmeden geniş yasakların ‘belirsizlik karşısında bir kumar’ olduğu görüşü var [@orben2026]. "
             "Öte yanda, çocuklar söz konusu olduğunda kesinliği beklemenin de bir tercih olduğu ve ihtiyatlı, yapısal önlemlerin "
             "savunulabileceği görüşü [@holly2026]. Klinikteki karşılığı daha yalın: bireysel düzeyde zararı düşük, yararı olası "
             "önlemler için yüksek bir kanıt eşiği gerekmez."),
            ("Hiç kullanmamak da risk mi?",
             "100.991 Avustralyalı öğrencide iyi oluşla ilişki U biçimliydi: en yüksek kullanımda düşük iyi oluş olasılığı belirgin "
             "biçimde artmıştı (7–9. sınıf kızlarda OR 3,13), ama hiç kullanmayanlarda da, özellikle geç ergenlikte, yüksekti "
             "(10–12. sınıf erkeklerde OR 3,00) [@singh2026]. Benzer bir eğri İngiltere’de 120.115 ergende gösterilmişti "
             "[@przybylski2017]. Hiç kullanmayan grup rastgele oluşmaz: dışlanma, kısıtlayıcı aile ortamı ya da başka güçlükler bu "
             "grupta daha sık olabilir. Bulgu, ölçülü kullanımın koruyucu olduğunu kanıtlamaz; iki ucun da öyküde sorulmaya değer "
             "olduğunu gösterir."),
        ],
        sorular=[
            S("Bir gazete ‘Sosyal medya depresyonu ikiye katlıyor’ başlığını, günde beş saatten fazla kullananlarla bir saatten az kullananları karşılaştıran kesitsel bir ankete dayandırıyor. Bu veriden çıkarılamayacak sonuç hangisidir?",
              ["Yoğun kullanıcılar arasında depresif belirtiler daha sık bildirilmiştir",
               "Kullanımı azaltmak depresyon riskini yarıya indirir",
               "İlişkinin yönü bu tasarımla belirlenemez",
               "Uç grupların karşılaştırılması farkı büyük gösterir"], 1,
              "Kesitsel veri birlikteliği gösterir; azaltmanın etkisini ancak deney gösterebilir. Depresif ergenin daha çok çevrimiçi kalması da aynı tabloyu üretir [@twenge2019] [@orben2019]. Uzak durma deneylerinin toplam sonucu ise sıfırdan ayırt edilemiyor [@ferguson2025]."),
            S("On altı yaşındaki Zeynep’in annesi ‘Araştırmalar etkinin çok küçük olduğunu söylüyormuş, demek ki sorun yok’ diyor. Zeynep gece üçe kadar çevrimiçi; okul devamsızlığı başlamış. En uygun yanıt hangisidir?",
              ["Haklısınız, araştırmalar sorun olmadığını gösteriyor",
               "Ortalama etki küçük olabilir; ama Zeynep’te uyku ve okul etkilenmiş, karar bu bulgulara göre verilir",
               "Araştırmalar yanılıyor; sosyal medya herkese zararlıdır",
               "Önce ayrıntılı laboratuvar incelemesi gerekir"], 1,
              "Toplum ortalaması tek bir çocuğun durumunu öngörmez. Uyku kaybı ve işlev kaybı varsa, klinik karar ortalamadaki küçük etkiye değil, bu bulgulara dayanır."),
            S("Bir meta-analiz yalnızca boylamsal ve deneysel çalışmaları alıp r=0,08 buluyor; bir başkası farklı ölçütlerle r=0,31 bildiriyor. Farkın en olası açıklaması hangisidir?",
              ["Meta-analizlerden biri hesap hatası yapmıştır",
               "Dahil edilen çalışmaların tasarımı ve seçimi sonucu belirler; kesitsel verilerde ters nedensellik ve ortak nedenler ilişkiyi büyütür",
               "Sosyal medya 2026’da daha zararlı hâle gelmiştir",
               "Fark tümüyle rastlantısaldır"], 1,
              "İki çalışma da 2026’da yayımlandı [@peachey2026] [@han2026]. Meta-analiz bir yöntemdir, hakem değildir: içine ne konduğuna bakılmadan sonucu aktarılmamalı."),
        ],
        akilda="Toplum düzeyinde ilişki küçük, nedenselliği tartışmalı. Klinikte soru ‘sosyal medya zararlı mı?’ değil, ‘bu çocukta neyi, nasıl etkiliyor?’ olmalı.",
    ),
    # ------------------------------------------------------------------ 4
    dict(
        no=4, kesim="k", kisa="Kime, ne zaman, nasıl?",
        baslik="Kime, ne zaman, nasıl? Ortalamanın altındaki farklar",
        slogan="Kronometreye değil, kontrol kaybına bakın.",
        bakis=("Ortalama etkinin küçük olması herkesin aynı ölçüde etkilendiği anlamına gelmez. Bu oturum etkiyi değiştiren üç ekseni "
               "ele alıyor: kim (yatkınlık ve klinik durum), ne zaman (gelişimsel dönem) ve nasıl (süre mi, kullanım örüntüsü mü)."),
        sorun=[
            "Son ay gördüğünüz hangi hastada sosyal medya açıkça yardımcıydı, hangisinde zararlıydı? Aradaki fark neydi?",
            "‘Günde kaç saat?’ sorusundan sonra ne soruyorsunuz?",
            "On bir yaşındaki bir kız ile on altı yaşındaki bir erkek için aynı öneriyi mi veriyorsunuz?",
        ],
        fikirler=[
            ("Süre değil, örüntü",
             "ABCD kohortundan 4285 çocuğun dört yıllık izleminde yaklaşık üçte biri, 11 yaşından başlayarak sosyal medya ya da "
             "telefonda bağımlılık benzeri kullanımı giderek artan bir seyir gösterdi. Bu grupta intihar davranışı riski, düşük seyirli "
             "gruba göre yaklaşık iki kattı (sosyal medya için risk oranı 2,14). Başlangıçtaki toplam ekran süresi ise sonuçlarla "
             "ilişkili değildi [@xiao2025]."),
            ("Yoğun kullanım ile sorunlu kullanım ayrı şeyler",
             "29 ülkenin HBSC verisinde sorunlu kullanım her ülkede daha düşük iyi oluşla ilişkiliydi. Yoğun ama sorunsuz kullanım ise "
             "ülkeye göre değişti; yoğun kullanımın yaygın olduğu ülkelerde yoğun kullanıcılar daha çok arkadaş desteği ve daha yüksek "
             "yaşam doyumu bildirdi [@boer2020]."),
            ("Aynı kullanım, farklı çocukta farklı etki",
             "Ergenlerin bir hafta boyunca günde altı kez anlık duygudurum bildirdiği çalışmada, sosyal medyada gezindikten sonra "
             "katılımcıların %46’sı kendini daha iyi, %10’u daha kötü hissetti; %44’ünde değişiklik olmadı [@beyens2020]."),
            ("Gelişimsel pencereler",
             "Britanya verisinde (boylamsal 17.409 kişi) yüksek sosyal medya kullanımının bir yıl sonraki yaşam doyumunu düşürdüğü "
             "dönemler kızlarda 11–13, erkeklerde 14–15 yaşlar ve her iki cinsiyette 19 yaştı [@orben2022]."),
            ("Erken sahiplik bir işaret",
             "10.588 çocukta 12 yaşında akıllı telefon sahibi olmak depresyon (OR 1,31), obezite (OR 1,40) ve yetersiz uyku (OR 1,62) "
             "ile ilişkiliydi. 12 yaşında telefonu olmayıp izleyen yıl edinenlerde 13 yaşında klinik düzeyde psikopatoloji olasılığı, "
             "edinmeyenlere göre daha yüksekti (OR 1,57) [@barzilay2026]. Çalışma gözlemseldir."),
            ("Ruhsal sorunu olan ergen farklı kullanıyor",
             "Klinik değerlendirme içeren Britanya örnekleminde (11–19 yaş, 3340 kişi) ruhsal bozukluğu olan ergenler sosyal medyada "
             "daha çok zaman geçiriyor ve çevrimiçi arkadaş sayısından daha az memnun kalıyordu. İçselleştirme bozukluğu olanlar "
             "kendilerini başkalarıyla daha çok karşılaştırıyor, aldıkları geri bildirimden duygudurumları daha çok etkileniyordu "
             "[@fassi2025]. Yine de bu alandaki çalışmaların yalnızca %11’i klinik örneklemle yapılmış [@fassi2024]."),
            ("Kızlarda ilişki daha güçlü; yol çoğu kez dolaylı",
             "On dört yaşındaki 10.904 ergende günde beş saat ve üzeri kullanım, kızlarda depresif belirti puanında %50, erkeklerde %35 "
             "artışla birlikteydi [@kelly2018]. İngiltere’deki boylamsal veride kızlarda çok sık kullanımın ruhsal sıkıntıyla ilişkisinin "
             "yaklaşık %58’i siber zorbalık, yetersiz uyku ve azalmış fiziksel etkinlik üzerinden açıklanıyordu [@viner2019]."),
            ("Yararlar da gerçek",
             "Ulusal Akademiler raporu yararları da sıralar: arkadaş ve aileyle bağlantı; LGBTQ+ gençler, ağır hastalıkla ya da yasla "
             "baş edenler için güvenli alan ve destek; eğitim kaynakları; ilgi alanlarının gelişmesi [@nasem2024]. İçerik üreticileriyle "
             "kurulan tek yönlü bağlar da iki yönlüdür: 17 çalışmalık meta-analizde hem iyi oluşla hem sorunlu kullanımla ilişkili "
             "bulundu [@li2026p]."),
        ],
        klinik=[
            "Süreyi sorun, ama orada durmayın. Dört soru ekleyin: Planladığından uzun sürüyor mu? Bırakmayı denediğinde ne oluyor? Uyku, okul ya da arkadaşlık bundan etkilendi mi? Kötü hissettiğinde ilk gittiği yer orası mı?",
            "İçselleştirme sorunu olan ergende karşılaştırmayı ve geri bildirime duyarlılığı ayrıca sorun: ‘Paylaştıktan sonra kaç kez bakıyorsun? Beklediğinden az tepki gelirse ne oluyor?’ [@fassi2025].",
            "11–13 yaşındaki kızlarda ve 14–15 yaşındaki erkeklerde kullanımdaki hızlı artışı önemseyin; boylamsal veride bu yaşlar daha duyarlı görünüyor [@orben2022].",
            "Hiç kullanmayan ergeni de sorun: kendi tercihi mi, yasak mı, dışlanma mı? Akran çevresi büyük ölçüde çevrimiçi olan bir ergende kopukluk ayrı bir risk olabilir [@singh2026].",
            "Çevrimiçi yararı haritalayın: destek grubu, ilgi alanı topluluğu, uzakta yaşayan akraba. Plan, yararlı kullanımı koruyacak biçimde yazılmalı.",
            "TR Türkiye’de bir çocuk psikiyatrisi polikliniğine başvuran 12–18 yaş ergenlerde internet bağımlılığı sıklığı %24,1, hiç psikiyatri başvurusu olmayan akranlarında %8,8 bulundu (toplam 310 ergen) [@yar2019]. Klinik örneklemde sorunlu kullanım istisna değil, sık eşlik eden bir tablodur.",
            "TR Ülkedeki çalışmaları birleştiren meta-analizde cinsiyet farkı küçüktü ve yıllar içinde daralıyordu; aile geliriyle ilişki anlamlı değildi [@kayir2026]. ‘Erkek çocuk sorunu’ ya da ‘yoksul aile sorunu’ kalıpları veriyle desteklenmiyor.",
        ],
        kitaplar=[
            ("lewis", "Azınlık gençliği bölümü çevrimiçi ortamın herkes için aynı olmadığını hatırlatır. Kitabın aktardığı günlük "
                      "çalışmasında Siyah ergenler günde ortalama beşten fazla ırk ayrımcılığı deneyimi bildirmiş, çevrimiçi "
                      "deneyimler çevrimdışı olanlardan sık çıkmıştı [@lewis6] [@english2020]. ‘Kim?’ sorusu kimliği de içerir."),
            ("williams", "Yazarlar geç ergenlerin sorumluluklardan çekilip oyuna yönelmesini hem klinik hem etik açıdan zor bir durum "
                         "olarak anar. Formülasyon örneklerinde ergenin kısa vadeli isteği ile ailenin uzun vadeli kaygısı aynı "
                         "tabloya yazılır; çözüm ikisinin birlikte görülmesiyle başlar [@williams2025]."),
            ("iacapap", "Değerlendirme bölümü gelişimin, büyüme eğrisi gibi zaman içinde kaydedilmesini önerir [@iacapap2]. Aynı "
                        "mantıkla, tek bir ölçüm yerine kullanımın seyri izlendiğinde belirtiyle hangisinin önce başladığı görülür."),
        ],
        tartisma=[
            ("‘Bağımlılık benzeri kullanım’ güvenilir ölçülüyor mu?",
             "Xiao ve arkadaşlarının ölçütleri çocukların kendi bildirimine dayanıyor [@xiao2025]; sorunlu kullanım ölçekleri kayıtlı "
             "kullanımla zayıf ilişkili [@parry2021]. Buna karşın bu ölçümün toplam süreden bağımsız olarak sonucu öngörmesi, süreden "
             "farklı bir şeyi yakaladığını düşündürüyor. ICD-11’de sosyal medya için bir tanı bulunmadığından eşik değerler uzlaşıya "
             "değil, araştırma ölçeklerine dayanıyor [@icd11]."),
            ("Erken telefon: neden mi, gösterge mi?",
             "Barzilay ve arkadaşları ebeveyn izlemi, sosyoekonomik durum ve başka cihazların varlığı için düzeltme yaptı; yine de "
             "telefonu erken alan ailelerle almayan aileler ölçülmeyen yönlerden farklı olabilir [@barzilay2026]. Randomize bir çalışma "
             "yok ve olması da güç. ‘Liseden önce akıllı telefon olmasın’ önerisi bu tür gözlemsel verilere dayanıyor [@haidt2024]."),
            ("Duyarlı pencereler politika için yeterli mi?",
             "Pencereler cinsiyete göre farklı yaşlara düşüyor ve etki büyüklükleri küçük [@orben2022]. Tek bir yasal yaş bu ayrıntıyı "
             "taşıyamaz. Yaş yerine gelişimsel hazır oluşu ölçüt almayı önerenler var [@zhangq2026]; ancak hazır oluşun nasıl "
             "ölçüleceği henüz belirsiz."),
        ],
        sorular=[
            S("İki ergen de günde yaklaşık dört saat sosyal medya kullanıyor. Aras planladığı sürede bırakabiliyor; uykusu ve dersleri yerinde. Duru bırakmayı deneyince huzursuzlanıyor, gece gizlice sürdürüyor, sabah okula gidemiyor. Güncel kohort verisine göre hangisi daha risklidir?",
              ["İkisi eşit risk taşır; süre aynıdır",
               "Duru; risk süreden çok bağımlılık benzeri kullanım örüntüsüyle ilişkilidir",
               "Aras; sorunu gizlemektedir",
               "İkisi de risk taşımaz; dört saat ortalamadır"], 1,
              "ABCD kohortunda toplam ekran süresi sonuçlarla ilişkili bulunmadı; bağımlılık benzeri kullanımı artan ergenlerde intihar davranışı riski yaklaşık iki kattı [@xiao2025]. Duru’da üç bileşen bir arada: kontrol kaybı, bırakınca huzursuzluk ve işlev kaybı."),
            S("On iki yaşındaki Ece’nin ailesi ona akıllı telefon almayı düşünüyor ve ‘Araştırmalar ne diyor?’ diye soruyor. En dengeli özet hangisidir?",
              ["12 yaşında telefon depresyona neden olur",
               "Büyük bir kohortta 12 yaşında telefon sahipliği yetersiz uyku ve depresyonla ilişkili bulundu; çalışma gözlemsel olduğundan nedensellik göstermez, ama uyku kurallarını baştan koymak için iyi bir gerekçedir",
               "Araştırmalar hiçbir ilişki bulmadı",
               "Telefon 16 yaşından önce yasaktır"], 1,
              "En güçlü ilişki yetersiz uykuyla (OR 1,62) [@barzilay2026]. Türkiye’de yasal yaş sınırı telefon sahipliği için değil, sosyal ağ hesabı için getirildi [@kanun7578]. Öneriyi ‘almayın’ yerine ‘hangi kurallarla?’ sorusuna çevirin."),
            S("Sosyal kaygısı olan 15 yaşındaki Mert ‘Arkadaşlarımın hepsi çevrimiçi; orada daha rahat konuşuyorum’ diyor. Ailesi bütün hesaplarını kapatmak istiyor. En uygun yaklaşım hangisidir?",
              ["Kapatmayı desteklemek; çevrimiçi iletişim kaçınmayı pekiştirir",
               "Çevrimiçi bağlantının işlevini değerlendirmek; yararlı kullanımı koruyup yüz yüze maruz bırakmayı adım adım planlamak",
               "Hiçbir değişiklik önermemek",
               "Yalnızca ilaç tedavisine başlamak"], 1,
              "Aynı kullanım farklı ergenlerde farklı etki yapar [@beyens2020]. Mert için çevrimiçi ortam tek sosyal temas alanı olabilir; tümüyle kapatmak yalnızlığı artırır. Öte yandan yalnızca çevrimiçi kalmak kaçınmayı sürdürür. Plan ikisini birlikte gözetmeli."),
        ],
        akilda="Kronometreye değil, kontrol kaybına bakın: aynı dört saat bir ergende hobi, bir başkasında kaçıştır.",
    ),
]
