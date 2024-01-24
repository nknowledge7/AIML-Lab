import heapq

def a_star_search(graph, start, goal, heuristic):
    open_list = [(0, start)]
    closed_set = set()
    g_score = {location: float('inf') for location in graph}
    g_score[start] = 0

    while open_list:
        current_g, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return g_score[goal]

        if current_node in closed_set:
            continue

        closed_set.add(current_node)

        for neighbor, distance in graph[current_node].items():
            tentative_g = g_score[current_node] + distance

            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    return float('inf')

example_map = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 4},
    'C': {'A': 3, 'D': 7, 'E': 8},
    'D': {'B': 4, 'C': 7, 'E': 2},
    'E': {'C': 8, 'D': 2, 'F': 6},
    'F': {'E': 6},
}

heuristic = {
    'A': 8,
    'B': 7,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 0
}

start_location = 'A'
goal_location = 'F'
shortest_distance = a_star_search(example_map, start_location, goal_location, heuristic)

if shortest_distance < float('inf'):
    print(f"The shortest distance from {start_location} to {goal_location} is {shortest_distance}.")
else:
    print(f"No path found from {start_location} to {goal_location}.")


