# słownik - para klucz - wartość
# {'user' : 'Radek'}
# klucze nie mogą sie powtarzać
# odpowiednik jsona

# pusty słownik
dictionary = {}
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

pusty_slownik = dict()
print(type(pusty_slownik))  # <class 'dict'>
print(pusty_slownik)  # {}

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 67
print(dictionary)  # {'imie': 'Radek', 'wiek': 67}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 67])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 67)])

dict_list = {"imie": ["radek", "Tomek", "Zenek"]}
print(dict_list)  # {'imie': ['radek', 'Tomek', 'Zenek']}
print(dict_list['imie'][0])  # radek

# wypisanie wartości
print(dictionary['imie'])

# print(dictionary["Imie"]) # KeyError: 'Imie'

print(dictionary.get("imie"))  # Radek
print(dictionary.get("Imie"))  # None
print(dictionary.get("Imie", "default"))  # default

dictionary.update({"data": "31-12-2025"})
print(dictionary)  # 'imie': 'Radek', 'wiek': 67, 'data': '31-12-2025'}

# input() - pozwala wprowadzić dane do komputera np.:  z kalwiatury
# tekst = input("Podaj imię")
# print(tekst)
# Podaj imięRadek
# Radek

# # napisać aplikację kalkulator
# #
# a = int(input("Podaj pierwszą liczbę"))  # -> str
# b = input("Podaj drugą liczbę")
#
# # print(a + b) # konkatencja
# print(int(a) + float(b))  # 12.0
# a = float(a)

# napisac aplikację słownik pol_ang
pol_ang = {"kot": "cat", "pies": "dog", "dach": "roof"}
print(f"Znam takie słowa: {pol_ang.keys()}")
odp = input("Podaj słówko do przetłumaczenia")
# print(f"Tłumaczenie:  {pol_ang[odp.strip().lower()]}")
# print("Tłumaczenie", pol_ang[odp.strip().lower()])

print(pol_ang.get(odp.strip().lower(), "Nie mo"))
#  Znam takie słowa: dict_keys(['kot', 'pies', 'dach'])
# Podaj słówko do przetłumaczenia Kot
# cat
# Podaj słówko do przetłumaczenia typ
# Nie mo

name1 = "GROSS"
name2 = "groß"
print(name1.lower() == name2.lower())  # False
print(name1.casefold() == name2.casefold())  # True
