import random
import math

key_dictionary ={}
ROWS = 4
cont = True

for a in range(ROWS):
    while cont:
        a = math.floor(random.random() * 4)
        print(a, key_dictionary)
        if a in key_dictionary.keys():
            pass
        else:
            if len(key_dictionary.keys()) == 4:
                cont = False
            else:
                up_or_down = input("Enter u or d to set the direction ")
                key_dictionary[a] = up_or_down


print(key_dictionary)