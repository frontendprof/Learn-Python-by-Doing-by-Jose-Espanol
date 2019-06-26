# B_R_R
# M_S_A_W


"""
We have people.txt file which has list of names.
We have nearby_friends.txt file too which is empty.
Our task is after responding the prompt, searching the given names from people.txt file. If founnd matches
then update it to nearby_friends.txt file. Before that throwing a message saying matched names are nearby. Meet with them.

"""

friends=input("Enter 3 friends names separated by commas(no space):\n ").split(",")

people=open("people.txt",'r')
people_nearby=[line.strip() for line in people.readlines()]
people.close()


friends_set=set(friends)
nearby_set=set(people_nearby)
friends_nearby_set=friends_set.intersection(nearby_set)


nearby_friend_file=open("nearby_friends.txt", "w")

for friend in friends_nearby_set:
    print(f"{friend} is nearby. Meet with them")
    nearby_friend_file.write(f'{friend}\n')

nearby_friend_file.close()
