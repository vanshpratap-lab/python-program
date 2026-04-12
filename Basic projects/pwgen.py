#----------HARD CODE---------- 
# import random
# import string 
# num = random.randint(1,9)
# num2 = random.randint(1,9)
# num3 = random.randint(1,9)
# b = string.ascii_letters
# f = string.punctuation
# length = int(input("please choose your password length"))
# for i in range(length):
#     print(i)
#     a = random.choice(b)
#     d = random.choice(b)
#     e = random.choice(b)
#     g = random.choice(f)
#     h = random.choice(f)
#     c = str(num) + str(num2) + str(num3) + a + d + e + g + h
#     print(c)

#----------FIXED CODE----------

import random
import string

length = int(input("please enter your password length"))

all_chars = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    char = random.choice(all_chars)
    password += char

print(f"generated password {password}")