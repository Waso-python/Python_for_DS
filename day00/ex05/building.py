import sys


def analyze_text(text: str):
    if text is None:
        return

    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punctuation = sum(1 for c in text if c in ".,;:!?")
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    try:
        if len(sys.argv) > 2:
            print("AssertionError: more than one argument is provided")
            return

        text = None
        if len(sys.argv) == 1:
            text = input("What is the text to count?\n")
        else:
            text = sys.argv[1]

        analyze_text(text)

    except Exception as e:
        print(f"AssertionError: {str(e)}")


if __name__ == "__main__":
    main()
