# B_R_R
# M_S_A_W

from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice:  \n"""

def menu():
    database.create_book_table()

    user_input=input(USER_CHOICE)
    while user_input!="q":

        if user_input=='a':
            prompt_add_book()

        elif user_input=='l':
            list_book()

        elif user_input=='r':
            prompt_read_book()

        elif user_input=='d':
            prompt_delete_book()


        else:
            print("Unknown commmand. Please try again.")

        user_input = input(USER_CHOICE)

def prompt_add_book():
    name=input("What is the name of the book: ")
    author=input("Who is the author of the book: ")

    database.add_book(name,author)


def list_book():
    books=database.get_all_books()
    for book in books:
        read= 'YES' if book['read'] else "NO"
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name=input("What is the name of the book that you've finished: ")

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("What is the name of the book that you've finished: ")

    database.delete_book(name)

menu()