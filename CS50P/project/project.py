from pyfiglet import Figlet
import time
import sys


def main():
    figlet = Figlet()
    figlet.setFont(font = "small")
    print(figlet.renderText("Welcome to RICE50"))
    print("""Perfect Rice Formula:
    * The rice-to-water ratio is "1:1". (e.g., 1 cup of rice = 1 cup of water)
    * Rinse the rice until the water runs clear to remove excess starch.
    * Cook the rice over medium heat until it begins to bubble.
    * Once it starts to bubble, reduce the heat to "low" and let it simmer for "15 minutes".
    * By following this formula, you will always achieve perfect rice.
    """)

    while True:
        user_input = input('Enter "S" to start cooking: ').upper()
        if user_input != "S":
            True
        else:
            break

    while True:
        try:
            Num_of_rice = add_rice(int(input('Enter number of rice in cups: ')))
        except ValueError:
            print("You must enter an integer")
            continue
        break

    loading(Num_of_rice)

    while True:
        try:
            Num_of_water = add_water(int(input('Enter number of water in cups: ')))
        except ValueError:
            print("You must enter an integer")
            continue
        break

    loading(Num_of_water)

    while True:
        level = str(input('Enter heat level ("L" for low, "M" for medium, and "H" for high): ')).upper()
        if level in ["L", "M", "H"]:
            heat, minutes = heat_and_time(level)
        else:
            print("Invalid input")
            continue
        break

    loading(heat, minutes)

    _, rice = Num_of_rice.split("r")
    _, water = Num_of_water.split("c")
    output = result(heat, minutes)


    if int(rice) < int(water):
        print(f'\nResult: Soggy, {output}\n')
    elif int(rice) > int(water):
        print(f'\nResult: Dry, {output}\n')
    elif int(rice) == int(water) and heat == "low" and minutes == 15:
        print("\nResult: Perfect rice\n")
    else:
        print(f"\nResult: {output.capitalize()}\n")


def add_rice(n):
    while True:
        response = input('Enter "R" to rinse rice: ').upper()
        if response == "R":
            return f"r{n}"
        else:
            print("Invalid input")
            continue


def add_water(n):
    while True:
        response = input('Enter "C" to proceed cooking: ').upper()
        if response == "C":
            return f"c{n}"
        else:
            print("Invalid input")
            continue


def heat_and_time(level):
    while True:
        try:
            time = int(input('Enter cooking time in minutes: '))
            if level == "L":
                return "low", time
            elif level == "M":
                return "medium", time
            elif level == "H":
                return "high", time

        except ValueError:
            print("You must enter an integer")
            continue


def result(heat, minutes):
    if heat == "high" and minutes >= 15:
        return "burnt rice"
    elif heat == "high" and minutes < 15:
        return "burnt and raw rice"
    elif heat == "medium" and minutes >= 15:
        return "burnt rice"
    elif heat == "medium" and minutes < 15:
        return "slightly burnt and raw rice"
    elif heat == "low" and 15 < minutes <= 30:
        return "slightly burnt rice"
    elif heat == "low" and minutes > 30:
        return "burnt rice"
    elif heat == "low" and minutes < 15:
        return "raw rice"


def loading(n, minutes = 0):
    if "r" in n:
        print('Washing rice until water is clear', end="")
    elif "c" in n:
        print('Cooking over medium heat until it begins to bubble', end="")
    else:
        print(f'Cooking in {n} heat, wait for {minutes} minutes', end="")

    for _ in range(5):
        time.sleep(1.5)
        sys.stdout.write('.')
        sys.stdout.flush()

    print()



if __name__ == "__main__":
    main()