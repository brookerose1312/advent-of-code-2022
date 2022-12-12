## Part 1

# Read input
elevation = open("day12input.txt", "r", encoding="utf-8").read().strip().split("\n")

# build elevation map
starting_location = (0, 0)
end_location = (0, 0)
unvisited_nodes = []
visited_nodes = []
elevation_map = []
travel_dict = dict()
HEIGHT = len(elevation)
WIDTH = len(elevation[0])
for row_index, row in enumerate(elevation):
    elevation_row = []
    for col_index, col in enumerate(row):
        if col == "S":
            elevation_row.append(ord("a") - ord("a"))
            starting_location = (row_index, col_index)
        elif col == "E":
            elevation_row.append(ord("z") - ord("a"))
            end_location = (row_index, col_index)
        else:
            elevation_row.append(ord(col) - ord("a"))
        unvisited_nodes.append((row_index, col_index))
    elevation_map.append(elevation_row)

# build a list of travelable nodes to run Dijkstra's on
for row_index in range(HEIGHT):
    for col_index in range(WIDTH):
        visitable_nodes = []
        for y_movement in [-1, 0, 1]:
            for x_movement in [-1, 0, 1]:
                if (
                    0 <= row_index + y_movement < HEIGHT
                    and 0 <= col_index + x_movement < WIDTH
                    and abs(x_movement) + abs(y_movement) == 1
                ):
                    if (
                        elevation_map[row_index + y_movement][col_index + x_movement]
                        - elevation_map[row_index][col_index]
                        <= 1
                    ):
                        visitable_nodes.append(
                            (row_index + y_movement, col_index + x_movement)
                        )
        travel_dict[(row_index, col_index)] = visitable_nodes


class Dijkstra:
    def __init__(self, unvisited, visited, start_node, end_node, node_map):
        self.unvisited = []
        for node in unvisited:
            self.unvisited.append((node[0], node[1]))
        self.visited = []
        for node in visited:
            self.visited.append((node[0], node[1]))
        self.start_node = start_node
        self.end_node = end_node
        self.node_map = node_map
        self.node_distance = dict(zip(unvisited_nodes, [999] * (HEIGHT * WIDTH)))
        self.node_distance[start_node] = 0

    def visit_node(self, current_node):
        for node in self.node_map[current_node]:
            if node not in self.visited:
                if self.node_distance[current_node] + 1 < self.node_distance[node]:
                    self.node_distance[node] = self.node_distance[current_node] + 1
        self.unvisited.remove(current_node)
        self.visited.append(current_node)

    def run_dijkstras(self):
        while self.end_node not in self.visited:
            current_node = min(self.unvisited, key=self.node_distance.get)
            self.visit_node(current_node)
        return self.node_distance[self.end_node]


class DijkstraMultiple:
    def __init__(self, unvisited, visited, start_node, end_nodes, node_map):
        self.unvisited = []
        for node in unvisited:
            self.unvisited.append((node[0], node[1]))
        self.visited = []
        for node in visited:
            self.visited.append((node[0], node[1]))
        self.start_node = start_node
        self.end_nodes = end_nodes
        self.node_map = node_map
        self.node_distance = dict(zip(unvisited_nodes, [999] * (HEIGHT * WIDTH)))
        self.node_distance[start_node] = 0

    def visit_node(self, current_node):
        for node in self.node_map[current_node]:
            if node not in self.visited:
                if self.node_distance[current_node] + 1 < self.node_distance[node]:
                    self.node_distance[node] = self.node_distance[current_node] + 1
        self.unvisited.remove(current_node)
        self.visited.append(current_node)

    def run_dijkstras(self):
        while not set(self.end_nodes).issubset(set(self.visited)):
            current_node = min(self.unvisited, key=self.node_distance.get)
            self.visit_node(current_node)
        return self.node_distance


graph = Dijkstra(
    unvisited_nodes, visited_nodes, starting_location, end_location, travel_dict
)
print(graph.run_dijkstras())

## Part 2

part_two_travel_dict = {}


for row_index in range(HEIGHT):
    for col_index in range(WIDTH):
        visitable_nodes = []
        for y_movement in [-1, 0, 1]:
            for x_movement in [-1, 0, 1]:
                if (
                    0 <= row_index + y_movement < HEIGHT
                    and 0 <= col_index + x_movement < WIDTH
                    and abs(x_movement) + abs(y_movement) == 1
                ):
                    if (
                        elevation_map[row_index + y_movement][col_index + x_movement]
                        - elevation_map[row_index][col_index]
                        >= -1
                    ):
                        visitable_nodes.append(
                            (row_index + y_movement, col_index + x_movement)
                        )
        part_two_travel_dict[(row_index, col_index)] = visitable_nodes

possible_starting_locations = []

for row_index in range(HEIGHT):
    for col_index in range(WIDTH):
        if elevation_map[row_index][col_index] == 0:
            possible_starting_locations.append((row_index, col_index))

graph = DijkstraMultiple(
    unvisited_nodes,
    visited_nodes,
    end_location,
    possible_starting_locations,
    part_two_travel_dict,
)

final_distances = graph.run_dijkstras()
print(final_distances[min(possible_starting_locations, key=final_distances.get)])
