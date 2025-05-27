#  wyjątek - bład podczas wykonywania programu

# print(5 / 0)  # ZeroDivisionError: division by zero
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\Pdnp-26-05-2025\day_2\wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1
print("Dalej")

try:
    # print(5 / 0)
    # print("a" * "23")
    # raise KeyError("Brak klucza")
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Bład typu")
except Exception as e:
    print("Błąd", e)
else:  # gdy nie ma błedu
    print("Wynik:", wynik)  # Wynik: 30.0
finally:
    print("Wykona się zawsze")
# Dalej
# Nie dziel przez zero
# Dalej
# Bład typu
# Dalej
# Błąd 'Brak klucza'
# Dalej
# Wynik: 30.0
# Wykona się zawsze
