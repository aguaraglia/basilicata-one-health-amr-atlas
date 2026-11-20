# Geografia pubblica - edizione Basilicata

La cartografia pubblica dell'edizione Basilicata comprende:

- `atlas_region.geojson`: confine regionale ISTAT 2026 (codice 17);
- `atlas_provinces.geojson`: 2 province ISTAT 2026: Potenza (076), Matera (077);
- `atlas_municipalities.geojson`: 131 comuni ISTAT al 1/1/2026.

Fonte: ISTAT, «Confini delle unità amministrative a fini statistici al 1° gennaio 2026», versione generalizzata (Limiti01012026_g.zip, SHA-256 in `metadata/SNAPSHOTS.tsv`), CC BY 4.0. Gli attributi dei DBF sono letti in UTF-8 e le coordinate sono convertite da EPSG:32632 a WGS84 da `scripts/build_istat_geography.py`.

Gli studi della letteratura curata stanno in layer distinti sotto `public/data/`. Nessuna struttura è un punto: nessuno studio incluso nomina un ospedale o un laboratorio da geocodificare, quindi nessuna richiesta a OSM Nominatim (`raw/nominatim/NOTE.md`). I macelli di Picerno e Abriola (42347197) non sono nominati e stanno sui poligoni comunali.
