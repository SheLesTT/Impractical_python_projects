import sys
from itertools import permutations
from collections import Counter
import loadDictionary
import trigram


def main():

	name = 'tmvoordle'
	name = name.lower()

	word_list_ini = loadDictionary.load("2of12.txt")
	trigrams_filtered = trigram.get_rare_trigrams("trigram.txt")
	print(trigrams_filtered)
	word_list = prep_words(name, word_list_ini)
	filtered_cv_map = cv_map_words(word_list)
	filter_l = cv_map_filter(name, filtered_cv_map)
	filter_2 = trigram_filter(filter_l, trigrams_filtered)
	filter_3 = letter_pair_filter(filter_2)
	view_by_letter(name, filter_3)


def prep_words(name, words_list_ini):
	"""Prepare list to search for anagrams"""
	print(f"default length of list {len(words_list_ini)}")
	word_list = []
	for word in words_list_ini:
		if len(word) == len(name):
			word_list.append(word)
	print(f"Length of new list {len(word_list)}")
	return word_list


def cv_map_words(word_list):
	vovels = "aeyuio"
	cv_map_words = []
	for word in word_list:
		temp = ''
		for letter in word:
			if letter in vovels:
				temp += 'v'
			else:
				temp += 'c'
		cv_map_words.append(temp)

	target = 0.05
	total = len(set(cv_map_words))
	n = int(total * target)
	count_prunned = Counter(cv_map_words).most_common(total - n)
	filtered_cv_map = []
	for pattern, count in count_prunned:
		filtered_cv_map.append(pattern)
	return filtered_cv_map


def cv_map_filter(name, filtered_cv_map):
	""" Delete permutation with rare letter combinations """

	perms = set()
	for i in permutations(name):
		perms.add(''.join(i))
	print(f"length of set at the beginning {len(perms)}")
	vowels = 'aeyuio'
	filter_1 = set()

	for candidate in perms:
		temp = ''
		for letter in candidate:
			if letter in vowels:
				temp += 'v'
			else:
				temp += 'c'
		if temp in filtered_cv_map:
			filter_1.add(candidate)
	print(f"length of the set after the first filter {len(filter_1)}")
	if 'voldemort' in filter_1:
		print('Voldemort in found')
	return filter_1


def trigram_filter(filter_1, trigrams_filtered):
	print(f'length of a set before filter_2 {len(filter_1)}')
	filtered = set()

	for candidate in filter_1:
		for triplet in trigrams_filtered:
			if triplet in candidate:
				filtered.add(candidate)
	filter_2 = filter_1 - filtered
	print(f'length of a set after filter_2 {len(filter_2)}')
	if 'voldemort' in filter_2:
		print('Voldemort in found')
	return filter_2


def letter_pair_filter(filter_2):
	print(f'lenght of a set before filter_3 {len(filter_2)}')
	filtered = set()
	rejects = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv',
			'td', 'tv', 'vd', 'vl', 'vm', 'vr', 'vt']
	first_pair_rejects = ['id', 'lm', 'it', 'lv', 'rd',
		'rl', 'rm', 'rt', 'rv', ' tl', 'tm']

	for candidate in filter_2:
		for r in rejects:
			if r in candidate:
				filtered.add(candidate)
		for f in first_pair_rejects:
			if f in candidate:
				filtered.add(candidate)
	filter_3 = filter_2 - filtered
	print(f'length of a set after filter_3 {len(filter_3)}')
	if 'voldemort' in filter_3:
		print('Voldemort in found')
	return filter_3


def view_by_letter(name, filter_3):

	print(f" letters which are left {name}")
	first = input("Choose letter you what to see first or press Enter to see all")

	subset = []
	for candidate in filter_3:
		if candidate.startswith(first):
			subset.append(candidate)

	print(*sorted(subset), sep='\n')
	print("Число вариантов, начинающихся с {} = {}".format(first, len(subset)))
	msg = "Попробуете еще раз? (Нажмите Enter либо любую другую клавишу для выхода):"

	try_again = input(msg)
	if try_again.lower() == '':
		view_by_letter(name, filter_3)
	else:
		sys.exit()


if __name__ == '__main__':
	main()
main()
