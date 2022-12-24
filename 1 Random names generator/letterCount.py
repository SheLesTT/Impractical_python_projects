import pprint
from collections import defaultdict

user_string = input("Enter a phrase where you whant to count letters")

letter_dict = {}
all_letters = 'qwertyuiopasdfghjklzxcvbnm'

for letter in all_letters:
	letter_dict.setdefault(letter,[])
for letter in user_string:
	letter_dict.setdefault(letter,[]).append(letter)

pprint.pprint(letter_dict)