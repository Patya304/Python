"""
1. feladat: A program kérjen be az egyenlő oldalú háromszög oldalát, majd számolja ki a kerület hetedét! Az eredményt két tizedesnyi pontossággal írja ki.
a + b + c
"""

a = int(input(" Kérem az egyenlő oldalú háromszög oldaát (a): "))
h_num = round(a*3/7, 2) # round() függvény- A függvény egy lebegőpontos számot ad vissza, amely a megadott szám kerekített változata a megadott tizedesjegyek számával.

print(f"A {a}cm oldalú háromszög kerületének hetede {h_num}cm.")

"""
2. feladat:  Feladat) Írj programot, mely miután beolvassa a kör sugarát, kiszámolja a kör kerületét (2 tizedesnyi pontosággal).
"""
import math
kor_sugar = int(input("Kérem a kör sugarát (r): "))

print(f"A {kor_sugar}cm sugarú kör kerülete {round(2 * kor_sugar * math.pi, 2)}")

"""
3. feladat: A program kérje be, hogy hány csillag legyen Béla jutalma.
A válasz alapján a képernyőn jelenjen meg a következő szöveg: Béla jutalma (és a folytatásban a kért számú csillag)
"""

star = int(input(" Hány csillag legyen Béla jutalma? "))

print(f"Béle jutalma:","",end="")
for i in range(star):
    print("*","",end="")
    
    """
4. feladat: A program kérjen be két számot és számolja ki a két szám között lévő számok összegét (a határszámokat ne vegye figyelembe!) 
Írja ki a kérdéses számokat és az összegüket!
"""
a_num = int(input("Kérem az alsó határt: "))
f_num = int(input("Kérem a felső határt: "))
o_num = 0

szoveg = f"A {a_num} és {f_num} közötti számok: "
print(szoveg, "",end="")

for i in range(a_num+1, f_num):
    print(i, ",", "", end="")
    o_num = o_num + i

szoveg = f"A {a_num} és {f_num} közötti számok összege: "
print(f"\n{szoveg} {o_num}")

"""
5. feladat: A program olvasson be tetszőleges számú számot (egészen addig míg 0-ra vegződő számot nem írunk és írja kia beírt számok összegét!)
"""
ossz = 0
mar = 1
i = 1

while mar > 0: 
    num = int(input(f"Kérem az {i}. számot: "))
    ossz = ossz + num
    mar = num % 10
    i = i+1
print(f"A beírt számok összege: {ossz}")
