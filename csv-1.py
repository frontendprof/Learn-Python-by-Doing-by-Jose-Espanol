# B_R_R
# M_S_A_W




""""
There is data in another file:
name,age,university,degree
AbdlMalik,30,mit,computer science
jose,90,oxford,computing
anna,30,cambridge,physics



"""


file=open("csv_data.txt", 'r')
lines=file.readlines()
file.close()

lines=[line.strip() for line in lines[1:]]

for line in lines:
    person_data=line.split(",")
    name=person_data[0].title()
    age=person_data[1]
    university=person_data[2].title()
    degree=person_data[3].capitalize()

    print("{} is {} years old, pursuing {} at {}".format(name,age,degree,university))
