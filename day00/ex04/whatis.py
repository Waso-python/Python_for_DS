import sys


def main():
    try:
        if len(sys.argv) != 2:
            print("AssertionError: more than one argument is provided")
            return
        number = int(sys.argv[1])
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    main()
