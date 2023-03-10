# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-




sentence = input("CÃ¼mle girin: ")

words = sentence.split()
count = len(words)

print("Kelime sayÄ±sÄ±:", count)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Bir sayÄ± girin: "))
print("FaktÃ¶riyeli:", factorial(num))

n = int(input("KaÃ§ sayÄ± istediÄŸinizi girin: "))

a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b

"""ilk program girilen cÃ¼mledeki kelime sayÄ±sÄ±nÄ± verir.
ikinci program bildiÄŸimiz bir sayÄ±nÄ±n faktÃ¶riyelini blon program
Ã¼Ã§Ã¼ncÃ¼ program bir sayÄ± giriyoruz ve onun kadar bize bir fibonacci serisi oluÅŸturuyor.
"""