# EKG eksperimenti — preglednik anotacija

Statična stranica za pregled EKG signala i anotacija iz baze BUT QDB, uz presude
modela razine A0 iz mjerenja v0.4. Bez frameworka i bez build koraka: otvoreni
HTML, CSS i JavaScript.

Živa stranica: *(upisati nakon uključivanja GitHub Pages)*

## Što stranica pokazuje

- **Cijela snimka** — sva četiri popisa ocjena kroz cijelu dužinu snimke, obojena po klasi.
- **EKG traka** — signal ondje gdje postoji, s EKG mrežom; klizač pomiče traku kroz snimku.
- **Anotacije** — poravnate ispod signala, na istoj vremenskoj osi.
- **Procjena prozora** — oznaka struke, presuda odabranog modela, prag njegovog folda i 18 SQI značajki.

## Struktura

```
index.html              cijela stranica (HTML, CSS i JS u jednoj datoteci)
podaci/anotacije.json   anotacije i signal (4 MB), dohvaća se iz stranice
alati/verzija.py        cache-busting prije pusha
```

## Tijek rada kod svake promjene

1. Uredi `index.html`.
2. Provjeri lokalno: `python3 -m http.server 8000`, pa otvori <http://127.0.0.1:8000>.
   Stranica **mora** ići preko poslužitelja — otvaranje datoteke dvoklikom ne radi,
   jer preglednik tada blokira dohvat `podaci/anotacije.json`.
3. `python3 alati/verzija.py`
4. `git add -A`, `git commit -m "<opis na hrvatskom>"`, `git push`
5. GitHub Pages objavi za 1–2 minute.

## Podaci

Signal i anotacije dolaze iz **Brno University of Technology ECG Quality Database
(BUT QDB)**, PhysioNet, DOI [10.13026/kah4-0w24](https://doi.org/10.13026/kah4-0w24),
licencija **CC BY 4.0**. Ta licencija dopušta dijeljenje i preradu uz navođenje
izvora, što ova stranica čini u odjeljku „Odakle su podaci".

U `podaci/anotacije.json` nalazi se 958 prozora od 5 sekundi (0,16 % trajanja
snimaka) i cjelovite anotacije za 15 snimaka. Cijele snimke nisu ovdje — svaka je
oko 178 MB.

## Mjerenja na stranici

Sve brojke koje stranica prikazuje izmjerene su, nijedna nije procijenjena:
presude modela čitaju se iz `predictions.csv` mjerenja v0.4, a SQI vrijednosti iz
`QRS_extended.csv`. Stranica ne računa ništa iznova.
