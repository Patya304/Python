'''
Írj egy Python függvényt, amely meghatározza egy adott egész szám osztóinak számát, majd írj ki egy ellenőrzőt az eredményhez!
'''
def osztoi_szam(szam):
    osztok = 0
    for i in range(1, szam+1):
        if szam % i == 0:
            osztok += 1
    return osztok
# Tesztelés
szam = 36
eredmeny = osztoi_szam(szam)
print(f"A(z) {szam} számnak {eredmeny} osztója van.")

'''
Írj egy Python függvényt, amely meghatározza, hogy egy adott szám prím-e vagy sem, majd írj ki egy ellenőrzőt az eredményhez!
'''
def prim_e(szam):
    if szam < 2:
        return False
    for i in range(2, int(szam**(1/2))+1):
        if szam % i == 0:
            return False
    return True
# Tesztelés
szam = 17
if prim_e(szam):
    print(f"A(z) {szam} szám prím.")
else:
    print(f"A(z) {szam} szám nem prím.")

'''
Írj egy Python függvényt, amely kiszámítja az adott szám faktoriálisát, majd írj ki egy ellenőrzőt az eredményhez!
'''
def faktorialis(szam):
    fakt = 1
    for i in range(1, szam+1):
        fakt *= i
    return fakt
# Tesztelés
szam = 5
eredmeny = faktorialis(szam)
print(f"A(z) {szam} szám faktoriálisa: {eredmeny}")

'''
Írj egy Python függvényt, amely kiszámítja az adott szám fibonacci sorozatának n-edik elemét, majd írj ki egy ellenőrzőt az eredményhez!
'''
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# Tesztelés
n = 8
eredmeny = fibonacci(n)
print(f"A(z) {n}. elem a Fibonacci sorozatban: {eredmeny}")

'''
Írj egy Python függvényt, amely kiszámítja két adott szám legnagyobb közös osztóját, majd írj ki egy ellenőrzőt az eredményhez!
'''
def lnko(szam1, szam2):
    nagyobb = max(szam1, szam2)
    kisebb = min(szam1, szam2)
    while kisebb != 0:
        maradek = nagyobb % kisebb
        nagyobb = kisebb
        kisebb = maradek
    return nagyobb
#Tesztelés
szam1, szam2 = 48, 60
eredmeny = lnko(szam1, szam2)
print(f"A(z) {szam1} és {szam2} számok legnagyobb közös osztója: {eredmeny}")

#------------------------------------------------------------------------------------------------------------------------------------------#
