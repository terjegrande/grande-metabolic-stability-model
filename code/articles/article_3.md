Artikkel 3 — Dynamikken i S(t): Stabilitet, hysterese og metabolsk treghet
(GitHub‑optimalisert versjon — Markdown)

1. Introduksjon
Denne artikkelen bygger videre på Artikkel 2 og beskriver dynamikken i S(t)-modellen:

stabilitet

ustabilitet

hysterese

treghet

separatrix‑grenser

Dette er kjernen i hvordan kroppen faktisk skifter mellom metabolske tilstander.

2. Systemet som differensialligning
Vi bruker den samme grunnligningen:

Code
dS/dt = (I(t) - S(t)) / F(t)
Men i Artikkel 3 analyserer vi dynamikken, ikke bare friksjonen.

3. Stabilitet
Et system er stabilt når:

Code
dS/dt → 0
S(t) → I(t)
Dette skjer når:

friksjonen er høy nok

input er konsistent

systemet ikke presses over terskler

4. Ustabilitet
Ustabilitet oppstår når:

friksjonen er for lav

input endrer seg raskt

stress eller søvnforstyrrelser senker F(t)

systemet får for store svingninger

Dette gir:

cravings

energikaos

store blodsukkersvingninger

dårlig toleranse for faste

5. Hysterese
Hysterese betyr:

Kroppen bruker én vei for å gå inn i en tilstand, og en annen vei for å komme ut av den.

Eksempel:

å gå inn i ketose krever lavt I(t) og lav friksjon

å komme ut av ketose krever mye mindre input

Dette gir en loop i S(t)-rommet.

6. Separatrix
Separatrix er grensen mellom:

stabil bane

ustabil bane

I praksis:

en person kan være “på kanten” av metabolsk kollaps

små endringer i input kan gi store endringer i S(t)

Dette forklarer hvorfor:

noen tåler stress dårlig

noen mister metabolsk kontroll av små triggere

noen får “crash” etter trening

7. Pseudokode for dynamikk‑analyse
Code
Initialize S = S0
For each timestep t:
    Compute I(t)
    Compute F(t)
    dS = (I(t) - S) / F(t)
    S = S + dS * dt

    If S crosses threshold:
        Mark separatrix crossing
        Update hysteresis state
8. Konklusjon
Artikkel 3 viser at:

friksjon bestemmer hvor raskt S(t) endrer seg

dynamikken bestemmer hvordan S(t) endrer seg

hysterese og separatrix forklarer hvorfor kroppen kan være stabil eller ustabil

Dette danner grunnlaget for Artikkel 4 og 5.
