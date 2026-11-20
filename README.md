# Basilicata One Health AMR Atlas

Edizione regionale `basilicata_amr_atlas`, pubblicata da Codex Vitae ETS sulla stessa
base dell'edizione Molise.

## Stato

La letteratura pubblicata con collegamento territoriale esplicito alla Basilicata
è un corpus molto piccolo. Ne restano 2 inclusi (20 novembre 2026), entrambi
sulla filiera alimentare avicola:

- Picerno e Abriola (Potenza): 1 studio (Campylobacter in due macelli avicoli non nominati, 2026);
- regione intera: 1 studio (Salmonella su campioni ufficiali di carne di pollo, 2021-2023, articolo del 2025).

Nessuna struttura è nominata e non ci sono coordinate di punto. I macelli di
Picerno e Abriola non sono nominati e stanno sui poligoni comunali ISTAT 2026.
Non è stata inviata alcuna richiesta a Nominatim.

Per scala: 0 strutture, 1 comune, 0 province, 1 regione. Per provincia: Potenza 1,
Matera 0, regione intera 1.

La gran parte della letteratura lucana proviene dall'IZS di Puglia e Basilicata
e non separa i dati della Basilicata, quindi non è contata. L'istituto ha sede
a Foggia: l'afferenza «Puglia e Basilicata» non è un'afferenza lucana.

L'edizione pubblica AR-ISS 2024 (copertura 88,8%, tre laboratori: San Carlo e
CROB a Potenza, Madonna delle Grazie a Matera, numerosità 30-211 isolati,
CC BY 4.0; attribuzione Istituto Superiore di Sanità) e AIFA Open Data 2024,
antibatterici J01 (CC BY 4.0; attribuzione Agenzia Italiana del Farmaco).
Non è stato trovato un rapporto ISTISAN o ISS regionale sulla Basilicata.

Sei layer (AMR umana, veterinaria, alimentare, ambientale, fauna selvatica,
contorno regionale):

- AMR umana: nessun elemento, nessuna evidenza pubblicata;
- AMR veterinaria: nessun elemento, nessuna evidenza pubblicata;
- AMR alimentare: 2 elementi (Picerno e Abriola; regione), 2 studi;
- AMR ambientale: nessun elemento, nessuna evidenza pubblicata;
- AMR nella fauna selvatica: nessun elemento, nessuna evidenza pubblicata;
- studi a scala regionale: nessun elemento (nessuno studio umano a scala regionale).

I layer vuoti e le aree senza segnaposto sono nessuna evidenza pubblicata,
non resistenza zero. Ogni popup cita lo studio e il DOI e ricorda che il
segnaposto è il luogo dello studio, non una prevalenza.

Confini ISTAT 2026 (131 comuni, 2 province, regione 17), letti in UTF-8.
Regione Basilicata, open data regionali, ASP Potenza, ASM Matera, AOR San Carlo,
CROB, ARPAB, il sito dell'IZS di Puglia e Basilicata e il PDF OsMed sono esclusi
o non disponibili: vedi `metadata/EXCLUDED_SOURCES.md`.

Il conteggio in homepage e in pubblicazioni legge
`public/data/literature-catalog.json` (2).

## Pagine

Sorgente su `main`. Il sito statico è pubblicato dal branch `gh-pages`
(GitHub Pages, cartella `/`). Nessun file `CNAME`. Analitica: GoatCounter
`https://atlanteamr.goatcounter.com/count`, come le edizioni Abruzzo, Lazio e Molise.

## Build locale

```bash
python3 -m http.server 8000
```

Aprire `http://localhost:8000/`.

Per rigenerare i dati pubblici servono gli input in `raw/` e, per i confini,
l'archivio ISTAT indicato in `metadata/SNAPSHOTS.tsv`. I DBF ISTAT si leggono
in UTF-8:

```bash
pip install -r requirements-geodata.txt
python3 scripts/build_istat_geography.py --source-root <Limiti01012026_g> --output-root public/geography
python3 scripts/build_literature_catalog.py
python3 scripts/build_study_evidence_layers.py
```
