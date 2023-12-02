#Get user input and get a greeting
def main():

    greeting = input("Greeting: ")
    value_to_print = value(greeting)
    #print answer
    print(f"${value_to_print}")

### functions

def value(greeting):
    #strips and lowers the input
    greeting = greeting.lower().strip()
    # check if the answer has hello, return $0
    if "hello" in greeting:
       return 0

    # check if the answer starts with H, return $20
    elif "h" == greeting[0]:
        return 20

    # else print("100")
    else:
        return 100


if __name__ == "__main__":
    main()
