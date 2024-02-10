import csv
import sys

new_list = []

def main():
    try:
        with open(check_arg_length()) as old_csv:
            before_list = csv.DictReader(old_csv)
            for row in before_list:
                last, first = row["name"].split(",")
                new_list.append({"first":first.strip(), "last": last.strip(), "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    write_to_csv()


def check_arg_length():
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >= 4:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        sys.exit("Either of the two argument is not a CSV file")
    else:
        return sys.argv[1]


def write_to_csv():
    with open(sys.argv[2], "w") as new_csv:
        writer = csv.DictWriter(new_csv, fieldnames=["first","last","house"])
        writer.writeheader()
        for row in new_list:
            writer.writerow({"first":row["first"], "last":row["last"], "house":row["house"]})

if __name__ == "__main__":
    main()