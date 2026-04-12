from functools import reduce

f = open('data.txt','r')
lines = f.readlines() #read all lines 
# print(lines)
data_lines = lines[1:] #skips header lines like name,marks
# print(data_lines)
int_marks = []
# for line in data_lines:
#     print(line)
for line in data_lines:
    line = line.strip()
    parts = line.split(',')
    
    name = parts[0]
    marks = parts[1]
    
    print(f" {name} : {marks}")
    int_marks.append(marks)

mapped_list = map(lambda m: int(m) ,int_marks )
filtered_list = list(filter(lambda m : m > 80 , mapped_list))
reduced_list = reduce(lambda a,b: a+b , filtered_list)
count = len(filtered_list)
average = reduced_list/count
print("filtered list :",filtered_list)
print(average)