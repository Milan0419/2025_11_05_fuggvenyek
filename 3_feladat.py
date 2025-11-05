#Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám! Kezeld azt az esetet is, ha a két szám egyenlő!

szam1 = int(input("Írd be az első számot:"))
szam2 = int(input("Írd be a második számot:"))

def hasonlit():
    if szam1 > szam2:
        valasz = 'Az első szám a nagyobb!'
    elif szam2 > szam1:
        valasz = 'A második szám nagyobb!'
    elif szam1 == szam2:
        valasz = 'A számok egyenlőek'
    print(valasz)

hasonlit()