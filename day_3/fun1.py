# funkcja - funkcja pozwala wykonac kod wielokrotnie w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# zeby urucomic funkcję musi zostac wywołana

a = 8
b = 6


# print nie zwraca wyniku -> None
# PEP8 zaleca dwie linijki odstępu
def dodaj():  # funkcja bez argumentów
    print(a + b)


def dodaj2(c, d):  # funkcja przyjmuje dwa obowiązkowe argumenty
    # uzywa lokalne argumenty
    print(c + d)


def odejmij(a, b, c=0):  # c - argument domyślnhy
    print(a - b - c)


# wywołanie funkcji
dodaj()  # 14

# przekazywanie po pozycji
dodaj2(8, 60)  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

odejmij(1, 2, 3)  # -4
odejmij(1, 2)  # c =0 , -1

# przekazywanie argumentów po nazwie
odejmij(a=1, c=4, b=8)  # -11

# mieszane
odejmij(1, b=9, c=7)  # -15

print(dodaj() + dodaj2(5, 9))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
