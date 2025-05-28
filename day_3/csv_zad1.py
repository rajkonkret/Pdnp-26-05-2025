# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

# csv - pliki tekstowe, dane rozdzielone znakiem podziału
import csv

row = ["Radek", 'coe', "3", 90]
fields = ['name', 'branch', 'year', 'cgpa']
filename = 'records.csv'

with open(filename, "w", newline="") as fh:
    csvwriter = csv.writer(fh, delimiter=";")
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

read_fields = []
read_rows = []

with open(filename, "r") as f:
    csvreader = csv.reader(f, delimiter=";")
    print(csvreader)  # <_csv.reader object at 0x000001C8A5713FA0>

    read_fields = next(csvreader)  # odczytanie pierwszej lini, ustawienie odczytu na drugą

    for row in csvreader:  # tu jestesmy na drugiej linii
        read_rows.append(row)

print(read_fields)
print(5 * "-")
print(read_rows)
# <_csv.reader object at 0x000001DABC0D0040>
# ['name', 'branch', 'year', 'cgpa']
# -----
# [['Radek', 'coe', '3', '90']]
