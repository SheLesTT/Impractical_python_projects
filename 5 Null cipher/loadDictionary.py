import sys  

def load(file):
	try:
		with open(file) as in_file:
			""" returns a list of separate words """
			loaded_txt = in_file.read().strip().split('\n')  #strip method without paramets removes speces
			for word in loaded_txt:
				word.lower()
			return loaded_txt
	except IOError as e:
		print(f'\n{e}ошибка при открытии файла {file}',file = sys.stderr)
		sys.exit(1)

