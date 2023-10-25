#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
print("En Büyük Sayı Bulma Programı")
i = float(input("1. Sayıyı Giriniz: "))
i1 = float(input("2. Sayıyı Giriniz: "))
i2 = float(input("3. Sayıyı Giriniz: "))

enBuyukSayiBul = max(i, i1, i2)
print(enBuyukSayiBul, "Aralarındaki en büyük sayıdır")