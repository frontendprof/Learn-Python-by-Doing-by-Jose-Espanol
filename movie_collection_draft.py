"""
So this would be program for movie collection, which has several functions
such as adding new movies to the existing collection, listing all
movies in the collection, finding some specific movie with details,
and finally exiting from the programm.
"""
# Still working on it. Need to fully grasp lambda function in order to take it in independently.


movies=list()

def menu():
    user_input=input("Press 'a' to add movie, 's' to show movies, 'f' to find, and 'q' to quit \n")

    while user_input!='q':
        if user_input=="a":
            add_movie()
        elif user_input=="s":
            show_movie()
        elif user_input=="f":
            find_movie()
        else:
            print("Unknown command. Please try again")

        user_input=input("\nPress 'a' to add, 's' to show, 'f' to find, 'q' to quit \n")


def add_movie():
    name=input("What is the name of the movie:  ")
    director=input("Who is the director of the movie:  ")
    year=int(input("When is the release of the movie:  "))

    """
    movie=[
    {'name': "name",
     'director':"director",
     "year":'year"}
     ]"""
    movies.append({"name":name,
                   "director":director,
                   "year": year})


def show_movie():
    for item in movies:
        show_movie_details(item)

def show_movie_details(movie):
    print(f"{movie['name']}")
    print(f"{movie['director']}")
    print(f"{movie['year']}")



def find_movie():
    find_by=input("With what property of movie are you looking for: ")
    lookin_for=input(f"What item are you looking for which is associated with '{find_by}' ")


    found_movies=find_by_attribute(movies,lookin_for, lambda x:x[find_by] )


def find_by_attribute(items,expected,finder):

    found=list()

    for i in items:
        if finder(i)==expected:
            found.append(i)

    return found




menu()
