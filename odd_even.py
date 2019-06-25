# B_R_R
# M_S_A_W


def func():
    while True:
        try:
            user_inp = int(input("WHat is your number? \n"))

        except ValueError:
            print("Please enter integers only. :) ")

        else:
            print(" {} is {}".format(user_inp, "even" if user_inp % 2 == 0 else "odd"))

        finally:
            inp = input("You want to play again? \n")
            if inp != "y":
                print("Goodbye")
                break


func()
