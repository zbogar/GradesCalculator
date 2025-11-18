# 2.0 verzió: Havi jutalom számítása korábbi hónapok átlagával

haviAtlagok = []
while True:
    haviAtlag = float(input("Add meg a korábbi hónapok átlagait (kilépés: 0): "))
    if haviAtlag == 0:
        break
    elif 0 < haviAtlag <= 5:
        haviAtlagok.append(haviAtlag)
    else:
        print("Hiba: érvénytelen átlag (0-5 között)")

tantargyak = ["Irodalom", "Magyar nyelv", "Matematika", "Állampolgári ismeretek", 
              "Történelem", "Német", "Digitális kultúra", 
              "Mozgóképkultúra és médiaismeret", "Testnevelés"]

fontossag = {"Irodalom": 1, "Magyar nyelv": 1, "Matematika": 2, "Állampolgári ismeretek": 1,
            "Történelem": 1, "Német": 0.5, "Digitális kultúra": 2, "Mozgóképkultúra és médiaismeret": 1,
            "Testnevelés": 0.5}

jegyek_dict = {t: [] for t in tantargyak}

for tantargy in tantargyak:
    while True:
        jegy = int(input(f"Add meg a {tantargy} tantárgyból szerzett jegyet (1-5, 0 a kilépéshez): "))
        if jegy == 0:
            break
        elif 1 <= jegy <= 5:
            sulyozas = float(input("Add meg a jegy súlyozását (0.5/1/2): "))
            jegyek_dict[tantargy].append(jegy)
        else:
            print("Hiba: nem érvényes jegy (1-5)")

if haviAtlagok:
    elozohonap_atlag = sum(haviAtlagok) / len(haviAtlagok)
else:
    elozohonap_atlag = 0

ossz_jegyek_ertek = 0
for tantargy in tantargyak:
    lista = jegyek_dict[tantargy]
    n1 = lista.count(1)
    n2 = lista.count(2)
    n3 = lista.count(3)
    n4 = lista.count(4)
    n5 = lista.count(5)
    
    ossz_ertek = (-2*n1 - n2 + n4 + 2*n5) * fontossag[tantargy]
    ossz_jegyek_ertek += ossz_ertek

atlag = 3000
if ossz_jegyek_ertek != 0:
    korabbi_szorz = (elozohonap_atlag / 3.0) if elozohonap_atlag else 1
    x = (atlag / ossz_jegyek_ertek) * korabbi_szorz
else:
    x = 0

jutalmak_dict = {}
osszJutalom = 0

for tantargy in tantargyak:
    lista = jegyek_dict[tantargy]
    n1 = lista.count(1)
    n2 = lista.count(2)
    n3 = lista.count(3)
    n4 = lista.count(4)
    n5 = lista.count(5)
    
    jutalom = (n1*(-2*x) + n2*(-x) + n3*0 + n4*x + n5*2*x) * fontossag[tantargy]
    jutalmak_dict[tantargy] = jutalom
    osszJutalom += jutalom

print("\n--- Tantárgyankénti jutalom ---")
for tantargy, jutalom in jutalmak_dict.items():
    print(f"{tantargy}: {jutalom:.2f} Ft")

print(f"\nÖsszesített havi jutalom: {osszJutalom:.2f} Ft")
print(f"(x = {x:.2f}, előző hónapok átlagához igazítva)")