import loadDictionary

word_list = loadDictionary.load("2of12.txt")

user_word = input("\nenter a word you whant to find anagrams to\n")
sorted_user_word = sorted(list(user_word))

print(user_word)

list_of_anagrams = []

for word in word_list:
	sorted_word = sorted(list(word))
	if (sorted_word == sorted_user_word and word != user_word):
		list_of_anagrams.append(word)
print(list_of_anagrams)


