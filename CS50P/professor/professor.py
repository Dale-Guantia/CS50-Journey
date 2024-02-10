from random import randint


def main():

    level = get_level()
    score = 0
    tries = 0

    for _ in range(10):

        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            try:
                ans = x + y
                user_ans = int(input(f"{x} + {y} = "))

                if user_ans == ans:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
                    if tries == 3:
                        print(f"{x} + {y} = {ans}")
                        break
                    else:
                        pass

            except ValueError:
                pass

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            user_input= int(input("Level: "))
            if user_input in [1,2,3]:
                return user_input
            else:
                pass
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return randint(0,9)
    elif level == 2:
        return randint(10,99)
    else:
        return randint(100,999)

if __name__ == "__main__":
    main()