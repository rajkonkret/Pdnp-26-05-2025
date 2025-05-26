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
