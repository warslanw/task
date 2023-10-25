#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
print("Girilen Değerin Palindrome Kontrolü")

PalindromKontrol = input("Lütfen Bir Değer Giriniz")

if PalindromKontrol == PalindromKontrol[::-1]: # [::-1]: Bir listeyi ters çevirmek için kullanılır
    print("Palindrom Değerdir")
else:
    print("Palindrom Değer Değildir")