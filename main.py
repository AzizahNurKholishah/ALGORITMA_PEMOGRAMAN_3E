r = float(input("Masukkan jari-jari lingkaran: "))

if r <= 0:
    print("Jari-jari harus lebih dari 0")
else:
    luas = 3.14 * r * r
    print("Luas lingkaran:", luas)