# ---- KORÁBBI HÓNAPOK ÁTLAGAI ----
haviAtlagok = []
while True:
    haviAtlag = float(input("Add meg a korábbi hónapok átlagait (1-5), kilépés: 0: "))
    if haviAtlag == 0:
        break
    elif 1 <= haviAtlag <= 5:
        haviAtlagok.append(haviAtlag)
    else:
        print("Hiba: az átlag 1 és 5 között lehet.")

if len(haviAtlagok) > 0:
    referencia_atlag = sum(haviAtlagok) / len(haviAtlagok)
else:
    referencia_atlag = 3.0   # Ha nincs korábbi adat, semleges alap

print(f"\nReferencia átlag (alap): {referencia_atlag}\n")

# ---- TANTÁRGYAK ----
tantargyak = ["Irodalom", "Magyar nyelv", "Matematika", "Állampolgári ismeretek",
              "Történelem", "Német", "Digitális kultúra",
              "Mozgókép- és médiaism.", "Testnevelés"]

fontossag = {"Irodalom": 1, "Magyar nyelv": 1, "Matematika": 2, "Állampolgári ismeretek": 1,
            "Történelem": 1, "Német": 0.5, "Digitális kultúra": 2, "Mozgókép- és médiaism.": 1,
            "Testnevelés": 0.5}

jegyek_dict = {t: [] for t in tantargyak}
sulyok_dict = {t: [] for t in tantargyak}

# ---- JEGYEK BEKÉRÉSE ----
for tantargy in tantargyak:
    while True:
        jegy = int(input(f"Add meg a {tantargy} tantárgyból szerzett jegyet (1-5, 0 = nincs több): "))
        if jegy == 0:
            break
        elif 1 <= jegy <= 5:
            sulyozas = float(input("Add meg a jegy súlyozását (0.5 / 1 / 2): "))
            jegyek_dict[tantargy].append(jegy)
            sulyok_dict[tantargy].append(sulyozas)
        else:
            print("Hiba: jegy csak 1 és 5 között lehet.")

# ---- HAVI SÚLYOZOTT ÁTLAG SZÁMÍTÁS ----
osszesitett_ertek = 0
osszesitett_suly = 0

for tantargy in tantargyak:
    for i in range(len(jegyek_dict[tantargy])):
        jegy = jegyek_dict[tantargy][i]
        suly = sulyok_dict[tantargy][i]
        font = fontossag[tantargy]

        osszesitett_ertek += jegy * suly * font
        osszesitett_suly += suly * font

if osszesitett_suly > 0:
    jelenlegi_atlag = osszesitett_ertek / osszesitett_suly
else:
    jelenlegi_atlag = referencia_atlag

print(f"\nJelenlegi súlyozott átlag: {jelenlegi_atlag:.2f}")
print(f"Referencia átlag: {referencia_atlag:.2f}")

# ---- JUTALOMKALKULÁCIÓ ----
# 3-as = 0 Ft
# 4-es = x Ft, 2-es = -x Ft
# 5-ös = 2x Ft, 1-es = -2x Ft

ossz_jegyszam = sum(len(v) for v in jegyek_dict.values())

# relatív teljesítmény index
relativ_teljesitmeny = jelenlegi_atlag / referencia_atlag

# x skálázása úgy, hogy átlagosan 3000 legyen
x = (3000 / ossz_jegyszam) * relativ_teljesitmeny

print(f"\nx érték: {x:.2f} Ft")

osszes_jutalom = 0

for tantargy in tantargyak:
    lista = jegyek_dict[tantargy]
    n1 = lista.count(1)
    n2 = lista.count(2)
    n3 = lista.count(3)
    n4 = lista.count(4)
    n5 = lista.count(5)

    tantargy_jutalom = (n4 * x) + (n5 * 2 * x) + (n2 * -x) + (n1 * -2 * x)
    tantargy_jutalom *= fontossag[tantargy]

    print(f"{tantargy}: {tantargy_jutalom:.2f} Ft")
    osszes_jutalom += tantargy_jutalom

print(f"\nÖsszes havi jutalom: {osszes_jutalom:.2f} Ft")