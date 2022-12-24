from itertools import  permutations, product
import numpy as np

results = []
columns = [1,2,3,4]

for perm in permutations(columns):
    for i in product([1,-1], repeat = 4):
        for k, sign in zip(perm,i):
            results.append(k*sign)
print(len(results)/4)