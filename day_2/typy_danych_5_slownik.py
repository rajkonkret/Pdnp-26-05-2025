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
