import math

# defines a city with all the atributes needed
class City:
    def __init__(self, name, heuristic):
        self.heuristic = heuristic
        self.name = name
        self.parent = None
        self.neighbors = []
        self.length_from_start = 0
        self.a_star_val = None # a_star_val = length_from_start + heuristic
        self.length_from_parent = None
        self.length_from_start_search = math.inf # used for bfs and dfs
    
    def add_connection(self, name, length):
        self.neighbors.append(Connection(name, length))


# defines a connection between two cities, used in queues and stacks
class Connection:
    def __init__(self, name, length):
        self.name = name
        self.length = length


# defines the graph which we will traverse
class Romania:
    def __init__(self):
        Oradea = City('Oradea', 380)
        Zerind = City('Zerind', 374)
        Arad = City('Arad', 366)
        Timisoara = City('Timisoara', 329)
        Lugoj = City('Lugoj', 244)
        Mehadia = City('Mehadia', 241)
        Dobreta = City('Dobreta', 242)
        Craiova = City('Craiova', 160)
        Rimnicu_Vilcea = City('Rimnicu Vilcea', 193)
        Sibiu = City('Sibiu', 253)
        Fagaras = City('Fagaras', 178)
        Pitesti = City('Pitesti', 98)
        Bucharest = City('Bucharest', 0)
        Giurgiu = City('Giurgiu', 77)
        Urziceni = City('Uziceni', 80)
        Hirsova = City('Hirsova', 151)
        Eforie = City('Eforie', 161)
        Vaslui = City('Vaslui', 199)
        Iasi = City('Iasi', 226)
        Neamt = City('Neamt', 234)
        Oradea.add_connection('Sibiu', 151)
        Oradea.add_connection('Zerind', 71)
        Zerind.add_connection('Arad', 75)
        Zerind.add_connection('Oradea', 71)
        Arad.add_connection('Sibiu', 140)
        Arad.add_connection('Timisoara', 118)
        Arad.add_connection('Zerind', 75)
        Timisoara.add_connection('Arad', 118)
        Timisoara.add_connection('Lugoj', 111)
        Lugoj.add_connection('Mehadia', 70)
        Lugoj.add_connection('Timisoara', 111)
        Mehadia.add_connection('Dobreta', 75)
        Mehadia.add_connection('Lugoj', 70)
        Dobreta.add_connection('Mehadia', 75)
        Dobreta.add_connection('Craiova', 120)
        Craiova.add_connection('Dobreta', 120)
        Craiova.add_connection('Rimnicu Vilcea', 146)
        Craiova.add_connection('Pitesti', 138)
        Rimnicu_Vilcea.add_connection('Sibiu', 80)
        Rimnicu_Vilcea.add_connection('Craiova', 146)
        Rimnicu_Vilcea.add_connection('Pitesti', 97)
        Sibiu.add_connection('Rimnicu Vilcea', 80)
        Sibiu.add_connection('Oradea', 151)
        Sibiu.add_connection('Arad', 140)
        Sibiu.add_connection('Fagaras', 99)
        Fagaras.add_connection('Sibiu', 99)
        Fagaras.add_connection('Bucharest', 211)
        Pitesti.add_connection('Rimnicu Vilcea', 97)
        Pitesti.add_connection('Craiova', 138)
        Pitesti.add_connection('Bucharest', 101)
        Bucharest.add_connection('Pitesti', 101)
        Bucharest.add_connection('Fagaras', 211)
        Bucharest.add_connection('Giurgiu', 90)
        Bucharest.add_connection('Urziceni', 85)
        Giurgiu.add_connection('Bucharest', 90)
        Urziceni.add_connection('Bucharest', 85)
        Urziceni.add_connection('Hirsova', 98)
        Urziceni.add_connection('Vaslui', 142)
        Hirsova.add_connection('Urziceni', 98)
        Hirsova.add_connection('Eforie', 86)
        Eforie.add_connection('Hirsova', 86)
        Vaslui.add_connection('Urziceni', 142)
        Vaslui.add_connection('Iasi', 92)
        Iasi.add_connection('Vaslui', 92)
        Iasi.add_connection('Neamt', 87)
        Neamt.add_connection('Iasi', 87)
        self.cities = {'Oradea': Oradea, 'Zerind': Zerind, 'Arad': Arad, 'Timisoara': Timisoara, 'Lugoj': Lugoj, 
        'Mehadia': Mehadia, 'Dobreta': Dobreta, 'Craiova': Craiova, 'Rimnicu Vilcea': Rimnicu_Vilcea, 'Sibiu': Sibiu, 
        'Fagaras': Fagaras, 'Pitesti': Pitesti, 'Bucharest': Bucharest, 'Giurgiu': Giurgiu, 'Urziceni': Urziceni, 
        'Hirsova': Hirsova, 'Eforie': Eforie, 'Vaslui': Vaslui, 'Iasi': Iasi, 'Neamt': Neamt}


# prints the path defined by the algorithms
def print_itinerary(country, destination, start):
    itinerary = []
    temp = country.cities[destination]
    while temp.parent != None and temp.name != start: # traverse path starting from destination
        itinerary.append(temp)
        temp = temp.parent
    print("Starting from", temp.name)
    total_length = 0
    for city in reversed(itinerary): # we need to go in reversed since we started itinerary from the destination
        length = city.length_from_parent
        total_length += length
        parent = city.parent
        print("Moving from", parent.name, "to", city.name, "with length of", length)
    print("Arrived at destination:", destination)
    print("Total length of trip:", total_length)