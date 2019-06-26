# B_R_R
# M_S_A_W

import csv

movies=[
    {"name": "The Matrix", "director": "Wachowski"},
    {"name": "Bourne Identity", "director": "Doug Liman"},
    {"name": "Godfather", "director": "Francis Ford Coppola"},
    {"name": "Shawshank Redemption", "director": "Frank Darabont"},
    {"name": "Pulp Fiction", "director": "Quentin Tarantino"},
    {"name": "Schindler's List", "director": "Steven Spielberg"},
    {"name": "Forrest Gump", "director": "Robert Zemeckis"}
]


def write_to_file(output):
    with open("file.csv", 'w') as f:
        f.write("      NAME *\t\t\t       DIRECTOR\n")
        f.write("=================*\t==================\n")
        for line in output:
            f.write(f'{line["name"]}\t  *---> \t{line["director"]}\n')



def read_from_file():
        with open('file.csv', 'r') as f:
            content=f.readlines()
            for line in content:
                columns=line.strip().split('*')
                print(f'{columns[0]}\t{columns[1]}')




write_to_file(movies)
read_from_file()
