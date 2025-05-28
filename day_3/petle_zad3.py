# while - pętla sterowana warunkiem

# while True: # zawsze prawda, pętla nieskończona
#     print("Komunikat 1 !")

licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print("Komunikat 2 !!")
    print(licznik)
    if licznik > 10:
        break  # przerywa pętlę

print(licznik)  # 11

licznik = 0
while licznik < 10:  # doki warunek True pętla będzie działać
    licznik += 1
    print("Komunikat 3 !!!")
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!

lista = []
while True:
    wej = input("Podaj liczbę")
    #  A string is numeric if all characters in the string are numeric
    if not wej.isnumeric():
        break
    lista.append(wej)

print(lista)

# usunięcie wszystkich wystąpień elementu 5, nie zmieni kolejności elementów w liście
my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
while 5 in my_list:
    my_list.remove(5)

print(my_list)  # [1, 2, 3, 4, 6]

# usunąć duplikaty liczby 5, pozostawić jeden element liczby 5, nie zmienia kolejności
my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
print(dict.fromkeys(my_list))
# {1: None, 5: None, 2: None, 3: None, 4: None, 6: None}
print(list(dict.fromkeys(my_list)))  # [1, 5, 2, 3, 4, 6] - tworzy nową listę
my_list = list(dict.fromkeys(my_list))
print(my_list)  # [1, 5, 2, 3, 4, 6]
