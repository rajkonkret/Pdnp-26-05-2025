# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if
# w zaleznosci czy warunek jest spełniony czy nie (True/Fase) wykona odpowiedni blok programu

# odp = True
odp = False
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
print("Dalsza część programu")
# True
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Dalsza częśc programu

odp = "Radek"

if odp == "Radek":
    print('Nadal Radek')  # Nadal Radek

odp = 0
if odp:
    print("Działa")
else:  # inny przypadek
    print("Zero -> False")
    # Zero -> False

a = "Radek"
if len(a) > 3:
    print(f"Długość wynosi {len(a)}, więcej niż 3")
    # Długość wynosi 5, więcej niż 3

a = "Radek"
n = len(a)
if n > 3:
    print(f"Długość wynosi {n}, więcej niż 3")

# walrus operator, operator morsa
if (n := len(a)) > 3:
    print(f"Długość wynosi {n}, więcej niż 3")
print(n)  # 5
#
# # kolejność warunków ma znaczenie
# podatek = 0
# zarobki = int(input("Podaj zarobki (roczne) PLN"))
# if zarobki < 10_000:  # 0 - 9999 -> 0
#     podatek = 0
# elif zarobki < 40_000:  # 10_000 - 39_999 -> 0.2
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki} pln.")
# 5
# Podaj zarobki (roczne) PLN1000000
# Podatek wynosi 900000.0 pln.
# Podaj zarobki (roczne) PLN35000
# Podatek wynosi 0 pln.

suma_zam = 150
if suma_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25
# ctrl / - komentowanie zaznaczonego kodu


# napisac test z...
# odp = input("Podaj datę chrztu Polski")  # str
# if odp == "966":
#     print("Dobrze")
# else:
#     print("Musisz się jeszcze douczyć!")
#
# a = 490
# b = int(input("podaj długość"))
# print(a - b)

alert_system = "console"
error_level = "error"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System Error")
    if error_level == "error":
        lista_b.append("Krytyczny")
    elif error_level == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inny")
else:
    print("Inny system")

print(lista_b)
