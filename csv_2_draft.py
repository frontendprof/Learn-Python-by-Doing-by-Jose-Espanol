# B_R_R
# M_S_A_W


movies=[
    {"name": "The Matrix", "director": "Wachowski"}
    {"name": "Bourne Identity", "director": "Doug Liman"}
    {"name": "Godfather", "director": "Francis Ford Coppola"}
    {"name": "Shawshank Redemption", "director": "Frank Darabont"}
    {"name": "Pulp Fiction", "director": "Quentin Tarantino"}
    {"name": "Schindler's List", "director": "Steven Spielberg"}
    {"name": "Forrest Gump", "director": "Robert Zemeckis"}

]


def write_to_file(output):
    with open("file.csv", 'w') as f:
        f.write("name, director\n")
        for line in output:
            f.write(f'{line["name"]}, {line['director']}\n')



def read_from_file():
        with open('file.csv', 'r') as f:
            content=f.readlines()
            for line in content[1:]:
                columns=line.strip().split(',')
                print(f'Name: {columns[0
