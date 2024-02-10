fixed_price = 50

while fixed_price > 0:
    print(f"Amount Due: {fixed_price}")
    inserted_coin = int(input("Insert Coin: "))

    if inserted_coin in [25, 10, 5]:
        fixed_price -= inserted_coin

print("Change Owed:", abs(fixed_price))