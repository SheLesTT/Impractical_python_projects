import random
from random import randint
from collections import Counter
import  numpy as np
import  matplotlib.pyplot as plt

NUM_EQUIV_VOLUMES = 1000
MAX_CIVS = 5000
TRIALS = 500
CIV_STEP_SIZE =100

x = []
y = []

for num_civs in range(2, MAX_CIVS + 2, CIV_STEP_SIZE):
    civs_per_vol = num_civs/ NUM_EQUIV_VOLUMES
    num_single_civs = 0

    for trial in range(TRIALS):
        locations = []
        while len(locations) < num_civs:
            location = random.randint(1, NUM_EQUIV_VOLUMES)
            locations.append(location)
        overlap_count = Counter(locations)
        overlap_rollup = Counter(overlap_count.values())
        num_single_civs += overlap_rollup[1]

    prob = 1 - (num_single_civs / (num_civs * TRIALS))

    print(f"civilization for volume {civs_per_vol}, probability of encounter {prob}")

    x.append(civs_per_vol)
    y.append(prob)


coefficients = np.polyfit(x,y,4)
p = np.poly1d(coefficients)
print("\n{}".format(p))
xp = np.linspace(0,5)
_ = plt.plot(x,y,'.',xp,p(xp),'-')
plt.ylim(-0.5,1.5)
plt.show()