# zbiór (set) - przechowuje unikalne wartości
# nie zachowuje kolejnosći przy dodawaniu eleemntów
# nie posiadda indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

# pusty zbiór
zb2 = set()
print(type(zb2))  # <class 'set'>
print(zb2)  # set()

# dodanie elemntów do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(24)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop()
print(zbior.pop())  # 33, usunie elemnt z pozycji pierwszej

zmienna = zbior.pop()
print("Usunięty:", zmienna)  # Usunięty: 66

# operacje na zbiorach
zbior_2 = {667, 11, 44, 12.34, 18, 52, 667, 62}
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {18, 667, 52, 11, 44, 12.34, 62}

# suma zbiorów
print(zbior | zbior_2)  # {777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica
print(zbior - zbior_2)  # {24, 777, 22}
print(zbior.difference(zbior_2))  # {24, 777, 22}
print(zbior_2.difference(zbior))  # {667, 52, 12.34, 62}

krotka = tuple(zbior)
print(777 in zbior)  # True
print(667 in lista)  # False
print(667 in krotka)  # False
