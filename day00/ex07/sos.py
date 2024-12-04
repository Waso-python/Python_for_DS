import sys


MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}


def encode_to_morse(text: str) -> str:
    """
    Encodes text to Morse code.
    Returns a string with Morse code or raises
    AssertionError for invalid characters.
    """
    try:
        # Check each character for validity and convert to uppercase
        morse = [MORSE_CODE[char.upper()] for char in text]
        return ' '.join(morse)
    except KeyError:
        raise AssertionError("the arguments are bad")


def main():
    try:
        # Check the number of arguments
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        # Get the string from the arguments
        text = sys.argv[1]

        # Encode and print the result
        result = encode_to_morse(text)
        print(result)

    except Exception as e:
        print(f"AssertionError: {str(e)}")


if __name__ == "__main__":
    main()
