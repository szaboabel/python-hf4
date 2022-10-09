import math

szam=int(input("Egy szám: "))
if szam%2==0:
    print("A szám páros")
elif szam%2!=0:
    print("nem páros")

szam2=int(input("Szám: "))
if szam2>0:
    print("pozitív")
elif szam2==0:
    print("nulla")
else: print("negatív")

ev=int(input("Adj meg egy évszámot! "))
if ev%4==0:
    print(f"{ev} szökőév")
else: print(f"{ev} nem szökőév")

elert=int(input("Elért pontszám: "))
max=int(input("Max pontszám: "))
kell=max*0.60
if elert >=kell:
    print("Sikeres vizsga")
else: print("Sikertelen vizsga")

s1=int(input("Szám1: "))
s2=int(input("Szám2: "))
s3=int(input("Szám3: "))
if s1<s2 and s1<s3:
    print(f"{s1} a legkisebb")
elif s2<s1 and s2<s3:
    print(f"{s2} a legkisebb")
elif s3<s1 and s3<s2:
    print(f"{s3} a legkisebb")

a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
s=(a+b+c)/2
if a and b and c>0:
    if c<a+b:
        print("szerkeszthető")
        print(f"kerülete: {a+b+c}")
        print(f"területe: {math.sqrt(s*(s-a)*(s-b)*(s-c))}")
    if a**2+b**2==c**2:
        print("derékszögű")
    else: print("hibás bemenet")