

message = """We will run the batteries at Vicksburg the night of April 16 and proceed to Grand Gulf 
where we will reduce the forts. Be prepared to cross the river on April 25 or 29. Admiral 
Porter."""

cipher_words = {"batteries": "HOUNDS", "vicksburg": "ODOR", "april": "CLAYTON", '16': 'SWEET', '25': 'MULTIPLY', "29.": 'ADD'}
COLS = 6
ROWS = 7
translation_matrix = [None] * COLS
KEYS =[-1,3,-2,6,5,-4]

def main():
   replaced_words = replace_words(message)
   plain_text = prepare_text(replaced_words)
   encrypt(plain_text)


def replace_words(message):
    message = message.lower()
    text = set(message.split())

    for key in cipher_words.keys():
        if key in text:
            message = message.replace(key, cipher_words[key])
    return message


def prepare_text(message):
    message = message.replace('.', '')
    message = message.upper().split()
    return message


def encrypt(message):
    start = 0
    stop = ROWS
    for key in KEYS:

        if key >0:
            translation_matrix[abs(key)-1] = message[start: stop]
        if key < 0:
            translation_matrix[abs(key)-1] = list(reversed(message[start: stop]))
        start +=ROWS
        stop +=ROWS
    print(translation_matrix)
main()

