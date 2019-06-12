# B_R_R
# M_S_A_W


# This is a program whereby first number is range, whereas second and third divisible numbers


print("Let's play FizBuzz")
print()
print("Enter three numbers, first number is range, whereas, second and third divisible numbers:  ")
print()
print()
a,b,c=[int(x) for x in input("What is your fizbuz numbers: ").split()]
print(a)
print(b)
print(c)
print()

for i in range(1,a):
    
    if i%b==0 and i%c==0:
        print("FizzBuzz")

    elif i%b==0:
        print("Fizz")
        
    elif i%c==0:
        print("Buzz")
        
    
    
    else:
      print(i)


