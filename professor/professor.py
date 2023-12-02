

import random


def main():
# call get_level
    level = get_level()
   
    score = simulate_game(level)
    print("Score:", score)

# call generate_integer

# prompt the user for a level 1, 2, or 3
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level


def generate_integer(level):

    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)


    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)

    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return (x,y)

def simulate_round(x,y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")


def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        response = simulate_round(x,y)
        if response ==True:
            score += 1
        count_round += 1
    return score



if __name__ == "__main__":
    main()


#. Give 10. questions in formula x + y = z format

#. If the answer is wrong type EEE put and increase wrong by 1
# If an answer is not correct (or not even a number), the program should output
# EEE and prompt the user again, allowing the user up to three tries in total for that problem.
# If the user has still not answered correctly after three tries, the program should output the correct answer.

#. Subtract 10 - wrong answer


#. Give user their score out of 10