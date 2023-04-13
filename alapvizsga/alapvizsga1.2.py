'''---------------------------------------------------------------------------

# Feladat: Két szám összege.
# Írj egy függvényt "osszead" néven, amely két számot kap ésvisszatér a két szám összegével.'''
def osszead(szam1, szam2):
    return szam1 + szam2
    
print(f'Két szám összege: 12 és -8 összege: 4')
print(f'Két szám összege: 12 és -8 összege: {osszead(12, -8)}\n')

'''-------------------------------------------------------------------

# Feladat: Melyik a kisebb?
# Írj egy függvényt "kisebb" néven, amely két számot kap és visszatér a legkisebbel.'''
def kisebb(szam1, szam2):
    if szam1 > szam2:
        return szam2
    else:
        return szam1
    

print(f'Melyik a kisebb?: 12 és -8 közül a kisebb: -8')        
print(f'Melyik a kisebb?: 12 és -8 közül a kisebb: {kisebb(12, -8)}\n')

'''---------------------------------------------------------------------------

# Feladat: Melyik a nagyobb?
# Írj egy függvényt "nagyobb" néven, amely két számot kap és visszatér a legnagyobbal.'''
def nagyobb(szam1, szam2):
    if szam1 > szam2:
        return szam1
    else:
        return szam2
    
print(f'Melyik a nagyobb?: 12 és -8 közül a nagyobb: 12')
print(f'Melyik a nagyobb?: 12 és -8 közül a nagyobb: {nagyobb(12, -8)}\n')

'''---------------------------------------------------------------------------

# Feladat: Számtani közép
# Írj "szamtani_kozep" néven függvényt, amely két számot kap bemenetként és visszatér a számtani középpel.'''

def szamtani_kozep(szam1, szam2):
    return (szam1+szam2) / 2
    

print(f'Számtani közép: 3.0 és 5.0 számtani közepe: 4.0')
print(f'Számtani közép: 3.0 és 5.0 számtani közepe: {szamtani_kozep(3, 5)}\n')

'''---------------------------------------------------------------------------

# Feladat: Négyzet kerülete
# Írj "negyzet_kerulet" néven függvényt, amely egy négyzet oldalhosszát kapja bemenetként és visszatér a négyzet kerületével.'''

def negyzet_kerulet(oldalhossz):
    return oldalhossz*4
    
    
print(f'Négyzet kerülete: Ha 5.1 a négyzet oldala, akkor a négyzet kerülete = 20.4')
print(f'Négyzet kerülete: Ha 5.1 a négyzet oldala, akkor a négyzet kerülete = {negyzet_kerulet(5.1)}\n')

'''---------------------------------------------------------------------------

# Feladat: Négyzet területe
# Írj "negyzet_terulet" néven függvényt, amely egy négyzet oldalhosszát kapja bemenetként és visszatér a négyzet területével.'''

def negyzet_terulet(oldalhossz):
    return oldalhossz*oldalhossz
    
print(f'Négyzet területe: Ha 5.0 a négyzet oldala, akkor a négyzet területe = 25.0')
print(f'Négyzet területe: Ha 5.0 a négyzet oldala, akkor a négyzet területe = {negyzet_terulet(5.0)}\n')

'''---------------------------------------------------------------------------

# Feladat: Téglalap kerülete
# Írj "teglalap_kerulet" néven függvényt, amely egy téglalap oldalhosszait kapja bemenetként és visszatér a téglalap kerületével.'''

def teglalap_kerulet(oldal1, oldal2):
    return 2*oldal1 + 2*oldal2
    
    
print(f'Téglalap kerülete: Ha 5 az egyik oldal és 6 a másik oldal, akkor a téglalap kerülete = 22')
print(f'Téglalap kerülete: Ha 5 az egyik oldal és 6 a másik oldal, akkor a téglalap kerülete = {teglalap_kerulet(5, 6)}\n')
  
'''---------------------------------------------------------------------------

# Feladat: Téglalap területe
# Írj "teglalap_terulet" néven függvényt, amely egy téglalap oldalhosszait kapja bemenetként és visszatér a téglalap területével.'''

def teglalap_terulet(oldal1, oldal2):
    return oldal1*oldal2
    

print(f'Téglalap területe: Ha 5 az egyik oldal és 6 a másik oldal, akkor a téglalap területe = 30')
print(f'Téglalap területe: Ha 5 az egyik oldal és 6 a másik oldal, akkor a téglalap területe = {teglalap_terulet(5, 6)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Két szám különbsége
# Írj "kulonbseg" néven függvényt, amely két számot kap bemenetként és visszatér a két szám különbségével.'''
def kulonbseg(szam1, szam2):
    return szam1 - szam2
    
    
print(f'Két szám különbsége: Ha 5 az egyik szám és 6 a másik szám, akkor a két szám különbsége = -1')
print(f'Két szám különbsége: Ha 5 az egyik szám és 6 a másik szám, akkor a két szám különbsége = {kulonbseg(5, 6)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Maradékos osztás:  
# Írj egy "maradek" nevü függvényt, amely két számot kap bemenetként és visszatér a két szám osztásának maradékával. '''
def maradek(szam1, szam2):
    return szam1 % szam2

print(f'Maradékos osztás: Ha 9 az egyik szám és 4 a másik szám, akkor a két szám osztásának maradéka = 1')
print(f'Maradékos osztás: Ha 9 az egyik szám és 4 a másik szám, akkor a két szám osztásának maradéka = {maradek(9, 4)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Páros szám:  
Írj egy "paros" nevü függvényt, amely egy számot kap bemenetként, majd True-val tér vissza, ha a szám páros és False-al ha a szám páratlan. '''
def paros(szam1):
    if szam1 % 2 == 0:
        return True
    else:
        return False

print(f'Páros szám: Ha a  szám 9 akkor a visszatérési érték: False')
print(f'Páros szám: Ha a  szám 9 akkor a visszatérési érték: {paros(9)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Kettővel osztható:  
# Írj egy "kettovel_oszthato" nevü függvényt, amely egy számot kap bemenetként és True-val tér vissza, ha a szám kettővel osztható és False-al ha nem. '''
def kettovel_oszthato(szam1):
    if szam1 % 2 == 0:
        return True
    else:
        return False

print(f'Kettővel osztható: Ha a  szám 12 akkor a visszatérési érték: True')
print(f'Kettővel osztható: Ha a  szám 12 akkor a visszatérési érték: {kettovel_oszthato(12)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Hárommal osztható:  
# Írj egy "harommal_oszthato" nevü függvényt, amely egy számot kap bemenetként és True-val tér vissza, ha a szám hárommal osztható és False-al ha nem. '''
def harommal_oszthato(szam1):
    if szam1 % 3 == 0:
        return True
    else:
        return False

print(f'Hárommal osztható: Ha a  szám 15 akkor a visszatérési érték: True')
print(f'Hárommal osztható: Ha a  szám 15 akkor a visszatérési érték: {harommal_oszthato(15)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Héttel osztható:  
# Írj egy "hettel_oszthato" nevü függvényt , amely egy számot kap bemenetként és True-val tér vissza, ha a szám héttel osztható és False-al ha nem. '''
def hettel_oszthato(szam1):
    if szam1 % 7 == 0:
        return True
    else:
        return False

print(f'Héttel osztható: Ha a  szám 21 akkor a visszatérési érték: True')
print(f'Héttel osztható: Ha a  szám 21 akkor a visszatérési érték: {hettel_oszthato(21)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Kocka térfogat:  
# Írj egy "kocka_terfogat" nevü függvényt , amely bemenetként megkapja a kocka oldal hosszúságát és a kocka térfogatával tér vissza. '''
def kocka_terfogat(oldal):
    return oldal **3
    
print(f'Kocka térfogat: Ha az oldal 2 akkor a visszatérési érték: 8')
print(f'Kocka térfogat: Ha az oldal 2 akkor a visszatérési érték: {kocka_terfogat(2)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Téglatest térfogat:  
# Írj egy "teglatest_terfogat" nevü függvényt , amely bemenetként megkapja a téglatest oldalainak hosszúságát és a téglatest térfogatával tér vissza. '''
def teglatest_terfogat(a, b, c):
    return a*b*c
    
print(f'Téglatest térfogat: Ha az oldalak hossza: 2, 3 és 4 akkor a visszatérési érték: 24')
print(f'Téglatest térfogat: Ha az oldalak hossza: 2, 3 és 4 akkor a visszatérési érték: {teglatest_terfogat(2, 3, 4)}\n')

'''------------------------------------------------------------------------------------------------------------

# Feladat: Derékszögü háromszög területe:  
# Írj egy "derekszogu_haromszog_terulet" nevü függvényt , amely bemenetként megkapja a befogók hosszát és a háromszög területével tér vissza. '''
def derekszogu_haromszog_terulet(befogo1, befogo2):
    return (befogo1*befogo2)/2
    
print(f'Derékszögü háromszög területe: Ha az elso befogó hossza: 3 és a második befogó hossza: 4  akkor a visszatérési érték: 6')
print(f'Derékszögü háromszög területe: Ha az elso befogó hossza: 3 és a második befogó hossza: 4  akkor a visszatérési érték: {derekszogu_haromszog_terulet(3, 4)}\n')

'''-----------------------------------------------------------------------------------------------------------

# Feladat: Derékszögü háromszög átlója: 
# Írj egy "derekszogu_haromszog_atloja" nevü függvényt , amely bemenetként megkapja a befogók hosszát és az átló hosszával tér vissza. '''
def derekszogu_haromszog_atloja(befogo1, befogo2):
    return (befogo1 ** 2 + befogo2 ** 2) ** 0.5
    
    
print(f'Derékszögü háromszög átlója: Ha az elso befogó hossza: 3 és a második befogó hossza: 4  akkor a visszatérési érték: 5.0')
print(f'Derékszögü háromszög átlója: Ha az elso befogó hossza: 3 és a második befogó hossza: 4  akkor a visszatérési érték: {derekszogu_haromszog_atloja(3, 4)}\n')


'''-----------------------------------------------------------------------------------------------------------

# Feladat: Négyzet átlója:  
# Írj egy "negyzet_atloja" nevü függvényt , amely bemenetként megkapja a négyzet oldalának hosszát és az átló hosszával tér vissza. '''
def negyzet_atloja(oldal):
    return oldal * (2 ** 0.5)
        
print(f'Négyzet átlója: Ha az oldal hossza: 10 akkor a visszatérési érték: 14.142135623730951')
print(f'Négyzet átlója: Ha az oldal hossza: 10 akkor a visszatérési érték: {negyzet_atloja(10)}\n')

'''-----------------------------------------------------------------------------------------------------------

# Feladat: Téglalap átlója: 
# Írj egy "teglalap_atloja" nevü függvényt , amely bemenetként megkapja az oldalak hosszát és az átló hosszával tér vissza. '''
def teglalap_atloja(oldal1, oldal2):
    return (oldal1**2 + oldal2 **2) **0.5
    
    
print(f'Téglalap átlója: Ha az egyik oldala hossza: 3 és a másik oldal hossza: 4  akkor a visszatérési érték: 5.0')
print(f'Téglalap átlója: Ha az egyik oldala hossza: 3 és a másik oldal hossza: 4  akkor a visszatérési érték: {teglalap_atloja(3, 4)}\n')


#========================================================================================================================
