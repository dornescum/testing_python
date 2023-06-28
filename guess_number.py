import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 1:
        print('wright a bigger number')
        quit()
else:
    print('wright a number next time')
    quit()

random_number = random.randint(0, top_of_range)
# print(random_number)
guesses = 0

while True:
    guesses += 1
    user_guess_input = input('make a guess :')
    # print(user_guess_input)
    if user_guess_input.isdigit():
        user_guess_input = int(user_guess_input)
    else:
        print('wright a number next time')
        continue

    if user_guess_input == random_number:
        print('Correct')
        print('you tried it ' + str(guesses) + ' times')
        break
    else:
        # print('Wrong ')
        if user_guess_input > random_number:
            print('You were above the number!')
        else:
            print('You were below the number!')

print("You got it in", guesses, "guesses")
