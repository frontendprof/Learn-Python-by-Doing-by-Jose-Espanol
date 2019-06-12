# B_R_R
# M_S_A_W

# Still needs some work on removing traces of whitespaces, left by looping through non prime numbers


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
    continue

print(f"There are {len(rand_list)} primes for a given range")
print()
print("They are following: ")
for z in rand_list:
  print(z)
print()
