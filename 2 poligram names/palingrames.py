import loadDictionary  

word_list = loadDictionary.load("2of12.txt")
print("started")
def find_palingrams():
	pali_list = []
	words = set(word_list)

	for word in words:
		rev_word = word[::-1]
		end = len(word)
		if end > 1:
			for i in range(end):
				if (rev_word[end-i:] in words 
						and rev_word[:end-i] == word[i:]):
					pali_list.append((word, rev_word))

				if (rev_word[:end-i] in words
						and rev_word[end-1:] == word[:end-i]):
					pali_list.append((rev_word[:end-i], word))

	return pali_list

palingrams = find_palingrams()

palingrams_sorted = sorted(palingrams)
print("finished")

print(f"\n Number of palingrams {len(palingrams)}\n")
for first, second in palingrams_sorted:
	print(f"{first} {second}")


