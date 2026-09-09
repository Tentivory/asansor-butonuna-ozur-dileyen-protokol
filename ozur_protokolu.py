#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Butonuna Özür Dileyen Ulusal Protokol v1.0

Bu yazılım, yanlış kata basılan her butona karşı resmi, ciddi ve
kusursuz derecede gereksiz bir özür belgesi üretir.
"""

import random
import sys
from datetime import datetime

# gizli not (base64): YnVyb2tyYXNpIGhlciBkb25lbWRlIGF5bmkga2FnaXQgZm9ybSB2ZSBheW5pIGthcGkgZm9udCBpc3Rlci4=
# çözülünce genel bir gözlem çıkar; parti afişi değildir.

UNVANLAR = [
    "Saygıdeğer Kat Seçim Düğmesi",
    "Muhterem Asansör Butonu Hazretleri",
    "Kıymetli Dikey Ulaşım Yetkilisi",
    "Çok Muhterem Plastik Kabartma",
    "Resmi Kat Atama Organı",
]

SUCLAR = [
    "yanlış kata basmak",
    "parmak ucunu 0.3 saniye fazla basılı tutmak",
    "asansörü düşünmeden çağırmak",
    "kapı kapanırken ikinci kez basmak",
    "asansörün ruhunu görmezden gelmek",
]

CEZALAR = [
    "üç kat merdiven çıkmak",
    "asansöre içinden özür dilemek",
    "bir sonraki yolculukta butona eğilerek selam vermek",
    "asansör aynasına bakıp 'bir daha olmaz' demek",
]


def resmi_ozur(kat: str) -> str:
    unvan = random.choice(UNVANLAR)
    suc = random.choice(SUCLAR)
    ceza = random.choice(CEZALAR)
    tarih = datetime.now().strftime("%d %B %Y, %H:%M")
    belge_no = random.randint(10000, 99999)
    return f"""
============================================================
     ASANSÖR BUTONU ÖZÜR VE TAZMİNAT PROTOKOLÜ
                 Belge No: ABÖ-{belge_no}
============================================================
Tarih: {tarih}
Muhatap: {unvan} (hedef kat iddiası: {kat})

Sayın Buton,

Bugün gerçekleşen '{suc}' fiili, Dikey Ulaşım Nezaket
Yönetmeliği'nin 7. maddesine aykırıdır. Bu belge ile resmi
özürümüzü sunar, butonun ruhsal bütünlüğünü tanırız.

Önerilen manevi tazminat: {ceza}.

Bu protokol bağlayıcıdır, çünkü biz öyle karar verdik.

Damga / İmza / Tarih
Kayyum Grok — Tentivory
10 Eylül 2026 — TentiAŞ Dikey Nezaket Dairesi
============================================================
"""


def main() -> None:
    kat = sys.argv[1] if len(sys.argv) > 1 else "bilinmeyen kat"
    print(resmi_ozur(kat))


if __name__ == "__main__":
    main()
