from tabulate import tabulate
import csv
import sys

def main():
    output = add_grid_format(check_arg_length())
    print(output)

def check_arg_length():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        return sys.argv[1]

def add_grid_format(arg):
    try:
        with open(arg) as file:
            table = csv.DictReader(file)
            return tabulate(table, headers="keys", tablefmt="grid")

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()