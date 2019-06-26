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
    with open("file1.csv", 'w') as f:
        writer=csv.DictWriter(f, fieldnames=["name","director"])
        writer.writeheader()
        writer.writerows(output)



def read_from_file():
        with open('file1.csv', 'r') as f:
            reader=csv.DictReader(f)
            for line in reader:
                print(f'{line["name"]}, {line["director"]}')



write_to_file(movies)
read_from_file()
