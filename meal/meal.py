# prompt user for the time out puts
# Breakfast Time between 7:00 and 8:00
# lunch time between 12:00 and 13:00
# dinner between 18:00 and 19:00
def main():

    t = input("What time is it? ")

    time = convert(t)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    float_hours = float(hours)
    float_minutes = float(minutes)
    div_float_minutes = float_minutes / 60

    float_time = float_hours + div_float_minutes
    return float_time

if __name__ == "__main__":


    main()
