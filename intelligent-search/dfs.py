from country import City
from country import Romania
from country import Connection
from country import print_itinerary
import math


# defs_helper just runs basic dfs
def dfs_helper(country, visited_nodes, start):
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited_nodes:
            visited_nodes.add(current)
            connections = current.neighbors
            for path in connections:
                stack.append(country.cities[path.name])
                length = path.length
                if current.length_from_start_search != math.inf:
                    length += current.length_from_start_search
                if length < country.cities[path.name].length_from_start_search and country.cities[path.name] != start: # if better path
                    country.cities[path.name].length_from_parent = path.length
                    country.cities[path.name].length_from_start_search = length
                    country.cities[path.name].parent = current


# depth first search with a helper function that performs depth first search
# in order to get best answer we run dfs on every node
def dfs(country, start):
    stack = [country.cities[start]]
    visited_nodes = set()

    while stack:
        current = stack.pop()
        if current not in visited_nodes:
            connections = current.neighbors
            visited_nodes_copy = set()
            for item in visited_nodes: # visited nodes for dfs helper function
                visited_nodes_copy.add(item)
            dfs_helper(country, visited_nodes_copy, current) # run dfs on every path possible
            for path in connections:
                stack.append(country.cities[path.name])
            visited_nodes.add(current)


if __name__ == "__main__":
  romania = Romania()
  destination = "Bucharest"
  start = "Oradea"
  dfs(romania, start)
  print_itinerary(romania, destination, start)
