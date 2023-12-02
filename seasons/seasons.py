from datetime import date

import re
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of birth: ")
    try:
        year, month, day = check_date(birth_date)
    except:
        sys.exit("Invalid Date")
    dob = date(int(year), int(month), int(day))
    current_date = date.today()
    difference = current_date - dob
    number_of_minutes = (difference.days * 24 * 60)
    output = p.number_to_words(number_of_minutes, andword = "")
   

    print(output.capitalize() + " minutes")



def check_date(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
       year, month, day = birth_date.split("-")
       return year, month, day



if __name__ == "__main__":
    main()
