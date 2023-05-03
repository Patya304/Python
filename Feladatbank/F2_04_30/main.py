#1--------------------------------------------------------------------------------------------

# Feladat: Első karakter
# Írj egy függvényt elso_karakter néven amely visszatér az adott string első karakterével!
def elso_karakter(szoveg):
    return szoveg[0]

assert elso_karakter("Hello") == "H"

#2--------------------------------------------------------------------------------------------

# Feladat: Utolsó karakter
# Írj egy függvényt utolso_karakter néven  amely visszatér az adott string utolso karakterével!
def utolso_karakter(szoveg):
    return szoveg[-1]

assert utolso_karakter("Hello") == "o"

#3--------------------------------------------------------------------------------------------

# Feladat: Legkisebb szám a listában. [Programozási tétel: Minimum kiválasztás]
# Készíts függvényt legkisebb néven,  amely visszatér egy számokat tartalmazó lista legkisebb számával.
# Figyelem! A feladat megoldása során nem használhatod a min függvényt! 
def legkisebb(lista):
    min_elem = lista[0]
    for elem in lista:
        if elem < min_elem:
            min_elem = elem
    return min_elem
assert legkisebb( [7, 4, 9, -4, -8, 3]) == -8

#4-------------------------------------------------------------------------------------------


# Feladat: Legnagyobb szám a listában. [Programozási tétel: Maximum kiválasztás]
# Készíts függvényt legnagyobb néven,  amely visszatér egy számokat tartalmazó lista legnagyobb számával.
# Figyelem! A feladat megoldása során nem használhatod a max függvényt! 
def legnagyobb(lista):
    max_elem = lista[0]
    for elem in lista:
        if elem > max_elem:
            max_elem = elem
    return max_elem
assert legnagyobb( [7, 4, 9, -4, -8, 3] ) == 9

#5-------------------------------------------------------------------------------------------

# Feladat: Listaban levő számok összege. [Programozási tétel: Összegzés]
# Készíts függvényt osszeg néven,  amely visszatér egy számokat tartalmazó lista számainak összegével.
# Figyelem! A feladat megoldása során nem használhatod a sum függvényt! 
def osszeg(lista):
    eredmeny = 0
    for szam in lista:
        eredmeny+= szam
    return eredmeny
    
assert osszeg( [1, 2, 3, 4, 5, 6] ) == 21

#6-------------------------------------------------------------------------------------------
       
# Feladat: Listában levő számok szorzata.
# Készíts függvényt szorzat néven,  amely visszatér egy számokat tartalmazó lista számainak szorzatával. 
def szorzat(lista):
    eredmeny = 1
    for szam in lista:
        eredmeny*= szam
    return eredmeny
assert szorzat( [1, 2, 3, 4, 5] )  == 120
    
#7-------------------------------------------------------------------------------------------
    
# Feladat: Páros számok száma a listában. [Programozási tétel: Megszámolás]
# Készíts függvényt parosok_szama néven,  amely visszatér egy számokat tartalmazó lista páros számainak számával.
def parosok_szama(szamok):
    parosok = 0
    for szam in szamok:
        if szam % 2 == 0:
            parosok+=1
    return parosok
        

assert parosok_szama( [7, 4, 9, -4, -8, 3, 1] ) == 3

#8-------------------------------------------------------------------------------------------

# Feladat: Páratlan számok száma a listában. [Programozási tétel: Megszámolás]
# Készíts függvényt paratlanok_szama néven,  amely visszatér egy számokat tartalmazó lista páros számainak számával. 
def paratlanok_szama(szamok):
    paratlanok = 0
    for szam in szamok:
        if szam % 2:
            paratlanok+=1
    return paratlanok
assert paratlanok_szama( [7, 4, 9, -4, -8, 3, 1]) == 4

#9-------------------------------------------------------------------------------------------

# Feladat: Pozitív számok száma a listában. [Programozási tétel: Megszámolás]
# Készíts függvényt pozitivok_szama néven,  amely visszatér egy számokat tartalmazó lista pozitív számainak számával.
def pozitivok_szama(szamok):
    pozitivok = 0
    for szam in szamok:
        if szam > 0:
            pozitivok += 1
    return pozitivok

assert pozitivok_szama( [-7, -4, 9, -4, -8, 3, 1, 0]) == 3

#10-------------------------------------------------------------------------------------------

# Feladat: Negatív számok száma a listában. [Programozási tétel: Megszámolás]
# Készíts függvényt negativok_szama néven,  amely visszatér egy számokat tartalmazó lista negativ számainak számával.
def negativok_szama(szamok):
    negativok = 0
    for szam in szamok:
        if szam < 0:
            negativok+=1
    return negativok

assert negativok_szama( [-7, -4, 9, -4, -8, 3, 1, 0]) == 4

#11-------------------------------------------------------------------------------------------
# Feladat: Benne van a szám a listában? [Programozási tétel: Eldöntés]
# Készíts függvényt benne_van_a_listaban néven,  amelynek első paramétere egy számokat tartalmazó lista, a második paramétere egy szám. 
# A visszatérési érték True, ha  a szám benne van a listában.
# A visszatérési érték False, ha  a szám nics benne a listában.
def benne_van_a_listaban(szamok, keresett_szam):
    for szam in szamok:
        if szam == keresett_szam:
            return True
    return False
    
assert benne_van_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 2) == False
assert benne_van_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 9) == True

#12-------------------------------------------------------------------------------------------
# Feladat: Benne van a betü a stringben? [Programozási tétel: Eldöntés]
# Készíts függvényt benne_van_a_stringben néven,  amelynek első paramétere egy string, a második paramétere egy betü. 
# A visszatérési érték True, ha  a betü benne van a stringben.
# A visszatérési érték False, ha  a betü nics benne a stringben.
def benne_van_a_stringben(szoveg, betu):
    for karakter in szoveg:
        if karakter == betu:
            return True
    return False

assert benne_van_a_stringben("abrakadabra", "x") == False
assert benne_van_a_stringben("abrakadabra", "d") == True

#13-------------------------------------------------------------------------------------------

# Feladat: Hányadik a listában? [Programozási tétel: Kiválasztás]
#         A listában a szám garantáltan megtalálható, nem kell vizsgálni a meglétét.         
# Készíts függvényt hanyadik_a_listaban néven,  amelynek első paramétere egy számokat tartalmazó lista, a második paramétere egy szám. 
# A visszatérési érték a paraméterként megadott szám első előfordulási helye a listában.
def hanyadik_a_listában(lista, szam):
    # for i in range(len(lista)):
    #     if lista[i] == szam:
    #         return i+1
    # return 
    return lista.index(szam)

assert hanyadik_a_listában([-7, -4, 9, -4, -8, 3, 1, 0], -7) == 0
assert hanyadik_a_listában([-7, -4, 9, -4, -8, 3, 1, 0],  9) == 2
#
#14-------------------------------------------------------------------------------------------
# Feladat: Hányadik a stringben? [Programozási tétel: Kiválasztás]
#          A betü garantáltan megtalálható a stringben, nem kell vizsgálnunk a meglétét.
# Készíts függvényt hanyadik_a_stringben néven, amelynek első paramétere egy string, a második paramétere egy betü. 
# A visszatérési érték a paraméterként megadott betü első előfordulási helye a stringben.
def hanyadik_a_stringben(lista, betu):
    return lista.index(betu)

assert hanyadik_a_stringben("abrakadabra", "a") == 0
assert hanyadik_a_stringben("abrakadabra", "k") == 4

#15-------------------------------------------------------------------------------------------
# Feladat: Benne van-e a listában és hanyadik helyen? [Programozási tétel: Keresés]
# Készíts függvényt kereses_a_listaban néven,  amelynek első paramétere egy számokat tartalmazó lista, a második paramétere egy szám. 
# Ha a szám benne van a listában, akkor a visszatérési érték a paraméterként megadott szám első előfordulási helye a listában.
# A visszatérési érték None, ha  a szám nics benne a listában.
def kereses_a_listaban(lista, szam):
    for i, elem in enumerate(lista):
        if elem == szam:
            return i
    return None
    
assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], -7) == 0
assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0],  9) == 2
assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0],  2) == None

#16-------------------------------------------------------------------------------------------
# Feladat: Hányadik a stringben? [Programozási tétel: Keresés]
# Készíts függvényt kereses_a_stringben néven, amelynek első paramétere egy string, a második paramétere egy betü. 
# A visszatérési érték a paraméterként megadott betü első előfordulási helye a stringben.
# A visszatérési érték None, ha  a betü nics benne a stringben.
def kereses_a_stringben(szoveg, betu):
    if betu in szoveg:
        return szoveg.index(betu)
    else:
        return None
    
assert kereses_a_stringben("abrakadabra", "a") == 0
assert kereses_a_stringben("abrakadabra", "k") == 4
assert kereses_a_stringben("abrakadabra", "s") == None

#17-------------------------------------------------------------------------------------------
    
# Feladat: Páros számok kiválogatása egy listából. [Programozási tétel: Kiválogatás]
# Készíts függvényt parosok_kivalogatasa néven,  amely visszatér egy listával amely a paraméterként átadott számokat tartalmazó lista páros számait tartalmazza. 
def parosok_kivalogatasa(szamok):
    parosok = []
    for szam in szamok:
        if szam % 2 == 0:
            parosok.append(szam)
    return parosok

assert parosok_kivalogatasa( [7, 4, 9, -4, -8, 3, 1, 12, 0] ) == [4, -4, -8, 12, 0]

#18-------------------------------------------------------------------------------------------

# Feladat: Páratlan számok számok kiválogatása egy listából. [Programozási tétel: Kiválogatás]
# Készíts függvényt paratlanok_kivalogatasa néven,  amely visszatér egy listával amely a paraméterként átadott számokat tartalmazó lista páratlan számait tartalmazza. 
def paratlanok_kivalogatasa(szamok):
    return [szam for szam in szamok if szam % 2 == 1]

assert paratlanok_kivalogatasa( [7, 4, 9, -4, -8, 3, 1, 12, 0] ) == [7, 9, 3, 1]

#19-------------------------------------------------------------------------------------------
    
# Feladat: Pozitív számok kiválogatása egy listából. [Programozási tétel: Kiválogatás]
# Készíts függvényt pozitivok_kivalogatasa néven,  amely visszatér egy listával amely a paraméterként átadott számokat tartalmazó lista pozitiv számait tartalmazza. 
def pozitivok_kivalogatasa(szamok):
    pozitivak = [szam for szam in szamok if szam > 0]
    return pozitivak

assert pozitivok_kivalogatasa( [7, 4, 9, -4, -8, 3, 1, 12, 0] ) == [7, 4, 9, 3, 1, 12]

#20-------------------------------------------------------------------------------------------

# Feladat: Negatív számok számok kiválogatása egy listából. [Programozási tétel: Kiválogatás]
# Készíts függvényt negatívok_kivalogatasa néven,  amely visszatér egy listával amely a paraméterként átadott számokat tartalmazó lista negatív számait tartalmazza. 
def negativok_kivalogatasa(szamok):
    negativ_szamok = []
    for szam in szamok:
        if szam < 0:
            negativ_szamok.append(szam)
    return negativ_szamok
    
assert negativok_kivalogatasa( [7, 4, 9, -4, -8, 3, 1, 12, 0] ) == [-4, -8]


#21-------------------------------------------------------------------------------------------

# Feladat: Két halmaz metszete. [Programozási tétel: Metszet]
# Készíts függvényt halmazok_metszete néven, amely két paraméterként átadott halmaz azonos elemeivel mint halmazzal tér vissza. 
def halmazok_metszete(halmaz1, halmaz2):
    return halmaz1.intersection(halmaz2)

assert halmazok_metszete({1, 2, 3, 4, 5, 6, 7}, {4, 5, 6, 7, 8, 9}) == {4, 5, 6, 7}

#22-------------------------------------------------------------------------------------------

# Feladat: Két lista metszete. [Programozási tétel: Metszet]
# Készíts függvényt listak_metszete néven, amely két paraméterként átadott lista azonos elemeivel mint listával tér vissza. 
def listak_metszete(lista1, lista2):
    halmaz1 = set(lista1)
    halmaz2 = set(lista2)
    metszet_halmaz = halmaz1 & halmaz2
    return list(metszet_halmaz)
    
assert listak_metszete([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 8, 9]) == [4, 5, 6, 7]

#23-------------------------------------------------------------------------------------------

# Feladat: Két halmaz uniója. [Programozási tétel: Unió]
# Készíts függvényt halmazok_unioja néven, amely két paraméterként átadott halmaz minden elemeivel mint halmazzal tér vissza. 
def halmazok_unioja(h1,h2):
    return h1.union(h2)

assert halmazok_unioja({1, 2, 3, 4, 5, 6, 7}, {4, 5, 6, 7, 8, 9}) == {1, 2, 3, 4, 5, 6, 7, 8, 9}


#24-------------------------------------------------------------------------------------------

# Feladat: Listaban levő számok átlaga (számtani közepe).
# Készíts függvényt lista_atlag néven,  amely visszatér egy számokat tartalmazó lista számainak átlagával.
def lista_atlag(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

assert lista_atlag([1, 2, 3, 4, 5, 6]) == 21/6


#25-------------------------------------------------------------------------------------------

# Feladat: Faktoriális.
# Készíts függvényt faktorialis néven,  amely visszatér a paraméterként megkapott szám faktoriálisával.
def faktorialis(n):
    fakt = 1
    for i in range(1, n+1):
        fakt *= i
    return fakt
# 
assert  faktorialis(0) == 1
assert  faktorialis(1) == 1
assert  faktorialis(2) == 1 * 2
assert  faktorialis(4) == 1 * 2 * 3 * 4
assert  faktorialis(5) == 1 * 2 * 3 * 4 * 5
