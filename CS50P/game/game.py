from random import randint

while True:
    try:
        user_input = int(input("Level: ").strip())
        if user_input > 0:
            num = randint(1,user_input)
            while True:
                guess = int(input("Guess: ").strip())
                if guess < num:
                    print("Too small!")
                    continue
                elif guess > num:
                    print("Too large!")
                    continue
                else:
                    print("Just right!")
                    break
            break
        else:
            continue
    except ValueError:
        continue