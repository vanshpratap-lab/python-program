def add(a,b):
    return a + b 

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a*b

def divide(a,b):
    if (b==0):
        return("this is wrong")
    return a/b
while True:
    print("----------------")
    print("------welcome to pycalc-------")
    print("----------------")
    print("what do you want to do")
    print("1 -> addition (1)")
    print("2 -> subtraction (2)")
    print("3 -> multiplication (3)")
    print("4 -> division (4)")
    print("5 -> quit")
    choice = input("enter your choice 1/2/3/4/5:")

    if choice == "5" :
        print("thanks for choosing pycalc, keep coding")
        break

    if choice not in ["1", "2", "3", "4", "5"]:
        print("invalid choice please select 1, 2, 3, 4, or 5")
        continue

    try:

        num1 = float(input("enter your first number:"))
        num2 = float(input("enter your second number:"))

    except ValueError:
        print("please try again")
        continue


    if choice == "1":
        result = add(num1,num2)
        symbol = "+"
    elif choice == "2":
        result = subtract(num1,num2)
        symbol = "-"
    elif choice == "3":
        result = multiply(num1,num2)
        symbol = "* "
    elif choice == "4":
        result = divide(num1,num2)
        symbol = "/"

    print(f"{num1} {symbol} {num2} = {result}")