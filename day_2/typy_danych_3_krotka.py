# krotka, tupla - niemutowalna lista
# pozwala efektywniej zarządzac pamięcią

tupla_imiona = ("Radek", "Tomek", "Zenek", "Mateusz")
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Mateusz')

tupla_liczby = 43, 55, 22.34, 11, 200
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>

tupla = 43
print(type(tupla))  # <class 'int'>

tupla2 = 43,
print(type(tupla2))  # <class 'tuple'>
print(tupla2)  # (43,)

# PEP8 zaleca tuple jednoelementowe robic z ()
tupla3 = ("Radek",)
print(type(tupla3))  # <class 'tuple'>
print(tupla3)  # ('Radek',)

# tupla jest niemutowalna
# tupla_liczby[3] = 123 # TypeError: 'tuple' object does not support item assignment

del tupla_liczby  # usunięcie tuplii z pamięci
# print(tupla_liczby) # NameError: name 'tupla_liczby' is not defined

print(tupla_imiona.index("Radek"))  # index 0
print(tupla_imiona.count("Radek"))  # wystepuje 1 raz
