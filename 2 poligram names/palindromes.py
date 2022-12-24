import loadDictionary
"""
word_list  = loadDictionary.load("2of12.txt")
pali_list = []

for word in  word_list:
	if len(word) >1 and word == word[::-1]:
		pali_list.append(word)

print(f"\nNumber of found polindromes{len(pali_list)}\n")
print(*pali_list,sep = '\n' ) # * - gets all arguments from a list
"""
# find polindromes with recursion

def is_polindrome(word, i):
	if (i > len(word)/2):
		print('tatei')
		return True

	ans = False
	if (word[i] == word[len(word)-i-1] and is_polindrome(word, i+1)):
		ans = True
	print(ans)
	return(ans)
is_polindrome("tatat", 0)