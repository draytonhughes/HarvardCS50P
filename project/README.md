# Movie Watch List Creator
#### Video Demo:  <https://youtu.be/CW5mHwW5LMA>

#### Description:
Drayton Hughes
Clarksville, TN USA
CS50P Final Project

In my final project I've created a movie watch list creator based on movie reviews. I created the csv file in my folder it is movies.csv  It consists of 3 main columns- title, rating, and year. I then use 3 functions to do 3 specific things.

On the 1st I verify that the input is correct and both files are csv and their are no issues with the number of files for input.

    ####
    def check_arguments():
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
            sys.exit("Not CSV Files")

The 2nd function then checks the rating and assigns a level on the watch list.

    ####
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

The third takes the year the movie was made and changes it to how old the movie is from 2023.  You have to change y the year to an int to do the math and then you have to change it back to a string otherwise you get an error.

    ####
    def how_old(y):
        age = 2023 - int(y)
        return "Age " + str(age)


I then rewrite a new csv file that has the title, a recommendation on which movie to watch first, and how old the movie is.

    ####
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "recommendation", "age"])
        writer.writerow({"title": "title", "recommendation": "recommendation", "age": "age"})
        for row in output:
            writer.writerow({"title": row["title"], "recommendation": row["recommendation"], "age": row["age"]})


The program is a modified version of one our other projects.  I'm guessing this will be par for the course for a while.  I can see ways that I can possibly improve it already.  Working with an API to upload all movies from a database, making the date adjustable so that it is constantly updated.  These are just a few ways to improve the code but I still do not feel comfortable with some of this... this is my first coding class since my first year of college... nearly 23 years ago.  We were doing Cobol and C++ back then.  I do like the VS code editor and I'm sure there are some ways for me to adjust this to make things easier.

I then set up a test program to check my functions.

TODO

Create main program based on parameters listed. - complete

Set up 3 functions -complete
    check arguments
    read and verify files for input and output
    check rating and add recommendations and create new field for new file
    check date the movie was made to see how old it is create new field for new file
    write new file using dictreader
Create test - complete
    need pytest to check argument function

Issues - i had an issue and the realized I was getting a key error because I had spaces after commas in my csv file I created    fixed that and my code was good to go.

    run code and verified that everything was working - complete

    run test and test look good- complete
        verify that test are set up as test_ and name of the function in main code.
        check
    create README file-complete

    create video-

    Upload to CS50 site and cook till a light golden brown

