wiek = 47  # int
rok = 2025  # int
temp = 36.6
print(type(temp))  # <class 'float'>
temp_2 = 36, 6
print(type(temp_2))  # <class 'tuple'>, krotka

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023209876543209877 -> float
print(rok // wiek)  # część caøkowita z dzielenia 2025 // 47 całych 43

print(rok % wiek)  # 4, modulo, reszta z dzielenia
print(10 % 3)  # 3 całe i 1 reszty

print(wiek ** rok)  # potęgowanie
# len() - długośc sekwencji
print(len(str(wiek ** rok)))  # 3386 znaków
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds
# the
# limit(4300
# digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 1 + 4 / 2)  # -155.0
print(54 - 5 * 43 + (4 / 1 + 4) / 2)  # -157.0

print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# występuej bład zaokrąglenia
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal - pozwala lepiej zarządzać błędem zaokrąglenia


# typ logiczny
# prawda, fałsz
# True, False
# 1 0

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, boolean, typ logiczny

print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True
print(bool("Radek"))  # True

print(bool(""))  # False
print(bool(None))  # False

# and - i
print(True and False)  # False
# True and True    True
# True and False    False
# False and True    False
# False and False    False

# or - lub
print(True or False)  # True
# True or True    True
# True or False    True
# False or True    True
# False or False    False

# not - negaccja
print(not True)  # False
print(not False)  # True

a = 6
b = 8

print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 6 > 8 = False
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 6 < 8 = True
print(f"Porównanie {a} >= {b} = {a >= b}")  # Porównanie 6 >= 8 = False
print(f"Porównnie {a >=b = }")  # Porównnie a >=b = False
print(f"{a=}")  # a=6
print(f"Porównnie {a} == {b} = {a == b}")  # Porównnie 6 == 8 = False, przyrównanie
print(f"Porównnie {a}jest równe{b} = {a == b}")  # Porównnie 6jest równe8 = False
print(f"Porównnie {a} != {b} = {a != b}")  # Porównnie 6 != 8 = True, czy różne
