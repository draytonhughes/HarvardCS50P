# Gets input from a user on a question

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# sets the input to lower case
lower_answer = answer.lower()
# strips any blank spaces away on either side
fixed_answer = lower_answer.strip()


# tries to find an answer in the form of 42 if you get it right it prints yes... otherwise you have to guess again
match fixed_answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

