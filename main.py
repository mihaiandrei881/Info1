import random

numer_secret = random.randint(1,10)


ghicit = 0

print ("Ghicheste numarul intre 1 si 10")

while ghicit != numer_secret:
    ghicit = int(input("Ghiceste numarul"))
if ghicit < numer_secret:
    print("Incearca un numar mai mare")
if ghicit > numer_secret:
    print("Incearca un numar mai mic")
else:
    print("L-ai ghicit!")
    print("test")

