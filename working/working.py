import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    correct_string = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if correct_string:
        piece = correct_string.groups()
        if int(piece[1]) > 12 or int(piece[5]) > 12:
            raise ValueError
        first_time = new_format(piece[1], piece[2], piece[3])
        second_time = new_format(piece[5], piece[6], piece[7])

        return first_time + ' to ' + second_time

    else:
        raise ValueError



def new_format(hour, minutes, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    ## minutes
    if minutes == None:
        new_minute = ':00'
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ':' + minutes
    return new_time


if __name__ == "__main__":
    main()
