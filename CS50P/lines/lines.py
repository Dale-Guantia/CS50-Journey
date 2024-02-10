import sys

line_count = 0

try:
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

except FileNotFoundError:
    sys.exit("File does not exist")

else:
    with open(sys.argv[1]) as file:
        file = file.readlines()
        for line in file:
            if line.lstrip().startswith("#"):
                continue
            elif line.isspace() == True:
                continue
            else:
                line_count += 1

print(line_count)