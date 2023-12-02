#implement a function called convert that accepts a str as input and returns the same input with any
# :) converted to a slightly smiling face and :( as a slightly frowning face
# other text should remain unchanged
# implement a function called main that prompts the user for input
# calls Convert on that input,
# prints the result

def main():
    phrase = input("Enter your phrase: ")
    converted_phrase = convert(phrase)
    print(converted_phrase)

# convert the smiles
def convert(phrase):
    phrase = phrase.replace(":)", "🙂")
    phrase = phrase.replace(":(", "🙁")
    return rphrase
# print(replaced)


main()
