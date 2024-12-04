import sys
from ft_filter import ft_filter


def main():
    try:
        # Check the number of arguments
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        # Get the string and number from the arguments
        string = sys.argv[1]
        number = sys.argv[2]

        # Check the types of the arguments
        if not isinstance(string, str) or not number.isdigit():
            raise AssertionError("the arguments are bad")

        number = int(number)

        # Split and filter them using ft_filter and lambda
        words = string.split()
        filtered_words = list(ft_filter(lambda x: len(x) > number, words))

        print(filtered_words)

    except Exception as e:
        print(f"AssertionError: {str(e)}")


if __name__ == "__main__":
    main()
