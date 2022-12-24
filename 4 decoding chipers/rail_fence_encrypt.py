"""Зашифровать текст зигзагообразным шифром времен Гражданской войны
        в США. Этот шифр является "двухрядным" и предназначен для
        коротких сообщений. Пример шифруемого текста:
        'Buy more Maine potatoes' (Купи еще мэнской картошки)
        Зигзагообразный стиль: BYOEANPTTE
        UMRMIEOAOS
        Чтение зигзага: \/\/\/\/\/\/\/\/\/\/
        Шифротекст: BYOEA NPTTE UMRMI EOSOS
"""
#-------------------------------------------------------------------------------------------------------
 # ВХОДНЫЕ ДАННЫЕ ПОЛЬЗОВАТЕЛЯ:
# шифруемая символьная цепочка (вставьте между кавычками):
plaintext = """Давай пересечем реку и отдохнем в тени деревьев"""
 # КОНЕЦ ВХОДНЫХ ДАННЫХ ПОЛЬЗОВАТЕЛЯ - НЕ РЕДАКТИРОВАТЬ
# НИЖЕ ЭТОЙ СТРОКИ!
#--------------------------------------------------------------------------------------------------------

def main():

    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)

def prep_plaintext(plaintext):
    plaintext = ''.join(plaintext.upper().split())
    return plaintext


def build_rails(plaintext):
    evens =plaintext[::2]
    odds = plaintext[1::2]
    rails = evens + odds
    return(rails)


def encrypt(rails):
    ciphertext = ''. join([rails[i:i+5] for i in range(0,len(rails), 5)])
    print(f' ciphertext = {ciphertext}')

main()
