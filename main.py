morse_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': '/',

    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',

}
word_dict = {code: word for word, code in morse_dict.items()}


def encode():
    """
    :return: takes text and returns its corresponding morse code.
    special characters like , @ etc have not been incorporated
    yet.

    """
    userinput = input('Enter Text: ').upper()

    morse_code = ''
    for word in userinput:
        morse_code += morse_dict[word] + ' '
    print(morse_code)


def decode():
    """

    :return: takes in morse code and returns its equivalent text.
    ',' separate letters while '/' separate words
    """
    morse_input = input('Enter Morse Code: ')
    morse_code_list = morse_input.split(',')

    word = ''
    for code in morse_code_list:
        word += word_dict[code]
    print(word.title())


while True:
    question = input('Do you want to encode or decode text? ').lower()
    if question == 'encode':
        encode()
    elif question == 'decode':
        decode()
    elif question == 'stop':
        break
    else:
        print('that was not the expected input. inputs("encode", "decode", "stop")'.title())
