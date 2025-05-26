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
