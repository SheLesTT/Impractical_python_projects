

def get_rare_trigrams(file):
	trigram_dict = {}
	total = 0
	with  open(file) as file:
		trigram_list = file.read().strip().split('\n')
		for trigram in trigram_list:
			trigram_pair = trigram.split('\t')
			trigram_pair[1] = int(trigram_pair[1])
			total += trigram_pair[1]
			trigram_dict[trigram_pair[0]] = trigram_pair[1]

	file.close()

	average = total / len(trigram_dict)
	for key in list(trigram_dict.keys()):
		if trigram_dict[key] > 0.01 * average:
			del trigram_dict[key]

	return list(trigram_dict.keys())



