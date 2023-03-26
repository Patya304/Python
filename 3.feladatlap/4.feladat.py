"""
4. feladat: Írj programot, mely miután beolvassa az egyenlő oldalú háromszög oldalát, területét (1 tizedesnyi pontosággal).
"""
# gyök3 ~ 1,73

oldal = int(input("Mennyi a háromszög oldala: "))
gyok3 = 1.73
m = oldal*gyok3/2

print(f"A háromszög területe: {round(oldal**2*gyok3/4, 1)}cm2")