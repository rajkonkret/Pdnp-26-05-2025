# {"name":"John", "age":30, "car":null}
# dane typu klucz-wartosc
# uzywany do komunikacji między systemami w internecie
# odpowiednik jsona - słownik
import json

person_dict = {'name': 'Radek', 'age': 40, "czy_pali": None}
print(type(person_dict))  # <class 'dict'>

with open("nasze_dane.json", "w") as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

# beautify
with open("nasze_dane.json", "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

with open('nasze_dane.json', "r") as f:
    data = json.load(f)

print(data)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

json_text = json.dumps(data)
print(json_text)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(json_text))  # <class 'str'>

dict_json = json.loads(json_text)
print(dict_json)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(dict_json))  # <class 'dict'>
