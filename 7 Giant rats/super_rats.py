

import time
import random
import statistics


GOAL = 50000
NUM_RATS = 20
INITIAL_MIN_WT = 200
INITIAL_MODE_WT = 300
INITIAL_MAX_WT = 600
MUTATE_ODDS = 0.01
MUTATE_MIN = 0.5
MUTATE_MAX = 1.2
LITTER_SIZE = 8
LITTERS_PER_YEAR = 10
GENERATION_LIMIT = 500

if NUM_RATS % 2 == 1:
    NUM_RATS += 1


def populate(num_rats, min_wt, max_wt, mode_wt):

    return[int(random.triangular(min_wt, max_wt, mode_wt)) for i in range(num_rats)]

def fitness(population, goal):

    avg = statistics.mean(population)
    return avg/goal

def select(population, to_retain):

    sorted_population = sorted(population) #acsending
    print(len(population)/2)
    to_retain_males = int(to_retain/2)
    member_per_sex = int(len(population)/2)
    females = sorted_population[:member_per_sex]
    males = sorted_population[member_per_sex:]
    selected_females = females[-to_retain_by_sex:]
    selected_males = males[-to_retain_by_sex:]
    return selected_males, selected_females



def breed(males, females, litter_size):
    random.shuffle(males)
    random.shuffle(females)
    children = []
    for male, female in zip(males, females):
        for child in range(litter_size):

            child =  random.randint(female, male)
            children.append(child)
    return children


def mutate(childeren, mutate_odds, mutate_min, mutate_max):
    for index, rat in enumerate(childeren):
        if mutate_odds >= random.random():
            childeren[index] = round(rat * random.uniform(mutate_min, mutate_max))
    return childeren


def main():

    parents = populate(NUM_RATS, INITIAL_MIN_WT, INITIAL_MAX_WT, INITIAL_MODE_WT)
    generations = 0
    print(f"starting weigths of population = {parents}")
    popl_fitness = fitness(parents, GOAL)
    print(f" population fitness in the begining {popl_fitness}")

    ave_wt = []

    while popl_fitness < 1 and generations < GENERATION_LIMIT:
        selected_males, selected_females = select(parents, NUM_RATS)
        children = breed(selected_males,selected_females, LITTER_SIZE)
        children =mutate(children,MUTATE_ODDS, MUTATE_MIN, MUTATE_MAX)
        parents = selected_females + selected_males + children
        popl_fitness = fitness(parents, GOAL)
        print(f" Приспособленность поколения {generations}, {popl_fitness:.4f}")
        ave_wt.append(int(statistics.mean(parents)))
        generations += 1

        print(f"Average weight {ave_wt}")
        print(f"\n number of generations {generations}")
        print(f"\n number of yeats  {int(generations/LITTERS_PER_YEAR)}")


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print(f" time of excecution { duration}")