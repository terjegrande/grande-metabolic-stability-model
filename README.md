# Metabolic Stability Model — Friction-Based Biological Dynamics

Dette repositoriet inneholder hele prosjektet for utviklingen av en friksjonsbasert modell for metabolsk stabilitet. Modellen kombinerer friksjon, kontrollsløyfer og faseoverganger for å beskrive hvordan biologiske systemer opprettholder eller mister stabilitet under stress.

Prosjektet består av:
- en teoretisk artikkelserie (Artikkel 0–5)
- simulerings‑notebooks
- datastruktur for figurer, rådata og prosesserte data
- kode for modellkomponenter og analyse

---

## 📚 Artikkelserie (0–5)

Alle artiklene ligger i `articles/` og utgjør en komplett teoretisk gjennomgang av modellen.

| Artikkel | Tittel | Innhold |
|---------|--------|---------|
| **0** | Introduksjon til Metabolsk Stabilitet | Masteroversikt, ζ–L–S‑rammeverket, hysterese, separatrix, recovery‑logikk |
| **1** | Friksjonsmodellen | Baseline‑friksjon, adaptiv friksjon, stress‑friksjon, matematiske former |
| **2** | Kontrollsystemer | Negativ/positiv feedback, feedforward, adaptiv kontroll |
| **3** | Faseoverganger | Kritiske terskler, Monte Carlo‑analyse, stabilitetssoner |
| **4** | Kliniske implikasjoner | Risiko, behandling, sykdomsforløp, stabilitetsanalyse |
| **5** | Fremtidige anvendelser | Wearables, AI‑overvåkning, personlig medisin, biomarkører |

---

## 📓 Notebooks

Notebookene ligger i `notebooks/` og genererer alle figurer, simuleringer og analyser brukt i artiklene.

| Notebook | Beskrivelse |
|----------|-------------|
| **metabolic_friction_main_clean.ipynb** | Hovedsimulering av friksjonsmodellen |
| **simulate_substances.ipynb** | Stoff‑ og parameterrespons, kontrollsløyfer |
| **monte_carlo.ipynb** | Monte Carlo‑analyse av stabilitet og faseoverganger |
| **figures_generator.ipynb** | Genererer figurer til artiklene |

---

---

## 🧠 Teoretisk rammeverk

Modellen bygger på tre hovedkomponenter:

### **ζ — Friksjon**
Motstand mot endring, både baseline, adaptiv og stress‑indusert.

### **L — Kontroll**
Feedback‑ og feedforward‑mekanismer som regulerer friksjon og metabolsk aktivitet.

### **S — Stabilitet**
Systemets faktiske tilstand, inkludert:
- stabil sone  
- metastabil sone  
- kritisk sone  
- kollapssone  

Dette rammeverket brukes i alle artiklene og notebookene.

---

## 📊 Figurer og data

Alle figurer generert fra notebookene lagres i:


## 📁 Mappestruktur

Repoet følger en profesjonell forskningsstruktur:

