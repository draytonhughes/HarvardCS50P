#inport the library
import emoji
# get a phrase from the user by prompting
phrase = input("Input: ")
#take a variable and use the library and function to change the phrase also use alias to change the _ or not to make the code
#useful in multipl ways
output = emoji.emojize(phrase, language='alias')
#print the answer
print('Output:', output)


