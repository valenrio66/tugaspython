# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 21:57:12 2021

@author: Acer
"""

def odd(n):
 nilai = n % 2
 if nilai != 0:
     tampilkan=True
 else:
     tampilkan=False
 return tampilkan

class Serigala():
    def __init__(self):
        print("Serigala bulu putih, mata biru laut")
tampilkan = Serigala()

class Perkenalan():
    def __init__(self):
        nama = input("Masukkan Nama : ")
        hobi = input("Masukkan Hobi : ")
        umur = input("Masukkan Umur : ")
        print("Halo, nama saya adalah %s, hobi saya adalah %s dan umur saya adalah %s tahun" % (nama, hobi, umur))
        
def pelangi(warna):
  print(f'Salah satu warna pelangi adalah {warna}')
  
class Kelulusan():
 
    def __init__(self, masukan_nama):
        self.nama = masukan_nama
 
    def nilai(self, nilai):
        if nilai >= 70:
            print(self.nama,'Selamat anda lulus dengan nilai',nilai)
        else:
            print(self.nama,'Maaf anda tidak lulus dengan nilai',nilai)
 
mhs=Kelulusan("VALEN")
print(mhs.nama)
mhs.nilai(90)