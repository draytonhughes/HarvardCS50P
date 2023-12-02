def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Should accept a str as input formattted as $##.## where each # is a decimal digit
    # remove the leading $
    d_without_dollar_sign = d.replace("$", "")
    # return the amount as a float
    return float(d_without_dollar_sign)

def percent_to_float(p):
    # accept a str as input formatted as ##%
    # remove % sign
    p_without_percentage = p.replace("%", "")
    # divide by 100
    p_new = float(p_without_percentage) / 100
    # return the percentage as a float
    return p_new

main()
