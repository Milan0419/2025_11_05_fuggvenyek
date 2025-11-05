#Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!

def legrovidebb(szavak):
    if len(szavak[0]) < len(szavak[1]) and len(szavak[0]) < len(szavak[2]):
        valasz = 'Az első szó a legrövidebb'
    elif len(szavak[1]) < len(szavak[0]) and len(szavak[1]) < len(szavak[2]):
        valasz = 'A második szó a legrövidebb'
    elif len(szavak[2]) < len(szavak[1]) and len(szavak[2]) < len(szavak[0]):
        valasz = 'A harmadik szó a legrövidebb'
    print(valasz)
    
    
szo1 = input("Írd be az első szót:")
szo2 = input("Írd be a második szót:")
szo3 = input("Írd be a harmadik szót:")

szavak = []

szavak.append(szo1)
szavak.append(szo2)
szavak.append(szo3)

print(szavak)

legrovidebb(szavak)