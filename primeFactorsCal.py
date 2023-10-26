#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
def primeFactorsCal(number):
    durum = False 
    if number<2:
        durum = False
    if number==2 or number==3:
        durum = True
    for i in range(2, number):
        if number % i ==0 :
            durum = False
            break
        else:
            durum = True
    return durum
 
def calculate(sayi):
    asalListesi = []
    for i in range(sayi+1):
        if primeFactorsCal(i):
            if sayi % i ==0:
                asalListesi.append(i) #Syntax Yapısı :liste_adi.append(eklenecek_eleman) Döngüde her döndüğünde listeye elemanları ekleyecektir.
    # bolunen = bolum * bolen
    bolunen = sayi
    i=0
    asallar = []
    bolunenler = [bolunen]
    while i<len(asalListesi):
        bolen = asalListesi[i]
        bolum = bolunen // bolen  #// Tam bölme işlemi
        if bolum % bolen == 0:
            bolen = asalListesi[i]
            bolunen = bolum
            asallar.append(bolen)
        else:
            bolunen = bolum
            i +=1
            asallar.append(bolen)
        bolunenler.append(bolunen)
    return {"asallar":asallar,"bolunenler":bolunenler}

sayi = int(input("Lütfen Bir Sayı Giriniz: "))
print(f'Girilen Sayı : {sayi}')
sonuc = calculate(sayi)
for i in range(len(sonuc["asallar"])):
    fillLen = len(str(sayi))
    print(f'{str(sonuc["bolunenler"][i]).rjust(fillLen)} | {sonuc["asallar"][i]}') # rjust Diziyi sağ tarafa yaslamak için kullandık.
print(f'{str(sonuc["bolunenler"][-1]).rjust(fillLen)} |')
