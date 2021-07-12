import math
import random

INDIVIDUAL_INDEX = 0
FITNESS_INDEX = 1
PROBABILITY_INDEX = 2

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Country:
    def __init__(self, num_cities = 25):
        self.cities = []
        for i in range(num_cities):
            temp = City(random.randint(0, 200), random.randint(0, 200))
            self.cities.append(temp)


def generate_init_population(country, size):
    population = []
    for i in range(size):
        temp = country.cities.copy()
        random.shuffle(temp)
        population.append([temp, 0, 0])
    return population


def calculate_population_fitness(population):
    best_fitness = math.inf
    fitness_sum = 0
    for individual in population[:]:
        fitness = 0

        # By not recalculating fitness, we cut runtime in almost halve
        if individual[FITNESS_INDEX] == 0: #  new item
            fitness = calculate_individual_fitness(individual[INDIVIDUAL_INDEX])
            individual[FITNESS_INDEX] = fitness
        else: # we allready calculated fitness
            fitness =individual[FITNESS_INDEX]

        fitness_sum += fitness
        if fitness < best_fitness:
            best_fitness = fitness        
    average = fitness_sum / len(population)

    # cut some out of population that is below average
    for individual in population[:]:
        if individual[FITNESS_INDEX] > average:
            population.remove(individual)
    return best_fitness


# fitness will be length to travel to all cities based on the path (lower is better)
def calculate_individual_fitness(individual):
    total = 0
    for i in range(len(individual) - 1):
        x = (individual[i].x - individual[i + 1].x) ** 2
        y = (individual[i].y - individual[i + 1].y) ** 2
        total += math.sqrt(x + y)
    return total


def roulette_wheel_selection(population, num_selections):
    set_probabilities(population)
    slices = []
    total = 0
    for i in range(len(population)):
        slices.append([i, total, population[i][PROBABILITY_INDEX]])
        total += population[i][PROBABILITY_INDEX]
    chosen = []
    for i in range(num_selections):
        rand_num = random.random()
        result = [s[0] for s in slices if s[1] <= s[2]]
        chosen.append(population[result[0]])
    return chosen


def set_probabilities(population):
    population_sum = 0
    for i in range(len(population)):
        population_sum += population[i][FITNESS_INDEX]
    new_sum = 0
    for i in range(len(population)):
        population[i][PROBABILITY_INDEX] = population[i][PROBABILITY_INDEX] /population_sum
        population[i][PROBABILITY_INDEX] = 1 - population[i][PROBABILITY_INDEX]
        new_sum += population[i][PROBABILITY_INDEX]


def reproduce_children(chosen):
    children = []
    for i in range(len(chosen)//2 - 1):
        children += breed(chosen[i][INDIVIDUAL_INDEX], chosen[i + 1][INDIVIDUAL_INDEX])
    return children


def breed(parent1, parent2):
    gene1 = int((random.random() * len(parent1)))
    gene2 = int((random.random() * len(parent1)))
    start = min(gene1, gene2)
    end = max(gene1, gene2)
    child1 = []
    child2 = []
    for i in range(start, end):
        child1.append(parent1[i])
        child2.append(parent2[i])

    child1_missing = [city for city in parent2 if city not in child1]
    child2_missing = [city for city in parent1 if city not in child2]
    return [[child1 + child1_missing, 0, 0], [child2 + child2_missing, 0, 0]]


def mutate(children, max_index):
    for child in children:
        random2 = random.randint(0, max_index)
        random1 = random.randint(0, max_index)
        temp = child[INDIVIDUAL_INDEX][random1]
        child[INDIVIDUAL_INDEX][random1] = child[INDIVIDUAL_INDEX][random2]
        child[INDIVIDUAL_INDEX][random2] = temp


#### THIS WAS FOR VISUALIZATION  OF THE PATHS 
#### IN A TXT EDITOR WE COULD SEE THE GROUPINGS OF CITIES 
#### AND THE ORDER PICKED BY THE ALGORITHM

# def get_best_path(population):
#     best_path = []
#     best_fitness = math.inf
#     for i in range(len(population)):
#         if population[i][FITNESS_INDEX] < best_fitness:
#             best_fitness = population[i][FITNESS_INDEX]
#             best_path = population[i][INDIVIDUAL_INDEX]
#     return best_path

# def print_path(cities):
#     path = []
#     for i in range(200):
#         temp = []
#         for j in range(200):
#             temp.append(".")
#         path.append(temp)
#     for i in range(len(cities)):
#         path[cities[i].y][cities[i].x] = i
#     f = open("data.txt", "w")
#     for i in range(len(path)):
#         for j in range(len(path[i])):
#             f.write(str(path[i][j]))
#         f.write("\n")
#     f.close()

NUM_GENERATIONS = 500
INITIAL_POPULATION_SIZE = 1000
MAX_MUTATION_INDEX = 24 # should be between 0 and number of cities - 1
SEED = 5
random.seed(SEED) # seed random number generator

if __name__ == "__main__":
    global_best_fitness = math.inf
    country = Country()
    global_population = generate_init_population(country, INITIAL_POPULATION_SIZE)
    for i in range(NUM_GENERATIONS):
        local_best_fitness = calculate_population_fitness(global_population)
        global_best_fitness = min(global_best_fitness, local_best_fitness)
        chosen = roulette_wheel_selection(global_population, 100) 
        children = reproduce_children(chosen)
        mutate(children, MAX_MUTATION_INDEX)
        global_population = global_population + children # append children to global population
    print("Random number seed:", SEED)
    print("Number of generations:", NUM_GENERATIONS)
    print("Initial population size:", INITIAL_POPULATION_SIZE)
    print("Best gloabal fitness (lower is better):", global_best_fitness)