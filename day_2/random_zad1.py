import random

# operacje na liczbach losowych

#  """Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # od 1 do 100 int

print(random.randrange(1, 100))  # od 1 do 99 int
print(random.randrange(5))  # int od 0 do 4

print(random.random())  # 0.8239814245049077 float od 0 do 0.999999
print(random.random() * 8)  # 6.576811415721201 float od 0 do 7.999999

lista = [67, 45, 32, 68, 69, 90, 42]
print(random.choice(lista))  # 67

lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)
wyn = random.choice(lista)
lista_kule.remove(wyn)
print(wyn)  # 32

print(random.choices(lista_kule, k=6))  # losuje z powtórzeniamy, [3, 45, 18, 18, 41, 22]
print(random.sample(lista_kule, k=6))  # losuje bez powtórzeń, [36, 41, 14, 30, 44, 20]
print(random.sample(lista_kule, 6))  # losuje bez powtórzeń, [23, 22, 31, 43, 29, 37]
