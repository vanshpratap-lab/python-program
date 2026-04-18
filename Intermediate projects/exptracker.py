from functools import reduce
cost_list = []
expense_list = []
while True:
    print("1. add expense")
    print("2. view expense")
    print("3. show total expense")
    print("4. filter expense")
    print("5. exit")

    user_input = input("please enter your choice")

    if user_input == "5":
        print("thanks have a good day")
        break

    elif user_input == "1":
        print("add expense")
        types = input("pleaase enter your type : ")
        cost = int(input("please enter your cost : "))
        with open('expense.txt', 'a') as f:
            f.write(f"{types};{cost}\n")
        

    elif user_input == "2":
        with open('expense.txt', 'r') as g:
            lines = g.readlines()

            for line in lines:
                line = line.strip()
                if not line :
                    continue



                parts = line.split(';')
                types = parts[0]
                cost = int(parts[1])
                print(f"{types}:{cost}")
                cost_list.append(int(cost))
                expense_list.append((types,int(cost)))
        

    elif user_input == "3":
        if cost_list :
            total = reduce(lambda c,d : c + d , cost_list)
        else:
            total = 0
        print(f"total : {total}")

    elif user_input == "4":
        expense = filter(lambda x : x[1] > 450, expense_list)
        filtered_expense = list(expense)
        for item in filtered_expense :
            print(f"{item[0]} : {item[1]}")
    else:
        print("inavlid input")
