# from functools import reduce
# cost_list = []
# expense_list = []
# while True:
#     print("1. add expense")
#     print("2. view expense")
#     print("3. show total expense")
#     print("4. filter expense")
#     print("5. exit")

#     user_input = input("please enter your choice")

#     if user_input == "5":
#         print("thanks have a good day")
#         break

#     elif user_input == "1":
#         print("add expense")
#         types = input("pleaase enter your type : ")
#         cost = int(input("please enter your cost : "))
#         with open('expense.txt', 'a') as f:
#             f.write(f"{types};{cost}\n")
        

#     elif user_input == "2":
#         with open('expense.txt', 'r') as g:
#             lines = g.readlines()

#             for line in lines:
#                 line = line.strip()
#                 if not line :
#                     continue



#                 parts = line.split(';')
#                 types = parts[0]
#                 cost = int(parts[1])
#                 print(f"{types}:{cost}")
#                 cost_list.append(int(cost))
#                 expense_list.append((types,int(cost)))
        

#     elif user_input == "3":
#         if cost_list :
#             total = reduce(lambda c,d : c + d , cost_list)
#         else:
#             total = 0
#         print(f"total : {total}")

#     elif user_input == "4":
#         expense = filter(lambda x : x[1] > 450, expense_list)
#         filtered_expense = list(expense)
#         for item in filtered_expense :
#             print(f"{item[0]} : {item[1]}")
#     else:
#         print("inavlid input")


from functools import reduce
FILE_NAME = "expense.txt"

def add_expense():
    types = input("please enter your expense")
    cost = int(input("please enter your cost"))

    with open(FILE_NAME,'a') as f:
        f.write(f"{types};{cost}")

    print("expense added")

def view_expense():
    try:
        with open(FILE_NAME, 'r') as g:
            lines = g.readlines()

            if not lines:
                print("no expense found")
                return
            
            print("all expenses: ")
            for line in line:
                line = line.strip()
                if not lines:
                    continue

                parts = line.split(';')
                print(f"{parts[0]} : {parts[1]}")
            print()
    except FileNotFoundError:
        print("no file found")

def show_total():
    cost_list = []
    try:
        with open(FILE_NAME, 'r') as h:
            lines = h.readlines()

            if not lines:
                print("no expense found ")
                return
            for line in lines:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(';')
                cost_list.append(int(parts[1]))
    
        total = reduce(lambda a,b : a+b , cost_list) if cost_list else 0
        print(f"total : {total}")
    except FileNotFoundError:
        print("no file found")


def filter_expense():
    expense_list = []

    try:
        limit = int(input("show expense greate than: "))

        with open(FILE_NAME,'r') as i:
            lines = i.readlines()

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(';')
                expense_list.append((parts[0], int(parts[1])))

            filtered = list(filter(lambda x : x[1] > limit, expense_list))

            if not filtered:
                print("no matching expense")
                return
            
            print("filtered expense: ")
            for item in filtered:
                print(f"{item[0]}:{item[1]}")
            print()

    except FileNotFoundError:
        print("no file found: ")

while True:
    print("1. add expense")
    print("2. view expense")
    print("3. show expense")
    print("4. total expense")
    print("5. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        show_total()
        
    elif choice == "4":
        filter_expense()

    elif choice == "5":
        print("exiting....goodbye")
        break

    else:
        print("invalid try again")


            


        

