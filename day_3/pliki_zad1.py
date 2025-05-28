# działąnia na plikach
# filehandler - rura do pliku
# context manager
# with - context manager w pythonie

#     ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding="utf-8") as fh:
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

# with open('test.log', "x") as f:
#     f.write("Powitanie") # FileExistsError: [Errno 17] File exists: 'test.log'

# w - tworzy plik, usunie gdy istnieje
with open('test.log', "w", encoding='utf-8') as f:
    f.write("Nowe\n")

with open('test.log', "a", encoding='utf-8') as fh:
    fh.write("Powitanie\n")
    fh.write("Powitanie\n")
    fh.write("Powitanie\n")
    fh.write("Dopisane\n")
    fh.write("dośdane\n")

with open('test.log', "r", encoding='utf-8') as file:
    lines = file.read()

# with open('C:\\Users\\CSComarch\\PycharmProjects\\Pdnp-26-05-2025\\extras\\1.txt', "r", encoding='utf-8') as file:
with open(r'C:\Users\CSComarch\PycharmProjects\Pdnp-26-05-2025\extras\1.txt', "r", encoding='utf-8') as file:
    lines = file.read()
print(lines)
# Nowe
# Powitanie
# Powitanie
# Powitanie
# Dopisane
