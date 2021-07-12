from country import City
from country import Romania
from country import Connection
from country import print_itinerary
import math

# breadth first search
def bfs(country, start):
    queue = [country.cities[start]]
    visited_nodes = set()

    while queue:
        current = queue.pop(0)
        if current not in visited_nodes:
            visited_nodes.add(current)
            connections = current.neighbors
            for path in connections:
                queue.append(country.cities[path.name])
                length = path.length
                if current.length_from_start_search != math.inf: # if not first node
                    length += current.length_from_start_search
                if length < country.cities[path.name].length_from_start_search and path.name != start: # if better connection
                    country.cities[path.name].length_from_parent = path.length
                    country.cities[path.name].length_from_start_search = length
                    country.cities[path.name].parent = current


if __name__ == "__main__":
  romania = Romania()
  destination = "Bucharest"
  start = "Oradea"
  bfs(romania, start)
  print_itinerary(romania, destination, start)
