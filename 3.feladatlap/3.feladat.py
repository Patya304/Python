"""
3. feladat: Írj programot, mely miután beolvassa a kör sugarát, kiszámolja a kör területét (1 tizedesnyi pontosággal).
"""
import math

r = int(input("Mennyi a kör sugara: "))
print(f"A kör területe: {round(r**2*math.pi, 1)}cm2")