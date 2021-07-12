from country import City
from country import Romania
from country import Connection
from country import print_itinerary


# checks if there is a conflict in the queue
def queue_conflict(queue, f_val, name):
    for item in queue:
        if item.name == name and f_val >= item.a_star_val:
            return True
    return False


def a_star(country, destination, start):
    queue = [country.cities[start]] # use as priority queue
    visited_nodes = set()
    nodes_in_queue = { country.cities[start] }

    while queue:
        current = queue.pop(0)
        nodes_in_queue.remove(current)
        if current not in visited_nodes:
            visited_nodes.add(current)
            if current.name == destination:
                return
            else:
                connections = current.neighbors
                for path in connections:
                   if country.cities[path.name] not in visited_nodes:
                        a_star_val = country.cities[path.name].heuristic
                        a_star_val += path.length
                        a_star_val += current.length_from_start
                        if not queue_conflict(queue, a_star_val, path.name): # update all the nodes state
                            country.cities[path.name].parent = current
                            country.cities[path.name].length_from_start = path.length + current.length_from_start
                            country.cities[path.name].a_star_val = a_star_val
                            country.cities[path.name].length_from_parent = path.length
                            if country.cities[path.name] not in nodes_in_queue: #if not in queue add to queue
                                queue.append(country.cities[path.name])
                                nodes_in_queue.add(country.cities[path.name])
        queue.sort(key=lambda x: x.a_star_val) # sort the queue so that best nodes are in the front



if __name__ == "__main__":
  romania = Romania()
  destination = "Bucharest"
  start = "Oradea"
  a_star(romania, destination, start)
  print_itinerary(romania, destination, start)
