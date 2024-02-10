def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            fraction = int(x) / int(y)
            fraction = round(fraction * 100)
            if fraction <= 100:
                return fraction
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()