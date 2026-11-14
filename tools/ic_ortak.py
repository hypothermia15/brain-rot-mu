# -*- coding: utf-8 -*-
"""Oturum içerikleri için ortak tanımlar."""

KESIMLER = {
    "m": "I · Manzara",
    "k": "II · Kanıt",
    "r": "III · Riskler",
    "p": "IV · Kurallar",
    "c": "V · Klinik",
}

KITAP_ADLARI = {
    "lewis": "Lewis 6. baskı",
    "rutter": "Rutter 7. baskı",
    "iacapap": "IACAPAP 2.0",
    "williams": "Williams ve Hill",
    "haidt": "Haidt",
    "notlar": "Ders notlarımız",
}


def S(soru, secenekler, dogru, aciklama):
    """Kurgusal vaka sorusu: seçenekler yazım sırasıyla, dogru = doğru seçeneğin sıra numarası (0'dan)."""
    return dict(soru=soru, secenekler=secenekler, dogru=dogru, aciklama=aciklama)
