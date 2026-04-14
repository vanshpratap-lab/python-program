types = input("pleaase enter your type : ")
cost = int(input("please enter your cost : "))

with open('expense.txt', 'a') as f:
    f.write(f"{types};{cost}\n")

with open('expense.txt', 'r') as g:
    lines = g.readlines()
    for line in lines :
        line = line.strip()
        parts = line.split(';')
        types = parts[0]
        cost = parts[1]
        print(f"{types}:{cost}")

