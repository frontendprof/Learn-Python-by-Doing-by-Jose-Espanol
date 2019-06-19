

# B_R_R

# M_S_A_W


# You can limit the release years of movies
# You can show the list of all movies then asking for movie then detail.
# While finding for specific movie, input is case sensitive----You have to fix it later too.



"""
- Enter "a" to add a movie, "l" to list all movies, "f" to find a movie, "q" to quit from the program

- Add a movie
- See movies
- Find a movie
- Quit the program

"""

"""
Tasks:

- Decide where to store movies
- What is the format of a movie
- Show the user the main interface and get their input
- Allow users to add movies
- Show all their movies
- Find a movie
- Stop running the program when they press "q"
"""



movies = list()

def menu():

    user_input =input("""
    \nTo add a movie press 'a',
    \nTo see the list of  your movies press 's',
    \nTo find a movie press 'f'
    \nTo quit press 'q': \n""").lower()

    while user_input!='q':

        if user_input=='a':
            add_movie()

        elif user_input=='s':
            show_movie()

        elif user_input=='f':
            find_movie()

        else:
            print("Unknown command. Please try again. :)\n")

        user_input = input("\nEnter 'a' to add a movie, 's' to list, 'f' to find , 'q' to quit  \n")


def add_movie():
    name=input("What is the name of the movie? ")
    director=input("Who is the director? ")
    year=input("What the release year? ")

    movies.append({
        'name': name,
        'director':director,
        'year': year
    })



def show_movie(movie_list):
    for mov in movie_list:
        show_movie_details(mov)



def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    find_by=input("What property are you lookin for with? ")
    lookin_for=input("What are you lookin for? ")

    found_movies=find_by_attribut(movies, lookin_for, lambda x: x[find_by])

    show_movie(found_movies)


def find_by_attribut(items, expected, finder):
    found=list()
    for i in items:
        if finder(i)==expected.lower():
            found.append(i)
    return found


    """movies.append({
        'name': name,
        'director':director,
        'year': year
    })"""






menu()
