from collections import Counter


MOST_COMMON = "etaion"

def main():
    file_name = input("What file do you whant to check ")
    with  open(file_name) as cipher:
        cipher_text = cipher.read()
    is_permutational(cipher_text)


def is_permutational(ciphertext):
    counter = 0
    ciphertext = ciphertext.lower()
    ciphertext_map = Counter(ciphertext)
    for letter in ciphertext_map.most_common(6):
        if letter[0] in MOST_COMMON:
            counter +=1
    if counter/6 >= 0.5:
        print("Cipher is permutational")
    else: print("It just build differently")


main()