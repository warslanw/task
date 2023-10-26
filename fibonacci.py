#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
a = 1
b = 1
n = 20 
series = [1, 1]

for x in range(2, n):
    next = series[x - 1] + series[x - 2] #  Fn = Fn-1 + Fn -2 fibonacci dizisi formülü
    series.append(next)
    
print(series)