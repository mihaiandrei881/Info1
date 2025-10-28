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

