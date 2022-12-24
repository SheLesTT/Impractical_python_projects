"""Дешифровать зигзагообразный шифр времен Гражданской войны в США.
Этот шифр является "двухрядным" и предназначен для коротких сообщений.
Пример шифруемого текста: 'Buy more Maine potatoes'
(Купи еще мэнской картошки)
Зигзагообразный стиль: BYOEANPTTE
UMRMIEOAOS
Чтение зигзага: \/\/\/\/\/\/\/\/\/\/
Шифротекст: BYOEA NPTTE UMRMI EOSOS
"""
import math
import itertools

#-----------------------------------------------------------------------------------------------------------
# ВХОДНЫЕ ДАННЫЕ ПОЛЬЗОВАТЕЛЯ:
# дешифруемая символьная цепочка (вставить между кавычками):
ciphertext = "LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES"
# КОНЕЦ ВХОДНЫХ ДАННЫХ ПОЛЬЗОВАТЕЛЯ - НЕ РЕДАКТИРОВАТЬ НИЖЕ ЭТОЙ СТРОКИ!
#----------------------------------------------------------------------------------------------------------

def main():
    message = prep_ciphertext(ciphertext)
    row1, row2 = split_rails(message)
    decrypt(row1, row2)


def prep_ciphertext(ciphertext):
    message = ''.join(ciphertext.lower().split())
    print(message)
    return message


def split_rails(message):
    row_1_len = math.ceil(len(message)/2)

    row1 = message[:row_1_len]
    row2 = message[row_1_len:]

    return row1, row2


def decrypt(row1, row2):
    plaintext = []

    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1)
        plaintext.append(r2)
        
        if None in plaintext:
            plaintext.pop()
    print(f" full text tata {''.join(plaintext)}")

if __name__ == '__main__':
    main()
#main()