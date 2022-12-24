# need to add gender for rats


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
    population = []
    weights = []
    for counter in range(num_rats):
        population.append([int(random.triangular(min_wt, max_wt, mode_wt))])
    population.sort(key = lambda population:population[0])
    for rat in population[-4:]:
        rat.append(1)
    for rat in population[0:16]:
        rat.append(0)
    return population

        #population[counter][1] = int(random.randint(0,1))



def fitness(population, goal):
    weights = []
    for rat in population:
        weights.append(rat[0])
    avg_wt = statistics.mean(weights)

    fitness = avg_wt/goal
    return fitness


def breed(males_selected, females_selected,litter_size):
    random.shuffle(males_selected)
    random.shuffle(females_selected)
    children = []

    for male, female in zip(males_selected, females_selected):
        for child in range(litter_size):
            children.append([0, random.randint(0,1)])
    for child in children:
        if child[1] == 0:
            child[0] = random.randint(female, male) - 50
        else:
            child[0] = random.randint(female, male)

    return children


def select(population, retain_males):
    population.sort(key = lambda population:population[0])
    print('population ', population)
    males  = population[-retain_males: ]
    females = population[-(2*retain_males+1): - retain_males ]
    print('females: ', females)
    print('males: ', males)

    return males, females

def mutate_children(mutation_odds, mutate_min, mutate_max, children):
    for child in children:
        a = random.random()
        if a < mutation_odds:
            child[0] *= random.uniform(mutate_min,mutate_max)

    return  children


def main():

    parents = populate(NUM_RATS,INITIAL_MIN_WT,INITIAL_MAX_WT, INITIAL_MODE_WT)
    print('parents: ', parents)
    fitness_gen = fitness(parents, GOAL)
    males_selected = parents[-4:]
    females_selected = parents[-9:-4]

    generations = 1
    ave_wt = []
    while generations <= 4:
        children = breed(males_selected, females_selected, LITTER_SIZE)
        children = mutate_children(MUTATE_ODDS,MUTATE_MIN,MUTATE_MAX,children)
        parents = children + males_selected + females_selected
        print(children)
        print(parents)
        fitness_gen = fitness(parents, GOAL)
        males_selected, females_selected = select(parents, 4)
        print(('teetet',males_selected, females_selected))

       # ave_wt.append(int(statistics.mean(parents[0])))
        generations += 1

        #print(f"Average weight {ave_wt}")
        print(f"\n number of generations {generations}")
        print(f"\n number of yeats  {int(generations/LITTERS_PER_YEAR)}")


main()