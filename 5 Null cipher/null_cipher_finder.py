import sys
import string

def load_text(file):
    with open(file) as f:
        return f.read().strip()


def solve_null_chiper(text,lookahead):
    # lookahead - amount of letters after punctuation character

    for i in range(1, lookahead+1):
        plaintext = ''
        counter = 0
        first_found = False
        for char in text:
            if char in string.punctuation:
                counter = 0
                first_found = True
            elif first_found is True:
                counter += 1
            if counter == i:
                plaintext += char
        print(f"text with {i} symbols = {plaintext}")




def main():

    try:
        loaded_message = load_text('trevion.txt')
    except IOError as e:
        print(f"End of program {e}", file=sys.stderr)
        sys.exit(1)

    message = ''.join(loaded_message.split())

    while True:
        lookahead = input("Enter possible key range")
        if lookahead.isdigit():
            lookahead = int(lookahead)
            break
        else:
            print("Enter a number please", file=sys.stderr)



    solve_null_chiper(message,lookahead)

main()
