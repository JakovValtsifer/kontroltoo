import random

def patsiendid():
    n = int(input("Sisestage patsientide arv: "))
    nimed = []
    D_vitamiini_sisaldus = []
    for i in range(n):
        nimi = input(f"Sisestage {i+1}. patsiendi nimi: ")
        nimed.append(nimi)
        D_vitamiini_sisaldus.append(random.randint(10, 50))
    return nimed, D_vitamiini_sisaldus

def patsientide_nimekiri(nimed, D_vitamiini_sisaldus):
    nimi_list = []
    for i in range(len(nimed)):
        if D_vitamiini_sisaldus[i] < 30:
            nimi_list.append(nimed[i])
    if nimi_list:
        print("D-vitamiini vaegusega patsientide nimekiri:")
        for nimi in nimi_list:
            print(nimi)
    else:
        print("D-vitamiini vaegusega patsiente pole.")

def keskmine(D_vitamiini_sisaldus):
    srednee = sum(D_vitamiini_sisaldus) / len(D_vitamiini_sisaldus)
    print(f"Keskmine D-vitamiin: {srednee:.2f}")

def rohkem_Dvitamiini(nimed, D_vitamiini_sisaldus):
    k = int(input("Sisestage kuvatavate patsientide arv: "))
    if k > len(nimed):
        k = len(nimed)
    sorted_indikaator = sorted(range(len(D_vitamiini_sisaldus)), key=lambda i: D_vitamiini_sisaldus[i], reverse=True)
    print(f"top-{k} kõrgeima vitamiinisisaldusega patsiendid D:")
    for i in range(k):
        print(f"{nimed[sorted_indikaator[i]]}: {D_vitamiini_sisaldus[sorted_indikaator[i]]}")

def otsi_nime_järgi(nimed, D_vitamiini_sisaldus):
    name = input("Sisesta otsimiseks nimi: ")
    found = False
    for i in range(len(nimed)):
        if nimed[i] == name:
            print(f"{nimed[i]}: {D_vitamiini_sisaldus[i]}")
            found = True
    if not found:
        print(f"Patsienti nimega {name} ei leitud.")

def keskmine_defitsiidi_protsent(nimed, D_vitamiini_sisaldus):
    n = len(nimed)
    defitsiidi_arv = 0
    for i in range(n):
        if D_vitamiini_sisaldus[i] < 30:
            defitsiidi_arv += 1
    defitsiidi_protsent = (defitsiidi_arv / n) * 100
    return defitsiidi_protsent



# Заполнение массивов
nimed, D_vitamiini_sisaldus = patsiendid()

# Меню
while True:
    print("Vali toiming:")
    print("1. Tehke nimekiri D-vitamiini vaegusega patsientidest")
    print("2. Leidke keskmine D-vitamiini väärtus")
    print("3. Kuva kõrgeima punktisumma saanud K patsiendi loend")
    print("4. Otsi töötajaid nime järgi")
    print("5. Keskmine D-vitamiini vaegusega patsientide protsent")
    print("0. Välju")
    choice = input("Vali toiming: ")
    if choice == "1":
        patsientide_nimekiri(nimed, D_vitamiini_sisaldus)
    elif choice == "2":
        keskmine(D_vitamiini_sisaldus)
    elif choice == "3":
        rohkem_Dvitamiini(nimed, D_vitamiini_sisaldus)
    elif choice == "4":
        otsi_nime_järgi(nimed, D_vitamiini_sisaldus)
    elif choice == "5":
        defitsiidi_protsent = keskmine_defitsiidi_protsent(nimed, D_vitamiini_sisaldus)
        print(f"Keskmine D-vitamiini vaegusega patsientide protsent: {defitsiidi_protsent:.2f}%")
    elif choice == "0":
        break
    else:
        print("Vale valik. Proovige uuesti.")




