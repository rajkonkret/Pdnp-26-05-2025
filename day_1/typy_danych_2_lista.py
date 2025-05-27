# kolekcja - przechowuje wiele elementów

# lista - przechowuje dowolną ilość elelemntów, dowowlnego typu na raz
# zachowuje kolenośc przy dodawaniu elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie eleemntów do listy
lista.append("Radek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marek")
lista.append("Kuba")
lista.append("Emilia")
lista.append("Anna")
print(lista)
# ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kuba', 'Emilia', 'Anna']
#     0         1       2        3        4        5        6
#     -7       -6       -5       -4       -3       -2       -1
# indeksy
print(lista[0])  # Radek
print(lista[2])  # Zenek
print(lista[4])  # Kuba

# print(lista[10])  # IndexError: list index out of range

print(len(lista))  # długośc listy 7
print(lista[len(lista) - 1])  # Anna
print(lista[-1])  # Anna, ostatni elelemnt z listy
print(lista[-2])
print(lista[-3])
# Anna
# Emilia
# Kuba

# slicowannie - fragment listy
print(lista[0:3])  # ['Radek', 'Tomek', 'Zenek'] indeksy 012
print(lista[:3])  # ['Radek', 'Tomek', 'Zenek']
print(lista[2:])  # ['Zenek', 'Marek', 'Kuba', 'Emilia', 'Anna'] do końca włącznie
print(lista[2:6])  # ['Zenek', 'Marek', 'Kuba', 'Emilia']

print(lista[2:15])  # ['Zenek', 'Marek', 'Kuba', 'Emilia', 'Anna']
print(lista[10:234])  # []
print(lista[:])  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kuba', 'Emilia', 'Anna']
print(lista[2:2])  # []
print(lista[2:3])  # ['Zenek'] indeks 2
print(lista[::2])  # ['Radek', 'Zenek', 'Kuba', 'Anna']

# # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kuba', 'Emilia', 'Anna']
# #     0         1       2        3        4        5        6
# #     -7       -6       -5       -4       -3       -2       -1

print(lista[-2:0])  # [] -> [4:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Zenek', 'Marek', 'Kuba'] [0:5]

lista_15 = list(range(15))  # od 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[::2])  # [0, 2, 4, 6, 8, 10, 12, 14], krok=2

print(lista[::-1])  # wypisze w odwrotnej kolejności
# ['Anna', 'Emilia', 'Kuba', 'Marek', 'Zenek', 'Tomek', 'Radek']

# nadpisanie elementu
lista[3] = "Radek"
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Radek', 'Kuba', 'Emilia', 'Anna']

# dopisanie do listy na wskazanym indeksie
lista.insert(1, "Roman")
print(lista)  # ['Radek', 'Roman', 'Tomek', 'Zenek', 'Radek', 'Kuba', 'Emilia', 'Anna']

# sprawdzenie indeksu dla elementu, pierwszy napotkany
print(lista.index("Radek"))  # 0

print(lista.count("Radek"))  # występuje 2 razy
# usunięcie elementu, usunie pierwszy napotkany
lista.remove("Radek")
print(lista)  # ['Roman', 'Tomek', 'Zenek', 'Radek', 'Kuba', 'Emilia', 'Anna']

# usunięcie po indeksie, zwraca usunięty element
print(lista.pop(5))  # Emilia
print(lista)  # ['Roman', 'Tomek', 'Zenek', 'Radek', 'Kuba', 'Anna']
print(lista.pop(-2))  # Kuba
print(lista.pop())  # Anna, usunie ostatni
