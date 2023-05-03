#01---------------------------------------------------------------------------
# Feladat: Két szám összege.
# Írj egy függvényt "osszead" néven, amely két számot kap és visszatér a két szám összegével.
def osszead(szam1, szam2):
    return szam1 + szam2

assert osszead(12, -8) == 4
assert osszead(12,  8) == 20

#02-------------------------------------------------------------------
# Feladat: Melyik a kisebb?
# Írj egy függvényt "kisebb" néven, amely két számot kap és visszatér a legkisebbel.
def kisebb(szam1, szam2):
    if szam1 > szam2:
        return szam2
    else:
        return szam1

assert kisebb(12, -8) == -8
assert kisebb(-8, 12) == -8

#03---------------------------------------------------------------------------
# Feladat: Melyik a nagyobb?
# Írj egy függvényt "nagyobb" néven, amely két számot kap és visszatér a legnagyobbal.
def nagyobb(szam1, szam2):
    if szam1 > szam2:
        return szam1
    else:
        return szam2

assert nagyobb(12, -8) == 12    
assert nagyobb(-8, 12) == 12    

#04---------------------------------------------------------------------------
# Feladat: Számtani közép
# Írj "szamtani_kozep" néven függvényt, amely két számot kap bemenetként és visszatér a számtani középpel.
def szamtani_kozep(szam1, szam2):
    return (szam1+szam2)/2

assert szamtani_kozep(3, 5) == 4.0

#05---------------------------------------------------------------------------
# Feladat: Négyzet kerülete
# Írj "negyzet_kerulet" néven függvényt, amely egy négyzet oldalhosszát kapja bemenetként és visszatér a négyzet kerületével.
def negyzet_kerulet(a):
    return a*4

assert negyzet_kerulet(5.1) == 20.4

#06---------------------------------------------------------------------------
# Feladat: Négyzet területe
# Írj "negyzet_terulet" néven függvényt, amely egy négyzet oldalhosszát kapja bemenetként és visszatér a négyzet területével.
def negyzet_terulet(a):
    return a*a

assert negyzet_terulet(5.0) == 25.0

#07---------------------------------------------------------------------------
# Feladat: Téglalap kerülete
# Írj "teglalap_kerulet" néven függvényt, amely egy téglalap oldalhosszait kapja bemenetként és visszatér a téglalap kerületével.
def teglalap_kerulet(a, b):
    return 2*(a+b)

assert teglalap_kerulet(5, 6) == 22

#08---------------------------------------------------------------------------
# Feladat: Téglalap területe
# Írj "teglalap_terulet" néven függvényt, amely egy téglalap oldalhosszait kapja bemenetként és visszatér a téglalap területével.
def teglalap_terulet(a,b):
    return a*b

assert teglalap_terulet(5, 6) == 30

#09------------------------------------------------------------------------------------------------------------

# Feladat: Két szám különbsége
# Írj "kulonbseg" néven függvényt, amely két számot kap bemenetként és visszatér a két szám különbségével.
def kulonbseg(szam1, szam2):
    return szam1-szam2

assert kulonbseg(5, 6) == -1

#10------------------------------------------------------------------------------------------------------------

# Feladat: Maradékos osztás:  
# Írj egy "maradek" nevü függvényt, amely két számot kap bemenetként és visszatér a két szám osztásának maradékával.
def maradek(szam1, szam2):
    return szam1 % szam2

assert maradek(9, 4) == 1
assert maradek(8, 4) == 0

#11------------------------------------------------------------------------------------------------------------
# Feladat: Páros szám:  
#Írj egy "paros" nevü függvényt, amely egy számot kap bemenetként, majd True-val tér vissza, ha a szám páros és False-al ha a szám páratlan.
def paros(szam):
    if szam % 2 == 0:
        return True
    else:
        return False

assert paros(9) == False
assert paros(8) == True

#12------------------------------------------------------------------------------------------------------------

# Feladat: Kettővel osztható:  
# Írj egy "kettovel_oszthato" nevü függvényt, amely egy számot kap bemenetként és True-val tér vissza, ha a szám kettővel osztható és False-al ha nem.
def kettovel_oszthato(szam):
    if szam % 2 == 0:
        return True
    else:
        return False

assert kettovel_oszthato(12) == True
assert kettovel_oszthato(13) == False

#13------------------------------------------------------------------------------------------------------------
# Feladat: Hárommal osztható:
# Írj egy "harommal_oszthato" nevü függvényt, amely egy számot kap bemenetként és True-val tér vissza, ha a szám hárommal osztható és False-al ha nem.
def harommal_oszthato(szam):
    if szam % 3 == 0:
        return True
    else:
        return False

assert harommal_oszthato(15) == True
assert harommal_oszthato(16) == False

#14------------------------------------------------------------------------------------------------------------
# Feladat: Héttel osztható:  
# Írj egy "hettel_oszthato" nevü függvényt , amely egy számot kap bemenetként és True-val tér vissza, ha a szám héttel osztható és False-al ha nem.
def hettel_oszthato(szam):
    if szam % 7 == 0:
        return True
    else:
        return False

assert hettel_oszthato(21) == True
assert hettel_oszthato(22) == False

#15------------------------------------------------------------------------------------------------------------
# Feladat: Kocka térfogat:  
# Írj egy "kocka_terfogat" nevü függvényt , amely bemenetként megkapja a kocka oldal hosszúságát és a kocka térfogatával tér vissza.
def kocka_terfogat(adat):
    return adat**3

assert kocka_terfogat(2) == 8
assert kocka_terfogat(3) == 27

#16------------------------------------------------------------------------------------------------------------
# Feladat: Téglatest térfogat:  
# Írj egy "teglatest_terfogat" nevü függvényt , amely bemenetként megkapja a téglatest oldalainak hosszúságát és a téglatest térfogatával tér vissza.
def teglatest_terfogat(a,b,c):
    return a*b*c

assert teglatest_terfogat(2, 3, 4) == 24

#17------------------------------------------------------------------------------------------------------------
# Feladat: Derékszögü háromszög területe:  
# Írj egy "derekszogu_haromszog_terulet" nevü függvényt , amely bemenetként megkapja a befogók hosszát és a háromszög területével tér vissza.
def derekszogu_haromszog_terulet(a,b):
    return a*b/2

assert derekszogu_haromszog_terulet(3, 4) == 6

#18-----------------------------------------------------------------------------------------------------------
# Feladat: Derékszögü háromszög átfogója: 
# Írj egy "derekszogu_haromszog_atfogo" nevü függvényt , amely bemenetként megkapja a befogók hosszát és az átló hosszával tér vissza.
def derekszogu_haromszog_atfogo(a,b):
    return (a**2 + b**2)**0.5

assert derekszogu_haromszog_atfogo(3, 4), 5.0

#19-----------------------------------------------------------------------------------------------------------
# Feladat: Négyzet átlója:  
# Írj egy "negyzet_atloja" nevü függvényt , amely bemenetként megkapja a négyzet oldalának hosszát és az átló hosszával tér vissza.
def negyzet_atloja(szam):
    return szam*(2**0.5)

assert round(negyzet_atloja(10),5) == round(14.142135623730951,5)

#20-----------------------------------------------------------------------------------------------------------
# Feladat: Téglalap átlója: 
# Írj egy "teglalap_atloja" nevü függvényt , amely bemenetként megkapja az oldalak hosszát és az átló hosszával tér vissza.
def teglalap_atloja(a,b):
    return (a**2+b**2)**0.5

assert teglalap_atloja(3, 4) == 5.0
assert teglalap_atloja(6, 8) == 10.0

#21-----------------------------------------------------------------------------------------------------------
# Feladat: Abszolútérték: 
# Írj egy "abszolut" nevü függvényt , amely a bemenő paraméterként kapott szám abszolút értékével tér vissza.
def abszolut(szam):
    ...

#assert abszolut( 3) == 3
#assert abszolut(-7) == 7
#assert abszolut( 0) == 0
#========================================================================================================================
