# od python 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang:
    case "python":
        lista.append("Znam pythona")
    case "java":
        lista.append("Znam jave")
    case _:  # odpowiednik else
        print("inny")

print(lista)
# Podaj znany Ci język programowaniajava
# ['Znam jave']
