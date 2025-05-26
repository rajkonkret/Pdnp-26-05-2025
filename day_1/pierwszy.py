import sys

print()  # wypisz/wydrukuj
# ctrl alt l - formatowanie kodu

print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
print("Nazywam się Radek")
# ctrl d - powielanie lini
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
# Process finished with exit code 0 - wszystko poszło poprawnie

# print('Nazywam się Radek")
#   File "C:\Users\CSComarch\PycharmProjects\Pdnp-26-05-2025\day_1\pierwszy.py", line 18
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 18)
# Process finished with exit code 1 - program zakończyl się błedem
# ctrl / - automatyczne komentowanie

print("Dalej")  # Dalej

# type() - sprawdzanie typu danch
print(type("radek"))  # <class 'str'>, dane tekstowe, stringi

print("39")
print(type("39"))  # <class 'str'>

print(39)
print(type(39))  # <class 'int'>, integer, liczby całkowite

print("39" + "39")  # 3939,połączył teksty, konkatenacja
print(39 + 39)  # 78

# int() - zamień tekst na liczbę
print(int("39") + int("39"))  # 78, int() - rzutowanie na liczbę

# print("39" + 39) # TypeError: can only concatenate str (not "int") to str
print(int("39") + 39)  # 78
print("39" + str(39))  # str() - zamien na stringa, 3939

print(168 * 35)  # 5880
print("168" * 35)
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print(int("168") * int(35))  # 5880
print(10 * "-")  # ----------

print(sys.int_info)
# sys.int_info(bits_per_digit=30,
# sizeof_digit=4, default_max_str_digits=4300,
# str_digits_check_threshold=640)