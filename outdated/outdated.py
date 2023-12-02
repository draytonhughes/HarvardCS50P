def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]


    while True:
        dates = input("Date: ")
        if "/" in dates:
            dates = dates.strip()
            month, day, year = dates.split("/")
        elif "," in dates:
            dates = dates.replace(",", "")
            parts = dates.split(" ")
            month = parts[0]
            day = parts[1]
            year = parts[2]

            if month in months:
                month = months.index(month) + 1
            else:
                continue
        else:
            continue
        try:
            if int(month) > 12 or int(day) > 31:
                continue
            else:
                break
        except ValueError:
            continue

    print(f"{year}-{int(month):02}-{int(day):02}")

main()
