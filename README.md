# Brain Rot mu? Dijital Çağda Gençlik

Çocuk ve ergenlerde sosyal medya, oyun, kısa video ve yapay zekâ sohbet botları üzerine etkileşimli rehber (Doç. Dr. Miraç Barış Usta, Kasım 2026). Aynı adlı ders sunumunun genişletilmiş hâlidir; sunum `sunum/` klasöründe durur.

**Canlı sürüm:** https://miracbarisusta.com/brain-rot-mu/ · **Sunum:** https://miracbarisusta.com/brain-rot-mu/sunum/

## İçerik

- **13 oturum, beş kesim:** Manzara (sayılar, ergen beyni ve tasarım), Kanıt (nedensellik tartışması; kime, ne zaman, nasıl), Riskler (uyku ve dikkat, beden, oyun, çevrimiçi zarar, algoritma ve tanı, yapay zekâ arkadaşları), Kurallar (yaş sınırları ve okul), Klinik (medya öyküsü ve plan, tedavide dijital araçlar).
- Her oturumda: genel bakış ve üç soru, ana fikirler, klinik karşılığı (Türkiye notlarıyla), ders kitaplarının yaklaşımı, tartışmalı noktalar, üç kurgusal vaka sorusu, akılda kalacak tek cümle ve kişisel not alanı.
- **Araçlar:** etki büyüklüğü çevirici (korelasyon ve risk oranını 100 kişiye çevirir), “Doğru mu, abartı mı?” iddia destesi, “Zor anlar” destesi, yazdırılabilir medya öyküsü ve aile planı çalışma sayfası, kavram kartları, Türkiye notları (7578 sayılı Kanun, yaş doğrulama yönetmeliği, başvuru hatları), karışık test, kaynakça.

## Kaynaklar

- Makale künyeleri PubMed kayıtlarından; PubMed’de dizinlenmeyen makaleler yayıncı (Crossref) kayıtlarından; Türkiye mevzuatı Resmî Gazete metinlerinden; raporlar ve duyurular yayımlayan kurumun sayfasından doğrulandı (Kasım 2026).
- Ders kitaplarından (Lewis 6. baskı, Rutter 7. baskı, IACAPAP e-Ders Kitabı 2.0, Williams ve Hill, Haidt) alıntı ya da kitap vakası yoktur; yaklaşımlar kendi sözcüklerimizle özetlenmiştir. Vakalar kurgusaldır.
- Çeviricideki taban riskler, belirtilmedikçe, varsayımsaldır. Mevzuat özetleri hukuki görüş değildir.

## Dosyalar

| Dosya | İçerik |
| --- | --- |
| `index.html` | Rehber (üretilen dosya; elle düzenlemeyin). |
| `rehber.css`, `rehber.js` | Görünüm ve etkileşim; dış betik ya da kütüphane kullanmaz. İlerleme yalnızca tarayıcıda (`localStorage`) saklanır. |
| `tools/olustur.py` | `index.html` üreticisi: `python3 tools/olustur.py`. |
| `tools/ic_bolum1.py` … `ic_bolum3.py`, `tools/icerik_oturumlar.py` | Oturum içerikleri. |
| `tools/icerik_araclar.py` | Araçların içeriği. |
| `tools/kaynaklar.json` | Kaynak künyeleri (DOI, PMID, bağlantı). |
| `sunum/` | 23 slaytlık web sunumu (`tools/donustur.py` ile üretilir). Memeler telif hakkı nedeniyle görselsizdir. |

## Lisans

© 2026 Miraç Barış Usta. Tüm hakları saklıdır; ayrıntılar için [LICENSE](LICENSE).
