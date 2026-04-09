f =  open('log.txt', 'r')
while True:
    user_input = input("please enter your answer or type exit")

    if user_input == "exit":
        print("thanks for using")
        break 
    elif user_input == "reset":
        f.seek(0)
        print("reset to beginning")
    else:
        line = f.readline()

        if not line:
            print("end of file reahced")
            break
        print(f"log : {line}")
        print(f"position : {f.tell()}")
