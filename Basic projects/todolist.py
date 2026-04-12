tasks = []

while True:
    print("-----whats on your mind------")
    print("1. enter tasks")
    print("2. view tasks")
    print("3. delete tasks")
    print("3.  exit ") 
    
    choice = input("enter your choice")

    if choice == "1":
        task = input("enter your task")
        tasks.append(task)
        print("task added")
    elif choice == "2":
        if len(tasks) == 0  :
            print("no task available")
        else:
            print("your tasks:")
            for i ,tasks in enumerate (tasks, start = 1):
                print(f"{i} {tasks}")
    elif choice == "3":
        if len(tasks) == 0:
            print("no task to delete")
        else:
            for i ,tasks in enumerate (tasks, start = 1):
                print(f"{i} {tasks}")
            
            try:
                num = int(input("enter your task no."))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num -1)
                    print(f"removed {removed}")
                else:
                    print("incorrect value")

            except ValueError:
                print("please enetr a valid number")
    elif choice == "4":
        print("thanks for yousing this")
        break
    else:
        print("invalid number")


