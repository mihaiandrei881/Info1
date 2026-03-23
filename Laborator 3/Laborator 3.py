import csv
import json

def citeste_produse_csv(fisier):
    produse = {}
    with open(fisier, "r") as f:
        r = csv.reader(f)
        next(r)
        for linie in r:
            if len(linie) == 0:
                continue
            idp = linie[0]
            produse[idp] = {
                "nume": linie[1],
                "pret": float(linie[2]),
                "stoc": int(linie[3])
            }
    return produse

def scrie_produse_csv(fisier, produse):
    with open(fisier, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "nume", "pret", "stoc"])
        for idp in produse:
            p = produse[idp]
            w.writerow([idp, p["nume"], p["pret"], p["stoc"]])

def citeste_reduceri_json(fisier):
    with open(fisier, "r") as f:
        return json.load(f)

def afiseaza_meniu(produse):
    print("\nID | NUME | PRET | STOC")
    for idp in produse:
        p = produse[idp]
        print(idp, p["nume"], p["pret"], p["stoc"])
    print()

def adauga_produs(comanda, produse, idp, cant):
    if idp not in produse:
        print("Produs invalid")
        return
    if cant <= 0:
        print("Cantitate invalida")
        return
    deja = comanda.get(idp, 0)
    stoc_real = produse[idp]["stoc"] - deja
    if cant > stoc_real:
        print("Stoc insuficient")
        return
    comanda[idp] = deja + cant

def scade_produs(comanda, idp, cant):
    if idp not in comanda:
        print("Nu exista in comanda")
        return
    if cant <= 0:
        print("Cantitate invalida")
        return
    nou = comanda[idp] - cant
    if nou < 0:
        print("Prea mult de scazut")
        return
    if nou == 0:
        del comanda[idp]
    else:
        comanda[idp] = nou

def calculeaza_total(comanda, produse):
    total = 0
    for idp in comanda:
        total += produse[idp]["pret"] * comanda[idp]
    return total

def calculeaza_reducere(total, tip, reduceri):
    if tip == "" or tip == "fara":
        return 0
    if tip not in reduceri:
        return 0
    r = reduceri[tip]
    if total < r["prag"]:
        return 0
    if r["tip"] == "procent":
        return total * r["valoare"] / 100
    if r["tip"] == "fix":
        return min(r["valoare"], total)
    return 0

def genereaza_bon(comanda, produse, total, reducere):
    l = []
    for idp in comanda:
        p = produse[idp]
        cant = comanda[idp]
        sub = p["pret"] * cant
        l.append(f"{p['nume']} x {cant} = {sub}")
    l.append(f"Total: {total}")
    l.append(f"Reducere: {reducere}")
    l.append(f"Total final: {total - reducere}")
    return "\n".join(l)

def scrie_bon_txt(fisier, text):
    with open(fisier, "w") as f:
        f.write(text)

def goleste_comanda(comanda):
    comanda.clear()

def main():
    produse = citeste_produse_csv("data/produse.csv")
    reduceri = citeste_reduceri_json("data/reduceri.json")
    comanda = {}
    reducere_curenta = ""

    while True:
        print("\n Meniu")
        print("1  Afisare produse")
        print("2  Adaugare produs")
        print("3  Scadere produs")
        print("4  Reducere")
        print("5  Finalizare")
        print("6  Anulare")
        print("0  Iesire")

        opt = input("Optiune: ")

        if opt == "1":
            afiseaza_meniu(produse)

        elif opt == "2":
            idp = input("ID produs: ")
            cant = int(input("Cantitate: "))
            adauga_produs(comanda, produse, idp, cant)

        elif opt == "3":
            idp = input("ID produs: ")
            cant = int(input("Cantitate de scazut: "))
            scade_produs(comanda, idp, cant)

        elif opt == "4":
            total = calculeaza_total(comanda, produse)
            if total == 0:
                print("Comanda goala")
                continue
            print("1 student")
            print("2 happy")
            print("3 cupon")
            print("4 fara reducere")
            print("0 inapoi")
            o = input("Alege: ")
            if o == "1": reducere_curenta = "student"
            elif o == "2": reducere_curenta = "happy"
            elif o == "3": reducere_curenta = "cupon"
            elif o == "4": reducere_curenta = "fara"

        elif opt == "5":
            total = calculeaza_total(comanda, produse)
            if total == 0:
                print("Comanda goala")
                continue
            reducere = calculeaza_reducere(total, reducere_curenta, reduceri)
            bon = genereaza_bon(comanda, produse, total, reducere)
            print("\n" + bon)
            scrie_bon_txt("bon.txt", bon)
            for idp in comanda:
                produse[idp]["stoc"] -= comanda[idp]
            scrie_produse_csv("data/produse.csv", produse)
            goleste_comanda(comanda)
            reducere_curenta = ""

        elif opt == "6":
            goleste_comanda(comanda)
            reducere_curenta = ""

        elif opt == "0":
            break

        else:
            print("Optiune invalida")

main()