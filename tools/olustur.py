# -*- coding: utf-8 -*-
"""Brain Rot mu? Dijital Çağda Gençlik · rehber: index.html üreticisi.

Kullanım:  python3 tools/olustur.py
Girdi:     tools/icerik_oturumlar.py (ic_bolum1-3.py), tools/icerik_araclar.py, tools/kaynaklar.json
Çıktı:     index.html (depo kökünde)
"""
import html
import json
import random
import re
import sys
from pathlib import Path

ARACLAR = Path(__file__).resolve().parent
KOK = ARACLAR.parent
sys.path.insert(0, str(ARACLAR))

import icerik_araclar as A  # noqa: E402
import icerik_oturumlar as O  # noqa: E402

KAYNAK = json.loads((ARACLAR / "kaynaklar.json").read_text(encoding="utf-8"))
KULLANIM = {}      # anahtar -> [(görünüm id, adım, etiket)]
BILINMEYEN = set()
BAGLAM = {"vid": "", "adim": "", "etiket": ""}
ADRES = "https://miracbarisusta.com/brain-rot-mu/"
AD = "Brain Rot mu? Dijital Çağda Gençlik"


def esc(s):
    return html.escape(str(s), quote=True)


def atif(m):
    k = m.group(1)
    r = KAYNAK.get(k)
    if not r:
        BILINMEYEN.add(k)
        return esc(k)
    yer = (BAGLAM["vid"], BAGLAM["adim"], BAGLAM["etiket"])
    if yer[0] and yer not in KULLANIM.setdefault(k, []):
        KULLANIM[k].append(yer)
    return f'<a class="atif" href="#k-{k}" data-k="k-{k}">{esc(r["etiket"])}</a>'


def md_duz(s):
    """Kaçış + **kalın**, *eğik*, [@atıf]."""
    t = esc(s)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"\[@([\w-]+)\]", atif, t)
    return t


def md(s):
    """md_duz + metinde bilerek bırakılmış <a href="#/…"> iç bağlantıları; geri kalan her şey kaçışlanır."""
    parcalar = re.split(r'(<a href="#/[\w/-]+">.*?</a>)', s)
    out = []
    for p in parcalar:
        m = re.fullmatch(r'<a href="(#/[\w/-]+)">(.*?)</a>', p)
        out.append(f'<a href="{m.group(1)}">{esc(m.group(2))}</a>' if m else md_duz(p))
    return "".join(out)


def baglam(vid, adim="", etiket=""):
    BAGLAM.update(vid=vid, adim=adim, etiket=etiket)


HARF = "ABCD"


def view(vid, baslik, ust, ic, data_baslik=None, sinif=""):
    return (f'<section class="view {sinif}" id="v-{vid}" data-view="{vid}" data-baslik="{esc(data_baslik or baslik)}" '
            f'aria-label="{esc(data_baslik or baslik)}"><header class="oturum-bas"><p class="ust-baslik">{esc(ust)}</p>'
            f'<h2 tabindex="-1">{esc(baslik)}</h2></header>{ic}'
            f'<div class="oturum-son"><nav class="ileri-geri" aria-label="Oturumlar arasında"></nav></div></section>')


def adim(vid, anahtar, ikon, baslik, govde):
    sid = f"{vid}-{anahtar}"
    return (f'<section class="adim adim-{anahtar}" id="{sid}" aria-labelledby="{sid}-b"><h3 id="{sid}-b">'
            f'<span class="adim-ikon" aria-hidden="true">{ikon}</span> {esc(baslik)}</h3>{govde}</section>')


# Doğru şıkların yeri: bütün sorularda dengeli ve her derlemede aynı
_tum_sorular = [q for o in O.OTURUMLAR for q in o["sorular"]]
_hedefler = [0, 1, 2, 3] * (len(_tum_sorular) // 4 + 1)
random.Random(20261114).shuffle(_hedefler)
HEDEF = {id(q): _hedefler[i] for i, q in enumerate(_tum_sorular)}


def karistir_soru(q):
    """Doğru şıkkı hedef konuma taşır, diğer şıkların göreli sırasını korur."""
    sec = list(q["secenekler"])
    dogru = sec[q["dogru"]]
    digerleri = [s for i, s in enumerate(sec) if i != q["dogru"]]
    h = min(HEDEF.get(id(q), q["dogru"]), len(sec) - 1)
    yeni = digerleri[:h] + [dogru] + digerleri[h:]
    return yeni, h


def test_listesi(vid, sorular):
    out = [f'<p class="sina-ust"><span class="sina-skor" data-test-skor="{vid}" aria-live="polite"></span>'
           f'<button type="button" class="sina-sifirla" data-test-sifirla="{vid}" hidden>Yanıtları sil</button></p><ol class="test">']
    for i, q in enumerate(sorular):
        assert 0 <= q["dogru"] < len(q["secenekler"]) <= 4, q["soru"]
        sec, dogru = karistir_soru(q)
        btn = "".join(f'<button type="button" data-secenek="{k}"><span class="harf" aria-hidden="true">{HARF[k]}</span>'
                      f'<span>{md(s)}</span></button>' for k, s in enumerate(sec))
        out.append(f'<li class="test-madde" data-dogru="{dogru}" data-no="{i}" data-ara><p class="soru">{md(q["soru"])}</p>'
                   f'<div class="secenekler" role="group" aria-label="Seçenekler">{btn}</div>'
                   f'<div class="test-aciklama"><p><strong>Doğru yanıt: {HARF[dogru]}.</strong> {md(q["aciklama"])}</p></div></li>')
    out.append("</ol>")
    return "".join(out)


def klinik_li(x):
    if x.startswith("TR "):
        return f'<li class="crs-tr" data-ara><span class="tr-rozet" title="Türkiye notu">TR</span> {md(x[3:])}</li>'
    return f"<li data-ara>{md(x)}</li>"


def cizelge_html(c):
    baslik, satirlar = c
    return (f'<div class="cizelge-kap"><h4 class="cizelge-baslik">{esc(baslik)}</h4><ol class="cizelge">'
            + "".join(f'<li data-ara><span class="cz-tarih">{esc(t)}</span><span class="cz-olay">{md(e)}</span></li>' for t, e in satirlar)
            + "</ol></div>")


# ---------------------------------------------------------------- oturumlar
ADIMLAR = [("bakis", "🔭", "Genel bakış", "Bakış"), ("fikirler", "🧭", "Ana fikirler", "Ana fikirler"),
           ("klinik", "🩺", "Klinikte", "Klinikte"), ("kitaplar", "📚", "Kitaplar ne diyor?", "Kitaplar"),
           ("tartisma", "⚖️", "Tartışmalı noktalar", "Tartışma"), ("test", "✍️", "Vaka soruları", "Sorular"),
           ("akilda", "🎯", "Akılda kalsın", "Akılda kalsın"), ("not", "🗒️", "Kendi notum", "Notum")]
oturum_views = []
for o in O.OTURUMLAR:
    vid = f'oturum-{o["no"]}'
    etiket = f'Oturum {o["no"]}'
    assert len(o["sorun"]) == 3 and len(o["sorular"]) == 3, vid
    parcalar = []
    baglam(vid, "bakis", etiket)
    parcalar.append(adim(vid, "bakis", "🔭", "Genel bakış",
                         f'<p class="kitapta" data-ara>{md(o["bakis"])}</p><p class="okurken-baslik">Başlamadan önce düşünün</p>'
                         f'<ol class="okurken">{"".join(f"<li data-ara>{md(q)}</li>" for q in o["sorun"])}</ol>'
                         + (cizelge_html(o["cizelge"]) if o.get("cizelge") else "")))
    baglam(vid, "fikirler", etiket)
    parcalar.append(adim(vid, "fikirler", "🧭", "Ana fikirler",
                         '<ol class="fikirler">' + "".join(
                             f'<li data-ara><p><strong>{md(h)}.</strong> {md(t)}</p></li>' for h, t in o["fikirler"]) + "</ol>"))
    baglam(vid, "klinik", etiket)
    tr_say = sum(1 for x in o["klinik"] if x.startswith("TR "))
    parcalar.append(adim(vid, "klinik", "🩺", "Klinikte",
                         ('<p class="not"><span class="tr-rozet">TR</span> etiketli maddeler Türkiye’ye özgüdür; '
                          'hepsi <a href="#/turkiye">Türkiye notları</a> sayfasında da toplandı.</p>' if tr_say else "")
                         + '<ul class="crs-liste">' + "".join(klinik_li(x) for x in o["klinik"]) + "</ul>"))
    baglam(vid, "kitaplar", etiket)
    for k, _ in o["kitaplar"]:
        assert k in O.KITAP_ADLARI, k
    parcalar.append(adim(vid, "kitaplar", "📚", "Kitaplar ne diyor?",
                         '<p class="not">Ders kitaplarının ve ders notlarımızın bu konudaki yaklaşımı, kendi sözcüklerimizle. '
                         'Kitaplardan alıntı yoktur; ayrıntı için kitabın kendisine başvurun.</p><ul class="kitap-liste">'
                         + "".join(f'<li data-ara><span class="kitap-ad kitap-{k}">{esc(O.KITAP_ADLARI[k])}</span><p>{md(t)}</p></li>'
                                   for k, t in o["kitaplar"]) + "</ul>"))
    baglam(vid, "tartisma", etiket)
    parcalar.append(adim(vid, "tartisma", "⚖️", "Tartışmalı noktalar",
                         '<p class="not">Kanıtın çeliştiği, eksik kaldığı ya da yorumun ayrıştığı yerler. Künyeler kaynakçada.</p>'
                         '<div class="tartisma-liste">' + "".join(
                             f'<article class="tartisma" data-ara><h4>{md(h)}</h4><p>{md(t)}</p></article>'
                             for h, t in o["tartisma"]) + "</div>"))
    baglam(vid, "test", etiket)
    parcalar.append(adim(vid, "test", "✍️", "Vaka soruları",
                         '<p class="not">Vakalar kurgusaldır.</p>' + test_listesi(vid, o["sorular"])))
    baglam(vid, "akilda", etiket)
    parcalar.append(adim(vid, "akilda", "🎯", "Akılda kalsın", f'<ul class="akilda"><li data-ara>{md(o["akilda"])}</li></ul>'))
    parcalar.append(adim(vid, "not", "🗒️", "Kendi notum",
                         f'<div class="vaka-not"><label for="{vid}-not-alan">Bu oturumla ilgili aklınıza gelenler, kendi '
                         f'pratiğinizle bağlantılar</label><textarea id="{vid}-not-alan" data-not="{vid}" rows="4" '
                         f'placeholder="Hasta kimlik bilgisi yazmayın."></textarea><p class="kucuk">Yazdıklarınız yalnızca bu '
                         f'tarayıcıda saklanır.</p></div>'))
    nav = ('<nav class="adimlar" aria-label="Bu oturumun kısımları">' + "".join(
        f'<a href="#/{vid}/{k}"><span aria-hidden="true">{i}</span> {esc(s)}</a>' for k, i, _, s in ADIMLAR) + "</nav>")
    bas = (f'<header class="oturum-bas"><p class="ust-baslik">{esc(O.KESIMLER[o["kesim"]])} · Oturum {o["no"]}</p>'
           f'<h2 tabindex="-1">{esc(o["baslik"])}</h2><p class="slogan">{md(o["slogan"])}</p></header>')
    html_ = (f'<section class="view bolum" id="v-{vid}" data-view="{vid}" data-baslik="Oturum {o["no"]}: {esc(o["kisa"])}" '
             f'aria-label="Oturum {o["no"]}">{bas}{nav}{"".join(parcalar)}'
             f'<div class="oturum-son"><button type="button" class="okundu" data-okundu="{vid}" aria-pressed="false">'
             f'Bu oturumu okudum</button><nav class="ileri-geri" aria-label="Oturumlar arasında"></nav></div></section>')
    oturum_views.append(dict(id=vid, no=o["no"], kesim=o["kesim"], kisa=o["kisa"], baslik=o["baslik"], slogan=o["slogan"],
                             html=html_, n_fikir=len(o["fikirler"]), n_soru=len(o["sorular"]), tr=tr_say))
OTAD = {v["no"]: f'Oturum {v["no"]} · {v["kisa"]}' for v in oturum_views}

# ---------------------------------------------------------------- etki büyüklüğü çevirici
baglam("etki", "", "Etki büyüklüğü çevirici")


def sayi_tr(x):
    return ("%g" % x).replace(".", ",")


def girdi(grup, k, ad, mn, mx, st, v, birim=""):
    return (f'<div class="tg"><label for="ek-{grup}-{k}">{esc(ad)}</label><div class="tg-satir">'
            f'<input type="range" data-ek-r="{k}" min="{mn}" max="{mx}" step="{st}" value="{v}" aria-label="{esc(ad)} kaydırıcı">'
            f'<span class="tg-sayi"><input type="number" id="ek-{grup}-{k}" data-ek="{k}" min="{mn}" max="{mx}" step="{st}" value="{v}" '
            f'inputmode="decimal">{f"<span aria-hidden=true>{birim}</span>" if birim else ""}</span></div></div>')


r_btn = "".join(
    f'<button type="button" class="filtre" data-ek-ayar="{k}" data-v="{v}" aria-pressed="{"true" if i == 0 else "false"}">'
    f'{esc(ad)} <span class="sayi">r={sayi_tr(v)}</span></button>' for i, (k, ad, v, _) in enumerate(A.ETKI_R))
r_ac = "".join(f'<p class="ek-aciklama kucuk" data-ek-ac="{k}" data-ara{"" if i == 0 else " hidden"}>{md(ac)}</p>'
               for i, (k, _, _, ac) in enumerate(A.ETKI_R))
or_btn = "".join(
    f'<button type="button" class="filtre" data-ek-ayar="{k}" data-tur="{tur}" data-v="{v}" data-p0="{p0}" '
    f'aria-pressed="{"true" if i == 0 else "false"}">{esc(ad)} <span class="sayi">{tur} {sayi_tr(v)}</span></button>'
    for i, (k, ad, tur, v, p0, _) in enumerate(A.ETKI_OR))
or_ac = "".join(f'<p class="ek-aciklama kucuk" data-ek-ac="{k}" data-ara{"" if i == 0 else " hidden"}>{md(ac)}</p>'
                for i, (k, _, _, _, _, ac) in enumerate(A.ETKI_OR))
r0, o0 = A.ETKI_R[0], A.ETKI_OR[0]
etki_ic = (f'<p class="giris-metin" data-ara>{md(A.ETKI_GIRIS)}</p>'
           '<div class="tarama etki" id="etki-r" data-ek-panel="r"><h3 class="etki-baslik">1 · Bir korelasyon ne anlatır?</h3>'
           f'<div class="tarama-ayarlar" role="group" aria-label="Hazır örnekler">{r_btn}</div>'
           f'<div class="ek-aciklamalar" aria-live="polite">{r_ac}</div>'
           f'<div class="tarama-girdiler etki-tek">{girdi("r", "r", "Korelasyon katsayısı (r, mutlak değer)", "0", "0.9", "0.01", r0[2])}</div>'
           '<div class="tarama-kpi">'
           '<div class="kpi"><span class="kpi-ad">Açıklanan varyans</span><span class="kpi-deger" data-c="r2">–</span>'
           '<span class="kpi-alt">r²: değişkenliğin birlikte değişen payı</span></div>'
           '<div class="kpi"><span class="kpi-ad">Cohen d karşılığı</span><span class="kpi-deger" data-c="d">–</span>'
           '<span class="kpi-alt">iki eşit grup karşılaştırılsaydı</span></div>'
           '<div class="kpi"><span class="kpi-ad">Uyum olasılığı</span><span class="kpi-deger" data-c="uyum">–</span>'
           '<span class="kpi-alt">ilişki yoksa %50</span></div></div>'
           '<p class="tarama-cumle" aria-live="polite"></p>'
           '<div class="yuzluk" data-yuzluk="r" aria-hidden="true"></div>'
           '<ul class="tarama-lejant"><li><span class="lj lj-gp"></span>Belirti puanı da ortancanın üstünde</li>'
           '<li><span class="lj lj-gn"></span>Belirti puanı ortancanın altında</li></ul>'
           '<p class="not">Uyum olasılığı iki değişkenin de normal dağıldığı varsayımıyla hesaplanır (½ + arcsin r / π). '
           'Hesap ilişkinin yönünü ve nedenini göstermez.</p></div>'
           '<div class="tarama etki" id="etki-or" data-ek-panel="or"><h3 class="etki-baslik">2 · “Riski iki katına çıkarıyor” ne demek?</h3>'
           f'<div class="tarama-ayarlar" role="group" aria-label="Hazır örnekler">{or_btn}</div>'
           f'<div class="ek-aciklamalar" aria-live="polite">{or_ac}</div>'
           '<div class="tarama-girdiler">'
           '<div class="tg"><label for="ek-or-tur">Ölçü</label><div class="tg-satir"><select id="ek-or-tur" data-ek="tur">'
           f'<option value="OR"{" selected" if o0[2] == "OR" else ""}>Olasılık oranı (OR)</option>'
           f'<option value="RR"{" selected" if o0[2] == "RR" else ""}>Risk oranı (RR, HR)</option></select></div></div>'
           + girdi("or", "v", "Oran", "0.2", "6", "0.01", o0[3], "×")
           + girdi("or", "p0", "Maruz kalmayanlarda risk (taban)", "0.1", "60", "0.1", o0[4], "%")
           + '</div><div class="tarama-kpi">'
           '<div class="kpi"><span class="kpi-ad">Maruz kalmayanlarda</span><span class="kpi-deger" data-c="p0">–</span>'
           '<span class="kpi-alt">taban risk</span></div>'
           '<div class="kpi"><span class="kpi-ad">Maruz kalanlarda</span><span class="kpi-deger" data-c="p1">–</span>'
           '<span class="kpi-alt">oranın karşılık geldiği risk</span></div>'
           '<div class="kpi"><span class="kpi-ad">Mutlak fark</span><span class="kpi-deger" data-c="fark">–</span>'
           '<span class="kpi-alt">yüzde puan</span></div></div>'
           '<p class="tarama-cumle" aria-live="polite"></p>'
           '<div class="yuzluk-cift" aria-hidden="true"><div><p class="yuzluk-ad">Maruz kalmayan 100 kişi</p><div class="yuzluk" data-yuzluk="p0"></div></div>'
           '<div><p class="yuzluk-ad">Maruz kalan 100 kişi</p><div class="yuzluk" data-yuzluk="p1"></div></div></div>'
           '<ul class="tarama-lejant"><li><span class="lj lj-yp"></span>Sonuç görülen</li><li><span class="lj lj-gn"></span>Sonuç görülmeyen</li></ul>'
           '<p class="not">Taban riskler, belirtilmedikçe, hesabı göstermek için seçilmiş varsayımsal değerlerdir; kendi değerinizi '
           'girebilirsiniz. Mutlak fark, ilişki tümüyle nedensel olsaydı beklenecek farktır; gözlemsel çalışmalarda gerçek etki daha küçük olabilir.</p></div>'
           '<p class="sim-js-yok">Çevirici için tarayıcıda JavaScript açık olmalı. Örnek: r=0,10 ise açıklanan varyans %1’dir; '
           'olasılık oranı 2,17 ve taban risk %30 ise maruz kalanlarda risk yaklaşık %48 olur.</p>'
           '<h3 class="tekrar-baslik"><span aria-hidden="true">🎯</span> Akılda kalsın</h3><ul class="akilda">'
           + "".join(f"<li data-ara>{md(x)}</li>" for x in A.ETKI_AKILDA) + "</ul>")
etki = dict(id="etki", label="Etki büyüklüğü çevirici",
            html=view("etki", "Etki büyüklüğü çevirici: sayı kaç kişi eder?", "Araçlar", etki_ic, data_baslik="Etki büyüklüğü çevirici"))


# ---------------------------------------------------------------- iki oyun destesi
def deste_html(vid, ad, ikon, veri, giris_metni, soru, birim, son, ilkeler, not_):
    baglam(vid, "", ad)
    for d, s, dg, ac, ot in veri:
        assert len(s) == 4 and 0 <= dg < 4 and ot in OTAD, d
    li = "".join(
        f'<li data-dogru="{dg}" data-oturum="{ot}" data-otad="{esc(OTAD[ot])}"><p class="za-durum" data-ara>{md(d)}</p>'
        + "".join(f'<span class="za-secenek">{md(x)}</span>' for x in s)
        + f'<p class="za-aciklama">{md(ac)}</p></li>' for d, s, dg, ac, ot in veri)
    return (f'<p class="giris-metin">{esc(giris_metni)} {len(veri)} {birim.lower()}, karışık sırayla.</p>'
            f'<div class="tahmin za-oyun" id="{vid}-oyun" data-za-ad="{vid}" data-soru="{esc(soru)}" data-birim="{esc(birim)}" data-son="{esc(son)}">'
            f'<h3><span aria-hidden="true">{ikon}</span> {esc(ad)}</h3>'
            '<div class="za-alan" aria-live="polite"></div>'
            '<button type="button" class="dugme za-basla">Başlat</button>'
            '<p class="sim-js-yok">Bu alıştırma için tarayıcıda JavaScript açık olmalı.</p>'
            f'<ol class="za-veri" hidden>{li}</ol></div>'
            '<h3 class="tekrar-baslik"><span aria-hidden="true">🎯</span> Bu alıştırmanın ilkeleri</h3><ul class="akilda">'
            + "".join(f"<li data-ara>{md(x)}</li>" for x in ilkeler) + f'</ul><p class="not">{esc(not_)}</p>')


IDDIA_ILKELER = [
    "Bir iddiayı duyduğunuzda üç şeyi sorun: ne ölçülmüş, hangi tasarımla, etki ne kadar büyük?",
    "Kullanım oranı, sorunlu kullanım oranı ve tanı aynı şey değildir.",
    "‘Hiç etkisi yok’ ile ‘kanıtlanmış neden’ arasında geniş bir alan vardır; verinin çoğu oradadır.",
    "Aileye belirsizliği söylemek, kanıtı olmayan bir kesinlik sunmaktan daha güven vericidir.",
]
iddialar = dict(id="iddialar", label="Doğru mu, abartı mı?",
                html=view("iddialar", "Doğru mu, abartı mı?", "Araçlar", deste_html(
                    "iddialar", "Doğru mu, abartı mı?", "🧪", A.IDDIALAR,
                    "Haberlerde, toplantılarda ve poliklinikte sık duyulan iddialar. Her biri için kanıtla en uyumlu değerlendirmeyi seçin; "
                    "açıklama ve kaynak hemen ardından açılır.",
                    "Hangi değerlendirme kanıtla en uyumlu?", "İddia",
                    "Kaçırdığınız iddiaların oturumlarına dönmek iyi bir tekrar olur.", IDDIA_ILKELER,
                    "Değerlendirmeler Kasım 2026 itibarıyla yayımlanmış kanıta dayanır; yeni çalışmalarla değişebilir.")))
zor_anlar = dict(id="zor-anlar", label="Zor anlar",
                 html=view("zor-anlar", "Zor anlar: en uygun yanıt hangisi?", "Araçlar", deste_html(
                     "zor-anlar", "Zor anlar", "🧯", A.ZOR_ANLAR,
                     "Poliklinikte ekran konusu açıldığında karşılaşılan kurgusal anlar. Her durumda en uygun yanıtı seçin; açıklama ve "
                     "ilgili oturum hemen ardından açılır.",
                     "En uygun yanıt hangisi?", "Durum",
                     "Gerçek klinikte tek bir doğru yanıt nadirdir; durumlar ilkeleri tartışmak için sadeleştirildi.", A.ZOR_ANLAR_ILKELER,
                     "Durumlar kurgusaldır ve ilkeleri tartışmak için sadeleştirilmiştir."), data_baslik="Zor anlar"))

# ---------------------------------------------------------------- medya öyküsü çalışma sayfası
baglam("medya-oykusu", "", "Medya öyküsü ve aile planı")
bolum_html = []
for fid, fbas, fipucu, alanlar in A.FORM_BOLUMLER:
    ic = []
    for k, et, tur, ek in alanlar:
        if tur == "metin":
            ic.append(f'<label class="alt-etiket" for="f-{k}">{esc(et)}</label><textarea id="f-{k}" data-form="{k}" rows="{ek}"></textarea>')
        elif tur == "satir":
            ic.append(f'<label class="alt-etiket" for="f-{k}">{esc(et)}</label><input id="f-{k}" type="text" data-form="{k}" placeholder="{esc(ek)}">')
        elif tur == "secim":
            kutu = "".join(f'<label class="secim"><input type="checkbox" value="{esc(x)}"> {esc(x)}</label>' for x in ek)
            sayac = f'<p class="kaynak-sayi kucuk" data-grup-sayi="{k}" aria-live="polite"></p>' if k == "kontrol" else ""
            ic.append(f'<p class="alt-etiket">{esc(et)}</p><div class="secim-grup" data-form-grup="{k}" role="group" aria-label="{esc(et)}">{kutu}</div>{sayac}')
        elif tur == "ayirici":
            satir = []
            for i in range(1, ek + 1):
                yer = A.FORM_DD_YER[i - 1]
                satir.append(f'<div class="dd-satir"><label class="gizli" for="dd-ad-{i}">Açıklama {i}</label>'
                             f'<input class="dd-ad" id="dd-ad-{i}" type="text" placeholder="{esc(yer)}">'
                             f'<label class="gizli" for="dd-y-{i}">Açıklama {i} olasılığı (yüzde)</label>'
                             f'<input class="dd-yuzde" id="dd-y-{i}" type="number" min="0" max="100" step="1" inputmode="numeric" placeholder="%"></div>')
            ic.append(f'<div class="dd">{"".join(satir)}</div><p class="dd-toplam" aria-live="polite">Toplam: –</p>')
        elif tur == "dongu":
            halka = "".join(f'<div class="dongu-kutu"><label class="gizli" for="dg-{i}">{esc(A.FORM_DONGU_YER[i - 1])}</label>'
                            f'<textarea class="dongu-halka" id="dg-{i}" rows="3" placeholder="{esc(A.FORM_DONGU_YER[i - 1])}"></textarea></div>'
                            + ('<span class="dongu-ok" aria-hidden="true">→</span>' if i < ek else
                               '<span class="dongu-ok dongu-don" aria-hidden="true">↺ başa döner</span>')
                            for i in range(1, ek + 1))
            ic.append(f'<div class="dongu-izgara">{halka}</div>')
    bolum_html.append(f'<fieldset class="form-alan form-bolum" id="fb-{fid}"><legend><span class="fb-ad">{esc(fbas)}</span></legend>'
                      f'<p class="form-ipucu">{esc(fipucu)}</p>{"".join(ic)}</fieldset>')
# örnek, formdaki seçeneklerle birebir uyuşmalı
_secenekler = {k: ek for _, _, _, al in A.FORM_BOLUMLER for k, _, tur, ek in al if tur == "secim"}
for k, v in A.FORM_ORNEK.items():
    if k in _secenekler:
        assert all(x in _secenekler[k] for x in v), (k, [x for x in v if x not in _secenekler[k]])
assert sum(int(y) for _, y in A.FORM_ORNEK["dd"]) == 100
form_ic = ('<p class="giris-metin">Medya öyküsünü ve aile planını tek sayfada toplamak için bir çalışma kâğıdı: cihazlar, tipik gün, '
           'içerik, işlev, denetim kaybı, riskler ve yararlar, olasılıkları %100’e tamamlanan açıklamalar, döngü ve ölçülebilir '
           'tek hedef. Doldurdukça otomatik kaydedilir; yazdırabilir ya da PDF olarak kaydedebilirsiniz. Ayrıntı için '
           '<a href="#/oturum-12">Oturum 12</a>.</p>'
           '<aside class="uyari"><strong>Gerçek hasta bilgisi girmeyin.</strong> Ad, doğum tarihi, okul ya da adres gibi kimliği belli '
           'eden bilgiler yazmayın. Veriler yalnızca bu tarayıcıda saklanır, sunucuya gönderilmez.</aside>'
           '<div class="form-dugmeler"><button type="button" class="dugme dugme-ikincil form-ornek">Örnek vakayı yükle</button>'
           '<button type="button" class="dugme form-yazdir">Yazdır / PDF</button>'
           '<button type="button" class="dugme dugme-ikincil form-kopyala">Metni kopyala</button>'
           '<button type="button" class="sina-sifirla form-temizle">Formu temizle</button>'
           '<span class="form-durum kucuk" aria-live="polite"></span></div>'
           f'<p class="kucuk form-ornek-ad">Örnek: {esc(A.FORM_ORNEK_AD)}</p>'
           f'<form class="formulasyon" id="formulasyon" autocomplete="off" data-ornek="{esc(json.dumps(A.FORM_ORNEK, ensure_ascii=False))}">'
           f'{"".join(bolum_html)}</form>'
           '<div class="form-baski" aria-hidden="true"></div>')
medya = dict(id="medya-oykusu", label="Medya öyküsü ve aile planı",
             html=view("medya-oykusu", "Medya öyküsü ve aile planı", "Araçlar", form_ic))

# ---------------------------------------------------------------- kavram kartları
baglam("kavramlar", "", "Kavram kartları")
kav_li = []
for i, (terim, tanim, ornek, ots) in enumerate(A.KAVRAMLAR):
    assert all(n in OTAD for n in ots), terim
    bag = ", ".join(f'<a href="#/oturum-{n}">Oturum {n}</a>' for n in ots)
    kav_li.append(f'<li class="kavram" id="kavram-{i}" data-id="kavram-{i}" data-ara><p class="kavram-terim">{esc(terim)}</p>'
                  f'<p class="kavram-tanim">{md(tanim)}</p><p class="kavram-ornek"><span class="guncel-etiket">Klinikte</span> '
                  f'{md(ornek)}</p><p class="ders-ref">{bag}</p></li>')
kavram_ic = ('<p class="giris-metin">Rehberdeki temel kavramlar, kendi tanımlarımızla. Kartı çevirin, bildiklerinizi işaretleyin; '
             'bilmedikleriniz daha sık karşınıza çıkar. Boşluk tuşu kartı çevirir.</p>'
             '<div class="kart-araclar"><button type="button" class="dugme dugme-ikincil kart-karistir">Karıştır</button>'
             '<button type="button" class="sina-sifirla kart-sifirla">Bilinenleri sıfırla</button></div>'
             '<div class="kart-sahne" aria-live="polite"></div><p class="kart-ilerleme"></p>'
             '<p class="sim-js-yok">Kartlar için tarayıcıda JavaScript açık olmalı; aşağıdaki sözlük JavaScript olmadan da okunur.</p>'
             f'<h3 class="tekrar-baslik">Kavram sözlüğü <span class="sayi">{len(A.KAVRAMLAR)}</span></h3>'
             f'<ul class="kavramlar">{"".join(kav_li)}</ul>')
kavramlar = dict(id="kavramlar", label="Kavram kartları", html=view("kavramlar", "Kavram kartları", "Araçlar", kavram_ic))

# ---------------------------------------------------------------- Türkiye notları
baglam("turkiye", "", "Türkiye notları")
tr_bloklar = []
for o in O.OTURUMLAR:
    maddeler = [x[3:] for x in o["klinik"] if x.startswith("TR ")]
    if not maddeler:
        continue
    tr_bloklar.append(f'<section class="tema" aria-labelledby="tr-{o["no"]}-b"><h3 id="tr-{o["no"]}-b"><span class="tema-no">{o["no"]}</span> '
                      f'<a href="#/oturum-{o["no"]}/klinik">{esc(o["kisa"])}</a></h3><ul class="crs-liste">'
                      + "".join(f"<li data-ara>{md(m)}</li>" for m in maddeler) + "</ul></section>")
sozluk = "".join(f'<div class="tr-terim" data-ara><dt>{esc(t)}</dt><dd>{md(a)}</dd></div>' for t, a in A.TURKIYE_SOZLUK)
turkiye_ic = (f'<p class="giris-metin" data-ara>{md(A.TURKIYE_GIRIS)}</p>'
              f'<h3 class="tekrar-baslik">Mevzuat ve başvuru sözlüğü</h3><dl class="tr-sozluk">{sozluk}</dl>'
              f'<h3 class="tekrar-baslik">Oturumlara göre notlar <span class="sayi">{sum(v["tr"] for v in oturum_views)}</span></h3>'
              + "".join(tr_bloklar))
turkiye = dict(id="turkiye", label="Türkiye notları",
               html=view("turkiye", "Türkiye notları: veri, mevzuat ve başvuru yolları", "Araçlar", turkiye_ic,
                         data_baslik="Türkiye notları"))

# ---------------------------------------------------------------- tekrar
baglam("tekrar", "", "Karışık test")
n_soru = sum(len(o["sorular"]) for o in O.OTURUMLAR)
akil = "".join(f'<li><a href="#/oturum-{o["no"]}">Oturum {o["no"]}</a> {md(o["akilda"])}</li>' for o in O.OTURUMLAR)
tekrar_ic = ('<div class="karisik" id="karisik"><h3><span aria-hidden="true">🎲</span> Karışık test</h3>'
             f'<p>Bütün oturumların {n_soru} vaka sorusu karışık sırayla. Yanıtınızı verin; açıklama hemen ardından açılır.</p>'
             '<div class="karisik-alan" aria-live="polite"></div><p class="karisik-dugmeler">'
             f'<button type="button" class="dugme karisik-basla" data-tur="test">Testi başlat ({n_soru} soru)</button></p></div>'
             '<h3 class="tekrar-baslik"><span aria-hidden="true">🎯</span> Akılda kalsın: oturum oturum</h3>'
             f'<ul class="akilda akilda-kucuk akilda-liste">{akil}</ul>')
tekrar = dict(id="tekrar", label="Karışık test", html=view("tekrar", "Karışık test ve hızlı tekrar", "Araçlar", tekrar_ic,
                                                           data_baslik="Karışık test"))

# ---------------------------------------------------------------- giriş
baglam("giris", "", "Giriş")
kesim_kartlari = {k: [] for k in O.KESIMLER}
for v in oturum_views:
    kesim_kartlari[v["kesim"]].append(
        f'<li><a class="kart" href="#/{v["id"]}" data-kart="{v["id"]}"><span class="kart-no" aria-hidden="true">{v["no"]}</span>'
        f'<span class="kart-govde"><span class="kart-ust">Oturum {v["no"]}</span><span class="kart-baslik">{esc(v["baslik"])}</span>'
        f'<span class="kart-slogan">{md(v["slogan"])}</span><span class="kart-meta">{v["n_fikir"]} ana fikir · '
        f'{v["n_soru"]} vaka sorusu</span><span class="kart-durum" data-durum="{v["id"]}"></span></span></a></li>')
kesim_bolumleri = "".join(
    f'<section aria-labelledby="kes-{k}-b"><h2 id="kes-{k}-b" class="bolum-baslik">{esc(ad)}</h2><ol class="kartlar">'
    f'{"".join(kesim_kartlari[k])}</ol></section>' for k, ad in O.KESIMLER.items())
ARAC_LISTE = [
    ("etki", "🧮", "Etki büyüklüğü çevirici", "Bir korelasyonun ya da risk oranının 100 kişide neye karşılık geldiğini görün."),
    ("iddialar", "🧪", "Doğru mu, abartı mı?", f"Sık duyulan {len(A.IDDIALAR)} iddiayı kanıtla karşılaştırın."),
    ("zor-anlar", "🧯", "Zor anlar", f"{len(A.ZOR_ANLAR)} kurgusal durumda en uygun yanıtı seçin."),
    ("medya-oykusu", "✎", "Medya öyküsü ve aile planı", "Cihazdan hedefe on başlıklı, yazdırılabilir çalışma sayfası."),
    ("kavramlar", "🃏", "Kavram kartları", f"{len(A.KAVRAMLAR)} temel kavram, kendi tanımlarımızla."),
    ("turkiye", "🇹🇷", "Türkiye notları", "TÜİK verisi, 7578 sayılı Kanun, yaş doğrulama ve başvuru hatları tek sayfada."),
    ("tekrar", "🎲", "Karışık test", f"{n_soru} vaka sorusu karışık sırayla."),
]
arac_kartlari = "".join(
    f'<li><a class="kart kart-arac" href="#/{i}"><span class="kart-no" aria-hidden="true">{ik}</span><span class="kart-govde">'
    f'<span class="kart-baslik">{esc(ad)}</span><span class="kart-slogan">{esc(ac)}</span></span></a></li>'
    for i, ik, ad, ac in ARAC_LISTE) + (
    '<li><a class="kart kart-arac" href="sunum/"><span class="kart-no" aria-hidden="true">▶</span><span class="kart-govde">'
    '<span class="kart-baslik">Sunum</span><span class="kart-slogan">Rehberin çıkış noktası olan 23 slaytlık, 20 dakikalık ders sunumu.</span></span></a></li>')
giris_ic = f"""
<div class="kahraman">
  <p class="ust-baslik">Kanıt, klinik ve mevzuat rehberi · Kasım 2026</p>
  <h1 tabindex="-1">Dijital Çağda Gençlik</h1>
  <p class="alt-baslik">Brain rot mu? Ekranlar, ergenler ve çocuk psikiyatrisi</p>
  <p class="kahraman-metin" data-ara>Sosyal medya, oyun, kısa video ve yapay zekâ sohbet botları çocukların ve ergenlerin gündelik
  yaşamının parçası. Bu rehber “zararlı mı?” sorusunu parçalarına ayırıyor: kim için, hangi kullanım, hangi sonuç ve ne büyüklükte?
  On üç oturumda güncel kanıtı, ders kitaplarının yaklaşımını, Türkiye’deki veriyi ve 2026’da yürürlüğe giren yaş sınırı
  düzenlemelerini poliklinikte kullanılabilir bir çerçeveye çeviriyor.</p>
  <div class="mesajlar"><p class="mesaj" data-ara>Kronometreye değil, kontrol kaybına bakın.</p>
  <p class="mesaj" data-ara>Beyin çürümez; neyi tekrar ederseniz onda ustalaşır.</p></div>
  <p class="kahraman-dugmeler"><a class="dugme" href="#/oturum-1">Oturum 1’den başla <span aria-hidden="true">→</span></a>
  <a class="dugme dugme-ikincil" href="#/etki">Etki büyüklüğü çevirici</a> <a class="dugme dugme-ikincil" href="#/iddialar">Doğru mu, abartı mı?</a>
  <a class="dugme dugme-ikincil" href="#/medya-oykusu">Medya öyküsü sayfası</a></p>
  <div class="kahraman-kpi">
    <div class="kpi"><span class="kpi-deger">%91,3</span><span class="kpi-alt">Türkiye’de 6–15 yaşta internet kullanımı {md("[@tuik2024]")}</span></div>
    <div class="kpi"><span class="kpi-deger">%66,1</span><span class="kpi-alt">aynı yaş grubunda sosyal medya kullanımı {md("[@tuik2024]")}</span></div>
    <div class="kpi"><span class="kpi-deger">%11</span><span class="kpi-alt">ergenlerde sorunlu sosyal medya kullanımı, 44 ülke {md("[@hbsc2024]")}</span></div>
    <div class="kpi"><span class="kpi-deger">15 yaş</span><span class="kpi-alt">Türkiye’de sosyal ağ için alt sınır, 1 Kasım 2026 {md("[@kanun7578]")}</span></div>
  </div>
  <aside class="yeni-not"><strong>Bu rehber, aynı adlı ders sunumunun genişletilmiş hâlidir.</strong> Ders kitaplarından alıntı ya da
  kitap vakası içermez; fikirler kendi sözcüklerimizle yazıldı, vakalar kurgusaldır. Her sayısal bulgunun kaynağı metinde ve
  <a href="#/kaynakca">kaynakçada</a> gösterildi. <a href="sunum/">Sunumu aç</a>.</aside>
</div>
<section class="ilerlemem" id="ilerlemem" hidden aria-labelledby="ilerleme-b"><h2 id="ilerleme-b" class="bolum-baslik">İlerlemem</h2>
<div class="ilerleme-kutular"></div>
<p class="kucuk">İlerleme yalnızca bu tarayıcıda saklanır. <button type="button" class="sina-sifirla hepsini-sil">Bütün ilerlemeyi sil</button></p></section>
<section class="kurallar kullanim" aria-labelledby="kurallar-b"><h2 id="kurallar-b" class="bolum-baslik">Nasıl kullanılır?</h2>
<ol><li data-ara><span class="kural-no">1</span> Oturumu açın: genel bakıştaki üç soruyu kendi pratiğinizle yanıtlayın, sonra ana fikirleri ve klinik karşılığını okuyun.</li>
<li data-ara><span class="kural-no">2</span> “Kitaplar ne diyor?” ve “Tartışmalı noktalar” kısımlarında ders kitaplarının yaklaşımını güncel yayınlarla karşılaştırın.</li>
<li data-ara><span class="kural-no">3</span> Vaka sorularıyla kendinizi sınayın; çeviriciyi, iddia destesini ve çalışma sayfasını seminerde ya da poliklinikte kullanın.</li></ol></section>
{kesim_bolumleri}
<section aria-labelledby="arac-b"><h2 id="arac-b" class="bolum-baslik">Araçlar</h2><ol class="kartlar">{arac_kartlari}</ol></section>
"""
giris = dict(id="giris", label="Giriş",
             html=f'<section class="view aktif" id="v-giris" data-view="giris" data-baslik="Giriş" aria-label="Giriş">{giris_ic}</section>')

# ---------------------------------------------------------------- kaynakça (en son: kullanım bilgisi gerekiyor)
ARAC_VIDS = ["etki", "iddialar", "zor-anlar", "medya-oykusu", "kavramlar", "turkiye", "tekrar"]
SIRA = ["giris"] + [v["id"] for v in oturum_views] + ARAC_VIDS
ETIKET = {"giris": "Giriş", "etki": "Etki büyüklüğü çevirici", "iddialar": "Doğru mu, abartı mı?", "zor-anlar": "Zor anlar",
          "medya-oykusu": "Medya öyküsü sayfası", "kavramlar": "Kavram kartları", "turkiye": "Türkiye notları", "tekrar": "Karışık test"}
ETIKET.update({v["id"]: f'Oturum {v["no"]}' for v in oturum_views})


def kaynak_li(k):
    r = KAYNAK[k]
    ek = []
    if r.get("doi"):
        ek.append(f'<a href="https://doi.org/{esc(r["doi"])}" target="_blank" rel="noopener">doi:{esc(r["doi"])}</a>')
    if r.get("pmid"):
        ek.append(f'<a href="https://pubmed.ncbi.nlm.nih.gov/{r["pmid"]}/" target="_blank" rel="noopener">PMID {r["pmid"]}</a>')
    if r.get("url"):
        alan = re.sub(r"^https?://(www\.)?([^/]+).*$", r"\2", r["url"])
        ek.append(f'<a href="{esc(r["url"])}" target="_blank" rel="noopener">{esc(alan)}</a>')
    yerler = sorted(KULLANIM.get(k, []), key=lambda y: SIRA.index(y[0]) if y[0] in SIRA else 99)
    gor = []
    for vid, ad, et in yerler:
        hedef = f"#/{vid}/{ad}" if ad else f"#/{vid}"
        if hedef not in [g[0] for g in gor]:
            gor.append((hedef, ETIKET.get(vid, et)))
    # aynı oturumun birden çok adımı tek bağlantıya iner
    tek = []
    for h, e in gor:
        if e not in [t[1] for t in tek]:
            tek.append((h, e))
    geri = (' <span class="kaynak-geri">Geçtiği yer: ' + ", ".join(f'<a href="{h}">{esc(e)}</a>' for h, e in tek) + "</span>") if tek else ""
    return f'<li id="k-{k}" data-ara>{esc(r["metin"])} {" · ".join(ek)}{geri}</li>'


KULLANILAN = [k for k in KAYNAK if k in KULLANIM]
GRUPLAR = [("makale", "Makaleler"), ("kitap", "Kitaplar"), ("rapor", "Raporlar ve kurum belgeleri"),
           ("mevzuat", "Mevzuat ve resmî duyurular"), ("haber", "Haberler ve sözlük duyuruları")]
assert all(KAYNAK[k]["tur"] in dict(GRUPLAR) for k in KULLANILAN)
grup_html, sayilar = [], {}
for tur, ad in GRUPLAR:
    ks = sorted([k for k in KULLANILAN if KAYNAK[k]["tur"] == tur], key=lambda k: KAYNAK[k]["metin"].lower())
    sayilar[tur] = len(ks)
    grup_html.append(f'<section class="kaynak-grup"><h3>{esc(ad)} <span class="sayi">{len(ks)}</span></h3><ol class="kaynaklar">'
                     + "".join(kaynak_li(k) for k in ks) + "</ol></section>")
n_pm = sum(1 for k in KULLANILAN if KAYNAK[k].get("pmid"))
n_2025 = sum(1 for k in KULLANILAN if re.search(r"\b202[56]\b", KAYNAK[k]["metin"]))
kay_ic = (f'<p class="giris-metin">Rehberde anılan {len(KULLANILAN)} kaynak; {n_2025} tanesi 2025–2026 tarihli. '
          f'{n_pm} makalenin künyesi Kasım 2026’da PubMed kayıtlarından, PubMed’de dizinlenmeyen makaleler yayıncı (Crossref) '
          'kayıtlarından, mevzuat Resmî Gazete metinlerinden, raporlar ve duyurular yayımlayan kurumun sayfasından doğrulandı. '
          'Her kaynağın yanında bağlantısı ve rehberde geçtiği yerler var.</p>'
          '<p class="kaynak-ara"><label for="kaynak-suz">Kaynakçada süz</label>'
          '<input id="kaynak-suz" type="search" placeholder="Yazar, yıl ya da başlık" autocomplete="off"></p>'
          '<p class="kaynak-sonuc" aria-live="polite"></p>' + "".join(grup_html))
kaynakca = dict(id="kaynakca", label="Kaynakça", html=view("kaynakca", "Kaynakça", "Araçlar", kay_ic))

ORDER = [giris] + oturum_views + [etki, iddialar, zor_anlar, medya, kavramlar, turkiye, tekrar, kaynakca]


# ---------------------------------------------------------------- gezinti
def nav_item(vid, no, ad):
    return (f'<li><a href="#/{vid}" data-nav="{vid}"><span class="nav-no" aria-hidden="true">{esc(no)}</span>'
            f'<span class="nav-ad">{esc(ad)}</span><span class="nav-durum" data-durum-nav="{vid}"></span></a></li>')


nav = ('<nav class="yan" id="yan" aria-label="Rehber içeriği"><div class="yan-ic">'
       '<ol class="nav-liste"><li><a href="#/" data-nav="giris"><span class="nav-no" aria-hidden="true">⌂</span>'
       '<span class="nav-ad">Giriş</span></a></li></ol>'
       + "".join(f'<p class="nav-baslik">{esc(ad)}</p><ol class="nav-liste">'
                 + "".join(nav_item(v["id"], str(v["no"]), v["kisa"]) for v in oturum_views if v["kesim"] == k) + "</ol>"
                 for k, ad in O.KESIMLER.items())
       + '<p class="nav-baslik">Araçlar</p><ol class="nav-liste">'
       + nav_item("etki", "🧮", "Etki büyüklüğü çevirici") + nav_item("iddialar", "🧪", "Doğru mu, abartı mı?")
       + nav_item("zor-anlar", "🧯", "Zor anlar") + nav_item("medya-oykusu", "✎", "Medya öyküsü sayfası")
       + nav_item("kavramlar", "🃏", "Kavram kartları") + nav_item("turkiye", "TR", "Türkiye notları")
       + nav_item("tekrar", "🎲", "Karışık test") + nav_item("kaynakca", "§", "Kaynakça")
       + '<li><a href="sunum/"><span class="nav-no" aria-hidden="true">▶</span><span class="nav-ad">Sunum</span></a></li></ol>'
       '<p class="ilerleme" data-ilerleme></p></div></nav>')

DESC = ("Çocuk ve ergenlerde sosyal medya, oyun, kısa video ve yapay zekâ sohbet botları üzerine etkileşimli rehber: 13 oturumda güncel "
        "kanıt, ders kitaplarının yaklaşımı, Türkiye verisi ve 2026 yaş sınırı düzenlemeleri; etki büyüklüğü çevirici, iddia destesi, "
        "kurgusal vaka soruları ve medya öyküsü çalışma sayfası.")

page = f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{AD} · Doç. Dr. Miraç Barış Usta</title>
<meta name="description" content="{esc(DESC)}">
<meta name="author" content="Miraç Barış Usta">
<meta name="theme-color" content="#f6f5f2">
<meta property="og:title" content="{AD}">
<meta property="og:description" content="{esc(DESC)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{ADRES}">
<link rel="canonical" href="{ADRES}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Lora:ital,wght@0,600;0,700;1,500&amp;display=swap">
<link rel="stylesheet" href="rehber.css">
<script src="rehber.js" defer></script>
</head>
<body>
<a class="atla" href="#icerik">İçeriğe geç</a>
<header class="ust">
  <a class="geri" href="https://miracbarisusta.com/rehberler/"><span aria-hidden="true">←</span> Rehberler</a>
  <a class="marka" href="#/">Dijital Çağda Gençlik</a>
  <div class="ara" role="search">
    <label class="gizli" for="ara">Rehberde ara</label>
    <input id="ara" type="search" placeholder="Rehberde ara…" autocomplete="off" aria-controls="ara-sonuc">
    <div class="ara-sonuc" id="ara-sonuc" hidden></div>
  </div>
  <button type="button" class="menu-dugme" aria-controls="yan" aria-expanded="false">Oturumlar</button>
</header>
<div class="duzen">
{nav}
<main id="icerik" tabindex="-1">
{"".join(v["html"] for v in ORDER)}
</main>
</div>
<footer class="alt">
  <p><strong>Hazırlayan:</strong> Doç. Dr. Miraç Barış Usta · Kasım 2026 · <a href="https://miracbarisusta.com">miracbarisusta.com</a></p>
  <p>Eğitim amaçlıdır; bilgiler Kasım 2026 itibarıyladır ve bu alanda kanıt ile mevzuat hızla değişmektedir. Vakalar kurgusaldır;
  çeviricideki taban riskler varsayımsaldır. Mevzuat özetleri hukuki görüş değildir. Tanı ve tedavi kararları için güncel kılavuzlara,
  yürürlükteki mevzuata ve klinik değerlendirmeye başvurun.</p>
  <p>Ders kitaplarından alıntı içermez; anılan kitapların, makalelerin ve raporların hakları sahiplerine aittir.</p>
  <p>© 2026 Miraç Barış Usta · <a href="https://github.com/hypothermia15/brain-rot-mu/blob/main/LICENSE">Kullanım koşulları</a> ·
  <a href="sunum/">Sunum</a></p>
</footer>
<div class="atif-pop" id="atif-pop" role="dialog" aria-label="Kaynak" hidden></div>
</body>
</html>
"""
(KOK / "index.html").write_text(page, encoding="utf-8")
kullanilmayan = sorted(k for k in KAYNAK if k not in KULLANIM)
dagilim = [0, 0, 0, 0]
for q in _tum_sorular:
    dagilim[karistir_soru(q)[1]] += 1
print(f"{len(ORDER)} görünüm, {len(oturum_views)} oturum, {n_soru} vaka sorusu (doğru şık dağılımı A–D: {dagilim}), "
      f"{len(A.KAVRAMLAR)} kavram, {len(A.IDDIALAR)} iddia, {len(A.ZOR_ANLAR)} zor an, {sum(v['tr'] for v in oturum_views)} TR notu, "
      f"{len(KULLANILAN)} kaynak ({sayilar}; 2025–2026: {n_2025}), {page.count('class=\"atif\"')} atıf → {KOK / 'index.html'} ({len(page) // 1024} KB)")
if BILINMEYEN:
    print("BİLİNMEYEN ATIF:", ", ".join(sorted(BILINMEYEN)))
if kullanilmayan:
    print("Kullanılmayan kaynak (kaynakçaya girmedi):", ", ".join(kullanilmayan))
