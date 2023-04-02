'''
Írj egy Python függvényt, amely megfordítja egy adott sztringet. A függvény visszatérési értéke legyen a megfordított sztring.
'''
def fordit(szoveg):
    return szoveg[::-1]
# Tesztelés
print(fordit("szia"))

'''
Írj egy Python függvényt, amely megszámolja, hogy egy adott sztringben hányszor fordul elő egy adott karakter.
A függvény visszatérési értéke legyen a karakter előfordulási száma.
'''
def szamol_karakter(szoveg, karak):
    szamol = 0
    for char in szoveg:
        if char == karak:
            szamol =+ 1
    return szamol
# Testelés
print(szamol_karakter("Szia uram", "a"))

'''
Írj egy Python függvényt, amely meghatározza, hogy egy adott szám palindrom-e vagy sem.
A függvény visszatérési értéke legyen True, ha a szám palindrom, és False, ha nem.
'''
def palindrome_szam(szam):
    if str(szam) == str(szam)[::-1]:
        return True
    else:
        return False
# Tesztelés
print(palindrome_szam(12321))

'''
Írj egy Python függvényt, amely meghatározza, hogy egy adott sztring palindrom-e vagy sem.
A függvény visszatérési értéke legyen True, ha a sztring palindrom, és False, ha nem.
'''
def palindrome_szoveg(szoveg):
    if szoveg == szoveg[::-1]:
        return True
    else:
        return False
# Tesztelés
print(palindrome_szoveg("hello"))

'''
Írj egy Python függvényt, amely egy adott számról eldönti, hogy Armstrong szám-e vagy sem.
Egy Armstrong szám olyan szám, amelynek a számjegyei köbének összege megegyezik a számmal. Például: 153 = 1^3 + 5^3 + 3^3.
'''
def armstrong(szam):
    sum = 0
    ord = len(str(szam))
    temp = szam
    while temp > 0:
        digit = temp % 10
        sum += digit ** ord
        temp //= 10
    if szam == sum:
        return True
    else:
        return False
# Tesztelés
print(armstrong(153))

'''
Írj egy Python függvényt, amely egy adott listát rendezett formában ad vissza. A függvény bemenete egy lista, a visszatérési értéke pedig a rendezett lista.
'''
def sort_lista(lista):
    return sorted(lista)
# Tesztelés 
print(sort_lista([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
print(sort_lista(['banana', 'apple', 'cherry', 'date', 'elderberry'])) # ['apple', 'banana', 'cherry', 'date', 'elderberry']

'''
Írj egy Python függvényt, amely egy adott listát összefűzött formában ad vissza. A függvény bemenete egy lista, a visszatérési értéke pedig az összefűzött lista.
'''
def osszefuz_lista(lista2):
    return ''.join(lista2)
# Tesztelés
print(osszefuz_lista(['h', 'e', 'l', 'l', 'o']))      # "hello"
print(osszefuz_lista(['e', 'z', ' ', 'e', 'g', 'y', ' ', 'l', 'i', 's', 't', 'a'])) # "this is a list"

'''
Írj egy Python függvényt, amely meghatározza a legnagyobb közös osztót két adott számnak. A függvény bemenete két szám, a visszatérési érték pedig a legnagyobb közös osztó.
'''
def legnagyobbkozos_oszt(szam1, szam2):
    if szam2 == 0:
        return szam1
    else:
        return legnagyobbkozos_oszt(szam2, szam1 % szam2)
# Tesztelés
print(legnagyobbkozos_oszt(8, 12))

'''
Írj egy Python függvényt, amely meghatározza egy adott stringben a leghosszabb szót, és visszaadja azt.
A függvény bemenete egy string, a visszatérési érték pedig a leghosszabb szó.
'''
def hosszabb_szo(text):
    szovegek = text.split()
    hosszabb = ''
    for szoveg in szovegek:
        if len(szoveg) > len(hosszabb):
            hosszabb = szoveg
    return hosszabb
# Tesztelés
print(hosszabb_szo('A gyors barna róka átugorja a lusta kutyát.'))