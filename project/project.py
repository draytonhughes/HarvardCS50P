## Drayton Hughes
## Clarksville, TN USA
## Movie Watch List
import sys
import csv

"""

This project takes a list of movies in a csv file and appends another csv file to let you know if you it
should be on a watch list or not based on the rating out of 100.  It also takes the year the film was made
and will return how old the film is instead of the year it was made.


"""

def main():
    ## Calls first function to check and make sure files are correct like the scourgify
    check_arguments()
    ## Creates a dictionary of the data
    data = []
    ## try goes reads the data and checks if the file exist
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("CSV file not here")
    ## Creates output list
    output = []
    for row in data:
        ## Calls the 2nd function to see what the rating and if we should put it on our watch list
        recommendation = should_we_watch(row['rating'])
        ## Calls the 3rd function to figure how old the movie is
        age = how_old(row['year'])
        ## appends the output file
        output.append({"title": row["title"], "recommendation": recommendation, "age": age})
        ## writing the out put file
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "recommendation", "age"])
        writer.writerow({"title": "title", "recommendation": "recommendation", "age": "age"})
        for row in output:
            writer.writerow({"title": row["title"], "recommendation": row["recommendation"], "age": row["age"]})


## Functions
def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV Files")



def should_we_watch(val):
    if val in ["95", "96", "97", "98", "99", "100"]:
        return "Must Watch"
    elif val in ["94", "93", "92", "91", "90", "89"]:
        return "Need to Watch"
    elif val in ["88", "87", "86", "85", "84", "83"]:
        return "Might Watch"
    elif val in ["82", "81", "80", "79", "78", "77"]:
        return "Is there nothing else on?"
    else:
        return "Pass"

def how_old(y):
    age = 2023 - int(y)
    return "Age " + str(age)


if __name__ == "__main__":
    main()
