# funkcja lambda
# skrócony zapis funkcji
# domyślnie zwraca wartość (return)
from math import lgamma


def odejmij(a, b):
    return a - b


print(odejmij(234, 89))  # 145

odejmij2 = lambda a, b: a - b
print(odejmij2(123, 87))  # 36

# mapowanie danych - przemiana danych na inne
lista = [1, 2, 3, 5, 10, 25, 50, 100, 500]

l = []
for i in lista:
    l.append(i * 2)
print(l)  # [2, 4, 6, 10, 20, 50, 100, 200, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 10, 20, 50, 100, 200, 1000]


def zmien(x):
    return x * 2


l2 = []
for i in lista:
    l2.append(zmien(i))
print(l2)  # [2, 4, 6, 10, 20, 50, 100, 200, 1000]

# map() - funkcja wyższeg rzedu# bieze elemnty kolekcji i wykonuje na nich zadaną funkcję
print(f"Zastosowanie map() {list(map(zmien, lista))}")
# Zastosowanie map() [2, 4, 6, 10, 20, 50, 100, 200, 1000]
# Lambda jako funkcja anonimowa
# użycie w miejscu deklaracji
print(f"Zastosowanie map() {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 3, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 8, lista))}")
# Zastosowanie map() [8, 16, 24, 40, 80, 200, 400, 800, 4000]

# filtrowanie danych - zwrca spełniające warunek
l3 = []
for i in lista:
    if i < 3:
        l3.append(i)
print(l3)  # [1, 2]

# filter()
print(f"Zastosowanie filter {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter [1, 2]
print(f"Zastosowanie filter {list(filter(lambda x: x > 3 and x < 100, lista))}")
# Zastosowanie filter [5, 10, 25, 50]
print(f"Zastosowanie filter {list(filter(lambda x: 3 < x < 100, lista))}")
# Zastosowanie filter [5, 10, 25, 50]
