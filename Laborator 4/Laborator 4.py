import json

#citirea datelor
def incarca_datele():
    try:
        with open("competitori.json", "r") as f:
            return json.load(f)
    except:
        print("Fisierul competitori.json nu a fost gasit sau este invalid.")
        return []

#salvarea datelor
def salveaza_datele(lista):
    with open("competitori.json", "w") as f:
        json.dump(lista, f, indent=4)

# Functie de comparare a competitorilor
def compara(a, b):
    # 1. punctaj descrescator
    if a["punctaj"] != b["punctaj"]:
        return a["punctaj"] > b["punctaj"]
    # 2. timp crescator
    if a["timp"] != b["timp"]:
        return a["timp"] < b["timp"]
    # 3. nume alfabetic
    return a["nume"] < b["nume"]

# Implementare Quicksort simpla
def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]
    stanga = []
    dreapta = []
    egale = []

    for x in lista:
        if compara(x, pivot):
            stanga.append(x)
        elif compara(pivot, x):
            dreapta.append(x)
        else:
            egale.append(x)

    return quicksort(stanga) + egale + quicksort(dreapta)

# Afisare lista competitori
def afiseaza(lista):
    if not lista:
        print("Nu exista competitori.")
        return
    for c in lista:
        print(f"{c['nume']} - Punctaj: {c['punctaj']} - Timp: {c['timp']}")

# Adaugare competitor
def adauga(lista):
    nume = input("Nume competitor: ").strip()
    if nume == "":
        print("Numele nu poate fi gol.")
        return

    punctaj = int(input("Punctaj: "))
    timp = int(input("Timp: "))

    lista.append({"nume": nume, "punctaj": punctaj, "timp": timp})
    print("Competitor adaugat.")

# competitor
def actualizeaza(lista):
    nume = input("Introdu numele competitorului de actualizat: ").strip()

    for c in lista:
        if c["nume"].lower() == nume.lower():
            print("Gasit. Introdu noile valori.")
            c["punctaj"] = int(input("Punctaj nou: "))
            c["timp"] = int(input("Timp nou: "))
            print("Actualizare realizata.")
            return

    print("Competitorul nu exista.")

# clasament cu pozitii
def clasament(lista):
    if not lista:
        print("Nu exista competitori.")
        return

    ordonata = quicksort(lista)

    print("\nLoc  Nume                Punctaj   Timp")
    loc = 1
    for i, c in enumerate(ordonata):
        if i > 0:
            prev = ordonata[i - 1]
            if c["punctaj"] == prev["punctaj"] and c["timp"] == prev["timp"]:
                pass  # loc ramane acelasi
            else:
                loc = i + 1
        print(f"{loc:<4} {c['nume']:<18} {c['punctaj']:<9} {c['timp']}")

# Statistici
def statistici(lista):
    if not lista:
        print("Nu exista competitori.")
        return

    punctaje = [c["punctaj"] for c in lista]
    timpuri = [c["timp"] for c in lista]

    print("\n--- Statistici ---")
    print("Numar competitori:", len(lista))
    print("Punctaj maxim:", max(punctaje))
    print("Punctaj minim:", min(punctaje))
    print("Media punctajelor:", sum(punctaje) / len(punctaje))
    print("Cel mai bun timp:", min(timpuri))

# Meniu

def meniu():
    lista = incarca_datele()

    while True:
        print("\n--- MENIU ---")
        print("1. Afiseaza competitori")
        print("2. Adauga competitor")
        print("3. Actualizeaza competitor")
        print("4. Sorteaza (Quicksort)")
        print("5. Afiseaza clasament")
        print("6. Statistici")
        print("0. Iesire")

        opt = input("Alege optiunea: ")

        if opt == "1":
            afiseaza(lista)
        elif opt == "2":
            adauga(lista)
            salveaza_datele(lista)
        elif opt == "3":
            actualizeaza(lista)
            salveaza_datele(lista)
        elif opt == "4":
            lista = quicksort(lista)
            print("Lista a fost sortata.")
        elif opt == "5":
            clasament(lista)
        elif opt == "6":
            statistici(lista)
        elif opt == "0":
            print("La revedere.")
            break
        else:
            print("Optiune invalida.")

meniu()