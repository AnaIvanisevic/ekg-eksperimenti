#!/usr/bin/env python3
"""Cache-busting prije svakog pusha.

GitHub Pages salje max-age=600, pa preglednik moze drzati staru stranicu uz
nove podatke ili obrnuto. Ova skripta upise svjezi timestamp u svaku poveznicu
na podatke, .js i .css, pa preglednik dohvati novu datoteku.

Pokretanje iz korijena projekta:  python3 alati/verzija.py
"""
import re
import sys
import time
from pathlib import Path

KORIJEN = Path(__file__).resolve().parent.parent
VERZIJA = str(int(time.time()))

# (uzorak, u kojim datotekama trazimo)
UZORCI = [
    (re.compile(r'(fetch\("[^"?]+\.json)(\?v=\d+)?(")'), '*.html'),
    (re.compile(r'(<script src="[^"?]+\.js)(\?v=\d+)?(")'), '*.html'),
    (re.compile(r'(<link rel="stylesheet" href="(?!https?:)[^"?]+\.css)(\?v=\d+)?(")'), '*.html'),
]


def main() -> int:
    promijenjeno = 0
    for uzorak, maska in UZORCI:
        for put in sorted(KORIJEN.glob(maska)):
            tekst = put.read_text(encoding='utf-8')
            novi, n = uzorak.subn(lambda m: m.group(1) + '?v=' + VERZIJA + m.group(3), tekst)
            if n and novi != tekst:
                put.write_text(novi, encoding='utf-8')
                promijenjeno += n
                print(f'  {put.relative_to(KORIJEN)}: {n} poveznica')
    if promijenjeno:
        print(f'Verzija {VERZIJA} upisana u {promijenjeno} poveznica.')
    else:
        print('Nista za promijeniti.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
