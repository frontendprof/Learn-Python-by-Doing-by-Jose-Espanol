

# B_R_R

# M_S_A_W

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


movies=list()

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to list all movies, 'f' to find a movie, 'q' to quit from the program!  ")

    while user_input!='q':

        if user_input == 'a':
            add_movie()

        elif user_input=='l':
            list_movies()

        elif user_input=='f':
            find_movie()

        else:
            print("Unkonwn command. Please try again. :)")

        user_input = input("\nEnter 'a' to add a movie, 'l' to list, 'f' to find , 'q' to quit  ")


def add_movie():
    name=input("What is the name of the movie? ")
    director=input("What is the director of the movie? ")
    year=int(input("What is the release year of the movie? "))

    movies.append({
        'name':name,
        'director':director,
        'year':year
    })

def list_movies():
    for movie in movies:
        list_movie_details(movie)


def list_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")

def find_movie():
    find_by=input("What property of a movie are you looking for? ")
    looking_for=input("What are you looking for ? ")

    found=list()

    for movie in movies:
        if movie['find_by']==looking_for:
            found.append(movie)
    return found


menu()
print(movies)
