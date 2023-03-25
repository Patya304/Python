"""
1. feladat: A program kérjen be egy vezetéknevet és egy keresztnevet. Üdvözölje a felhasználót 
Vezetéknév - keresztnév sorrendben
Keresztnév - vezetéknév sorrendben
"""

v = input("Kérem a vezetéknevet: ")
k = input("Kérem a keresztknevet: ")

print(f"Üdvözöllek {v,k} \nÜdvözöllek {k,v}")

"""
2. feladat: A program kérjen egy számot, majd írja annak megelőzőjét, illetve rákövetkezőjét
"""
num = int(input("Kérek egy számot? "))

print(f"A {num} megelőzője: {num-1} \nA {num} rákövetkezője: {num+1}")

"""
3. feladat: A program kérjen be két számot, majd számolja ki azok összegét, különbségét, szorzatát és hányadást 
"""

e_num = int(input("Kérem az első számot: "))
m_num = int(input("Kérem a második számot: "))

print(f"A két szám összege: {e_num+m_num} \nA két szám különbsége: {e_num-m_num} \nA két szám szorzata: {e_num*m_num} \nA két szám hányadosa: {e_num/m_num}")

"""
4. feladat: A program kérjen be két változót (a és b).
Számolja a c változó értékét a következő képlet segítségével: c = 2*a + 3*b
Számolja a d változó értékét a következő képlet segítségével: d = c - 2*a - 3b
"""

a_valtozo = int(input("Kérem az a változó értékét: "))
b_valtozo = int(input("Kérem az b változó értékét: "))
c = 2*a_valtozo + 3*b_valtozo
d = c - 2*a_valtozo - 3*b_valtozo


print(f"A c változó értéke: {c} \n A d változó értéke: {d}")
