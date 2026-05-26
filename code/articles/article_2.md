Artikkel 2 — Friksjon som metabolsk stabilisator i S(t)-modellen
(GitHub‑optimalisert versjon — Markdown)

1. Introduksjon
Metabolsk friksjon er den manglende variabelen i klassiske modeller for metabolsk regulering.
Friksjon beskriver motstanden i systemet — hvor vanskelig eller lett det er for kroppen å endre metabolsk tilstand S(t).

Friksjon påvirker:

stabilitet

fleksibilitet

respons på mat

respons på faste

respons på stress

energiregulering

Denne artikkelen beskriver den matematiske kjernen i friksjonsmodellen.

2. S(t) som dynamisk tilstand
S(t) representerer kroppens metabolske tilstand som en kontinuerlig funksjon over tid.

Den påvirkes av:

energitilgang

hormoner

stress

søvn

aktivitet

faste

Men S(t) endrer seg ikke direkte.
Endringen skjer gjennom friksjon F(t).

3. Grunnligningen
Endringen i metabolsk tilstand beskrives som:

Code
dS/dt = (I(t) - S(t)) / F(t)
Der:

S(t) = metabolsk tilstand

I(t) = input (mat, stress, aktivitet, hormoner)

F(t) = friksjon

Effekt:

Høy friksjon → treg endring → stabilitet

Lav friksjon → rask endring → ustabilitet

4. Hva bestemmer friksjon F(t)?
Friksjon er dynamisk og påvirkes av:

4.1 Søvn
Dårlig søvn → lav friksjon → ustabilitet.

4.2 Stress
Kronisk stress senker friksjonen og gjør systemet hyperresponsivt.

4.3 Faste
Moderat faste → lav friksjon.
Lang faste → høy friksjon (katabolt stress).

4.4 Trening
Akutt: lav friksjon.
Langsiktig: høy friksjon (robusthet).

4.5 Hormoner
Insulin, kortisol, leptin og adrenalin påvirker friksjon direkte.

5. U‑ og J‑formet friksjon
Friksjon kan modelleres som:

U‑form
Optimal friksjon i midten.
For lite eller for mye input → høy friksjon.

J‑form
Vanlig hos personer med metabolsk dysregulering:

lav friksjon ved moderat faste

høy friksjon ved overspising

ekstremt høy friksjon ved lang faste

Dette gir fleksibilitet i simuleringene.

6. Pseudokode for friksjonsmodellen
Dette er en GitHub‑klar pseudokode‑blokk som viser hvordan S(t) oppdateres:

Code
Initialize S = S0
For each timestep t:
    Compute input I(t)
    Compute friction F(t)
    dS = (I(t) - S) / F(t)
    S = S + dS * dt
Return S over time
7. Modellering av friksjon
U‑formet friksjon
Code
F(t) = a * (x - x0)^2 + b
Asymmetrisk U
Code
F(t) = a * (x - x0)^2 + c * (x - x0) + b
J‑formet friksjon
Code
F(t) = b + a * exp(k * (x - x0))
8. Praktisk implikasjon
To personer kan spise samme måltid, men få helt ulik respons fordi friksjonen er forskjellig:

høy friksjon → stabil respons

lav friksjon → store svingninger

Dette forklarer:

hvorfor noen tåler karbohydrater bedre

hvorfor faste fungerer for noen, men ikke andre

hvorfor stress ødelegger metabolsk kontroll

hvorfor søvn er en metabolsk superkraft

9. Konklusjon
Friksjon er den sentrale mekanismen som bestemmer:

stabilitet

fleksibilitet

respons

robusthet

S(t)-modellen er ikke komplett uten friksjon.
Friksjon gjør modellen biologisk realistisk og simulerbar.

