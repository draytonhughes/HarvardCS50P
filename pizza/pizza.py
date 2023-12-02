import sys
import csv


from tabulate import tabulate

# from tabulate import tabulate

def main():
    check_command_line()

    data = []

   # try to open the file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

        # print the table
        print(tabulate(data[1:], headers= data[0], tablefmt="grid"))

    # file doesn't exist
    except FileNotFoundError:
         sys.exit("File does not exist")



def check_command_line():
    # how many elements
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # is it a csv file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()