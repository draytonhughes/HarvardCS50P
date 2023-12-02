# Create a code that takes a fraction and sends over a percentage.
#  Round to the nearest integer
#. if 1% or less remains output E to indicate that it is empty
#. if 99% or more output F to inidcate that it is Full.

#. X/Y
#. if X or Y not an integer prompts again
#. if X is greater than Y prompt again
#.  if Y is 0 Prompt again
#. if  be sure to display Value Error and Zero Division Error
def main():
    fraction = input("Fraction:  ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)



def convert(fraction):

    while True:

        try:
            numerator, denominator = fraction.split("/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)

            f = new_numerator / new_denominator

            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass


        except: (ValueError, ZeroDivisionError)
        raise

def gauge(percentage):


    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()