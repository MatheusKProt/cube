class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


class Solver:
    def __init__(self, problem, algorithm='BFS'):
        self.num_visited = 0
        self.algorithm = algorithm
        self.problem = problem

    def solve(self):
        if self.algorithm == 'BFS':
            return self.BFS()
        elif self.algorithm == 'DFS':
            return self.DFS()
        elif self.algorithm == 'IDFS':
            exit(1)
        elif self.algorithm == 'UCS':
            exit(1)
        elif self.algorithm == 'A*':
            return self.MEU()

    def BFS(self):
        queue = [['']]
        explored = []

        while queue:
            self.num_visited += 1
            path = queue.pop(0)
            node = path[-1]

            for neighbour in self.problem.successors():
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if self.problem.is_target(new_path[1:]):
                    print(f'Solution found! {self.num_visited} nodes visited')
                    return new_path[1:]

            explored.append(node)

        return "So sorry, but a connecting path doesn't exist :("

    def DFS(self):
        queue = [['']]
        explored = []

        while queue:
            self.num_visited += 1
            path = queue.pop(len(queue) - 1)
            node = path[-1]

            for neighbour in self.problem.successors():
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if self.problem.is_target(new_path[1:]):
                    print(f'Solution found! {self.num_visited} nodes visited')
                    return new_path[1:]

            explored.append(node)

        return "So sorry, but a connecting path doesn't exist :("
