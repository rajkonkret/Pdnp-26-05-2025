# klasy - element programowania obiektowego
# klasa - szablon, opis, przepis, stempel, matryca
# cechy - zmienne, funkcje - metody
# obiekt - stworzony z klasy
# klasa musi byc zadeklarowana przed użyciem
# tworzenie obiektu uruchamia metode inicjalizującą
# paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja

# PascalCase
class Human:
    """
    Klasa Human w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam sie {self.imie}")


print(Human.__doc__)  # Klasa Human w Pythonie
print(print.__doc__)
#  cd .\day_3\
# cd day_3
#  pydoc -w kl1

# tworzenie obiektu
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x000001E7A3FB70E0>
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
# k
#
# None
cz1.wiek = 56
cz1.imie = "Radke"
cz1.plec = "m"
print(cz1.plec)
print(cz1.imie)
print(cz1.wiek)
# m
# Radke
# 56
cz1.powitanie()
# Nazywam sie Radke

cz2 = Human()
cz2.imie = "Anna"
cz2.wiek = 34
print(cz2.imie)
print(cz2.wiek)
# Anna
# 34
cz2.powitanie()
# Nazywam sie Anna
