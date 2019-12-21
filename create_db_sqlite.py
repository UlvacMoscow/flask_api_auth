import sqlite3


connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, name text, email text, password text, age int)"

cursor.execute(create_table)

insert_query = "INSERT INTO users VALUES (?, ?, ?, ?, ?)"

users = [
    (1, 'Ivan', 'ivan@mail.ru', 'qwerty1', 23),
    (2, 'Vasja', 'vasja@mail.ru', 'qwerty2', 24),
    (3, 'Senja', 'senja@mail.ru', 'qwerty3', 25),
    (4, 'John', 'john@mail.ru', 'qwerty4', 26),
    (5, 'Armen', 'armen@mail.ru', 'qwerty5', 27),
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
