# B_R_R
# M_S_A_W


"""

Create movie collector app:
that adds new movies,
that lists movies,
that finds movies,
and quits from app...

"""
movies=[]
def menu():
    user_input=input("""
                        Enter 'a' to add a new movie, \t\t'l' to list the movies, 
                        'f' to find a movie, \t\t'q' to quit from the programm\n""")

    while user_input!='q':
        if user_input=='a':
            add_movie()


        elif user_input=='l':
            list_movies(movies)


        elif user_input=='f':
            find_movies()


        else:
            print("Unknown command. Can you repeat again please")

        user_input = input("""
                                Enter 'a' to add a new movie, \t\t'l' to list the movies, 
                                'f' to find a movie, \t\t'q' to quit from the programm\n""")


def add_movie():
    name=input("What is the name of the movie you want to add? ")
    director=input("Who is the director of the movie? ")
    year=input("What is the year of the movie? ")


    movie={'name':name, 'director':director,'year': year}

    movies.append(movie)



def list_movies(movies_list):
    for mov in movies_list:
        show_mov_details(mov)


def show_mov_details(movie):
    print(f"Name: {movie['name']}")
    print(f'Director: {movie["director"]}')
    print(f'Year: {movie["year"]}')



def find_movies():
    find_by=input("WHat parameter are you looking for with? ")
    looking_for=input("WHat is the value of the parameter are you looking for? ")

    found_movies=find_movies_by_attribute(movies,looking_for,lambda x: x[find_by])
    show_mov_details(found_movies)


def find_movies_by_attribute(items,expected,finder):

    found=[]
    for i in items:
        if finder(i)==expected:
            found.append(i)
    return found


menu()

