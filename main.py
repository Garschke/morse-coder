from morse_dict import MORSE_CODE_DICT


def text_to_morse(text):
    text = text.upper()
    morse_code = [MORSE_CODE_DICT.get(char, '') for char in text]
    return ' '.join(morse_code)


if __name__ == "__main__":
    user_input = input("Enter text to convert to Morse Code: ")
    print("Morse Code:", text_to_morse(user_input))
