# numbers = [1,2,3]
# new_list = [n+1 for n  in numbers]
# print(new_list)

name = 'Angela'
new_name = [name for name in name]
# print(new_name)


values = [item * 2 for item in range(1,5)]
print(values)

names = ['alex', 'beth', 'caroline','dave', 'eleanor', 'freddie']
short_names = [name for name in names if len(name)< 5]
# print(short_names)

long_names = [name.upper() for name in names if len(name)> 5]
print(long_names)


numbers = [1,1,2,3, 5, 8, 13, 21, 34,55]
result = [num for num in numbers if num % 2 == 0]

print(result)
