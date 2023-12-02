#import sys program
import sys

def main():

    # check the command line arguments
    check_command()

    # try to open
    try:
        f = open(sys.argv[1], "r")
        lines = f.readlines()

    # set a variable to count the lines
        count_lines = 0
        for line in lines:
            if check_is_code(line) == False:
                count_lines += 1
        print(count_lines)



    # is there a file? if no file files does not exit sys.exit
    except FileNotFoundError:
        sys.exit("File does not exist")


    # loop through the lines and see if any start with "#" or " "






def check_command():

    # check the number of elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

   # print(sys.argv)

    # check if it is a python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")

def check_is_code(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False




if __name__ == "__main__":
    main()