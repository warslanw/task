#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
#EBOB => EN BÜYÜK ORTAK BÖLEN
#EKOK => EN KÜÇÜK ORTAK KAT

import math #math sınıfını kullanbilmek için import edilmiştir.

sayi1=int(input("1. sayıyı giriniz: "))
sayi2=int(input("2. sayıyı giriniz: "))

ebob=math.gcd(sayi1,sayi2) # math.gcd() => Verilen iki sayının EBOB’unu verir.
ekok= (sayi1*sayi2)/ebob   #

print ("EBOB = ",ebob)
print ("EKOK = ",ekok)