# B_R_R

# M_S_A_W


# I still have some amendments to make
# As getting your prompt, the program should return how many prime numbers for a given range and print them all out.

# This project is not complete yet.
""" Have to work on:
---> On first three ordinal numbers, let it print out st, nd, rd respectively instead of th.
---> Remove whitespaces left behind after looping through not prime numbers
"""



num=eval(input("What is your number: "))
rand_list=list()

for a in range(2,num):
  for b in range(2, a):
    if a%b==0:
      print()
      break

  else:
    rand_list.append(a)
    print()
    print(f"The  {len(rand_list)}th prime in {num} is -----> {a}")
    continue

print(f"There are {len(rand_list)} primes for a given range")
print()
print()
