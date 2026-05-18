import sympy as sp

# Definer symboler for koblingsstyrker
kRN, kGN, kBN, kNR = sp.symbols('kRN kGN kBN kNR')
kNG, kGG, kGR = sp.symbols('kNG kGG kGR')
kNB, kGB, kBB, kBR = sp.symbols('kNB kGB kBB kBR')
kNR2, kGR2, kBR2, kRR = sp.symbols('kNR2 kGR2 kBR2 kRR')

# Module interaction matrix (N, G, B, R)
M = sp.Matrix([
    [-kRN,   kGN,   kBN,  -kNR],   # dN/dt
    [ kNG,  -kGG,     0,  -kGR],   # dG/dt  (KORRIGERT)
    [ kNB,   kGB,  -kBB,  -kBR],   # dB/dt
    [-kNR2, -kGR2, -kBR2,  kRR]    # dR/dt
])

# Nullrom
nullspace = M.nullspace()

print("Nullspace basis vector(s):")
for v in nullspace:
    print(v)

