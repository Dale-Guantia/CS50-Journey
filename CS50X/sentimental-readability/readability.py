from cs50 import get_string


def main():
    text = get_string("Text: ")

    num_words = 1
    num_sentences = 0
    num_letters = 0

    for i in range(len(text)):
        if text[i] == " ":
            num_words += 1
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            num_sentences += 1
        if text[i].isalpha():
            num_letters += 1

    L = (num_letters / float(num_words)) * 100
    S = (num_sentences / float(num_words)) * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


if __name__ == "__main__":
    main()
