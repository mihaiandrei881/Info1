import csv

glosar = {}

def adauga_termen():
    termen = input("termen: ").strip().lower()

    if termen in glosar:
        print("Termenul exista deja in glosar")
        return

    definitie = input("Definitie: ").strip()
    categorie = input("Categorie: ").strip()
    exemplu = input("Exemplu: ").strip()

    glosar[termen] = {
        "definitie": definitie,
        "categorie": categorie,
        "exemplu": exemplu
    }

    print("Termen adaugat cu succes")


def cauta_exact():
    termen = input("Introduceti termenul: ").strip().lower()

    if termen not in glosar:
        print("Termenul nu exista in glosar")
        return

    print("\nRezultat:")
    for cheie, valoare in glosar[termen].items():
        print(f"{cheie.capitalize()}: {valoare}")


def cauta_partial():
    fragment = input("Introduceti fragmentul cautat: ").strip().lower()
    rezultate = [t for t in glosar if fragment in t]

    if not rezultate:
        print("Nu s-au gasit termeni care contin fragmentul.")
        return

    print("\nTermeni gasiti:")
    for t in rezultate:
        print(f"- {t}")

def stergere_termen():
     termen = input("Introduceti termenul: ").strip().lower()
     if termen not in glosar:
         return

     if termen in glosar:
         del glosar[termen]

def actualizeaza_termen():
    termen = input("Introduceti termenul de actualizat: ").strip().lower()

    if termen not in glosar:
        print("Termenul nu exista.")
        return

    print("Ce doriti sa modificati?")
    print("1. Definitie")
    print("2. Categorie")
    print("3. Exemplu")

    opt = input("Alegeti optiunea: ")

    if opt == "1":
        glosar[termen]["definitie"] = input("Noua definitie: ")
    elif opt == "2":
        glosar[termen]["categorie"] = input("Noua categorie: ")
    elif opt == "3":
        glosar[termen]["exemplu"] = input("Noul exemplu: ")
    else:
        print("Optiune invalida.")
        return

    print("Termen actualizat cu succes!")


def sterge_termen():
    termen = input("Introduceti termenul de sters: ").strip().lower()

    if termen not in glosar:
        print("Termenul nu exista.")
        return

    del glosar[termen]
    print("Termen sters cu succes!")

def afisare_glosar():
    if not glosar:
        print("Este gol")
        return

    print("glosar:")
    for termen, info in glosar.items():
        print(f"{termen.capitalize()}: {info['definitie']}")

def meniu():
    while True:
        print("\n===== MENIU GLOSAR =====")
        print("1. Adauga termen")
        print("2. Cauta termen (exact)")
        print("3. Cauta termen (partial)")
        print("4. Actualizeaza termen")
        print("5. Sterge termen")
        print("6. Afiseaza tot glosarul")
        print("7. Statistici")
        print("8. Salveaza in CSV")
        print("9. Incarca din CSV")
        print("0. Iesire")

        opt = input("Alegeti o optiune: ")

        if opt == "1":
            adauga_termen()
        elif opt == "2":
            cauta_exact()
        elif opt == "3":
            cauta_partial()
        elif opt == "4":
            actualizeaza_termen()
        elif opt == "5":
            sterge_termen()
        elif opt == "6":
            afiseaza_tot()
        elif opt == "7":
            statistici()
        elif opt == "8":
            salveaza_csv()
        elif opt == "9":
            incarca_csv()
        elif opt == "0":
            print("La revedere")
            break
        else:
            print("Optiune invalida")


#3
meniu()