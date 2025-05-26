tekst = "Witaj Świecie"

print(tekst)  # Witaj Świecie
print(type(tekst))  # <class 'str'>

# teksty są niemutowalne
#  """ Return a copy of the string converted to uppercase. """
tekst.upper()
print(tekst)  # Witaj Świecie
print(tekst.upper())  # WITAJ ŚWIECIE, wyswietliło kopię
upper_case = tekst.upper()
print(upper_case)  # WITAJ ŚWIECIE

print(tekst.capitalize())  # Witaj świecie
print(tekst.lower())  # witaj świecie

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

# strip() - usunięcie białych znaków i spacji wiodących i końcowch
print(tekst.removeprefix("Witaj").strip())  # "Świecie" - nie bedzie spacji

encoded_s = tekst.encode("utf-8")
print(encoded_s)  # b'Witaj \xc5\x9awiecie' dane bajtowe
# \xc5\x9a - kod znaku Ś w formie szesnastkowej
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj Świecie

print(tekst)
# Witaj Świecie
# 01234567890... indeksy od 0

print(tekst[4])  # j, indeks 4, pozycja: 5

print(tekst.count("i"))  # wustępuje 3 razy
print(type(tekst.count("i")))  # wustępuje 3 razy, <class 'int'>

print(tekst.count("j"))  # wystapi 1 raz
print(tekst.count("j", 0, 4))  # wystąpi 0 razy, z prwej przedział otwarty, indeksy 0123

imie = "Radek"
print(imie)

print("Imie", imie)  # Imie Radek

starszy = "Witaj %s!"  # %s - string
print(starszy % imie)  # Witaj Radek!

# f - string
tekst_format = f"Mam na imię {imie} i lubię pythona"
print(tekst_format)  # Mam na imię Radek i lubię pythona

tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# "	 Mam na imię Radek
#  i lubię pythona"
# \t - tab
# \n - nowa linia
# \b - backspace

print("Witaj {}!".format(imie))  # Witaj Radek!

print("""\"Tekst
    wielolinijkowy\"""")

# "Tekst
#     wielolinijkowy"

"""Komentrz
wielolinijkowy"""
