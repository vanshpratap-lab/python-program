while True:
    print("welcome to quiz")
    score = 0   
    print("who is the prime minister of india")
    choice = ("1. narendra modi\n"
    "2. amit shah\n"
    "3. yogi adtiynath\n")
    print(choice)
    user_input = input("please enter your answer: ")
    if user_input not in ["1","2","3"]:
        print("please enter a valid number")
        continue
    elif user_input == "1":
        print("yes its the correct answer")
        score += 1
    elif user_input in ["2","3"]:
        print("no its the wrong answer")
    break
while True :

    print("ok get ready for second question")
    print("")
    print("who created python programming language")

    choice2 = ("1. chrales babbage\n"
    "2. Guido van Rossum\n"
    "3. David Heinemeier Hansson\n")
    print(choice2)
    user_input2 = input("please enter your answer ")
    if user_input2 not in ["1","2","3"]:
        print("please enter a valid number")
        continue
    elif user_input2 == "2":
        print("yes its the correct answer")
        score += 1
    elif user_input2 in ["1", "3"]:
        print("no its the wrong answer")
    break
while True:
    print("ok so your third question is")
    print(" ")
    print("which programing langauge is know as mother of all langauges")
    choice3 = ("1. c\n"
    "2. fortan\n"
    "3. cobol\n")
    print(choice3)
    user_input3 = input("please enter your answer ")
    if user_input3 not in ["1","2","3"]:
        print("please enter a valid number")
        continue
    elif user_input3 == "1":
        print("yes its the correct answer")
        score += 1
    elif user_input3 in ["2", "3"]:
        print("no your answer is worng")
    break

while True:
    print("great you have made it this far\n so now your next question is..")
    print(" ")
    print("in which year was FORTRAN language created by John Backus")
    choice4 = ("1. 1978\n"
    "2. 1967\n"
    "3. 1957\n")
    print(choice4)
    user_input4 = input("please enter you answer")
    if user_input4 not in ["1" ,"2" ,"3"]:
        print("please enter a valid number")
        continue
    elif user_input4 == "3":
        print("yes its the correct answer ")
        score += 1
    elif user_input4 in ["1","2"]:
        print("please enter a valid number")
    break
print(f"ok so your score is : {score}")
    