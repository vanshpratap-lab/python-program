from functools import reduce
types = input("pleaase enter your type : ")
cost = int(input("please enter your cost : "))

with open('expense.txt', 'a') as f:
    f.write(f"{types};{cost}\n")
cost_list = []
expense_list = []
with open('expense.txt', 'r') as g:
    lines = g.readlines()
    for line in lines :
        line = line.strip()
        parts = line.split(';')
        types = parts[0]
        cost = parts[1]
        print(f"{types}:{cost}")
        cost_list.append(int(cost))
        expense_list.append((types,int(cost)))

if cost_list:
    total = reduce(lambda a,b : a + b, cost_list )
else:
    total = 0
print(f"total : {total}")
expense = filter(lambda x : x[1] > 450, expense_list)
filtered_expense = list(expense)
for item in filtered_expense :
    print(f"{item[0]} : {item[1]}")