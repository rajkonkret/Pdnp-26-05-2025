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
