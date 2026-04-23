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
    types = input("Enter expense type: ")
    cost = int(input("Enter amount: "))

    with open(FILE_NAME, 'a') as f:
        f.write(f"{types};{cost}\n")

    print("✅ Expense added!\n")


def view_expense():
    try:
        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()

            if not lines:
                print("No expenses found.\n")
                return

            print("\n📄 All Expenses:")
            for line in lines:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(';')
                print(f"{parts[0]} : {parts[1]}")
            print()

    except FileNotFoundError:
        print("No file found. Add expenses first.\n")


def show_total():
    cost_list = []

    try:
        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(';')
                cost_list.append(int(parts[1]))

        total = reduce(lambda a, b: a + b, cost_list) if cost_list else 0
        print(f"\n💰 Total Expense: {total}\n")

    except FileNotFoundError:
        print("No file found. Add expenses first.\n")


def filter_expense():
    expense_list = []

    try:
        limit = int(input("Show expenses greater than: "))

        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()

            for line in lines:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(';')
                expense_list.append((parts[0], int(parts[1])))

        filtered = list(filter(lambda x: x[1] > limit, expense_list))

        if not filtered:
            print("No matching expenses.\n")
            return

        print("\n🔍 Filtered Expenses:")
        for item in filtered:
            print(f"{item[0]} : {item[1]}")
        print()

    except FileNotFoundError:
        print("No file found. Add expenses first.\n")


# 🔁 Main Menu Loop
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Filter Expenses")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expense()

    elif choice == "3":
        show_total()

    elif choice == "4":
        filter_expense()

    elif choice == "5":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.\n")


            


        

