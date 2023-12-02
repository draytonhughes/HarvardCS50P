import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():

    check_command_line()

    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # open shirt
    shirtfile = Image.open("shirt.png")

    # get the size of shirt
    size = shirtfile.size

    # resize muppet image to fit shirt
    muppet = ImageOps.fit(imagefile, size)

    # paste shirt image
    muppet.paste(shirtfile, shirtfile)

    # Create output image
    muppet.save(sys.argv[2])

def check_command_line():

    # Check how many arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Use splitext to split of the file types
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    # Check to see if the files are image files
    if check_extension(file1[1]) == False:
        sys.exit("Invalid Input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid Output")
    # Check if the file types are the same
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")


def check_extension(file):

    # Check if it is a JPG, JPEG, or PNG file
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False


    # if ".jpg" not in sys.argv[1] and ".jpg" not in sys.argv[2]:
    #     sys.exit("Not a JPG, PNG, or JPEG file")
    # if ".jpeg" not in sys.argv[1] and ".jpeg" not in sys.argv[2]:
    #     sys.exit("Not a JPG, PNG, or JPEG file")


if __name__ == "__main__":
    main()
