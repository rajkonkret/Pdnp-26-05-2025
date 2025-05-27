dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}
print(type(dictionary))  # <class 'dict'>

# wypisze klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wypisze wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisze pary klucz wartość
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.

for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski

for k, v in dictionary.items():
    print(k, v, sep="=>", end="<====>")
print("Radek")
# imie=>Radek<====>nazwisko=>Kowalski<====>Radek

print("Tomek")
# imie=>Radek<====>nazwisko=>Kowalski<====>Radek
# Tomek

pol_ang = {"kot": "cat", "pies": "dog", "dach": "roof"}
ang_pol = {}  # słownik
for k, v in pol_ang.items():  # "kot": "cat", k="kot", v="cat"
    # slownik[klucz] = wartosc
    ang_pol[v] = k  # ang_pol[v="cat"] = k="kot"
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

# {value:key}
print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}
