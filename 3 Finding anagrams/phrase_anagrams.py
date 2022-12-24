import sys
from collections import Counter
import loadDictionary

dict_file = loadDictionary.load("2of12.txt")

ini_name = input("Enter  a name ")


def find_anagrams(name, word_list):
	name_letter_map = Counter(name)
	anagrams = []
	for word in word_list:
		test = ''
		word_map = Counter(word.lower())
		for letter in word:
			if word_map[letter] <= name_letter_map[letter]:
				test += letter
			if Counter(test) == word_map:
				anagrams.append(word)
	print(*anagrams, sep='\n')
	print ()
	print("Остальные буквы = {}".format(name))
	print("Число остальных букв = {}".format(len(name)))
	print("Число остальных анаграмм (реальных слов) = {}".format(len(anagrams)))


def process_choice(name):
	""" Check user variant for validity and return other variants """
	while True:
		msg = '\n Choose or press Enter to start again or print \# to exit '

		choice = input(msg)

		if choice == '':
			main()
		elif choice == '#':
			sys.exit()
		else:

			candidate = ''.join(choice.lower().split())

			left_over_list = list(name)
			for letter in candidate:
				if letter in left_over_list:
					left_over_list.remove(letter)
			if len(name) - len(left_over_list) == len(candidate):
				break  
			else:
				print(f"Will not work, try another variant {choice}")
	name = ''.join(left_over_list)
	print (name)

	return choice, name

def main():
	""" Help user create anagram of his name """

	name = ''.join(ini_name.lower().split())

	limit = len(name)
	phrase = ''
	running = True 

	while running:
		temp_phrase = phrase.replace(' ','')
		if len(temp_phrase) < limit:
			print(f"Length of amagram {len(temp_phrase)}")
			find_anagrams(name, dict_file)
			print(f"Current anagram = {phrase}")

			choice, name = process_choice(name)
			phrase += choice + ' '

		elif len(temp_phrase) == limit:
			print('****DONE****/n')
			print(f'Name anagram = {phrase}\n')
			msg = ('try again? Press Enter to continue or n to finish')
			try_again = input(msg)
			if try_agin == 'n':
				running =False
				sys.exit()
			else:
				main()
		
	if __name__ =='__main__':
		main()

main()