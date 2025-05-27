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
