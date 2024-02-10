import inflect

p = inflect.engine()

name_list = []

while True:
    try:
        name = input("Name: ").title().strip()
        name_list += [name]
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(name_list)}")
        break