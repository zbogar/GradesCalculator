tantargyak = ["Irodalom", "Magyar nyelv", "Matematika", "Állampolgári ismeretek", "Történelem", "Német", "Digitális kultúra", "Mozgóképkultúra és médiaismeret", "Testnevelés"]
irodalom = []
magyarNyelv = []
matematika = []
allampolgariIsmeretek = []
tortenelem = []
nemet = []
digitalisKultura = []
mozgokepkulturaEsMediaismeret = []
testneveles = []
irodalomErtek = []
magyarNyelvErtek = []
matematikaErtek = []
allampolgariIsmeretekErtek = []
tortenelemErtek = []
nemetErtek = []
digitalisKulturaErtek = []
mozgokepkulturaEsMediaismeretErtek = []
testnevelesErtek = []

for i in range(len(tantargyak)):
    akar = "i"
    while akar.lower() == "i":
        jegy = int(input(f"Add meg a {tantargyak[i]} tantárgyból szerzett jegyet: "))
        if jegy == 0:
            akar = "n"
        elif jegy >= 1 and jegy <= 5:
            sulyozas = float(input("Add meg a jegy súlyozását (0.5/1/2): "))
            jegyErtek = jegy * sulyozas
            if i == 0:
                irodalom.append(jegy)
                irodalomErtek.append(jegyErtek)
            elif i == 1:
                magyarNyelv.append(jegy)
                magyarNyelvErtek.append(jegyErtek)
            elif i == 2:
                matematika.append(jegy)
                matematikaErtek.append(jegyErtek * 2) #2x olyan fontos minden matek jegy mint a többi jegy
            elif i == 3:
                allampolgariIsmeretek.append(jegy)
                allampolgariIsmeretekErtek.append(jegyErtek)
            elif i == 4:
                tortenelem.append(jegy)
                tortenelemErtek.append(jegyErtek)
            elif i == 5:
                nemet.append(jegy)
                nemetErtek.append(jegyErtek * 0.5) #fele olyan fontos minden nemet jegy mint a tobbi jegy
            elif i == 6:
                digitalisKultura.append(jegy)
                digitalisKulturaErtek.append(jegyErtek * 2) #2x olyan fontos minden info jegy mint a többi jegy
            elif i == 7:
                mozgokepkulturaEsMediaismeret.append(jegy)
                mozgokepkulturaEsMediaismeretErtek.append(jegyErtek)
            elif i == 8:
                testneveles.append(jegy)
                testnevelesErtek.append(jegyErtek * 0.5) #fele olyan fontos minden tesi jegy mint a tobbi jegy
            akar = input("Van még? (i/n): ")
        else:
            print("Hiba: nem érvényes jegy")
            akar = "i"

osszJegyekSzama = len(irodalom) + len(magyarNyelv) + len(matematika) + len(allampolgariIsmeretek) + len(tortenelem) + len(nemet) + len(digitalisKultura) + len(mozgokepkulturaEsMediaismeret) + len(testneveles)
print(f"Összes jegy száma: {osszJegyekSzama}")