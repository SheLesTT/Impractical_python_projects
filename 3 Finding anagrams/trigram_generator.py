# open a dictionary Clean it up
# get user string. separate letter in it
# get a list of words that can be created from it
#  for each word in a set get a new set of word which can be created from letters left
#   Check the length of anagram with user string
#    If it longer go to next word
#    If it equal add it to the list of anagrams
#    else create a new list of letters left


from collections import Counter
import loadDictionary

word_list = loadDictionary.load("2of12.txt")
for word in word_list:
    if len(word) == 1:
        word_list.remove(word)
word_list.append("a")
word_list.append("I")
bad_letters = set()


ini_string = input("Enter a string to search anagrams for ")
list_of_anagrams = []


def main():
    name = ''.join(ini_string.lower().split())
    name = list(name)
    current_anamgram = ''
    create_an_anagram(name, word_list, current_anamgram)
    print("finished")
    print(list_of_anagrams)


"""def create_an_anagram(name, word_list):
    name_map = Counter(name)
    anagrams = []
    for word in word_list:
        temp= ''
        for letter in word_list:
   """


def create_an_anagram(name, word_list, current_anagram):
    #print('name at the begining' )
   # print(name)
    name_map = Counter(name)
    test=''
    for leter in name:
        test += leter
    for word in word_list:

        test_anagram = current_anagram
        word_map = Counter(word)
        temp = ''
        for letter in word:
            if word_map[letter] <= name_map[letter]:
                temp += letter
            if word_map == Counter(temp) and word != test:
                test_anagram += word
               # print(test_anagram)

                #print()

                left_over_list = list(name)
               # print(left_over_list)
                for let in word:
                    left_over_list.remove(let)
                #print(left_over_list)

                if len(left_over_list) == 0:
                    list_of_anagrams.append(' ' + word)
                    print(list_of_anagrams)
                elif len(left_over_list) > 1:
                  #  print(left_over_list)
                    print(left_over_list)
                    print( test_anagram)
                    create_an_anagram(left_over_list, word_list, test_anagram)


    print(" end of a branch")

main()
