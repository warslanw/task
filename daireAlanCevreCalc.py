#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
import math
print("Dairenin Alanını ve Çevresini Hesaplama İşlemi")
yariCap = complex(input("Lütfen Yarıçapını Giriniz: "))

A = complex (math.pi * yariCap**2)
print(A, "Dairenin Alanı")

cevre = complex (2 * (math.pi) * yariCap)
print(cevre, "Dairenin Çevresi")