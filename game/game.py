# Have user put in an integer.  If they put in a negative prompt again
import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
                break
    except:
        pass





# set random number

number = random.randint(1, level)

# Get Guess and check
while True:
    try:
        guess = int(input("Guess: "))

        if guess > number:
            print("Too large!")

        elif guess < number:
            print("Too small!")

        else:
            print("Just Right!")
            break

    except:
        pass



