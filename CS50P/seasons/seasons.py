from datetime import date
import inflect
import sys


def main():
    birthday = input("Date of Birth: ")
    Date = validate_date(birthday)
    minutes = convert_to_minutes(Date)
    print(convert_to_words(minutes))


def validate_date(birthday):
    try:
        year, month, day = birthday.split("-")
        return date(int(year), int(month), int(day))

    except ValueError:
        sys.exit("Invalid Date")


def convert_to_minutes(Date):
    difference = date.today() - Date
    return difference.days * 24 * 60


def convert_to_words(minutes):
    p=inflect.engine()
    text = p.number_to_words(minutes, andword="")
    return f"{text.capitalize()} minutes"

 
if __name__ == "__main__":
    main()