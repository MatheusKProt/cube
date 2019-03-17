def bfs_shortest_path(graph, start, goal):
    explored = []
    queue = [[start]]

    if start == goal:
        return "That was easy! Start = goal"

    while queue:
        path = queue.pop(0)
        node = path[-1]
        print()
        print(explored)
        if node not in explored:
            neighbours = graph[node]
            print(neighbours)
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path

            explored.append(node)

    return "So sorry, but a connecting path doesn't exist :("


graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F', 'G'],
         'D': ['H', 'I'],
         'E': ['J', 'K'],
         'F': [],
         'G': [],
         'H': [],
         'I': [],
         'J': [],
         'k': []}
print(bfs_shortest_path(graph, 'A', 'J'))  # returns ['G', 'C', 'A', 'B', 'D']
