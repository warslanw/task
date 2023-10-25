#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
print("Vücut Kitle Endeksi Hesaplama")
boy = float (input ("Lütfen Boyunuzu Metre Biriminde Giriniz: "))
kilo = float (input ("Lütfen Ağırlığınızı KG Biriminde Giriniz: "))

vucutKitleIndeks = kilo / (boy * boy)
print("Vücut Kitle İndesksiniz: ", vucutKitleIndeks)
