"""
5. feladat: Írj programot, mely miután megkérdezi, hogy hány éves vagy, annyiszor kiírja (új soronként), hogy: LEGYEN SZÉP NAPOD!
"""
kor = int(input("Hány éves vagy: "))

for i in range(1, kor+1):
    print("Legyen szép napod!")