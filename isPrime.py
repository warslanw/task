# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
#Asal sayılar, sadece kendisi ve 1 sayısına bölünebilen 1'den büyük pozitif tam sayılardır.
sayi=int(input("Lütfen Sayı Girininiz : "))
if sayi > 1:
   
   for i in range(2,sayi): #(range)Döngüdeki başlangıcımız 2'dir; yani 2 den başlar 1 arttırarak girilen sayı değerine kadar aradaki bütün sayılardır.
       if (sayi % i) == 0: 
           print(sayi," Asal Sayı Değildir.") 
           break
   else:
       print(sayi," Asal Sayıdır.")
else:
   print(sayi," Asal Sayı Değildir.")