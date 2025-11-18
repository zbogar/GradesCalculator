tantargyak = ["Irodalom", "Magyar nyelv", "Matematika", "Állampolgári ismeretek", 
              "Történelem", "Német", "Digitális kultúra", 
              "Mozgóképkultúra és médiaismeret", "Testnevelés"
]

fontossag = {
    "Irodalom": 1, "Magyar nyelv": 1, "Matematika": 2, "Állampolgári ismeretek": 1,
    "Történelem": 1, "Német": 0.5, "Digitális kultúra": 2, "Mozgóképkultúra és médiaismeret": 1,
    "Testnevelés": 0.5
}

jegyek_dict = {t: [] for t in tantargyak}

for tantargy in tantargyak:
    while True:
        jegy = int(input(f"Add meg a {tantargy} tantárgyból szerzett jegyet (1-5, 0 a kilépéshez): "))
        if jegy == 0:
            break
        elif 1 <= jegy <= 5:
            sulyozas = float(input("Add meg a jegy súlyozását (0.5/1/2): "))
            jegyErtek = jegy * sulyozas * fontossag[tantargy]
            jegyek_dict[tantargy].append(jegy)
        else:
            print("Hiba: nem érvényes jegy (1-5)")

n1 = sum(j.count(1) for j in jegyek_dict.values())
n2 = sum(j.count(2) for j in jegyek_dict.values())
n3 = sum(j.count(3) for j in jegyek_dict.values())
n4 = sum(j.count(4) for j in jegyek_dict.values())
n5 = sum(j.count(5) for j in jegyek_dict.values())
N = n1 + n2 + n3 + n4 + n5

atlag = 3000
ossz_ertek = -2*n1 - n2 + n4 + 2*n5
x = atlag * N / ossz_ertek if ossz_ertek != 0 else 0

def szamol_jutalom(lista):
    return lista.count(1)*(-2*x) + lista.count(2)*(-x) + lista.count(3)*0 + lista.count(4)*x + lista.count(5)*2*x

osszJutalom = 0
for tantargy in tantargyak:
    jutalom = szamol_jutalom(jegyek_dict[tantargy])
    print(f"{tantargy}: {jutalom:.2f} Ft")
    osszJutalom += jutalom

print(f"\nÖsszesített havi jutalom: {osszJutalom:.2f} Ft (x={x:.2f})")