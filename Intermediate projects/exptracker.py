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

def delete_expense():
    try:
        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()
        
        if not lines:
            print("no expense to delete")
            return 
        print("expense : ")
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            print(f"{i} : {line}")
        
        index = int(input("enter index to delete : "))

        if index < 0 or index >= len(lines):
            print("invalid index")
            return
        deleted = lines.pop(index)

        with open(FILE_NAME, "w") as f:
            f.writelines(lines)

            print(f"deleted : {deleted.strip()}\n")

    except FileNotFoundError : 
        print("no file found")

    except ValueError :
        print("invalid input")

def edit_expense():
    try:
        # 1. Read all lines from the file into a list (in-memory)
        with open(FILE_NAME, 'r') as f:
            lines = f.readlines()
        
        if not lines:
            print("No expenses to edit.\n")
            return
        
        # 2. Show expenses with index numbers using enumerate()
        print("\n📄 Select an expense to edit:")
        for i, line in enumerate(lines):
            # line.strip() removes the newline character for display
            print(f"{i} : {line.strip()}")

        # 3. Ask user which index to edit
        # 8. ValueError will be caught if input is not an integer
        index = int(input("\nEnter index to edit: "))

        # 4. Validate index properly
        if index < 0 or index >= len(lines):
            print("❌ Invalid index!\n")
            return
        
        # 5. Ask for new data
        new_type = input("Enter new expense type: ")
        new_amount = int(input("Enter new amount: "))

        # 6. Replace the selected line in the 'lines' list (memory)
        # We must include the semicolon and the newline character \n
        lines[index] = f"{new_type};{new_amount}\n"

        # 7. Rewrite the whole file using writelines()
        # Using 'w' mode overwrites the entire file with our updated list
        with open(FILE_NAME, "w") as f:
            f.writelines(lines)

        print("✅ Expense updated successfully!\n")

    except FileNotFoundError:
        # 8. Handle case where file doesn't exist yet
        print("❌ No file found. Add expenses first.\n")
    except ValueError:
        # 8. Handle case where user enters non-numeric data
        print("❌ Invalid input. Please enter numbers for index and amount.\n")


# 🔁 Main Menu Loop
while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Filter Expenses")
    print("5. Delete Expenses")
    print("6. Edit Expense")
    print("7. Exit")

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
        delete_expense()

    elif choice == "6":
        edit_expense()

    elif choice == "7":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice. Try again.\n")


            


        

