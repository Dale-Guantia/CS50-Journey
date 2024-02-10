groceries = {}

while True:
    try:
        item = input().upper()
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1

    except EOFError:
        print()
        for i in sorted(groceries):
            print(f"{groceries[i]} {i}")
        break