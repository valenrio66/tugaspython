print("===============================")
print("Menghitung Luas Bangun Datar")
print("===============================")
print(" a. Segitiga \n b. Trapesium \n c. Lingkaran")
pil = str(input("Masukkan Pilihan Bangun Datar : "))
if pil == "a":
    a = float(input("Masukkan Alas : "))
    t = float(input("Masukkan Tinggi : "))

    luas_sgt = 1/2 * (a*t)
    print("Luas Segitiga : ", luas_sgt)

elif pil == "b":
    a = float(input("Masukkan Panjang Sisi Atas : "))
    b = float(input("Masukkan Panjang Sisi Bawah : "))
    t = float(input("Masukkan Tinggi : "))

    luas = (((a+b)/2)*t)
    print("Luas Trapesium : ", luas)

elif pil == "c":
    phi = 3.14
    r = float(input("Masukkan Jari - Jari : "))

    luas = (phi*(r*r))
    print("Luas Lingkaran : ", luas)
