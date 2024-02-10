import re


def main():
    print(count(input("Text: ")))


def count(s, um_count = 0):
    if matches := re.findall(r"\bum\b", s, re.IGNORECASE):
        um_count += len(matches)

    return um_count


if __name__ == "__main__":
    main()