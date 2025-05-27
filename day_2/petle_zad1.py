# pętla - możliwość wykonanina kodu wielokrotnie
# for - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in range(5):
    pass  # nic nie rób

for _ in range(5):  # niema zmienna, od 0 do 4
    print("Test podłoga")
    # print(_)
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga
# Test podłoga

for i in range(10):
    print(i * 2)
    print(i + 2)

lista_kule = list(range(1, 50))  # od 1 do 49
lista_wyn = []

for i in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wyn.append(wyn)

print(lista_wyn) # [26, 48, 16, 3, 25, 47]

