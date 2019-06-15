# B_R_R
# M_S_A_W

# Lottery Game Logic

# Let's say we have already produced 100 lotteries with 6 random numbers.

# Upon purchase, we ask the customers first and second name, so it prints out the winner info at the end.
import random

lottery_num=set(random.sample(list(range(1,19)),6))


players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

top_player=players[0]

for player in players:
  # Find length of intersection of two sets
  our_len=len(player["numbers"].intersection(lottery_num))

  winner_len=len(top_player["numbers"].intersection(lottery_num))

  # if our expression is greater than top_player's then winner will be us.

  if our_len>winner_len:

    top_player=player

reward=1000 ** (len(player["numbers"].intersection(lottery_num)))

print("Congratulations. {}, You won the award equal to {} dollars".format(player['name'], reward))
