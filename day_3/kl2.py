class Human:
    """
    Klasa opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam sie {self.imie}")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę")


# cz1 = Human() # TypeError: Human.__init__() missing 2 required positional arguments: 'imie' and 'wiek'
cz1 = Human("Anna", 34)
print(cz1.imie)
print(cz1.wiek)
# Anna
# 34
print(cz1)  # <__main__.Human object at 0x00000233211470E0>
cz1.powitanie()  # Nazywam sie Anna
cz1.wypisz_wiek()  # Mam 34 lat.
cz1.ruszaj()  # Ruszyłam w drogę
