from functools import reduce
numbers = [10,34,88,11,1,47,45,14,33,48,69,31,51,23,67]
filtered_numbers = filter(lambda num: num % 2 == 0 and 20 < num < 60, numbers)
# squared_numbers = map(lambda num2: num2*num2 , filtered_numbers)
mapped_numbers = list(map(lambda num2: num2 * num2 , filtered_numbers))
reduced_numbers = reduce(lambda a,b: a+b, mapped_numbers)
reduced_numbers2 = reduce(lambda c,d : c*d, mapped_numbers)
# print(list(filtered_numbers))
# print(list(mapped_numbers))
print(f"sum : {reduced_numbers} and multiply : {reduced_numbers2}")

