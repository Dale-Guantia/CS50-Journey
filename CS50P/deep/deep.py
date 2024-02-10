ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

match ans:
    case "42" | "forty-two" | "forty two" | "fortytwo":
        print("Yes")
    case _:
        print("No")
