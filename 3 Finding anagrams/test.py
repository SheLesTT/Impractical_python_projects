from itertools import permutations

perms = {''.join(i) for i in permutations('tere') }
terms = set()
for i in permutations('tere'):
    terms.add(''.join(i))
print(perms)
print(terms)