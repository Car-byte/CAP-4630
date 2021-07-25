import random
import math

class Ant:
  def __init__(self, num_cities, random_city_factor, alpha, beta, distance_list):
    self.visited = []
    # Pick start city randomly
    self.visited.append(random.randint(0, num_cities -1))
    self.random_city_factor = random_city_factor
    self.num_cities = num_cities
    self.alpha = alpha
    self.beta = beta
    self.distance_list = distance_list
  
  def visit_city(self, pheromone_trails):
    # Randomly choose to visit a city randomly or probabilistically
    if random.random() < self.random_city_factor:
      self.visited.append(self.visit_random_city())
    else:
      probabilities = self.visit_city_probabilisticly(pheromone_trails)
      self.visited.append(self.roulette_wheel_selection(probabilities))

  def visit_random_city(self):
    all_cities = set(range(0, self.num_cities))
    possible = all_cities - set(self.visited)
    return random.randint(0, len(possible) - 1)

  def visit_city_probabilisticly(self, pheromone_trails):
    current_city = self.visited[len(self.visited) - 1]
    all_cities = set(range(0, self.num_cities))
    possible_cities = all_cities - set(self.visited)
    possible_indexes = []
    probabilities = []
    total_probability = 0
    for city in possible_cities:
      possible_indexes.append(city)
      pheromones = math.pow(pheromone_trails[current_city][city], self.alpha)
      heuristic_val = math.pow(1 / self.distance_list[current_city][city], self.beta)
      probability = pheromones * heuristic_val
      probabilities.append(probability)
      total_probability += probability
    probabilities = [probability / total_probability for probability in probabilities]
    return [possible_indexes, probabilities, len(possible_cities)]

  def roulette_wheel_selection(self, probabilities):
    possibilites = []
    total = 0
    possible_indexes = probabilities[0]
    possible_probabilities = probabilities[1]
    possible_city_count = probabilities[2]
    for i in range(possible_city_count):
      possibilites.append([possible_indexes[i], total, total + possible_probabilities[i]])
      total += possible_probabilities[i]
    spin = random.random()
    result = 0
    for i in range(len(possibilites)):
      if possibilites[i][1] < spin and possibilites[i][2] >= spin:
        result = possibilites[i][0]
        break
    return result

  def get_distance_travelled(self):
    total_distance = 0
    for i in range(1, len(self.visited)):
      total_distance += self.distance_list[self.visited[i]][self.visited[i - 1]]
    total_distance += self.distance_list[self.visited[0]][self.visited[len(self.visited) - 1]]
    return total_distance


class Aco:
  def __init__(self, num_ants_factor, alpha, beta):
    self.num_ants_factor = num_ants_factor
    self.colony = []
    self.pheromone_trails = []
    self.best_dist = math.inf
    self.best_ant = None
    self.alpha = alpha
    self.beta = beta

  def ants_setup(self, num_ants_factor, num_cities, random_city_factor, distance_list):
    num_ants = int(num_ants_factor * num_cities)
    self.colony.clear()
    for i in range(num_ants):
      self.colony.append(Ant(num_cities, random_city_factor, self.alpha, self.beta, distance_list))

  def pheromone_setup(self, distance_list):
    for i in range(len(distance_list)):
      pheromones = []
      for i in range(len(distance_list)):
        pheromones.append(1)
      self.pheromone_trails.append(pheromones)
  
  def move_ants(self, population):
    for ant in population:
      ant.visit_city(self.pheromone_trails)
  
  def get_best_ant(self, colony):
    for ant in colony:
      dist = ant.get_distance_travelled()
      if dist < self.best_dist:
        self.best_ant = ant
        self.best_dist = dist
    return self.best_ant

  def pheromone_update(self, evaporation_rate, num_cities):
    for i in range(num_cities):
      for j in range(num_cities):
        # Decrease pheromone_trail
        self.pheromone_trails[i][j] = self.pheromone_trails[i][j] * evaporation_rate
        # Update for every ant
        for ant in self.colony:
          self.pheromone_trails[i][j] += .3

  def solve(self, iterations, evaporation_rate, num_cities, distance_list, num_ant_factor, random_city_factor):
    self.pheromone_setup(distance_list)
    for i in range(1, iterations + 1):
      # create ants for this itteration
      self.ants_setup(num_ant_factor, num_cities, random_city_factor, distance_list)
      for j in range(num_cities - 1):
        self.move_ants(self.colony)
      self.pheromone_update(evaporation_rate, num_cities)
      self.best_ant = self.get_best_ant(self.colony)
      if i == 1 or i % (iterations / 10) == 0:
        print("Iterations #:", i, "\tFastest Path:", self.best_ant.get_distance_travelled())
    return self.best_ant
    

class City:
  def __init__(self, x, y):
    self.x = x
    self.y = y


# Used for visualization of paths

# def print_cities(ant, cities):
#   f = open("data.txt", "w")
#   path = []
#   for i in range(200):
#     temp = []
#     for j in range(200):
#       temp.append('.')
#     path.append(temp)
#   for i in range(len(ant.visited)):
#     city = cities[ant.visited[i]]
#     path[city.x][city.y] = i
#   for i in range(len(path)):
#     for j in range(len(path[i])):
#       f.write(str(path[i][j]))
#     f.write("\n")
#   f.close()


def setup_map(distance_list, num_cities):
  cities = []
  for i in range(num_cities):
    city = City(random.randint(0, 200), random.randint(0, 200))
    cities.append(city)
    distance_list.append([i]) # use index instead of city
  # calculate distances 
  # small pitfall is that they are calculated twice
  for i in range(len(cities)):
    for j in range(len(cities)):
      if i != j:
        x = (cities[i].x - cities[j].x) ** 2
        y = (cities[i].y - cities[j].y) ** 2
        distance_list[i].append(math.sqrt(x + y))


SEED = 9
random.seed(SEED)
NUM_CITIES = 25
NUM_ANT_FACTOR = .2 # how many ants we have
ITERATIONS = 10000 # stopping condition
EVAPORATION_RATE = .6 # factor for decrease in pheromone_trails
RANDOM_CITY_FACTOR = .5 # halve the time pick random city halve spin wheel
ALPHA = 5
BETA = 8


if __name__ == "__main__":
  distance_list = []
  setup_map(distance_list, NUM_CITIES)
  aco = Aco(NUM_ANT_FACTOR, ALPHA, BETA)
  best_ant = aco.solve(ITERATIONS, EVAPORATION_RATE, NUM_CITIES, distance_list, NUM_ANT_FACTOR, RANDOM_CITY_FACTOR)
  print("\n-----------------------------------------------------------------\n")
  print("Number of Itterations:", ITERATIONS, "\tRandom Number Seed:", SEED)
  print("Best path discovered:", best_ant.get_distance_travelled())
