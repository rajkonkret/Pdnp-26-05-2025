class Ptak:
    """
    Kalsa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizacyjna
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)


# dziedziczenie
class Kura(Ptak):  # kalsa Kura dziedziczy po kalsie Ptak
    """
    Klasa Kura, dziedziczy po kalsie Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # super() - klasa wyższa

    def latam(self):
        print('Tu', self.gatunek, "Ja nie latam.")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    """
    Dziedziczy po Ptak
    """

    def polowanie(self):
        print("tu", self.gatunek, "rozpoczynam polowanie")


or1 = Ptak("Orzeł", 45)
or1.latam()  # Tu Orzeł Lecę z szybkością 45
kur1 = Ptak("Kura", 0)
kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam.
kur2.dziobanie()  # Tu Kura domowa Idę sobie podziobać
