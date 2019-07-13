# B_R_R
# M_S_A_W

"""
It stores and retrieves books from the JSON file.
Format of JSON file:
[
    {
        "name": 'Clean Code',
        "author": "Robert",
        'read': True
    }
]

"""
from typing import List, Dict, Union
from .database_connection import DatabaseConnection
Book=Dict(str, Union(str, int))

books_file="books.json"

def create_book_table():
    with DatabaseConnection('data.db') as connection:

        cursor=connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)")


def add_book(name:str, author:str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,author))



def get_all_books()->List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor=connection.cursor()

        cursor.execute("SELECT * FROM books")
        books=[{"name":row[0],"author":row[1],"read":row[2]} for row in cursor.fetchall()]

    return books



def mark_book_as_read(name:str) ->:
    with DatabaseConnection('data.db') as connection:
        cursor=connection.cursor()

        cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))


def delete_book(name:str):
    with DatabaseConnection('data.db') as connection:
        cursor=connection.cursor()

        cursor.execute('DELETE from books WHERE name=?', (name,))

