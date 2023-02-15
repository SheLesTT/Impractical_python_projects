import random


def fitness(combo, attempt):
    """Check how many keys satisfie pasword"""
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1

    return grade


def main():
    combo = '6758354753'

    list_combo = []
    for i in combo:
        list_combo.append(int(i))

    # generating with zeroes everywhere
    key = []
    for i in range(10):
        key.append(0)
    # digits we didn't guess yet
    to_guess = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  #

    key_fitnes = fitness(list_combo, key)
    tata = True
    gen = 0

    while tata:
        val = random.randint(0, 9)
        pos = random.choice(to_guess)
        attempt = key
        attempt[pos] = val

        att_fitnes = fitness(list_combo, attempt)
        # if new guess fits better change current fitness, key and digits yet to guess
        if (att_fitnes > key_fitnes):
            key_fitnes = att_fitnes
            key = attempt
            to_guess.remove(pos)

        if (att_fitnes == 10):
            tata = False
        gen += 1

    print((gen))
    print(key)


main()
