#Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
szam = int(input("Írd be egy számot és eldöntöm hogy negatív vagy pozitív:"))


def pozneg():
    if szam >= 0:
        valasz = "pozitív"
    elif szam < 0:
        valasz = "negatív"
    
    print(f"Ez a szám {valasz}")

pozneg()