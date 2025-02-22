from morse_dict import MORSE_CODE_DICT


def text_to_morse(text):
    text = text.upper()
    morse_code = [MORSE_CODE_DICT.get(char, '') for char in text]
    return ' '.join(morse_code)


if __name__ == "__main__":
    print("Morse Code Converter\nEnter text to be converted:")
    user_input = input("")
    print(f"Morse Code:\n, {text_to_morse(user_input)}")
