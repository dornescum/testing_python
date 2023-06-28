print('Welcome to my computer quiz!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("okay ! let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
    print('score cpu :' + str(score))
else:
    print("Incorrect!")
    score -= 1
    if score < 1:
        score = 0
    print('score ram : ' + str(score))

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
    print('score gpu: ' + str(score))
else:
    print("Incorrect!")
    score -= 1
    if score < 1:
        score = 0
    print('score ram :' + str(score))

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
    if score < 1:
        score = 0
    print('score ram : ' + str(score))
else:
    print("Incorrect!")
score -= 1
if score < 1:
    score = 0
    print('score ram :' + str(score))

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
    print('score psu : ' + str(score))
else:
    print("Incorrect!")
    score -= 1
    print('score ram :' + str(score))

# print(score)
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
