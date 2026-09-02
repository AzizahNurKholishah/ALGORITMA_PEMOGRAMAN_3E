a = int(input("masukan sisi a: "))
b = int(input("masukan sisi b: "))
c = int(input("masukan sisi c: "))

if a <= 0 or b <= 0 or c <= 0:
    print ("Bukan Segitiga")

elif a + b <= c or a + c <= b or b + c <= a:
    print("Bukan Segitiga")

elif a == b and b == c:
    print("Segitiga sama sisi")

elif a == b or a == c or b == c:
    print("Segitiga sama kaki")

else:
    print("Segitga sembarang")