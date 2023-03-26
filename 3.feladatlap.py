"""
1. feladat: Írj programot, mely miután megkérdezi, hogy milyen van van ma, kiírja azt.
"""
nap = input("Milyen nap van ma: ")
print(f"Ma Egész nap {nap} van.")

"""
2. feladat: Írj programot, mely egy beolvasott számra kiírja
a) annak kétszeresét
a szám 10-zel nagyobb értékét
"""
num = int(input("Kérek egy számot: "))
print(f"A szám kétszerese: {num*2} \nA számtól tizzel nagyobb szám: {num+10}")

"""
3. feladat: Írj programot, mely miután beolvassa a kör sugarát, kiszámolja a kör területét (1 tizedesnyi pontosággal).
"""
import math

r = int(input("Mennyi a kör sugara: "))
print(f"A kör területe: {round(r**2*math.pi, 1)}cm2")

"""
4. feladat: Írj programot, mely miután beolvassa az egyenlő oldalú háromszög oldalát, területét (1 tizedesnyi pontosággal).
"""
# gyök3 ~ 1,73

oldal = int(input("Mennyi a háromszög oldala: "))
gyok3 = 1.73
m = oldal*gyok3/2

print(f"A háromszög területe: {round(oldal**2*gyok3/4, 1)}cm2")

"""
5. feladat: Írj programot, mely miután megkérdezi, hogy hány éves vagy, annyiszor kiírja (új soronként), hogy: LEGYEN SZÉP NAPOD!
"""
kor = int(input("Hány éves vagy: "))

for i in range(1, kor+1):
    print("Legyen szép napod!")
