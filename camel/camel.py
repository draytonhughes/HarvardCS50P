# Enter something in camelCase.  Camel case means doing upper case... python prefers adding _ instead of camelCase

# Get input from user in camelCase
camelCase = input("camelCase: ")

#print it in snake case the end makes it where the line doesn't return
print("snake_case: ", end="")

#Loop through every letter
for letter in camelCase:
    if letter.isupper():
        print("_" + letter.lower(), end="")
    else:
        print(letter, end="")

print()


