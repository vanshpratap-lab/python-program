# import random
# while True:
#     a = random.randint(1,10)
#     b = int(input("enter your answer"))


#     if (a==b):
#         print(f"{a} - yes your answer is correct")
#     elif (a!=b):
#         print(f" the correct answer was {a} and you chose {b}. im sorry you are worng!")
#     continue


import random
while True:
    a = random.randint(1,10)
    attempts = 0 

    print("guess no. between 1 to 10")
    while True:
        try:
            b = int(input("enter you answer"))
            attempts += 1
            if b < a :
                print("too low")
            elif b > a :
                print("too high")
            else:
                print(f"you guessed it correct in {attempts} attempts")
                break 

        except ValueError :
            print("please enter a valid number")

    play_again = input("play again? (y/n):")
    if play_again.lower() != "y":
        print("thnaks for playing!")
        break

        

