import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")
else:
    value = float(sys.argv[1])

bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
coin = bitcoin.json()

try:
    price = (coin["bpi"]["USD"]["rate_float"]) * value
    print(f"${price:,.4f}")

except requests.RequestException:
    sys.exit("Request Exception Error")
