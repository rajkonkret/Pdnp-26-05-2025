# bazy danych - system do przechowywania danych, posiada silnik do przetwarzania danych
# baza sql w pythonie

import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect("baza.db")
    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłaczona")

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    salary REAL NOT NULL);
    """

    cursor.execute(query)
    sql_connection.commit()

    insert = """
    INSERT INTO developers (id,name,salary) VALUES (1, 'Radek',10000);
    """

    cursor.execute(insert)
    sql_connection.commit()
except sqlite3.Error as e:
    print("Bład", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")
# Baza danych zostałą podłaczona
# Baza danych została zamknięta
