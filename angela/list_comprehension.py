"""
This is a module-level docstring.

Describe the purpose of your module here.
You can provide additional details and usage instructions.
"""

# Your Python code goes here
# ...


with open('file1.txt') as file1:
    file_1_data = file1.readlines()

with open('file1.txt') as file2:
    file_2_data = file2.readlines()    

# print(file_1_data)
# print(file_2_data)

# result = [int(num) for num in file_1_data if num in file_2_data]
result = [int(num) for num in open("file1.txt") if num in open("file2.txt")]

print(result)
