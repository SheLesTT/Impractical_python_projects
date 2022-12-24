
# create list of words in new message
# go throught the message letter by letter
#
import loadDictionary

def main():
    message =  ""
    message = ''.join(message.lower().split())
    supporters_list = loadDictionary.load('supporters.txt')
    cipher_list = create_cipher_list(message, supporters_list)

    print(cipher_list)
    for name in cipher_list:
        print(name)



def create_cipher_list(message, supporters):
        names_list = ['Lily']
        counter = 0
        for char in (message):
            if counter == 5:
                names_list.append("Stuard")
            if counter == 8:
                names_list.append("Jacob")

            counter +=1
            if counter % 2 == 1:
                for name in supporters:
                    if (name[1] == char) and (name not in names_list)
                        names_list.append(name)
                        break
            else:
                for name in supporters:
                    if (name[2] == char) and (name not in names_list):
                        names_list.append(name)
                        break
        return names_list

main()