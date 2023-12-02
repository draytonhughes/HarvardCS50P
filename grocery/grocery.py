#. Create a dictionary for groceries add things one at a time and then add up the count

grocery = {}

# Loop forever

while True:
    try:
        # Get user input
        item = input().lower()
        # Check if item is already in the dictionary
        if item in grocery:
            # If it is, add 1 in the count
            grocery[item] += 1
        #otherwise, add the item for the first time
        else:
            grocery[item] = 1
    except EOFError:
        # Print all the items in alphabetical order
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        # stop the while loop
        break