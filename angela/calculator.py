# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# bill = 150
# persons_number = 5
# percentage = 0.12
#
# tip = bill * percentage
#
# print(tip)
#
# split_bill = (tip + bill) /persons_number
#
# # print(split_bill)
# print(round(split_bill, 2))

bill = 150
persons_number = 5
percentage = 0.12

# Calculate the tip amount
tip = bill * percentage

# Calculate the total amount to be paid by each person
split_bill = (tip + bill) / persons_number

# Print the result rounded to 2 decimal places
print(round(split_bill, 2))
formatted_bill = "{:.2f}".format(split_bill)

# Print the formatted result
print(formatted_bill)