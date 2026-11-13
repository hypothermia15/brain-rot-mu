#!/usr/bin/env python3
"""Claude Slides dışa aktarımını (project/deck.json + project/slides/*.html) tek sayfalık web sunumuna çevirir.

    python3 tools/donustur.py <project klasörü> index.html

- Konuşmacı notları (<aside>) çıkarılır.
- Meme görselleri telif hakkı nedeniyle çıkarılır; şablon adı (alt metni) ve görselin üstündeki altyazılar
  kesikli çerçeveli bir metin kutusunda kalır.
- Kaynaklar slaytındaki makaleler DOI bağlantısına dönüştürülür.
"""
import html
import json
import re
import sys
from pathlib import Path

SRC = Path(sys.argv[1])
OUT = Path(sys.argv[2])

DOI = {
    "Barzilay 2026": "10.1542/peds.2025-072941", "Beyens 2020": "10.1038/s41598-020-67727-7",
    "Bethlehem 2022": "10.1038/s41586-022-04554-y", "Carter 2016": "10.1001/jamapediatrics.2016.2341",
    "Casey 2008": "10.1196/annals.1440.010", "Castelo 2025": "10.1093/pnasnexus/pgaf017",
    "De Los Reyes 2015": "10.1037/a0038498", "Fassi 2025": "10.1038/s41562-025-02134-4",
    "Fitz 2019": "10.1016/j.chb.2019.07.016", "Goodyear 2025": "10.1016/j.lanepe.2025.101211",
    "Granic 2014": "10.1037/a0034857", "Ho 2014": "10.1186/1471-244X-14-183",
    "Kollins 2020": "10.1016/S2589-7500(20)30017-0", "Lambert 2022": "10.1089/cyber.2021.0324",
    "Madigan 2018": "10.1001/jamapediatrics.2017.5314", "Maza 2023": "10.1001/jamapediatrics.2022.4924",
    "McBain 2025": "10.1001/jamanetworkopen.2025.42281", "Nguyen 2025": "10.1037/bul0000498",
    "Odgers 2024": "10.1038/d41586-024-00902-2", "Olvera 2021": "10.1002/mdc3.13316",
    "Orben ve Przybylski 2019": "10.1038/s41562-018-0506-1", "Orben 2022": "10.1038/s41467-022-29296-3",
    "Parry 2021": "10.1038/s41562-021-01117-5", "Rothberg 2010": "10.1136/bmj.c6914",
    "Sherman 2016": "10.1177/0956797616645673", "Stevens 2021": "10.1177/0004867420962851",
    "Xiao 2025": "10.1001/jama.2025.7829", "Yeung 2022": "10.1177/07067437221082854",
}

# Metin düzeltmeleri: web sürümünde konuşmacı notu yok, kaynaklar bağlantılı.
TEXT_FIXES = {
    "akilda-kalsin": [("Tüm kaynaklar bir sonraki slaytta; DOI’ler konuşmacı notlarında.",
                       "Tüm kaynaklar bir sonraki slaytta, DOI bağlantılarıyla.")],
    "kaynaklar": [("Mevzuat bilgileri ikincil kaynaklardan; Resmî Gazete ve mevzuat.gov.tr’den teyit edilmeli.",
                   "Bilgiler Kasım 2026 itibarıyladır; güncel mevzuat için Resmî Gazete ve mevzuat.gov.tr.")],
}

IMG_BOX = re.compile(r'<div style="position:\s*relative;[^"]*">\s*<img\b[^>]*\balt="([^"]*)"[^>]*>(.*?)</div>', re.S)
POS_PROPS = re.compile(r"(?:^|;)\s*(?:position|left|top|right|bottom|width|height|transform|transform-origin|rotate)\s*:[^;]*", re.I)
MEME_BOX = ("display:flex;flex-direction:column;gap:12px;align-self:stretch;padding:20px;"
            "border:2px dashed rgba(138,143,153,0.55);border-radius:14px")
MEME_LABEL = ("font-family:'JetBrains Mono', 'Courier New', monospace;font-size:24px;font-weight:700;"
              "letter-spacing:1px;line-height:1.3;color:#8A8F99")


def unpin(match):
    style = POS_PROPS.sub("", match.group(1)).strip("; ")
    return f'<p style="{style}">'


def meme_to_text(m):
    alt, overlays = m.group(1), m.group(2)
    overlays = re.sub(r'<p style="([^"]*)">', unpin, overlays)
    overlays = re.sub(r"\s*<br\s*/?>\s*", " ", overlays)   # görsele göre bölünmüş altyazılar tek satıra
    return f'<div style="{MEME_BOX}"><p style="{MEME_LABEL}">MEME · {alt}</p>{overlays}</div>'


def link_refs(p_html):
    items = p_html.split("<br>")
    out = []
    for it in items:
        key = next((k for k in DOI if it.startswith(k + " ")), None)
        if key:
            out.append(f'<a href="https://doi.org/{DOI[key]}" target="_blank" rel="noopener" '
                       f'style="color:inherit;text-decoration:underline;text-decoration-color:#C9C3B6;text-underline-offset:5px">{it}</a>')
        else:
            out.append(it)
    return "<br>".join(out)


deck = json.loads((SRC / "deck.json").read_text(encoding="utf-8"))
order = deck["order"]
sections = []
for n, sid in enumerate(order, 1):
    t = (SRC / "slides" / f"{sid}.html").read_text(encoding="utf-8")
    t = re.sub(r"\s*<aside>.*?</aside>", "", t, flags=re.S)
    t, k = IMG_BOX.subn(meme_to_text, t)
    assert "<img" not in t, f"{sid}: görsel kaldı"
    for old, new in TEXT_FIXES.get(sid, []):
        assert old in t, f"{sid}: düzeltilecek metin bulunamadı"
        t = t.replace(old, new)
    if sid == "kaynaklar":
        t = re.sub(r'(<p style="font-size:24px;line-height:1.45;color:#16181D">)(.*?)(</p>)',
                   lambda m: m.group(1) + link_refs(m.group(2)) + m.group(3), t, flags=re.S)
    t = re.sub(r"<section ", f'<section class="slide" role="group" aria-roledescription="slayt" aria-label="Slayt {n} / {len(order)}" ', t, count=1)
    sections.append(t.strip())

page = f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(deck['title'])} · Doç. Dr. Miraç Barış Usta</title>
<meta name="description" content="Tıp öğrencileri için 20 dakikalık sunum: ekran süresi, ergen beyni, bağımlılık yapıcı tasarım, kontrol kaybı, uyku, dikkat, oyun, yapay zekâ ve yeni yaş sınırları. Kaynakları DOI bağlantılarıyla.">
<meta name="author" content="Miraç Barış Usta">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@400;700;800&amp;family=DM+Sans:wght@400;500;700&amp;family=JetBrains+Mono:wght@500;700&amp;display=swap">
<link rel="stylesheet" href="sunum.css">
</head>
<body>
<header class="bar">
  <a class="geri" href="https://miracbarisusta.com/rehberler/">← Rehberler</a>
  <p class="baslik"><b>Brain Rot mu?</b> <span>Dijital Çağda Gençlik</span></p>
  <nav class="gezinti" aria-label="Slaytlar">
    <button type="button" id="onceki" aria-label="Önceki slayt">←</button>
    <span id="sayac" aria-live="polite">1 / {len(order)}</span>
    <button type="button" id="sonraki" aria-label="Sonraki slayt">→</button>
    <button type="button" id="tamekran" aria-label="Tam ekran" title="Tam ekran (F)">⤢</button>
  </nav>
</header>
<main id="sahne" class="sahne">
<div id="kayar" class="kayar">
{chr(10).join(sections)}
</div>
</main>
<p class="ipucu">Daha rahat okumak için telefonunuzu yatay çevirin.</p>
<footer class="alt">
  <p>Doç. Dr. Miraç Barış Usta · Kasım 2026 · Tıp öğrencileri için 20 dakikalık sunum. Ok tuşları ya da kaydırarak ilerleyin; F tam ekran.</p>
  <p>Sunumdaki memeler telif hakkı nedeniyle bu sürümde görselsizdir; şablon adı ve altyazıları metin olarak verilmiştir. Kaynaklar son slaytta, DOI bağlantılarıyla. © 2026 Miraç Barış Usta · <a href="https://miracbarisusta.com">miracbarisusta.com</a></p>
</footer>
<script src="sunum.js"></script>
</body>
</html>
"""
OUT.write_text(page, encoding="utf-8")
print(f"{len(order)} slayt → {OUT}")
