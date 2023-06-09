# Python_3.

# Az assert előtt levő # eltávolításával egyenként, szelektíven tesztelni tudod a megoldásodat.
# A feladat kezdetekor, majd minden feladat során futtatni kell a unit teszteket.
#    (pipa a baloldali menüsávon, majd a kék Run tests gomb megnyomása)
# A feladat beadásához a képernyő jobb felső részén a SUBMIT gombot kell megnyomni.

#01===================================================================================
# Feladat: Karakterek száma a fájlban.
# Írj egy függvényt karakterek_szama néven amely paraméterként egy fájlnevet kap és visszatér a fájlban levő karakterek számával. ('\n karakterekkel együtt')
def karakterek_szama(faljneve):
    with open(faljneve) as f:
        szoveg = f.read()
    return len(szoveg)

assert karakterek_szama("lorem.txt") == 18047

#02-------------------------------------------------------------    
# Feladat: Szavak száma a fájlban.
# Írj egy függvényt szavak_szama néven amely paraméterként egy fájlnevet kap és visszatér a fájlban levő szavak számával.
def szavak_szama(faljneve):
    with open(faljneve) as f:
        szoveg = f.read()
    return len(szoveg.split())

assert szavak_szama("lorem.txt") == 2304

#03-------------------------------------------------------------  
# Feladat: Sorok száma a fájlban. 
# A sorok_szama(fname) függvény visszatér a  fájlban levő sorok számával.   
def sorok_szama(fname):
    with open(fname) as f:
        szoveg = f.read()
    return len(szoveg.split("\n"))

assert sorok_szama("lorem.txt") == 82

#04-------------------------------------------------------------
# Feladat: r betük száma a fájlban. 
# Az r_betuk_szama(fname) függvény visszatér a  fájlban levő 'r' betük számával.
def r_betuk_szama(fname):
    with open(fname) as f:
        szoveg = f.read()
    return szoveg.count("r")

assert r_betuk_szama("lorem.txt") == 790 

#05.-------------------------------------------------------------        
# Feladat: lorem szavak száma a fájlban. 
# 5. A lorem_szavak_szama(fname) függvény visszatér a  fájlban levő "lorem" szavak számával.
def lorem_szavak_szama(fname):
    with open(fname) as f:
        szoveg = f.read()
    return szoveg.count("lorem")

assert lorem_szavak_szama("lorem.txt") == 27 

#06-------------------------------------------------------------    
# Feladat: A leggyakoribb karakter a fájlban. 
# A leggyakoribb_karakter(fname) függvény visszatér a  fájlban leggyakrabban előforduló karakterrel.


#assert leggyakoribb_karakter("lorem.txt") ==  "i"

#07------------------------------------------------------------- 
# Feladat: A leghosszabb sor hossza a fájlban. 
# A leghosszabb_sor_hossza(fname) függvény visszatér a  fájlban levő leghosszabb sor hosszával.

#assert leghosszabb_sor_hossza("lorem.txt") == 304

#08-------------------------------------------------------------
# Feladat: Téglalap osztály definiálása. [Objektumorientált programozás]
# Hozz létre egy osztályt Teglalap néven.
# A Teglalap osztály lehetővé teszi a téglalap oldalhosszúságainak tárolását.
# A Teglalap osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
# A Teglalap osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
class Teglalap:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def kerulet(self):
        k = (self.a + self.b)*2
        return k
        
    def terulet(self):
        t = self.a * self.b
        return t

assert Teglalap(3, 4).kerulet() == 14
assert Teglalap(3, 4).terulet() == 12

#09-------------------------------------------------------------
# Feladat: Négyzet osztály definiálása. [Objektumorientált programozás]
# Hozz létre egy osztályt Negyzet néven.
# A Negyzet osztály lehetővé teszi a negyzet oldalhosszúságának tárolását.
# A Negyzet osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
# A Negyzet osztály rendelkezik egy kerulet() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum kerületét.
class Negyzet:
    def __init__(self, a):
        self.a = a
        
    def kerulet(self):
        k = self.a * 4
        return k
        
    def terulet(self):
        t = self.a**2
        return t

assert Negyzet(3).kerulet() == 12
assert Negyzet(3).terulet() == 9

#10-------------------------------------------------------------
# Feladat: Kocka osztály definiálása. [Objektumorientált programozás]
# Hozz létre egy osztályt Kocka néven.
# A Kocka osztály lehetővé teszi a kocka oldalhosszúságának tárolását.
# A Kocka osztály rendelkezik egy tefogat() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum térfogatát.
# A Kocka osztály rendelkezik egy felszin() nevü metódussal, amely az osztály segítségével létrehozott objektum metódusaként visszaadja az adott objektum felszínét.
class Kocka:
    def __init__(self, a):
        self.a = a
        
    def terfogat(self):
        k = self.a ** 3
        return k
        
    def felszin(self):
        t = self.a*self.a*6
        return t

assert Kocka(3).terfogat() == 27
assert Kocka(3).felszin() == 54

#11-------------------------------------------------------------
# Feladat: String fájlba írása
# Készíts függvényt string_fajlba néven amely az első paraméterként kapott sztringet fájlba írja.
# A fájl nevét második paraméterként kapja meg a függvény.


#string_fajlba("csacska macska", "szoveg.txt"); assert open("szoveg.txt").read().strip() == "csacska macska"

#12-------------------------------------------------------------
# Feladat: Számtani sorozat fájlba írása
# Készíts függvényt szaz_szam_fajlba néven amely 1-tól 100-ig egyesével kiírja a számokat egy fájlba.
# Minden szám kerüljön új sorba.
# A fájl nevét paraméterként kapja meg a függvény.
def szaz_szam_fajlba(faljneve):
    with open(faljneve, "w") as file:
        for i in range(1,101):
            file.write(str(i)+"\n")

szaz_szam_fajlba("szazas.txt"); assert len(open("szazas.txt").read())
szaz_szam_fajlba("szazas.txt"); assert sum([int(i) for i in open("szazas.txt")]) == 5050

#13--------------------------------------------------------------------------------------------

# Feladat: Első karakter a szövegfájlban
# Írj egy függvényt elso_karakter_a_fajlban néven amely visszatér egy szövegfájl első karakterével.
# A függvény bemenő paramétere a fájl neve.
def elso_karakter_a_fajlban(faljneve):
    with open(faljneve) as f:
        szoveg = f.read()
    return szoveg[0]

#assert elso_karakter_a_fajlban("lorem.txt") == "L"

#14--------------------------------------------------------------------------------------------

# Feladat: Utolsó karakter a szövegfájlban
# Írj egy függvényt utolso_karakter_a_fajlban néven amely visszatér egy szövegfájl utolsó karakterével.
# A függvény bemenő paramétere a fájl neve.
def utolso_karakter_a_fajlban(faljneve):
    with open(faljneve) as f:
        szoveg = f.read()
    return szoveg[-1]


assert utolso_karakter_a_fajlban("lorem.txt") == "."
