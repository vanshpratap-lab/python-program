f =  open('log.txt', 'r')
while True:
    user_input = input("please enter your answer or type exit")

    if user_input == "exit":
        print("thanks for using")
        break 
    elif user_input == "reset":
        f.seek(0)
        print("reset to beginning")
    elif user_input == "read":
        line = f.readline()

        if not line:
            print("end of file reahced")
            break
        print(f"log : {line}")
        print(f"position : {f.tell()}")
    elif user_input == "jump":
        pos = int(input("please enter your position: "))
        print(f"jumped to : {f.tell()}")

    elif user_input == "pos":
        print(f"current position : {f.tell()}")
    else:
        print("invalid command")
 