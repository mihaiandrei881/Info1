import os
import json

PRODUSE_INITIALE = [
    ("1", "espresso", 8.0, 20),
    ("2", "latte", 12.0, 15),
    ("3", "cappuccino", 11.0, 18),
    ("4", "ceai", 7.0, 30),
    ("5", "ciocolata calda", 10.0, 12),
    ("6", "croissant", 9.0, 10),
]

REDUCERI_INITIALE = {
    "student": {
        "prag": 30,
        "tip": "procent",
        "valoare": 10
    },
    "happy": {
        "prag": 50,
        "tip": "procent",
        "valoare": 15
    },
    "cupon": {
        "prag": 25,
        "tip": "fix",
        "valoare": 7
    }
}

def scrie_fisiere_initiale():
    with open("data/produse.csv", "w", encoding="utf-8") as f:
        f.write("id,nume,pret,stoc\n")
        for pid, nume, pret, stoc in PRODUSE_INITIALE:
            linie = f"{pid},{nume},{pret},{stoc}\n"
            f.write(linie)

    #  reduceri.json
    with open("data/reduceri.json", "w", encoding="utf-8") as f:
        text = json.dumps(REDUCERI_INITIALE, indent=2)
        f.write(text)

def citeste_produse_csv(fisier):
    produse = {}
    with open(fisier, "r", encoding="utf-8") as f:
        linii = f.readlines()
    # sar peste
    for linie in linii[1:]:
        linie = linie.strip()
        if linie == "":
            continue
        parti = linie.split(",")
        pid = parti[0]
        nume = parti[1]
        pret = float(parti[2])
        stoc = int(parti[3])
        produse[pid] = {"nume": nume, "pret": pret, "stoc": stoc}
    return produse

def citeste_reduceri_json(fisier):
    with open(fisier, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def afiseaza_meniu(produse):
    print("\nId, Nume, Stoc :")
    for pid in produse:
        p = produse[pid]
        print(pid, p["nume"], p["pret"], p["stoc"])

def adauga_produs(comanda, produse, id_produs, cantitate):
    if id_produs not in produse:
        print("Produs invalid")
        return
    if cantitate <= 0:
        print("Cantitate invalida")
        return
    deja = comanda.get(id_produs, 0)
    stoc_real = produse[id_produs]["stoc"] - deja
    if cantitate > stoc_real:
        print("Stoc insuficient")
        return
    comanda[id_produs] = deja + cantitate
    print("Produs adaugat in comanda")

def scade_produs(comanda, id_produs, cantitate):
    if id_produs not in comanda:
        print("Produsul nu este in comanda")
        return
    if cantitate <= 0:
        print("Cantitate invalida")
        return
    nou = comanda[id_produs] - cantitate
    if nou < 0:
        print("Prea mult de scazut")
        return
    if nou == 0:
        del comanda[id_produs]
    else:
        comanda[id_produs] = nou
    print("Produs actualizat in comanda")

def calculeaza_total(comanda, produse):
    total = 0
    for pid in comanda:
        cant = comanda[pid]
        pret = produse[pid]["pret"]
        total = total + pret * cant
    return total

def calculeaza_reducere(total, tip_reducere, reduceri):
    if tip_reducere == "" or tip_reducere == "fara":
        return 0
    if tip_reducere not in reduceri:
        return 0
    r = reduceri[tip_reducere]
    prag = r["prag"]
    tip = r["tip"]
    valoare = r["valoare"]
    if total < prag:
        print("Pragul pentru reducere nu este indeplinit")
        return 0
    if tip == "procent":
        return total * valoare / 100
    elif tip == "fix":
        if valoare > total:
            return total
        else:
            return valoare
    return 0

def genereaza_bon(comanda, produse, total, reducere):
    linii = []
    for pid in comanda:
        p = produse[pid]
        cant = comanda[pid]
        sub = p["pret"] * cant
        linii.append(f"{p['nume']} x {cant} = {sub}")
    linii.append(f"Total: {total}")
    linii.append(f"Reducere: {reducere}")
    linii.append(f"Total final: {total - reducere}")
    text = "\n".join(linii)
    return text

def scrie_bon_txt(fisier, text_bon):
    with open(fisier, "w", encoding="utf-8") as f:
        f.write(text_bon)

def goleste_comanda(comanda):
    comanda.clear()

def scrie_produse_csv_din_dic(fisier, produse):
    with open(fisier, "w", encoding="utf-8") as f:
        f.write("id,nume,pret,stoc\n")
        for pid in produse:
            p = produse[pid]
            linie = f"{pid},{p['nume']},{p['pret']},{p['stoc']}\n"
            f.write(linie)

def main():
    # la fiecare rulare, rescriem fisierele din cod

    produse = citeste_produse_csv("data/produse.csv")
    reduceri = citeste_reduceri_json("data/reduceri.json")
    comanda = {}
    reducere_curenta = ""

    while True:
        print("\nMeniu")
        print("1 - Afisare meniu produse")
        print("2 - Adaugare produs in comanda")
        print("3 - Scadere/eliminare produs din comanda")
        print("4 - Aplicare reducere")
        print("5 - Finalizare comanda")
        print("6 - Anulare comanda")
        print("7 - Modificare stoc manual")
        print("0 - Iesire")

        opt = input("Optiune: ")

        if opt == "1":
            afiseaza_meniu(produse)

        elif opt == "2":
            pid = input("ID produs: ")
            try:
                cant = int(input("Cantitate: "))
            except:
                print("Cantitate invalida")
                continue
            adauga_produs(comanda, produse, pid, cant)

        elif opt == "3":
            pid = input("ID produs: ")
            try:
                cant = int(input("Cantitate de scazut: "))
            except:
                print("Cantitate invalida")
                continue
            scade_produs(comanda, pid, cant)

        elif opt == "4":
            total = calculeaza_total(comanda, produse)
            if total == 0:
                print("Comanda este goala")
                continue
            print("1 - student")
            print("2 - happy")
            print("3 - cupon")
            print("4 - fara reducere")
            print("0 - inapoi")
            o = input("Alege: ")
            if o == "1":
                reducere_curenta = "student"
            elif o == "2":
                reducere_curenta = "happy"
            elif o == "3":
                reducere_curenta = "cupon"
            elif o == "4":
                reducere_curenta = "fara"
            elif o == "0":
                continue
            else:
                print("Optiune reducere invalida")
                continue
            print("Reducere curenta:", reducere_curenta)

        elif opt == "5":
            total = calculeaza_total(comanda, produse)
            if total == 0:
                print("Comanda este goala")
                continue
            reducere_val = calculeaza_reducere(total, reducere_curenta, reduceri)
            bon = genereaza_bon(comanda, produse, total, reducere_val)
            print("\n" + bon)
            scrie_bon_txt("bon.txt", bon)
            # udpate stoc
            for pid in comanda:
                produse[pid]["stoc"] = produse[pid]["stoc"] - comanda[pid]
            scrie_produse_csv_din_dic("data/produse.csv", produse)
            goleste_comanda(comanda)
            reducere_curenta = ""
            print("Comanda finalizata")

        elif opt == "6":
            goleste_comanda(comanda)
            reducere_curenta = ""
            print("Comanda anulata")

        elif opt == "7":
            pid = input("ID produs: ")
            if pid not in produse:
                print("Produs invalid")
                continue
            try:
                nou_stoc = int(input("Stoc nou: "))
            except:
                print("Stoc invalid")
                continue
            produse[pid]["stoc"] = nou_stoc
            scrie_produse_csv_din_dic("data/produse.csv", produse)
            print("Stoc modificat")

        elif opt == "0":
            break

        else:
            print("Optiune invalida")

main()