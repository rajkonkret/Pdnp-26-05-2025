# stworzyc funkcję, która oblicza średnią

def liczby(name=None, *cyfry):  # * dowolna ilość argumentów pozycyjnych
    print(cyfry)  # (1, 2, 3, 4, 5, 6)
    try:
        count = len(cyfry)
        suma = 0
        sum_p = sum(cyfry)
        for c in cyfry:
            suma += c
        avg = suma / count
        avg_p = sum_p / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
        print(f"Średnia dla ucznia {name} wynosi {avg_p}")
    finally:
        print("Obliczenia zakończone")


# (1, 2, 3, 4, 5, 6)
# Średnia wynosi 3.5
# Obliczenia zakończone
# ()
# Bład division by zero
# Obliczenia zakończone
liczby(1, 2, 3, 4, 5, 6)
liczby()
liczby("Radek", 5, 5, 5, 6, 5, 5, 5)
name, *cyfry = ("Radek", 5, 5, 5, 6, 5, 5, 5)
# (5, 5, 5, 6, 5, 5, 5)
# Średnia dla ucznia Radek wynosi 5.142857142857143
# Średnia dla ucznia Radek wynosi 5.142857142857143
# Obliczenia zakończone
