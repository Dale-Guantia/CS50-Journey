from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height < 1 or height > 8:
        continue
    else:
        break

for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")
    for k in range(i):
        print("#", end="")
    print()
