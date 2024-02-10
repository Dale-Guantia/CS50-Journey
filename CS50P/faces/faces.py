def main():
    text = input()
    output = convert(text)
    print(output)

def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()