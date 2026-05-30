# Artikkel 0 — Introduksjon til Metabolsk Stabilitet
Denne artikkelen gir en samlet introduksjon til prosjektets teoretiske rammeverk, inkludert friksjonsmodellen, kontrollsløyfer, faseoverganger og det nye ζ–L–S‑rammeverket. Artikkelen fungerer som en masteroversikt for hele serien (Artikkel 0–5).

---

## 1. Bakgrunn
Biologiske systemer opererer under kontinuerlig stress, men opprettholder likevel stabilitet gjennom selvregulerende mekanismer. Dette prosjektet utvikler en matematisk modell for å beskrive hvordan slike systemer:

- motstår endring (friksjon)
- regulerer seg selv (kontrollsløyfer)
- kan kollapse eller stabilisere seg (faseoverganger)
- responderer på belastning (stressrespons)

---

## 2. Hovedidé: Metabolsk Stabilitet som Friksjon + Kontroll + Faseoverganger
Modellen bygger på tre grunnpilarer:

### **2.1 Friksjon (ζ)**
Friksjon representerer motstand mot metabolsk endring. Den består av:
- baseline‑friksjon  
- adaptiv friksjon  
- stress‑indusert friksjon  

Dette gir en dynamisk motstand som endrer seg med systemets tilstand.

### **2.2 Kontroll (L)**
Kontrollsløyfer regulerer friksjon og metabolsk aktivitet gjennom:
- negativ feedback  
- positiv feedback  
- feedforward‑kontroll  
- adaptiv kontroll  

### **2.3 Stabilitet (S)**
Stabilitet er resultatet av samspillet mellom friksjon og kontroll. Systemet kan befinne seg i:
- stabil sone  
- metastabil sone  
- kritisk sone  
- kollapssone  

Dette leder til faseoverganger.

---

## 3. Det nye ζ–L–S‑rammeverket
Dette rammeverket ble introdusert etter at Artikkel 0B ble skrevet, og erstatter deler av den gamle strukturen.

### **ζ (zeta): Friksjonskomponenten**
Representerer motstand mot endring.

### **L (lambda): Kontrollkomponenten**
Representerer styrken og kvaliteten på reguleringssløyfene.

### **S (sigma): Stabilitetskomponenten**
Representerer systemets faktiske tilstand og robusthet.

Dette rammeverket brukes i alle senere artikler.

---

## 4. Kritiske konsepter som ble lagt til (C8 og C9)

### **C8 — Hysterese og separatrix**
Systemet kan ha to mulige tilstander ved samme input, avhengig av historikk.  
Separatrixen er grensen mellom stabil og ustabil bane.

### **C9 — Recovery‑logikk**
Systemets evne til å komme tilbake etter stress avhenger av:
- friksjonsnivå  
- kontrollsløyfer  
- hvor langt systemet har beveget seg inn i kritisk sone  

Dette er viktig for kliniske implikasjoner.

---

## 5. Simuleringsgrunnlag
Artikkel 0 refererer til fire notebooker:

- `metabolic_friction_main_clean.ipynb`  
- `simulate_substances.ipynb`  
- `monte_carlo.ipynb`  
- `figures_generator.ipynb`

Disse notebookene genererer:
- friksjonskurver  
- kontrollrespons  
- faseovergangsdiagrammer  
- Monte Carlo‑fordelinger  
- figurer til artiklene  

---

## 6. Struktur for resten av serien
Artikkel 0 fungerer som en oversikt. De andre artiklene går i dybden:

- **Artikkel 1:** Friksjonsmodellen  
- **Artikkel 2:** Kontrollsystemer  
- **Artikkel 3:** Faseoverganger  
- **Artikkel 4:** Kliniske implikasjoner  
- **Artikkel 5:** Fremtidige anvendelser  

---

## 7. Oppsummering
Denne oppdaterte versjonen av Artikkel 0 inkluderer:
- ζ–L–S‑rammeverket  
- C8 og C9  
- nye modeller  
- nye figurer  
- konsistens med Artikkel 1A, 1B, 5 og 6  
- en struktur som passer Nature Aging‑formatet  

Artikkel 0 er nå den riktige masterversjonen for hele prosjektet.
