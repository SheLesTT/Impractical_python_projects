ciphertext = '16 12 8 4 0 1 5 9 13 17 18 14  10  6 2 3 7 11 15 19'

ciphertext = list(ciphertext.split())

COLS = 4
ROWS = 5
key = '-1 2 -3 4'

translation_matrix = [None] * COLS
plaintext = ''
start = 0
stop = ROWS

key_int = []
for i in key.split():
    key_int.append(int(i))
print(key_int)

for k in key_int:
    if k < 0:
        col_items = ciphertext[start:stop]
    elif k > 0:
        col_items = list(reversed(ciphertext[start:stop]))

    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS

print("\nшифротекст = {}".format(ciphertext))
print("\nпереводная матрица =", *translation_matrix, sep="\n")
print("\nдлина ключа = {}".format(len(key_int)))

for i in range(ROWS):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + " "

print("\nоткрытый текст = {}".format(plaintext))