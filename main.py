_stiri = """În prima săptămână, valorile termice diurne vor fi în creștere treptată de la o zi la alta, spre valori mai ridicate decât mediile multianuale specifice perioadei, cu valori la începutul intervalului, în medie, de 14–17°C, ce vor urca spre 22–26°C în data de 25 octombrie, apoi vor scădea spre medii de 16–20°C. În cea de-a doua săptămână nu vor mai fi variații termice semnificative, astfel că mediile se vor situa între 13 și 18°C. În prima săptămână, temperaturile nocturne vor fi treptat în creștere, de la valori medii de 2–5°C în prima noapte (20 spre 21 octombrie), spre minime medii de 8–12°C. În cea de-a doua săptămână, nopțile vor fi mai reci, cu valori ușor sub cele specifice perioadei, cuprinse între 2 și 6°C. Probabilitatea de ploaie va fi mai ridicată în intervalul 24–28 octombrie"""

_impartire2parti = len(_stiri) //2

_partea1 =  _stiri[:_impartire2parti]
_partea2 = _stiri[_impartire2parti:]

_partea1 = _partea1.upper() ##Le transform in upper case si ii las acelasi nume
_partea1 = _partea1.strip() ##Dar deja nu i-am dat copy paste fara spatiu la inceput si sfarsit?


_partea2 = _partea2[::-1]
_partea2 = _partea2.capitalize()
_partea2 = _partea2.replace(".", "").replace(",", "").replace("!", "").replace("?","")


_resultatfinal = _partea1 + " " +_partea2
print(_resultatfinal)
