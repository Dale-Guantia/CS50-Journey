from PIL import Image, ImageOps
from os.path import splitext
import sys


def main():
    try:
        img = Image.open(check_arg_validity())
    except FileNotFoundError:
        sys.exit(f"{sys.argv[1]} does not exist")

    overlay_shirt(img)


def check_arg_validity():

    first_arg = splitext(sys.argv[1])
    second_arg = splitext(sys.argv[2])

    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 4:
        sys.exit("Too many command-line arguments")
    elif first_arg[1] not in [".jpg",".jpeg",".png"] or second_arg[1] not in [".jpg",".jpeg",".png"]:
        sys.exit("Invalid input")
    elif first_arg[1] != second_arg[1]:
        sys.exit("Input and output have different extensions")
    else:
        return sys.argv[1]


def overlay_shirt(img):
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(img, size)
    photo.paste(shirt, shirt)
    photo.save(sys.argv[2])


if __name__ == "__main__":
    main()