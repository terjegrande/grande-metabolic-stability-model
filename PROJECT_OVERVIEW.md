# Grande – Metabolic Stability Model  
Friction-Based Biological Dynamics

Dette prosjektet samler teori, simuleringer, data og kode for en friksjonsbasert modell for metabolsk stabilitet. Modellen kombinerer friksjon (ζ), kontrollsløyfer (L) og stabilitetssoner (S) for å beskrive hvordan biologiske systemer tåler, tilpasser seg eller kollapser under belastning.

---

## 🔹 Artikkelserie (0–5)

Alle artikler ligger i `articles/` og utgjør en sammenhengende teoretisk pakke:

- **Artikkel 0 – Introduksjon til Metabolsk Stabilitet**  
  Masteroversikt, ζ–L–S‑rammeverket, hysterese, separatrix, recovery‑logikk.

- **Artikkel 1 – Friksjonsmodellen**  
  Baseline‑, adaptiv og stress‑friksjon, matematiske former og parameterisering.

- **Artikkel 2 – Kontrollsystemer**  
  Negativ/positiv feedback, feedforward, adaptiv kontroll og regulering av friksjon.

- **Artikkel 3 – Faseoverganger**  
  Kritiske terskler, Monte Carlo‑analyse, stabilitetssoner og overgangsdynamikk.

- **Artikkel 4 – Kliniske implikasjoner**  
  Risiko, sykdomsforløp, behandlingsrespons og stabilitetsanalyse i kliniske forløp.

- **Artikkel 5 – Fremtidige anvendelser**  
  Wearables, AI‑overvåkning, personlig medisin og biomarkør‑integrasjon.

---

## 🔹 Notebooks

Notebookene i `notebooks/` genererer simuleringer, analyser og figurer brukt i artiklene:

- `metabolic_friction_main_clean.ipynb` – hovedsimulering av friksjonsmodellen  
- `simulate_substances.ipynb` – stoff‑ og parameterrespons, kontrollsløyfer  
- `monte_carlo.ipynb` – Monte Carlo‑analyse av stabilitet og faseoverganger  
- `figures_generator.ipynb` – genererer figurer til artiklene

---

## 🔹 Data og figurer

Datastrukturen er organisert slik:

- `data/raw/` – rådata  
- `data/processed/` – prosesserte datasett klare for analyse  
- `data/figures/` – figurer generert fra notebookene

---

## 🔹 Kode og modeller

Koden er organisert i moduler for å støtte videre utvikling:

- `code/` og `src/` – modellkomponenter, node‑funksjoner og analyseverktøy  
- `models/` – lagrede modellkonfigurasjoner og parametre  
- `scripts/` – hjelpe‑skript for kjøring, batch‑simuleringer og prosessering

---

## 🔹 Formål

Målet er å etablere en publiserbar, friksjonsbasert modell for metabolsk stabilitet som:

- kan brukes i forskning og klinisk analyse  
- kan kobles til wearables og sensordata  
- kan inngå i fremtidige AI‑systemer for kontinuerlig metabolsk overvåkning.
