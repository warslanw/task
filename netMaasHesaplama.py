#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
print("Zamlı Maaş Hesaplama")
netMaas = float (input("Net Maaşınızı Yazınız: "))
print("%50 Örneğin 1.50 olarak girilecektir")
zamOranı = float(input("Zam Oranını % Biriminden Giriniz: "))

zamlıMaas = netMaas * zamOranı
print("Zamlı Maaşınız: ", zamlıMaas, "TL Tebrikler")