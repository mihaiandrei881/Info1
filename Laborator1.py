#Laborator 1
produse = ["espresso", "latte", "cappuccino", "ceai", "ciocolata calda", "croissant"]
preturi = [8.0, 12.0, 11.0, 7.0, 10.0, 9.0]
stoc = [20, 15, 18, 30, 12, 10]
cant_comanda = [0, 0, 0, 0, 0, 0]

reducere_curenta = 0




def afisare_meniu(produse, preturi, stoc):
    print("\n Meniu")
    for i in range(len(produse)):
        print(f"{i}. {produse[i]} - {preturi[i]} lei (stoc: {stoc[i]})")
    print("")


def adaugare_produs(cant_comanda, stoc, index, cantitate):
    if index < 0 or index >= len(cant_comanda):
        print("Index invalid.")
        return

    if cantitate <= 0:
        print("Cantitatea trebuie sa fie pozitiva.")
        return

    if cantitate > stoc[index] - cant_comanda[index]:
        print("Stoc insuficient.")
        return

    cant_comanda[index] += cantitate
    print("Produs adaugat cu succes.")


def scadere_produs(cant_comanda, index, cantitate):
    if index < 0 or index >= len(cant_comanda):
        print("Index invalid.")
        return

    if cantitate <= 0:
        print("Cantitatea prea mica")
        return

    if cantitate > cant_comanda[index]:
        print("Nu poti scadea mai mult decat ai in comanda")
        return

    cant_comanda[index] -= cantitate
    print("Produs scazut cu succes")


def calcul_total(cant_comanda, preturi):
    total = 0
    for i in range(len(cant_comanda)):
        total += cant_comanda[i] * preturi[i]
    return total


def stabilire_reducere(total, tip):
    if tip == "student":
        if total >= 30:
            return total * 0.10
        else:
            print("Total insuficient pentru reducerea student")
            return 0

    elif tip == "happy":
        if total >= 50:
            return total * 0.15
        else:
            print("Total insuficient pentru reducerea happy hour")
            return 0

    elif tip == "cupon":
        if total >= 25:
            return 7
        else:
            print("Total insuficient pentru cupon")
            return 0

    return 0


def afisare_bon(produse, preturi, cant_comanda, reducere):
    print("\n Bon Fiscal ")
    total = calcul_total(cant_comanda, preturi)

    for i in range(len(produse)):
        if cant_comanda[i] > 0:
            subtotal = cant_comanda[i] * preturi[i]
            print(f"{produse[i]} x {cant_comanda[i]} = {subtotal} lei")

    print(f"\nTotal: {total} lei")
    print(f"Reducere: {reducere} lei")
    print(f"Total final: {total - reducere} lei")
    print("")


def finalizare_comanda(stoc, cant_comanda):
    for i in range(len(stoc)):
        stoc[i] -= cant_comanda[i]
        cant_comanda[i] = 0


def anulare_comanda(cant_comanda):
    for i in range(len(cant_comanda)):
        cant_comanda[i] = 0

#   MENIU PRINCIPAL

while True:
    print("""
 - - Cafenea - -1
1. Afisare meniu produse
2. Adaugare produs in comanda
3. Scadere produs din comanda
4. Aplicare reducere
5. Finalizare comanda
6. Anulare comanda
0. Iesire
""")

    opt = input("Alege optiunea: ")

    if opt == "1":
        afisare_meniu(produse, preturi, stoc)

    elif opt == "2":
        idx = int(input("Index produs: "))
        cant = int(input("Cantitate: "))
        adaugare_produs(cant_comanda, stoc, idx, cant)

    elif opt == "3":
        idx = int(input("Index produs: "))
        cant = int(input("Cantitate de scazut: "))
        scadere_produs(cant_comanda, idx, cant)

    elif opt == "4":
        total = calcul_total(cant_comanda, preturi)
        if total == 0:
            print("Comanda este goala.")
            reducere_curenta = 0
            continue

        print("""
--- Reduceri ---
1. student (10% peste 30 lei)
2. happy (15% peste 50 lei)
3. cupon (-7 lei peste 25 lei)
4. fara reducere
5. inapoi
""")

        r = input("Alege reducerea: ")

        if r == "1":
            reducere_curenta = stabilire_reducere(total, "student")
        elif r == "2":
            reducere_curenta = stabilire_reducere(total, "happy")
        elif r == "3":
            reducere_curenta = stabilire_reducere(total, "cupon")
        elif r == "4":
            reducere_curenta = 0
            print("Reducerea a fost resetata.")
        elif r == "5":
            pass
        else:
            print("Optiune invalida.")

    elif opt == "5":
        total = calcul_total(cant_comanda, preturi)
        if total == 0:
            print("Nu exista produse in comanda.")
            continue

        # recalculam reducerea la finalizare
        reducere_finala = min(reducere_curenta, total)

        afisare_bon(produse, preturi, cant_comanda, reducere_finala)

        finalizare_comanda(stoc, cant_comanda)
        reducere_curenta = 0

    elif opt == "6":
        anulare_comanda(cant_comanda)
        reducere_curenta = 0
        print("Comanda anulata")

    elif opt == "0":
        print("La revedere")
        break

    else:
        print("Optiune invalida.")