elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]


#A1
for i in range(len(elevi)):
    print(elevi[i], "are nota", note[i])

#A2

nota_maxima = max(note)
nota_minima = min(note)

pozitie_max = note.index(nota_maxima)
pozitie_min = note.index(nota_minima)

elev_max = elevi[pozitie_max]
elev_min = elevi[pozitie_min]

print("Elevul", elev_max, "are nota maxima", nota_maxima, "si Elevul", elev_min, "are nota minima", nota_minima)

#A3

media_clasei = sum(note) / len(note)

print("Media clasei este:",media_clasei)


#A4

for i in range(len(elevi)):
    if note[i] >= 5:
        print("Elevii cu notele peste 5", elevi[i], note[i])



#PARTEA B

#B5
for i in range(len(elevi)):
    print("La aceste note s-au adaugat un punct:", note[i] + 1)

#B6

elevi.append(elev_nou)
note.append(nota_elev_nou)

print ("Numarul de elevi si notele au fost actualizate cu un elev nou si acum arata:", elevi, note)

#B7
if elev_de_sters in elevi:
    pozitie_elevedesters = elevi.index(elev_de_sters)

    elevi.pop(pozitie_elevedesters)
    note.pop(pozitie_elevedesters)

#B8
print(elevi, note, "Elevul Darius a fost sters din lista")

#Partea C


