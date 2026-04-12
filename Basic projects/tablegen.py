while True:
    user_input = input("enter a number or type 'exit' to quit: ")

    if user_input == "exit":
        print("thanks! goodbye")
        break
    try:
        num = int(user_input)
    except ValueError:
        print("please enter a valid number")
        continue
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")