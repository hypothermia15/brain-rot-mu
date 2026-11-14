# -*- coding: utf-8 -*-
"""Dijital Çağda Gençlik rehberi: oturum içerikleri (üç parçadan birleştirilir).

Her oturum: no, kesim, kisa, baslik, slogan, bakis, sorun[3], fikirler[(başlık, metin)], klinik[str; "TR " ile başlayanlar Türkiye
notu], kitaplar[(kitap anahtarı, metin)], tartisma[(başlık, metin)], sorular[3], akilda ve isteğe bağlı cizelge (başlık, [(tarih, olay)]).
Metinlerde [@anahtar] biçimi tools/kaynaklar.json içindeki kaynağa bağlanır.
"""
from ic_ortak import KESIMLER, KITAP_ADLARI, S  # noqa: F401
from ic_bolum1 import OTURUMLAR_1
from ic_bolum2 import OTURUMLAR_2
from ic_bolum3 import OTURUMLAR_3

OTURUMLAR = OTURUMLAR_1 + OTURUMLAR_2 + OTURUMLAR_3
assert [o["no"] for o in OTURUMLAR] == list(range(1, len(OTURUMLAR) + 1))
