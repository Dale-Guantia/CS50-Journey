from cs50 import get_float


def main():
    # Ask how many cents the customer is owed
    cents = get_cents()

    # Calculate the number of quarters to give the customer
    quarters = calculate_quarters(cents)
    cents = cents - (quarters * 25)

    # Calculate the number of dimes to give the customer
    dimes = calculate_dimes(cents)
    cents = cents - (dimes * 10)

    # Calculate the number of nickels to give the customer
    nickels = calculate_nickels(cents)
    cents = cents - (nickels * 5)

    # Calculate the number of pennies to give the customer
    pennies = calculate_pennies(cents)
    cents = cents - (pennies * 1)

    # Sum coins
    coins = quarters + dimes + nickels + pennies

    # Print total number of coins to give the customer
    print(coins)


def get_cents():
    while True:
        owed = get_float("Change owed: ")
        if owed < 0:
            continue
        else:
            return owed * 100


def calculate_quarters(cents):
    num_quarters = 0

    while True:
        if 25 <= cents:
            num_quarters += 1
            cents -= 25
        else:
            return num_quarters


def calculate_dimes(cents):
    num_dimes = 0

    while True:
        if 10 <= cents:
            num_dimes += 1
            cents -= 10
        else:
            return num_dimes


def calculate_nickels(cents):
    num_nickels = 0

    while True:
        if 5 <= cents:
            num_nickels += 1
            cents -= 5
        else:
            return num_nickels


def calculate_pennies(cents):
    num_pennies = 0

    while True:
        if 1 <= cents:
            num_pennies += 1
            cents -= 1
        else:
            return num_pennies


if __name__ == "__main__":
    main()
