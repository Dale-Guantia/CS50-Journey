def main():
    shorten_word = shorten(input("Input: ").strip())
    print(f"Output: {shorten_word}")

def shorten(word):
    for char in word:
        if char in ["A", "E", "I", "O" ,"U", "a", "e", "i", "o", "u"]:
            word = word.replace(char, "")
    return word

if __name__ == "__main__":
    main()