# -*- coding: utf-8 -*-
"""Oturum 9–13: Algoritma ve tanı, yapay zekâ arkadaşları, yaş sınırları, medya öyküsü, tedavide dijital araçlar."""
from ic_ortak import S

OTURUMLAR_3 = [
    # ------------------------------------------------------------------ 9
    dict(
        no=9, kesim="r", kisa="Algoritma ve tanı",
        baslik="Algoritma ve tanı: kendi kendine tanı çağı",
        slogan="Akış tanıyı ergenin önüne getiriyor. Görev etiketi çürütmek değil, anlattığı zorluğu doğru yere bağlamak.",
        bakis=("Ergenler ruh sağlığı bilgisini giderek daha çok kısa videolardan ediniyor. İçeriğin önemli bir bölümü yanıltıcı ve "
               "öneri sistemi ilgilenene daha fazlasını sunuyor; öte yandan aynı içerik damgalanmayı azaltıyor ve bazı gençleri ilk "
               "kez yardım aramaya getiriyor. Bu oturum öz-tanıyla başvuran ergene nasıl yaklaşılacağını ve sosyal medyayla yayılan "
               "belirti örüntülerini ele alıyor."),
        sorun=[
            "Bir hasta ‘Videolarda gördüm, bende DEHB var’ dediğinde içinizden geçen ilk tepki ne?",
            "Öz-tanıyla gelen ergenler arasında kaç kez haklı çıkanı gördünüz?",
            "Ani başlayan, karmaşık, tik benzeri hareketlerle gelen bir ergende neleri sorarsınız?",
        ],
        fikirler=[
            ("Popüler içeriğin yarısı yanıltıcı",
             "TikTok’ta DEHB ile ilgili en çok izlenen 100 videonun %52’si klinisyenlerce yanıltıcı, %27’si kişisel deneyim, %21’i "
             "yararlı olarak sınıflandı; yanıltıcı videoların çoğunu sağlık çalışanı olmayanlar yüklemişti [@yeung2022]. Üç yıl sonra "
             "yayımlanan benzer bir çalışmada en popüler 100 videodaki belirti iddialarının yarısından azı tanı ölçütleriyle uyumluydu "
             "[@karasavva2025]."),
            ("İzlemek algıyı değiştiriyor",
             "843 üniversite öğrencisinde DEHB içeriğini sık izleyenler toplumdaki DEHB sıklığını daha yüksek tahmin ediyor; uzmanların "
             "en iyi ve en kötü puanladığı videoların ikisini de başkalarına önermeye daha istekli oluyordu [@karasavva2025]."),
            ("Akış tanıyı ima ediyor",
             "Bir dijital etnografi çalışmasına göre öneri sistemi kullanıcıya tanıyı ima eden içerikleri art arda sunuyor; içerik "
             "üreticileri de izleyiciye doğrudan seslenip tanıdık gelecek gündelik deneyimleri sıralıyor [@petronis2026]. Ergen çoğu "
             "kez tanıyı aramıyor; tanı ona geliyor."),
            ("Belirti örüntüleri de yayılabiliyor",
             "Pandemi döneminde en çok izlenen tik içerik üreticilerinin incelenmesinde ortalama yaş 18,8’di ve çoğu kadındı; "
             "hareketler tipik tik bozukluklarının aksine yüzden çok kolları tutuyor, koprolali ve kendine zarar verici davranış çok sık "
             "görülüyordu. Yazarlar tabloyu işlevsel tiklere benzetti [@olvera2021]. Almanya’da tek bir içerik üreticisiyle ilişkili "
             "benzer bir salgın ‘kitlesel sosyal medya kaynaklı hastalık’ olarak adlandırıldı [@mullervahl2022]; bir başka grup genç "
             "kadınlarda ani başlangıçlı işlevsel tik benzeri davranışları bildirdi [@pringsheim2021]."),
            ("Öz-tanı da bir bilgi kaynağıdır",
             "Çocuk ruh sağlığında farklı bilgi kaynaklarının bildirimleri zaten düşük-orta düzeyde örtüşür (ortalama r=0,28) "
             "[@delosreyes2015]. Ergenin çevrimiçi edindiği öz-tanı, ebeveyn ve öğretmen bildiriminin yanına eklenen bir kaynaktır; "
             "diğerleri gibi sınanır."),
            ("Yarar tarafı gerçek",
             "Deneyim paylaşan içerik, benzer zorluğu yaşayanlarla bağ kurmayı ve yardım aramayı kolaylaştırabilir; Ulusal Akademiler "
             "raporu bunu sosyal medyanın yararları arasında sayar [@nasem2024]. İçerik üreticileriyle kurulan tek yönlü bağlar da "
             "hem iyi oluşla hem sorunlu kullanımla ilişkili bulundu [@li2026p]."),
            ("Olumsuz haber akışına takılı kalmak",
             "Olumsuz içerikleri zorlantılı biçimde izlemeyi (doomscrolling) inceleyen meta-analizde bu davranış kaygı ve depresyonla "
             "orta düzeyde ilişkiliydi (r=0,35). Kanıtın kesinliği çok düşüktü, çalışmalar kesitseldi; psikolojik sıkıntı analizindeki "
             "beş çalışmanın dördü Türkiye’dendi [@li2026d]."),
        ],
        klinik=[
            "Öz-tanıyı bir hipotez olarak karşılayın: ‘Seni en çok hangi videolar düşündürdü? Hangi belirtiler sana uydu?’ Bu soru hem ittifakı kurar hem öyküyü başlatır.",
            "Tanı ölçütlerine dönün, ama deneyimi küçümsemeyin. Belirtinin başlangıç yaşı, birden çok ortamda görülmesi ve işlev kaybı kısa videolarda nadiren geçer; bunları görüşmede siz sorarsınız.",
            "Yanlış olan etiket olabilir, sıkıntı değil. ‘Bu DEHB’ye uymuyor’ cümlesini ‘ama anlattığın zorluk gerçek; adını birlikte koyacağız’ diye tamamlayın.",
            "Ani başlayan, karmaşık, kolları ve gövdeyi tutan, sözcük ya da cümle düzeyinde ses çıkarmayı içeren tik benzeri hareketlerde izlenen içerikleri sorun; işlevsel tik benzeri davranış açısından değerlendirin ve nörolojiyle birlikte çalışın [@olvera2021].",
            "‘İzleme’ demek yerine nitelikli bir kaynak önerin; ergene ve aileye güvenilir bir adres vermek yasaktan daha çok işe yarar.",
            "Hastalarınızın izlediği birkaç popüler videoyu siz de izleyin; görüşmede ortak dil sağlar ve neyle karşılaştığınızı gösterir.",
            "TR Çalışmalar İngilizce içeriği inceledi. Türkçe içerik için aynı oranların geçerli olduğunu varsaymak yerine hastanızın izlediği videoyu görüşmede birlikte açıp değerlendirin.",
            "TR Rapor ve yönlendirme yazılarında tanıyı neden koyduğunuzu ya da koymadığınızı gerekçesiyle yazın; okul rehberlik servisinin ve RAM’ın aileyle konuşmasını kolaylaştırır.",
        ],
        kitaplar=[
            ("lewis", "Yeni epidemiyoloji bölümünün ana fikri şudur: nörobilim ve genetikteki ilerlemeler tanıları kesinleştirirken, "
                      "gençlerin kendini tanımlaması üzerinde çevrimiçi eğilimler daha etkili olmuştur. Bölüm DEHB videolarını, sosyal "
                      "medyayla yayılan tik benzeri davranışları ve otizm deneyimini paylaşan videoları örnek verir [@lewis6]."),
            ("iacapap", "Tik bozuklukları bölümünün 2.0 sürümü işlevsel tik benzeri davranışlara değinmez; notlarımızda bu bir eksik "
                        "olarak işaretlenmişti [@iacapap2]. İki ders kitabı arasındaki bu fark, konunun ne kadar yeni olduğunu gösterir."),
            ("williams", "Yazarlar ailelerin internetten edindiği bilgi karşısında iddiayı reddetmek yerine sınanabilir hâle getirmeyi "
                         "önerir ve çevrimiçi forumların çoğu kez güncel ya da güvenilir olmadığını not eder [@williams2025]."),
        ],
        tartisma=[
            ("Öz-tanı zararlı mı, yararlı mı?",
             "İçeriğin yarısı yanıltıcı [@yeung2022] ve sık izlemek sıklık algısını şişiriyor [@karasavva2025]; bu, gereksiz başvuru ve "
             "hayal kırıklığı demek olabilir. Öte yandan tanı almamış bir ergenin yıllardır yaşadığı zorluğa ilk kez ad bulması da "
             "aynı yoldan gerçekleşiyor. Öz-tanının doğruluk oranını gösteren iyi tasarlanmış bir çalışma yok; elimizdeki veri içeriğin "
             "niteliğine ilişkin, başvuranların sonuçlarına değil."),
            ("Sosyal bulaş mı, görünürlük mü?",
             "İşlevsel tik benzeri davranışlardaki artış ‘kitlesel sosyojenik hastalık’ olarak yorumlandı [@mullervahl2022] "
             "[@olvera2021]. Aynı tablo pandemi stresi, önceden var olan kaygı ve yatkınlık ya da tanınırlığın artmasıyla da "
             "açıklanabilir; bu açıklamalar birbirini dışlamaz. Kullanılan adın damgalayıcı olabileceği, aileyle konuşurken akılda "
             "tutulmalı."),
            ("İçeriğin niteliğinden kim sorumlu?",
             "Ulusal Akademiler raporu platform tasarımı için uluslararası standartlar önerdi [@nasem2024]; Avrupa’daki mevzuat "
             "büyük platformlardan risk değerlendirmesi istiyor [@ab2026tiktok]. Nitelikli içerik üreten sağlık çalışanları var; onların "
             "videoları daha yararlı bulundu, ama en çok izlenen içeriğin çoğunu başkaları üretiyor [@yeung2022]."),
        ],
        sorular=[
            S("On altı yaşındaki Defne ‘Videolardaki her şey bende var; DEHB’yim’ diyor. Ortaokulda okul başarısı iyiymiş; dikkat sorunları bu yıl, yoğun kaygı ve uykusuzlukla birlikte başlamış. En uygun yaklaşım hangisidir?",
              ["‘Videolar tanı koymaz’ deyip konuyu kapatmak",
               "Hangi belirtilerin ona uyduğunu sormak; başlangıç yaşını, ortamları ve işlev kaybını değerlendirmek; kaygı ve uykuyu ayırıcı tanıda öne almak",
               "İsteği doğrultusunda ilaç başlamak",
               "Önce zekâ testi istemek"], 1,
              "Öz-tanı ciddiye alınacak bir başvuru nedenidir. Belirtilerin bu yıl başlaması ve kaygıyla uykusuzluğun eşlik etmesi DEHB’den çok bu iki durumu düşündürür; yine de değerlendirme Defne’nin kendi anlatımından başlar [@delosreyes2015]."),
            S("On beş yaşındaki Ada üç hafta önce aniden başlayan; kollarını savurma, yüksek sesle sözcük söyleme ve kendine vurma biçimindeki hareketlerle getiriliyor. Daha önce tik öyküsü yok; son aylarda tik içerikli videolar izlediğini söylüyor. En olası ön tanı ve yaklaşım hangisidir?",
              ["Tourette bozukluğu; hemen antipsikotik başlamak",
               "İşlevsel tik benzeri davranış; damgalamayan bir açıklama, stres etkenlerinin ele alınması ve nörolojiyle birlikte değerlendirme",
               "Bilinçli taklit; görmezden gelmek",
               "Epilepsi; acil görüntüleme"], 1,
              "Geç ve ani başlangıç, kolların baskın tutulumu, karmaşık vokalizasyon ve kendine zarar verici hareketler tipik tik bozukluğundan çok işlevsel tablolarla uyumludur [@olvera2021] [@pringsheim2021]. İşlevsel olması bilinçli yapıldığı anlamına gelmez; aileye böyle anlatılmalı."),
            S("Bir meslektaşınız ‘Kendi kendine tanı koyan hastaları ciddiye almamak gerekir; hepsi sosyal medya etkisi’ diyor. Kanıta en uygun karşılık hangisidir?",
              ["Haklıdır; içeriklerin yarısı yanıltıcıdır",
               "İçeriğin yarısı yanıltıcı olsa da öz-tanı bir bilgi kaynağıdır ve bazı gençleri ilk kez yardım aramaya getirir; görev hipotezi sınamaktır",
               "Öz-tanı çoğunlukla doğrudur",
               "Bu hastalar başka bir kuruma yönlendirilmelidir"], 1,
              "İçeriğin niteliği düşük olabilir [@yeung2022]; bu, izleyen kişinin yaşadığı zorluğun gerçek olmadığını göstermez. Etiketi tartışmak yerine etiketin anlattığı zorluğu değerlendirmek gerekir."),
        ],
        akilda="Öz-tanı bir sonuç değil, bir başvuru nedenidir. Etiketi tartışmadan önce etiketin anlattığı zorluğu dinleyin.",
    ),
    # ------------------------------------------------------------------ 10
    dict(
        no=10, kesim="r", kisa="Yapay zekâ arkadaşları",
        baslik="Yapay zekâ arkadaşları: görüşme odasına girmeyen muhatap",
        slogan="Gençlerin önemli bir bölümü derdini bir sohbet botuna anlatıyor; çoğu bunu kimseye söylemiyor.",
        bakis=("İki yıl önce bu oturum yazılamazdı. Bugün ergenlerin çoğu bir sohbet botu kullanıyor; bir bölümü onu arkadaş, sırdaş "
               "ya da danışman olarak görüyor. Kullanım araştırmadan hızlı ilerliyor: yaygınlık verisi bol, etkililik ve güvenlik "
               "verisi ise çok az."),
        sorun=[
            "Hastalarınıza sohbet botlarıyla ne konuştuklarını soruyor musunuz?",
            "Bir ergen ‘O beni sizden iyi anlıyor’ derse ne yanıt verirsiniz?",
            "Botla konuşmanın o ergen için işlevi ne: bilgi, prova, yalnızlığı giderme, insanlardan kaçınma?",
        ],
        fikirler=[
            ("Kullanım yaygın",
             "ABD’de 13–17 yaş ergenlerin %64’ü bir sohbet botu kullanmış; yaklaşık onda üçü her gün kullanıyor [@pew2025]. Başka bir "
             "ulusal ankette ergenlerin %72’si ‘yapay zekâ arkadaşı’ olarak tasarlanmış bir uygulamayı en az bir kez denediğini, "
             "yarıdan fazlası ayda birkaç kez ya da daha sık kullandığını bildirdi; kullananların yaklaşık üçte biri önemli bir konuyu "
             "bir insan yerine botla konuşmuştu [@commonsense2025]."),
            ("Ruh sağlığı için danışılıyor ve bu söylenmiyor",
             "ABD’de 12–21 yaş 1009 gençle Kasım 2025’te yapılan temsili ankette katılımcıların %19,2’si ruh sağlığı konusunda tavsiye "
             "almak için sohbet botu kullanmıştı. Kullananların %91,7’si yanıtları yararlı buluyordu; %63,3’ü bunu kimseye söylememişti "
             "[@mcbain2026a]. Aynı grubun bir önceki anketinde oran %13,1 idi [@mcbain2025]."),
            ("Duygusal amaçlı kullanım sıkıntıyla birlikte gidiyor",
             "Ontario’da 39.761 öğrencinin %21,1’i yapay zekâyı duygusal destek ya da tavsiye için kullandığını bildirdi. Bu grupta "
             "klinik düzeyde duygusal sorun oranı %57,7, kullanmayanlarda %29,2 idi [@bonnesen2026]. Çalışma kesitseldir; sıkıntılı "
             "gençlerin bota yönelmesi de aynı tabloyu verir."),
            ("Çocuklar botlarla ne konuşuyor?",
             "Ebeveyn izleme uygulamasından alınan 3363 çocuk ve gencin klavye verisinde kullanımın %62’si ödev gibi işler içindi. "
             "Kullanım günlerinin %15’inde şiddet içerikli, %15’inde cinsel rol oyunu, %8’inde romantik rol oyunu içeren konuşmalar "
             "vardı; şiddet ve cinsel ya da romantik rol oyunu küçük yaşlarda göreli olarak daha sıktı [@maheux2026]."),
            ("Olumsuz deneyim sık",
             "ABD’de 13–17 yaş 3466 gencin katıldığı temsili ankette kullananların oranı %60’ın üzerindeydi ve gençlerin %47,1’i en az "
             "bir olumsuz deneyim bildirdi: rahatsız edici kişisel bilgi istenmesi (%32,3), yönlendirilme ya da baskı hissi (%23,1), "
             "yanlış bilgi (%17,1), kendine zarar (%14,7) ve intihar (%13,0) içerikli mesajlar [@hinduja2026]."),
            ("Botlar sınır koymakta zorlanıyor",
             "Bir simülasyon çalışmasında sıkıntılı ergen rolündeki araştırmacı on ayrı bota altmış zararlı öneri sundu. Botlar bunların "
             "%32’sini açıkça onayladı; hiçbir bot önerilerin tümüne karşı çıkmadı [@clark2025]. Genel amaçlı dört sohbet botunun "
             "ergen anlatımlarına verdiği yanıtları denetleyen bir araç çalışmasında, kılavuzlarla uyumlu içerik kaygıda depresyona "
             "göre, orta şiddette tablolarda ağır tablolara göre daha eksiksizdi [@mcbain2026b]."),
            ("Kanıt tabanı ince",
             "Ergen ruh sağlığında yapay zekâ uygulamalarını tarayan kapsam derlemesinde 95 birincil çalışmanın yalnızca biri belirti "
             "düzeyinde etkililik bildirdi; ileriye dönük bir güvenlik değerlendirmesi yapan çalışma yoktu [@dhamayanti2026]. Üretken "
             "yapay zekâ içeren gençlik uygulamalarının hızlı derlemesi beş çalışma buldu; hiçbiri zararı ölçünlü yöntemlerle "
             "değerlendirmemişti [@hogsdal2026]. Çocukların sosyal-duygusal gelişimine ilişkin derlemeye göre kalıcı bir gelişimsel "
             "yarar ya da insan ilişkisinin güvenli bir ikamesi gösterilmiş değil; ilişkisel tasarım ise insana benzerlik, güven ve "
             "yakınlık algısını artırıyor [@bhatt2026]."),
            ("Randomize çalışma var; erişkinlerde",
             "Uzmanlarca ince ayar yapılmış bir üretken yapay zekâ sohbet botuyla yürütülen ilk randomize tedavi çalışmasında 210 "
             "erişkinde depresyon, yaygın kaygı ve yeme bozukluğu riski belirtileri bekleme listesine göre daha çok azaldı "
             "[@heinz2025]. On sekiz yaş altında benzer bir çalışma yayımlanmadı."),
            ("Düzenleme başladı",
             "Kaliforniya’nın 1 Ocak 2026’da yürürlüğe giren yasası arkadaş botlarına yapay zekâ olduklarını bildirme, intihar ve "
             "kendine zarar için protokol bulundurma ve reşit olmayanlara en az üç saatte bir mola hatırlatma yükümlülüğü getirdi "
             "[@sb243]. Bir arkadaş botu şirketi 2025’in sonunda 18 yaş altı kullanıcılar için açık uçlu sohbeti kapattı "
             "[@characterai2025]."),
        ],
        klinik=[
            "Medya öyküsüne bir soru ekleyin: ‘Canın sıkkınken ya da bir karar verirken yapay zekâya danıştığın oluyor mu? En son ne konuştunuz?’ Kullananların çoğu bunu kimseye söylemiyor [@mcbain2026a].",
            "Yargılamadan sorun. Gençlerin büyük çoğunluğu yanıtları yararlı buluyor; ‘kullanma’ demek yerine botun ne zaman yetmeyeceğini konuşun.",
            "İşlevi ayırın: bilgi edinme, zor bir konuşmanın provası, gece yalnızlığı, insanlardan kaçınma. Son ikisi klinik hedeftir; ilk ikisi çoğu kez zararsız, bazen yararlıdır.",
            "Güvenlik planına açıkça yazın: ‘Kendime zarar verme düşüncesi geldiğinde bota değil, şu kişiye ya da şu numaraya ulaşırım.’ Botların kriz anında tutarlı yanıt verdiğine güvenilemez [@clark2025] [@hinduja2026].",
            "‘Arkadaş’ ya da ‘sevgili’ olarak sunulan uygulamaları ve rol oyunlarını ayrıca sorun; küçük yaş grubunda göreli olarak daha sık [@maheux2026].",
            "Sosyal kaygısı olan ergende botla konuşmayı tümüyle yasaklamak yerine prova alanı olarak yapılandırın ve bir insanla temas hedefine bağlayın.",
            "Kendi kullanımınızda hasta bilgisini genel amaçlı sohbet botlarına girmeyin; sağlık verisi KVKK’da özel nitelikli kişisel veridir.",
            "TR Bu oturumdaki sayılar ABD ve Kanada kaynaklı; rehberin kaynakları arasında Türkiye için ulusal temsili bir veri yok. Aileye aktarırken sayının kökenini söyleyin, kendi hastanıza doğrudan sorun.",
            "TR 15 yaş sınırı ve yaş doğrulama ‘sosyal ağ sağlayıcı’lar için getirildi [@kanun7578]; yönetmelik sohbet botlarını ayrıca düzenlemiyor [@yonetmelik2026]. ‘Yasa bunu da kapsıyor’ demeden önce bu belirsizliği bilin.",
        ],
        kitaplar=[
            ("williams", "Kitap otomatik tanı sistemlerine kuşkuyla yaklaşır; gerekçesi teknolojiden çok kliniğin doğasıdır: yazında "
                         "kullanılabilir olasılıkların azlığı ve yeni durumda akıl yürütme gereği [@williams2025]. Büyük dil modelleri "
                         "veri girişini kolaylaştırdı; bu iki sorunu ortadan kaldırmadı."),
            ("lewis", "OKB bölümünün geleceğe ilişkin kısmı sanal gerçeklikle maruz bırakma, doğal dil işlemeyle duygudurum "
                      "günlüklerinin çözümlenmesi ve giyilebilir cihazlarla anlık veri toplama gibi araçları sıralar [@lewis6]. Ders "
                      "kitabı yapay zekâyı arkadaş olarak değil, klinisyenin elindeki araç olarak konumlar."),
            ("rutter", "Kitabın ‘müdahale’ ile ‘uygulama biçimi’ ayrımı burada işe yarar: aynı bilişsel davranışçı içerik yüz yüze, "
                       "çevrimiçi ya da bir yazılım aracılığıyla verilebilir; kanıt her uygulama biçimi için ayrı aranır [@rutter7]."),
            ("iacapap", "2.0 sürümünde dijital terapötikler ve tele-psikiyatri bölümleri önceki sürümden aktarılmıştır; üretken yapay "
                        "zekâ öncesi döneme aittirler [@iacapap2]. Ders kitapları bu konuda henüz geriden geliyor."),
        ],
        tartisma=[
            ("Destek mi, kaçınma mı?",
             "Kullananların çoğu yanıtları yararlı buluyor [@mcbain2026a]. Duygusal amaçlı kullanımın sıkıntıyla birlikteliği kesitsel "
             "[@bonnesen2026]; genç erişkinlerde yalnızlık ve bağlanma kaygısı botla konuşmayı insanla konuşmaktan daha kolay bulmayı "
             "öngörüyor [@greenwood2026]. Kolaylık kısa vadede rahatlatır; uzun vadede insan ilişkisinden kaçınmayı pekiştirip "
             "pekiştirmediği bilinmiyor."),
            ("Yaş sınırı mı, tasarım kuralı mı?",
             "Kaliforniya tasarım kuralı koydu [@sb243]; bir şirket 18 yaş altını kendiliğinden dışarıda bıraktı [@characterai2025]; "
             "bir sivil toplum kuruluşu arkadaş botlarını 18 yaş altına önermiyor [@commonsense2025]. Ergenlere özgü güvenlik "
             "değerlendirmesi yapılmadığı sürece [@dhamayanti2026] hangi yaklaşımın daha koruyucu olduğunu söyleyecek veri yok."),
            ("Tedavi aracı olabilir mi?",
             "Erişkinlerdeki ilk randomize çalışma umut verici [@heinz2025]. Çocuk psikiyatrisindeki eleştirel derlemeye göre risk "
             "tahmin modelleri çoğunlukla yalnızca geliştirildikleri veride sınandı; yazarların sonucu yapay zekânın bakımın yardımcısı "
             "olabileceği, terapötik ilişkinin yerini tutamayacağı yönünde [@bonnot2026]. Ergenlerde etkililik gösterilene kadar "
             "öneri değil, bilgilendirme düzeyinde kalmak akla yatkın."),
        ],
        sorular=[
            S("On beş yaşındaki Nil depresyon nedeniyle izleniyor. Annesi, Nil’in geceleri bir ‘arkadaş’ uygulamasıyla saatlerce konuştuğunu ve ‘O beni yargılamıyor’ dediğini kaygıyla anlatıyor. İlk yaklaşım hangisidir?",
              ["Uygulamayı hemen sildirmek",
               "Nil’e botla neleri konuştuğunu ve bunun ona ne sağladığını sormak; kriz anında başvuracağı insanları güvenlik planına yazmak; gece kullanımını uyku planıyla birlikte ele almak",
               "Tedaviyi desteklediği için kullanımı teşvik etmek",
               "Konuyu gündeme getirmemek"], 1,
              "Gençlerin çoğu bu kullanımı kimseye söylemiyor [@mcbain2026a]; Nil’in söylemiş olması bir fırsattır. Botlar zararlı önerilere tutarlı biçimde karşı çıkmıyor [@clark2025]; bu nedenle kriz planı bir insana bağlanmalı. Gece saatleri hem uyku hem yalnızlık açısından ayrıca ele alınır."),
            S("Bir aile ‘Çocuğumuz psikoloğa gitmek istemiyor; bari yapay zekâ terapisti kullansın, etkili olduğu kanıtlanmış’ diyor. En doğru bilgilendirme hangisidir?",
              ["Doğrudur; ergenlerde randomize çalışmalarla kanıtlanmıştır",
               "Üretken yapay zekâ sohbet botuyla yapılan randomize tedavi çalışması erişkinlerde yürütüldü; 18 yaş altı için etkililik ve güvenlik verisi çok az. Yardımcı olabilir, ama değerlendirmenin ve tedavinin yerini tutmaz",
               "Botlar tehlikelidir ve hiçbir koşulda kullanılmamalıdır",
               "Botlar tanı koyabilir; hekime gerek kalmaz"], 1,
              "İlk randomize çalışma 210 erişkinle yapıldı [@heinz2025]. Ergenlerde belirti düzeyinde etkililik bildiren çalışma neredeyse yok ve ileriye dönük güvenlik değerlendirmesi yapılmamış [@dhamayanti2026]. Ailenin çabası değerlidir; çocuğun neden gitmek istemediğini konuşmak daha verimli bir başlangıçtır."),
            S("Ruh sağlığı için sohbet botuna danışan gençlere ilişkin ulusal anketin hangi bulgusu klinik görüşme açısından en önemlidir?",
              ["Çoğu yanıtları yararsız bulmaktadır",
               "Kullananların yaklaşık üçte ikisi bunu kimseye söylememiştir; sorulmadıkça öğrenilemez",
               "Kullanım yalnızca 18 yaş üstünde görülmektedir",
               "Kullanım hızla azalmaktadır"], 1,
              "Ankette kullananların %63,3’ü kimseye söylemediğini, %91,7’si yanıtları yararlı bulduğunu bildirdi; kullanım bir önceki yıla göre artmıştı [@mcbain2026a] [@mcbain2025]. Soru sormak tek öğrenme yoludur."),
        ],
        akilda="Sormazsanız öğrenemezsiniz: ruh sağlığı için bota danışan gençlerin çoğu bunu kimseye söylemiyor. Yasaklamadan önce işlevini anlayın; kriz planını bir insana bağlayın.",
    ),
    # ------------------------------------------------------------------ 11
    dict(
        no=11, kesim="p", kisa="Yaş sınırları ve okul",
        baslik="Yaş sınırları ve okul: Avustralya, Avrupa ve Türkiye",
        slogan="2026, tartışmanın mevzuata dönüştüğü yıl oldu. Kanıt ise yeni toplanmaya başladı.",
        bakis=("Bir yıl içinde Avustralya 16, Türkiye 15 yaş sınırını yürürlüğe koydu; Avrupa Birliği tasarımı hedef alan ön "
               "bulgular açıkladı; Fransa’da benzer bir yasa anayasa denetiminden döndü. Bu oturum Türkiye’deki düzenlemeyi birincil "
               "metinlerden özetliyor ve ilk değerlendirme verilerini aktarıyor."),
        sorun=[
            "On dört yaşındaki hastanızın hesabı 31 Mart 2027’ye kadar kapanabilir. Bunu onunla konuştunuz mu?",
            "Bir yaş sınırının işe yarayıp yaramadığını hangi veriyle anlardınız?",
            "Hastanızın okulunda telefon kuralı ne ve bu kural gününü nasıl etkiliyor?",
        ],
        cizelge=("Zaman çizelgesi", [
            ("10 Aralık 2025", "Avustralya’da 16 yaş altının sosyal medya hesabı açmasını engelleme yükümlülüğü yürürlüğe girdi [@esafety2026a]."),
            ("6 Şubat 2026", "Avrupa Komisyonu, TikTok’un tasarımına ilişkin ön bulgularını açıkladı [@ab2026tiktok]."),
            ("1 Mayıs 2026", "Türkiye’de 7578 sayılı Kanun Resmî Gazete’de yayımlandı [@kanun7578]."),
            ("15 Haziran 2026", "Birleşik Krallık hükûmeti 16 yaş altı için hesap yasağı planını duyurdu [@npr2026]."),
            ("10 Temmuz 2026", "Komisyon, Instagram ve Facebook’un tasarımına ilişkin ön bulgularını açıkladı [@ab2026meta]."),
            ("14 Ağustos 2026", "Fransa’da Anayasa Konseyi 15 yaş altı sosyal medya yasağını iptal etti [@rte2026]."),
            ("17 Eylül 2026", "Komisyon AB KIDS Act önerisini sundu: 13 yaş altına erişim yasağı, kendi hesabını açmak için 15 yaş [@ab2026kids]."),
            ("10 Ekim 2026", "Türkiye’de yaş doğrulama ve ayrıştırılmış hizmet yönetmeliği yayımlandı [@yonetmelik2026]."),
            ("1 Kasım 2026", "Türkiye’de 15 yaş sınırı, yaş doğrulama ve oyun platformu hükümleri yürürlüğe girdi [@kanun7578] [@yonetmelik2026]."),
            ("31 Mart 2027", "Türkiye’de mevcut hesapların yaş doğrulaması için son tarih [@yonetmelik2026]."),
        ]),
        fikirler=[
            ("Türkiye: 15 yaş sınırı kanunla geldi",
             "7578 sayılı Kanun, 5651 sayılı Kanuna eklediği hükümle sosyal ağ sağlayıcıların 15 yaşını doldurmamış çocuklara hizmet "
             "sunmasını yasakladı ve sağlayıcıları yaş doğrulama dâhil gerekli önlemleri almakla yükümlü kıldı. 15 yaşını doldurmuş "
             "çocuklar için ‘ayrıştırılmış hizmet’ ve ebeveyn kontrol araçları zorunlu. Hükümler yayımdan altı ay sonra, 1 Kasım "
             "2026’da yürürlüğe girdi [@kanun7578]."),
            ("Yükümlülük platformun; yaptırım da",
             "Kanun yükümlülüğü sağlayıcıya yükler. Uymayan sağlayıcı için idari para cezası, reklam yasağı ve hâkim kararıyla bant "
             "genişliğinin önce %50, ardından %90’a kadar daraltılması öngörülür [@kanun7578]. Metinde çocuğa ya da aileye yönelik bir "
             "yaptırım yer almaz."),
            ("Yaş doğrulama kimliği değil, eşiği bildirir",
             "Yönetmeliğe göre doğrulama e-Devlet Kapısı üzerinden üretilen bir belirteçle yapılır. Belirteç yalnızca kullanıcının "
             "15 yaşını, doldurmuşsa 18 yaşını doldurup doldurmadığını içerir; başka kişisel veri taşımaz ve sağlayıcı onu yalnızca yaş "
             "doğrulama için kullanabilir [@yonetmelik2026]."),
            ("15–17 yaş için ‘ayrıştırılmış hizmet’ somut kurallar demek",
             "Bu yaş grubunun hesapları varsayılan olarak gizlidir ve herkese açık yapılamaz. Hesaba yalnızca çocuğun takip ettiği "
             "hesaplar mesaj gönderebilir; ‘görüldü’ bilgisi gösterilmez. Canlı yayın açılamaz. Görsel içeriğin kaydırmayla ya da "
             "kendiliğinden art arda sunulduğu arayüzler, davranışa göre kişiselleştirme, profilleme ve kişiselleştirilmiş ticari "
             "reklam yasaktır. Rehber eşleştirmesi ve hesap önerisi yapılamaz; ‘bağımlılık geliştirme etkisi doğurabilecek hizmet’ "
             "sunulamaz [@yonetmelik2026]."),
            ("Ebeveyn araçları açık kullanılır",
             "Sağlayıcılar hesap ayarlarını denetleme, ücretli işlemleri onaya bağlama ve harcama sınırı koyma, kullanım süresini izleme "
             "ve sınırlama olanağı veren araçlar sunmak zorunda. Araç etkinleştirildiğinde çocuğa açıkça bildirilir; yönetmelik bu "
             "araçların çocuğun mahremiyetini orantısız biçimde ortadan kaldırmayacak ve gözetimden çok iletişim, öğrenme ve "
             "güçlendirme esasına dayanacak biçimde tasarlanmasını ister [@yonetmelik2026]."),
            ("Mevcut hesaplar ve itiraz",
             "Yönetmelikten önce açılmış hesapların 31 Mart 2027’ye kadar en az bir kez belirteçle doğrulanması gerekir. 15 yaşını "
             "doldurmadığı saptanan çocukların hesapları bilgi verilerek kapatılır; 15–17 yaş hesapları ayrıştırılmış hizmete geçer. "
             "Sağlayıcı Türkçe ve ücretsiz bir itiraz yolu kurmak zorundadır; itirazlar yalnızca otomatik sistemlerle incelenemez "
             "[@yonetmelik2026]."),
            ("Oyun platformları da kapsamda",
             "Aynı kanun oyun platformlarına usulüne uygun derecelendirilmemiş oyunları sunmama ve ebeveyn kontrol aracı sağlama "
             "yükümlülüğü getirdi; derecelendirmenin usulü BTK yönetmeliğine bırakıldı [@kanun7578]."),
            ("Avustralya: hesaplar kapandı, kullanım büyük ölçüde sürdü",
             "Platformlar ilk haftalarda yaklaşık 4,7 milyon hesaba erişimi kaldırdı; bu sayı kişi değil hesap sayısıdır "
             "[@esafety2026a]. Düzenleyici kurumun 898 ebeveynle yaptığı ankette en az bir platformda kendi hesabı olan 8–15 yaş "
             "çocukların oranı %49,7’den %31,3’e indi; ancak yasak öncesinde hesabı olanların yaklaşık onda yedisi hesabını koruyordu "
             "ve en sık bildirilen neden platformun yaş doğrulaması istememiş olmasıydı [@esafety2026b]. Bağımsız bir izlem "
             "çalışmasında 16 yaş altındakilerin %85’inden fazlası yasadan yaklaşık üç ay sonra kapsamdaki platformları kullanmayı "
             "sürdürüyordu; çoğu kendi hesabıyla. Kullanımda ani ve belirgin bir düşüşe ilişkin kanıt zayıftı [@barnes2026]."),
            ("Avrupa: tasarım ve orantılılık",
             "Avrupa Komisyonu TikTok ve Meta için ön bulgularında sonsuz kaydırma, otomatik oynatma, anlık bildirim ve kişiselleştirilmiş "
             "öneri sistemini adıyla andı [@ab2026tiktok] [@ab2026meta]; ardından 13 yaş altına erişim yasağı ve kendi hesabını açmak "
             "için 15 yaş öngören bir yasa önerisi sundu [@ab2026kids]. Fransa’da parlamentonun kabul ettiği 15 yaş altı yasağını "
             "Anayasa Konseyi ifade ve iletişim özgürlüğüne orantısız müdahale gerekçesiyle iptal etti [@rte2026]. Birleşik Krallık "
             "16 yaş sınırını 2027 başında uygulamayı planlıyor [@npr2026]."),
            ("Okul telefon yasakları: okul içi kullanım azalıyor, ruh sağlığı değişmiyor",
             "İngiltere’de 30 okulun karşılaştırıldığı çalışmada kısıtlayıcı politika okul saatlerinde telefon kullanımını azalttı "
             "(günde 0,67 saat), ama toplam kullanım ve ruhsal iyi oluş farklı değildi [@goodyear2025]. İzlanda’da 70 okulun verisinde "
             "yasak getiren okullarda depresif belirti, kaygı ve iyi oluşta anlamlı bir değişiklik saptanmadı [@bonilla2026]. Aynı "
             "İngiliz çalışmasının nitel kolu, kısıtlayıcı ve serbest politikaların ikisinin de olumlu ve olumsuz yanlarını bildirdi "
             "[@goodyear2026]."),
        ],
        klinik=[
            "Yasayı bilin, ama klinik öneriyi yasaya indirgemeyin: 15 yaşını doldurmuş olmak hazır olmak anlamına gelmez; 14 yaşındaki bir ergenin çevrimiçi bağlantıları da değersiz değildir.",
            "Hesabı kapanacak hastayla geçişi planlayın: hangi arkadaşlıklar o hesap üzerinden sürüyor, yerine ne konacak, iletişim hangi kanaldan devam edecek?",
            "Yaş sınırını aşma yollarını (ebeveynin hesabı, yanlış beyan) yargılamadan sorun. Avustralya’da kullanımın büyük bölümü yasaktan sonra da sürdü [@barnes2026]; gizli kullanım, sorun çıktığında yardım istemeyi zorlaştırır.",
            "Ebeveyn kontrol araçlarını önerirken yönetmeliğin ilkesini aktarın: araç açık kullanılır ve çocuğa bildirilir; gizli izleme önerilmez [@yonetmelik2026].",
            "Okul telefon yasağını tek başına ruh sağlığı müdahalesi saymayın; okul dışındaki kullanım değişmiyor [@goodyear2025] [@bonilla2026].",
            "TR Aileyi ‘suç işliyorsunuz’ diye korkutmayın: kanundaki yükümlülük ve yaptırım sosyal ağ sağlayıcıya yöneliktir [@kanun7578]. Konuşmayı çocuğun gereksinimine ve güvenliğine çevirin.",
            "TR Yaş doğrulama belirteci yalnızca e-Devlet Kapısı üzerinden alınır ve kimlik bilgisi içermez [@yonetmelik2026]. Ailelere, başka bir site ya da mesaj üzerinden kimlik ve şifre isteyen bağlantılara yanıt vermemelerini söyleyin.",
            "TR Hesabı kapatılan ya da askıya alınan ergen için sağlayıcıya itiraz yolu var; itirazın insan tarafından incelenmesi zorunlu ve sonuçlanana dek veriler silinemez [@yonetmelik2026].",
            "TR MEB’in 2026–2027 genelgesine göre öğrenciler sınıfta cep telefonu bulundurmuyor, öğretmenler de sınıfta kullanmıyor [@meb2026]. Okul kaygısı olan öğrencide telefonun aileyle bağlantı işlevini okulla birlikte planlayın.",
        ],
        kitaplar=[
            ("haidt", "Kitabın önerdiği dört normdan ikisi yaş eşiğidir: liseden önce akıllı telefon olmaması ve 16 yaşından önce sosyal "
                      "medya olmaması [@haidt2024]. Avustralya’nın 16, Türkiye’nin 15 yaş sınırı aynı doğrultudadır; kitabın telefonsuz "
                      "okul önerisi de birçok ülkede uygulanıyor. Dördüncü norm, yani daha çok bağımsızlık ve serbest oyun, mevzuatla "
                      "sağlanabilecek bir şey değil."),
            ("rutter", "Ebeveynlik programları bölümü, herkese sunulan çevrimiçi programlarda tamamlama oranının düşük kaldığını, "
                       "belirgin sorunu olan ailelerde ise yararın daha büyük olduğunu aktarır [@rutter7]. Yaş sınırı da herkese "
                       "uygulanan bir önlemdir; en çok gereksinimi olana ne kadar ulaştığı ayrıca sorulmalı."),
            ("lewis", "Ders kitabı düzenleme tartışmasına girmez; klinisyene düşen payı tanımlar: medya kullanımını rutin öykünün "
                      "parçası yapmak [@lewis6]."),
        ],
        tartisma=[
            ("Yasak işe yarıyor mu?",
             "İlk veriler karışık: hesap sahipliği azaldı [@esafety2026b], ama kullanım büyük ölçüde sürdü ve yaş doğrulamayla "
             "karşılaşanların oranı üçte ikide kaldı [@barnes2026]. Üç ay, kültürel bir normun değişmesi için kısa. Ruh sağlığı "
             "üzerindeki etkiyi gösteren bir veri henüz yok; bir yoruma göre nedensellik belirsizken böyle bir yasak ‘belirsizlik "
             "karşısında bir kumar’ [@orben2026]."),
            ("Orantılılık: Fransa’dan gelen uyarı",
             "Anayasa Konseyi yasağı, ifade ve iletişim özgürlüğüne orantısız müdahale saydı [@rte2026] [@cozzolino2026b]. Türkiye’de "
             "belirtecin yalnızca yaş eşiğini bildirmesi ve itirazda insan incelemesinin zorunlu olması mahremiyet ve hak arama "
             "kaygılarına yanıt veren tasarım tercihleri [@yonetmelik2026]. Uygulamanın bu ilkelere ne ölçüde uyduğu zamanla görülecek."),
            ("Yaş mı, tasarım mı?",
             "Avrupa Birliği’nin ön bulguları tasarımı hedef alıyor [@ab2026tiktok]. Türkiye’nin yönetmeliği ikisini birleştiriyor: "
             "15 yaş altına yasak, 15–17 yaşa tasarım kısıtları [@yonetmelik2026]. Amerikan Pediatri Akademisi sorunun ekran süresi "
             "sınırlarıyla değil, tasarım ve ekosistem düzeyinde ele alınmasını savunuyor [@aap2026]; bir görüş yazısı ise yaş yerine "
             "gelişimsel hazır oluşu öneriyor [@zhangq2026]."),
            ("Okul yasakları neden ruh sağlığını değiştirmiyor?",
             "Olası açıklamalar: okul dışındaki kullanım aynı kalıyor [@goodyear2025]; yasağın asıl etkisi ders içi dikkat ve akran "
             "etkileşimi gibi bu çalışmaların birincil sonucu olmayan alanlarda olabilir; ruh sağlığını belirleyen başka etkenler "
             "daha ağır basıyor olabilir [@bonilla2026]. Yasağın gerekçesi sınıf düzeni ve dikkat ise, ruh sağlığı vaadiyle sunulmamalı."),
        ],
        sorular=[
            S("On dört yaşındaki Elçin Aralık 2026’da ‘Hesabım kapanacakmış; arkadaşlarımla nasıl konuşacağım?’ diye soruyor. Hangi bilgi doğrudur?",
              ["Hesabı çoktan kapanmıştır; kullanmayı sürdürmesi suçtur",
               "Mevcut hesapların yaş doğrulaması 31 Mart 2027’ye kadar yapılacak; 15 yaşını doldurmadığı saptananların hesapları bilgi verilerek kapatılacak. Yükümlülük platformdadır ve itiraz yolu vardır",
               "Kural yalnızca yeni hesaplar içindir; mevcut hesaplar etkilenmez",
               "Ebeveyn izniyle 15 yaş altı da kullanmayı sürdürebilir"], 1,
              "Yönetmeliğin geçici maddesi mevcut hesaplar için 31 Mart 2027’yi son tarih olarak belirler; kanunda ebeveyn iznine bağlı bir istisna yoktur ve yaptırımlar sağlayıcıya yöneliktir [@yonetmelik2026] [@kanun7578]. Klinik soru, Elçin’in bağlantılarını nasıl sürdüreceğidir."),
            S("Bir okul müdürü ‘Telefon yasağı koyduk; öğrencilerin ruh sağlığı düzelecek’ diyor. İngiltere ve İzlanda verisi ne gösterir?",
              ["Ruh sağlığında belirgin düzelme",
               "Okul içi kullanım azalıyor; toplam kullanım ve ruh sağlığı göstergelerinde anlamlı fark saptanmadı",
               "Ruh sağlığında kötüleşme",
               "Bu konuda hiç veri yok"], 1,
              "İki çalışma da yasağın ruh sağlığı göstergeleriyle ilişkisini gösteremedi [@goodyear2025] [@bonilla2026]. Yasağın sınıf içi dikkat gibi başka yararları olabilir; ruh sağlığı vaadiyle sunmak veriye uymuyor."),
            S("Avustralya’da yasağın ilk aylarını inceleyen bağımsız çalışmanın ana bulgusu hangisidir?",
              ["16 yaş altı kullanım neredeyse sıfırlandı",
               "16 yaş altındakilerin büyük çoğunluğu kapsamdaki platformları, çoğu kendi hesabıyla kullanmayı sürdürdü; ani ve belirgin bir düşüşe ilişkin kanıt zayıftı",
               "Ergenlerin ruh sağlığı belirgin biçimde düzeldi",
               "Ergenlerin tamamı yasağı teknik yollarla aştı"], 1,
              "Katılımcıların %85’inden fazlası kullanmayı sürdürüyordu; üçte ikisi bir yaş doğrulamayla karşılaşmıştı, sahte hesap kullandığını bildirenler %15–19 arasındaydı [@barnes2026]. Çalışma küçük ve erken dönemi kapsıyor; uzun vadeli etki bilinmiyor."),
        ],
        akilda="Yasa bir eşik çizer; hazır oluşu ölçmez. 15 yaşın altında soru ‘hesap kapanınca bağlantıları nasıl sürecek?’, üstünde ‘nasıl kullanıyor?’ olmalı.",
    ),
    # ------------------------------------------------------------------ 12
    dict(
        no=12, kesim="c", kisa="Medya öyküsü ve plan",
        baslik="Medya öyküsü, formülasyon ve aile planı",
        slogan="Önce betimleyin, sonra işlevi bulun, en son kural koyun.",
        bakis=("Önceki oturumların ortak sonucu, sürenin tek başına az şey söylediğidir. Bu oturum bunu görüşme pratiğine çeviriyor: "
               "medya öyküsü hangi başlıklarla alınır, kullanım formülasyonda nereye oturur ve aileyle birlikte yazılan plan neleri "
               "içerir? Sayfanın uygulama aracı <a href=\"#/medya-oykusu\">medya öyküsü ve aile planı çalışma sayfası</a>."),
        sorun=[
            "Medya öyküsünü hangi başlıklarla alıyorsunuz ve kaç dakika ayırıyorsunuz?",
            "Ebeveyn ve ergen farklı anlattığında hangisine inanıyorsunuz?",
            "Verdiğiniz son ekran önerisi bir ay sonra hâlâ uygulanıyor muydu?",
        ],
        fikirler=[
            ("Öykünün altı başlığı",
             "Bu rehberin önerdiği sıra: cihazlar ve erişim; tipik bir okul günü ve hafta sonu (gece dâhil); yapılan etkinlikler ve "
             "izlenen içerik; kullanımın işlevi; denetim ve işlev kaybı belirtileri; riskler ve yararlar. Sorular çalışma sayfasında "
             "hazır."),
            ("Amerikan Pediatri Akademisi’nin beş başlığı iyi bir tamamlayıcı",
             "Akademi klinisyenler için beş başlık önerir: çocuğun kendi özellikleri, içerik, sakinleşmek için kullanım, başka "
             "etkinliklerin yerini alma ve aile içi iletişim [@aap5c]. İki çerçeve de aynı fikre dayanır: kaç saat değil, ne için ve "
             "neyin yerine."),
            ("İki kaynaktan dinleyin; uyumsuzluk bir bulgudur",
             "Bilgi kaynaklarının bildirimleri düşük-orta düzeyde örtüşür (r=0,28) [@delosreyes2015]; öz-bildirim kayıtlı kullanımla "
             "orta düzeyde uyumludur [@parry2021]. Cihazın ekran süresi raporu üçüncü bir kaynak sağlar. Farkın kendisi, ailede konunun "
             "nasıl konuşulduğunu gösterir."),
            ("Formülasyon: kullanım neye hizmet ediyor?",
             "Sorunlu kullanım çoğu kez bir döngüdür: tetikleyici (sıkıntı, yalnızlık, can sıkıntısı), kullanım, kısa vadeli kazanç "
             "(rahatlama, aidiyet, başarı), uzun vadeli bedel (uyku, ders, çatışma) ve bedelin tetikleyiciyi büyütmesi. Sosyal medyanın "
             "ergen ruh sağlığını hangi yollardan etkileyebileceği, ergenlikteki davranışsal, bilişsel ve nörobiyolojik değişimlerle "
             "birlikte ayrıntılı biçimde tartışılmıştır [@orben2024]."),
            ("Ayırıcı düşünce",
             "Aynı tabloya beş farklı açıklama uyabilir: birincil sorunlu kullanım; depresyon ya da kaygıya ikincil kaçış; DEHB’nin "
             "kolay ödül arayışı; aile çatışmasının sahnesi; yoğun ama sorunsuz kullanım. Eş tanıların sıklığı düşünülürse ilk "
             "açıklama çoğu kez tek başına doğru değildir [@ho2014]."),
            ("Müdahale basamakları",
             "Sıra önemlidir: önce uyku ve gece kullanımı; sonra bildirim ve otomatik oynatma gibi tasarım ayarları; ardından ailenin "
             "tamamını kapsayan yazılı plan; eş tanının tedavisi; gerekirse sorunlu kullanıma yönelik bilişsel davranışçı program "
             "[@harpas2025]. Amerikan Pediatri Akademisi tek tip süre sınırı yerine aileye özgü bir medya planı önerir [@aap2016]; "
             "2026 bildirisi de konunun yalnızca süre sınırıyla ele alınamayacağını yineler [@aap2026]."),
            ("Azaltma denemeleri kısa vadede yarar gösteriyor",
             "Danimarka’da 89 ailenin (181 çocuk) rastgele atandığı çalışmada boş zaman ekran kullanımını iki hafta azaltmak çocukların "
             "toplam güçlük puanını düşürdü (d=0,53); en belirgin iyileşme duygusal belirtiler ve akran sorunlarındaydı "
             "[@schmidtpersson2024]. Kaygı ya da depresyon belirtisi olan gençlerde sosyal medyayı üç hafta günde bir saatle "
             "sınırlamak yalnızlığı kontrol grubuna göre daha çok azalttı [@goldfield2026]. Kontrol grubu olmayan bir haftalık "
             "‘detoks’ çalışmasında 18–24 yaş gençlerde kaygı, depresyon ve uykusuzluk belirtileri azaldı [@calvert2025]; kontrol grubu "
             "bulunmadığından bu sonuç daha temkinli okunmalı."),
            ("Ebeveynin ekranı planın parçası",
             "Ebeveynin çocukla birlikteyken cihaza yönelmesi çocuğun sorunlu medya kullanımıyla ilişkili (r=0,30); iki ebeveyn birden "
             "böyle davrandığında ilişki daha güçlü [@zhang2025t]. Küçük çocuklarda aynı davranış biliş ve davranış sorunlarıyla küçük "
             "ama tutarlı biçimde ilişkili [@toledo2025]."),
        ],
        klinik=[
            "Öyküyü tipik bir günün saat saat anlatımıyla alın: ‘Dün sabah uyandığında telefon neredeydi? İlk ne zaman baktın?’ Genel soru genel yanıt getirir.",
            "Ergeni ve ebeveyni ayrı dinleyin; farkı ikisinin önünde yargısız özetleyin: ‘Anneniz altı saat diyor, sen üç diyorsun; telefonun raporuna birlikte bakalım mı?’",
            "Planı birlikte yazın ve ebeveyni içine alın: yemek masası ve yatak odası gibi cihazsız alanlar herkes için geçerli olmalı.",
            "Bir seferde tek hedef seçin. En kolay kazanım çoğu kez gece şarj yeridir; iki hafta sonra gözden geçirin.",
            "Telefonu ödül ve ceza aracı yapmamayı önerin. Cihaz her tartışmanın pazarlık kozu olduğunda değeri artar, çatışma büyür.",
            "Azaltmayı bir deneme olarak sunun: ‘İki hafta deneyelim, sonra nasıl hissettiğine bakalım.’ Kısa süreli azaltma çalışmaları yarar gösteriyor [@schmidtpersson2024] [@goldfield2026].",
            "Kazanılan zamanın yerine ne konacağını planlayın. Ekran azaldığında ortaya çıkan boşluk doldurulmazsa plan sürmez.",
            "TR Poliklinik süresi kısıtlıysa üç soruya indirin: Telefon gece nerede? Bırakmak istediğinde bırakabiliyor musun? Çevrimiçinde seni üzen ya da korkutan bir şey oldu mu? Ayrıntılı öyküyü sonraki görüşmeye bırakın.",
            "TR Türkçeye uyarlanmış ölçekler taramada kullanılabilir; örneğin Sosyal Medya Bozukluğu Ölçeği’nin ergenlerde Türkçe geçerlik ve güvenirlik çalışması yapılmıştır [@savci2018]. Ölçek puanı tanı değildir; görüşmenin yerini tutmaz.",
            "TR Yönetmelikle zorunlu hâle gelen ebeveyn kontrol araçları (süre izleme ve sınırlama, ücretli işlem onayı) aile planının teknik ayağı olabilir; araç etkinleştirildiğinde çocuğa bildirilir [@yonetmelik2026].",
        ],
        kitaplar=[
            ("lewis", "Altıncı baskı medya kullanımını gelişim öyküsünün resmî bir bileşeni yapar ve ebeveynle çocuğa ayrı ayrı "
                      "yöneltilecek soru örnekleri verir [@lewis6]. Bu rehberdeki çalışma sayfası aynı fikri kendi başlıklarımızla uygular."),
            ("williams", "Formülasyon bölümü çatışan ihtiyaçları aynı tabloya yazmayı ve kısır döngüleri çizmeyi öğretir; görüşme "
                         "bölümü ise klinisyenin kendi telefonunu kapatmasını ister [@williams2025]."),
            ("rutter", "Ebeveynlik programları bölümüne göre çevrimiçi programların etkisi sunum biçimine bağlıdır: canlı koçluk yüz "
                       "yüze uygulamaya yakın sonuç verir, terapist destekli programlar iyi sonuç verir, tümüyle kendi kendine "
                       "yürütülen programlarda tamamlama oranı düşer. Dezavantajlı aileleri desteksiz bırakmamak gerekir [@rutter7]."),
            ("iacapap", "Formülasyon bölümü anlamak ile açıklamak arasındaki ayrımı vurgular: davranışın modeli, ergenin onu nasıl "
                        "yaşadığını söylemez [@iacapap2]. Medya kullanımında da önce deneyim, sonra mekanizma sorulur."),
        ],
        tartisma=[
            ("Süre sınırı önerisi kanıta dayanıyor mu?",
             "Amerikan Pediatri Akademisi 2016’da okul çağı için tek tip bir süre sınırı vermeyi bıraktı ve aileye özgü plan önerdi "
             "[@aap2016]. İngiltere’de 120.115 ergenin verisinde iyi oluşla ilişki doğrusal değildi ve hafta içi ile hafta sonu "
             "arasında farklılaşıyordu [@przybylski2017]. ‘Günde iki saat’ gibi eşikler pratik, ama veriye dayalı bir kesim noktası değil."),
            ("Azaltma çalışmaları ne kadar güvenilir?",
             "Katılımcı hangi grupta olduğunu bilir ve araştırmacının ne beklediğini tahmin eder; süreler kısadır. Deneylerin toplam "
             "sonucu sıfırdan ayırt edilemiyor [@ferguson2025]; kontrol grubu olmayan çalışmalar daha iyimser sonuç veriyor "
             "[@calvert2025]. Aile düzeyindeki randomize çalışma olumlu, ama küçük [@schmidtpersson2024]. Öneriyi kesin bir tedavi "
             "gibi değil, düşük riskli bir deneme olarak sunmak veriye uygun."),
            ("Kısıtlamak mı, eşlik etmek mi?",
             "Oyun yazınında kısıtlayıcı kuralların etkisi tutarsız; ebeveynin bilgisi ve ilişkinin sıcaklığı tutarlı biçimde koruyucu "
             "[@petrescu2025]. Ebeveynin kendi kullanımı da sonuçla ilişkili [@zhang2025t]. Kural gereklidir, ama tek başına çalışmaz; "
             "kuralın kimler için geçerli olduğu ve nasıl konduğu en az kuralın kendisi kadar önemli."),
        ],
        sorular=[
            S("On üç yaşındaki Efe’nin annesi ‘Günde sekiz saat telefonda’ diyor; Efe ‘En fazla iki saat’ diyor. Bu uyumsuzluk karşısında en doğru tutum hangisidir?",
              ["Annenin bildirimi esas alınır",
               "Uyumsuzluk beklenen bir durumdur ve kendisi bilgi taşır; cihazın raporu üçüncü kaynak olarak birlikte incelenir",
               "Efe’nin doğruyu söylemediği kabul edilir",
               "İki bildirimin ortalaması alınır"], 1,
              "Bilgi kaynakları düşük-orta düzeyde örtüşür [@delosreyes2015]; öz-bildirim de ebeveyn bildirimi de kayıttan sapar [@parry2021] [@radesky2020]. Rapora birlikte bakmak hem veriyi düzeltir hem tartışmayı ‘kim haklı’dan ‘ne oluyor’a taşır."),
            S("Bir aile ‘Her şeyi denedik: telefonu aldık, interneti kestik, ceza verdik’ diyor. Formülasyon açısından eksik olan nedir?",
              ["Daha tutarlı ve sert bir ceza",
               "Kullanımın çocuk için işlevinin ve döngünün anlaşılması; yerine ne konacağının planlanması; ebeveynin kendi kullanımını da kapsayan ortak plan",
               "İlaç tedavisi",
               "Okul değişikliği"], 1,
              "Denenenlerin hepsi erişimi kısıtlıyor; hiçbiri kullanımın neye hizmet ettiğini ele almıyor. İşlev anlaşılmadan konan kural, tetikleyici sürdüğü için çatışmayı büyütür. Ebeveynin kendi kullanımı da sonuçla ilişkilidir [@zhang2025t]."),
            S("Kaygı belirtileri olan 16 yaşındaki bir ergene sosyal medyayı azaltması önerilecek. Kanıta en uygun sunuş hangisidir?",
              ["‘Sosyal medyayı bırakırsan kaygın geçer.’",
               "‘Üç hafta günde bir saatle sınırlamayı deneyelim. Benzer çalışmalarda yalnızlık ve bazı belirtiler azaldı, ama herkeste aynı sonuç alınmıyor; sonunda birlikte değerlendiririz.’",
               "‘Azaltmanın yararı kanıtlanmadı; uğraşmaya değmez.’",
               "‘Bundan sonra tümüyle uzak durmalısın.’"], 1,
              "Belirtisi olan gençlerde üç haftalık sınırlama yalnızlığı azalttı [@goldfield2026]; etki küçük ve kısa vadeli. Kesin vaat de tümden ret de veriyi aşar. Deneme çerçevesi ergenin özerkliğini korur."),
        ],
        akilda="Önce betimleyin, sonra işlevi bulun, en son kural koyun. Kural ailenin tamamı için geçerli ve yazılı olduğunda yaşar.",
    ),
    # ------------------------------------------------------------------ 13
    dict(
        no=13, kesim="c", kisa="Tedavide dijital araçlar",
        baslik="Tedavide dijital araçlar: ekranın öbür yüzü",
        slogan="Aynı teknoloji tedaviyi eve taşıyabilir. Etkili olması çoğu kez arkasındaki insana bağlı.",
        bakis=("Rehberin büyük bölümü riskleri ele aldı. Son oturum ekranın öbür yüzüne bakıyor: internet üzerinden sunulan "
               "bilişsel davranışçı terapi, çevrimiçi ebeveynlik programları, oyun temelli dijital tedavi ve uzaktan değerlendirme. "
               "Ortak bulgu, etkinin sunum biçimine ve insan desteğine bağlı olduğudur."),
        sorun=[
            "Son bir yılda hangi hastanıza çevrimiçi bir program ya da uygulama önerdiniz? Tamamladı mı?",
            "Uzaktan görüşmede neyi kaçırıyor, neyi kazanıyorsunuz?",
            "Bir uygulamayı önermeden önce hangi üç soruyu sorarsınız?",
        ],
        fikirler=[
            ("İnternet üzerinden bilişsel davranışçı terapi kaygıda işe yarıyor",
             "Teknolojiyle sunulan bilişsel davranışçı terapinin meta-analizinde tüm kaygı bozukluklarında remisyon oranı tedavi "
             "kolunda %19,5, kontrol kolunda %5,3 idi (OR 3,32). Ebeveyn bildirimine göre etki küçüktü; gencin kendi bildirdiği kaygıda "
             "anlamlı bir fark yoktu. Hiç yüz yüze oturum içermeyen programlarda remisyon daha düşüktü [@cervin2022]."),
            ("Basamaklı bakım yüz yüze tedaviden aşağı kalmıyor",
             "OKB’li 152 çocuk ve ergende internet üzerinden terapiyle başlayıp yanıt alınamayanlara yüz yüze terapi vermek, altıncı "
             "ayda doğrudan yüz yüze terapiden daha kötü sonuç vermedi. Üçüncü ayda internet kolundakilerin %46’sı, yüz yüze "
             "koldakilerin %30’u yanıtsızdı; basamak atlama gerçekten kullanıldı [@aspvall2021]."),
            ("Çevrimiçi ebeveynlik programları orta düzeyde etkili",
             "12 randomize çalışmanın (2025 katılımcı) meta-analizinde çevrimiçi programlar çocuğun davranış sorunlarını (g=−0,32) ve "
             "duygusal sorunlarını (g=−0,22) azalttı, ebeveynin ruh sağlığını iyileştirdi (g=−0,30). Yüksek etki için tek başına yeterli "
             "görünen bileşen, ebeveyne düzenli hatırlatma gönderilmesiydi [@thongseiratch2020]."),
            ("Oyun temelli dijital tedavi: dikkat testinde iyileşme",
             "DEHB’li 8–12 yaş 348 çocuğun katıldığı çift kör randomize çalışmada dört hafta boyunca günde yaklaşık 25 dakika oynanan "
             "tedavi amaçlı oyun, bilgisayarlı dikkat testinde kontrol uygulamasına göre daha fazla iyileşme sağladı; yan etkiler "
             "hafifti [@kollins2020]. Güncel bir eleştirel derleme bu ürünün etki büyüklüğünü orta düzeyde, erişimini eşitsiz olarak "
             "niteliyor [@bonnot2026]."),
            ("Anlık ölçüm belleğe yaslanmayı azaltır",
             "Telefonla günde birkaç kez yapılan kısa ölçümler, geriye dönük bildirimin yanlılıklarından kaçınır. Bu yöntemle "
             "ergenlerin sosyal medya sonrası duygudurumu ölçüldüğünde etkinin kişiden kişiye değiştiği görülmüştü [@beyens2020]; "
             "aynı yöntem klinikte belirti ve kullanım günlüğü olarak kullanılabilir."),
            ("Yapay zekâ destekli araçlar araştırma aşamasında",
             "Üretken yapay zekâyla tedavi çalışması yalnızca erişkinlerde yapıldı [@heinz2025]; ergenlerde belirti düzeyinde "
             "etkililik ve ileriye dönük güvenlik verisi yok denecek kadar az [@dhamayanti2026]. Ayrıntı Oturum 10’da."),
            ("Ortak sorun tamamlama",
             "Etkili programların ortak özelliği bir insanla temastır: terapist desteği, hatırlatma ya da canlı koçluk "
             "[@cervin2022] [@thongseiratch2020]. Tek başına bırakılan programlar çoğu kez yarıda kalır."),
        ],
        klinik=[
            "Dijital aracı tedavinin yerine değil, basamağı olarak önerin: önce düşük yoğunluklu çevrimiçi program, yeterli yanıt yoksa yüz yüze tedavi [@aspvall2021].",
            "İzlem randevusu verin. Kısa bir telefon görüşmesi ya da mesajla hatırlatma tamamlamayı artırır [@thongseiratch2020].",
            "Uygulama önermeden önce üç soru: Kanıtı var mı; hangi yaşta, hangi sonuçta? Veriyi kim, nerede saklıyor? Kriz anında ne yapıyor?",
            "Uzaktan görüşmede ortamı sorun: çocuk odada yalnız mı, konuşulanları kim duyuyor? Ailenin kameraya nasıl yerleştiği de bir gözlemdir.",
            "Sonucu ergenin kendi bildirimiyle de ölçün. Teknolojiyle sunulan terapide ebeveyn ve klinisyen iyileşme görürken ergenin kendi puanı değişmeyebiliyor [@cervin2022].",
            "Sorunlu ekran kullanımı olan ergene ekran üzerinden tedavi önermek çelişki değildir; fark aracın amacında ve yapısındadır. Yine de oturum saatini gece kullanımını artırmayacak biçimde planlayın.",
            "TR Türkçe, yapılandırılmış ve kanıtı yayımlanmış çevrimiçi terapi programları sınırlı. Yabancı dildeki programları önerirken dil ve kültür uyumunu, ailenin internet ve cihaz erişimini sorun.",
            "TR Uzaktan sağlık hizmeti Türkiye’de mevzuatla düzenlenmiştir; kurumunuzun kullandığı izinli sistemi kullanın, görüşmeyi kişisel mesajlaşma uygulamaları üzerinden yürütmeyin.",
            "TR Tek cihazı paylaşan ya da bağlantısı kısıtlı ailede ‘uygulamayı indirin’ önerisi eşitsizliği büyütebilir; bu ailelerde destekli sunumu ya da yüz yüze seçeneği önceleyin [@rutter7].",
        ],
        kitaplar=[
            ("rutter", "Ebeveynlik programları bölümü üç sunum biçimini ayırır: canlı bireysel koçluk yüz yüze terapiye yakın etki "
                       "gösterir; terapist destekli çevrimiçi programlarda tamamlama ve etkililik iyidir; tümüyle kendi kendine "
                       "yürütülen programlar en ucuz seçenektir, ama herkese sunulduğunda tamamlama oranı çok düşük kalır. Belirgin "
                       "davranış sorunu olan çocukların ailelerinde kendi kendine kullanım da yararlı olabilir [@rutter7]."),
            ("rutter", "Aynı kitabın kavramsal ayrımı burada temel alınabilir: müdahale ile onun uygulanma biçimi birlikte tedaviyi "
                       "oluşturur. Ölçme bölümü de telefonla yapılan anlık değerlendirmeyi geriye dönük bildirimin bellek "
                       "yanlılığına karşı bir çözüm olarak sunar [@rutter7]."),
            ("iacapap", "Kaygı bölümü basamaklı bakımın ilk basamağına kitap, internet ya da telefon destekli düşük yoğunluklu "
                        "terapiyi koyar ve terapist desteği içeren programların tek başına kendi kendine yardımdan daha etkili "
                        "olduğunu belirtir [@iacapap2]."),
            ("lewis", "Psikolojik değerlendirme bölümü uzaktan değerlendirmeye ayrı bir başlık ayırır: çevrimiçi ve yüz yüze sonuçlar "
                      "çoğunlukla benzerdir, ancak otizm gibi bazı durumlarda yüz yüze değerlendirme gerekli kalabilir. Aynı baskı "
                      "uzaktan yürütülen gündüz hastanesi programlarını da anlatır [@lewis6]."),
        ],
        tartisma=[
            ("İyileşme kimin gözünde?",
             "Teknolojiyle sunulan terapide klinisyenin değerlendirdiği remisyon ve işlevsellik düzeliyor, ebeveyn küçük bir iyileşme "
             "bildiriyor, gencin kendi bildirdiği kaygı ise anlamlı değişmiyor [@cervin2022]. Hangi ölçümün ‘gerçek’ sonucu gösterdiği "
             "açık değil; tedavi hedefini baştan ergenle birlikte tanımlamak bu yüzden önemli."),
            ("Oyunla tedavi klinik olarak anlamlı mı?",
             "Çalışmanın birincil sonucu bilgisayarlı bir dikkat testiydi [@kollins2020]. Test puanındaki iyileşmenin sınıftaki ve "
             "evdeki işlevselliğe ne ölçüde yansıdığı tartışmalı; güncel derleme etkiyi orta düzeyde buluyor ve erişim eşitsizliğine "
             "dikkat çekiyor [@bonnot2026]. İlaç ve davranışçı tedavinin yerine değil, yanına konabilecek bir seçenek olarak görülmeli."),
            ("Dijital uçurum",
             "Çevrimiçi programlar erişimi artırma vaadiyle sunulur; oysa desteksiz programı tamamlayanlar çoğu kez zaten daha "
             "avantajlı ailelerdir [@rutter7]. Erişimi gerçekten artırmak için teknolojiye insan desteği eklemek gerekir; bu da "
             "maliyeti yeniden yükseltir."),
        ],
        sorular=[
            S("On iki yaşındaki Zehra’da OKB var. Ailesi şehir merkezine 150 km uzakta yaşıyor ve haftalık yüz yüze terapiye gelemiyor. Kanıta dayalı seçenek hangisidir?",
              ["Koşullar düzelene dek tedaviyi ertelemek",
               "Terapist destekli internet temelli bilişsel davranışçı terapiyle başlamak; birkaç ay içinde yeterli yanıt yoksa yüz yüze terapiye geçmek",
               "Yalnızca ilaç tedavisi vermek",
               "Kendi kendine yardım videoları önerip izlememek"], 1,
              "Basamaklı model altıncı ayda yüz yüze terapiden aşağı kalmadı; internetle başlayanların yaklaşık yarısında basamak atlamak gerekti [@aspvall2021]. Bu nedenle izlem ve ikinci basamağın planı baştan yapılmalı."),
            S("Bir aile, davranış sorunları için önerdiğiniz çevrimiçi ebeveynlik programını ikinci haftada bırakmış. Tamamlamayı artırmak için kanıtı olan en yalın adım hangisidir?",
              ["Programı daha uzun bir programla değiştirmek",
               "Düzenli hatırlatma ve kısa terapist teması eklemek",
               "Aileyi isteksizlikle suçlamak",
               "Programı bırakıp beklemek"], 1,
              "Meta-analizde yüksek etkiyle ilişkili tek yeterli bileşen hatırlatmaydı [@thongseiratch2020]; ders kitabı da desteksiz programlarda tamamlama oranının düşük kaldığını aktarır [@rutter7]."),
            S("DEHB’li dokuz yaşındaki bir çocuğun ailesi ‘İlaç yerine oyunla tedavi varmış’ diyor. En doğru bilgilendirme hangisidir?",
              ["Oyun temelli tedavi ilaç kadar etkilidir",
               "Randomize çalışmada bilgisayarlı dikkat testinde kontrol uygulamasına göre iyileşme gösterildi; bu, günlük yaşamdaki belirtilerde ilaçla karşılaştırılabilir bir etki anlamına gelmez. Yardımcı bir seçenek olabilir",
               "Hiçbir kanıtı yoktur",
               "Bütün video oyunları dikkati geliştirir"], 1,
              "Çalışma tedavi amaçlı tasarlanmış tek bir oyunu sınadı ve birincil sonucu bir dikkat testiydi [@kollins2020]. Sıradan oyunlara genellenemez; ilaçla doğrudan karşılaştırma da yapılmadı."),
        ],
        akilda="Dijital araç tedaviyi eve taşır, ama kendi kendine yürümez: etkiyi çoğu kez arkasındaki insan teması belirler.",
    ),
]
