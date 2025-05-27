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

print(lista_wyn)  # [26, 48, 16, 3, 25, 47]

for i in range(10):
    if i % 2 == 0:  # modulo
        print(i, "parzysta")

# list comprehensions
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista3:
    if c > 4:
        print("Większe od 4")
    else:
        print("Mniejsze, równe 4")
# Mniejsze, równe 4
# Mniejsze, równe 4
# Mniejsze, równe 4
# Większe od 4
# Większe od 4

for i in range(0, 10, 2):  # start, stop, krok -> krok 2
    print(i)
# 0
# 2
# 4
# 6
# 8

for i in range(-10, 0):
    print(i)
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1
for i in range(10, 0, -1):  # ujemny krok, idziemy w dół
    print(i)
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print(c)  # tylko dla c=2
    print("Przy każdym przejściu pętli")

print("Po zakońzeniu pętli")
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
# Przy każdym przejściu pętli
# 3
# Przy każdym przejściu pętli
# Przy każdym przejściu pętli
# Przy każdym przejściu pętli
# Przy każdym przejściu pętli
# Po zakońzeniu pętli

imiona = ["Radek", "Tomek", "Zenek", "Ania"]
print(imiona)
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# 0 Radek
for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enemurate() - numeruje kolekcje i zwraca numer i element
for p in enumerate(imiona):
    print(p)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
a, b = (3, 'Ania')
print(a, b)  # 3 Ania

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

imiona = ["Radek", "Tomek", "Zenek", "Ania", "Ela"]
wiek = [45, 65, 32, 43]

# Radek 45
# for p in imiona:
#     print(p, wiek[imiona.index(p)]) # IndexError: list index out of range

# zip() - łączenie kolekcji
for i in zip(imiona, wiek):
    print(i)  # ('Ania', 43)

for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 45
# Tomek 65
# Zenek 32
# Ania 43
