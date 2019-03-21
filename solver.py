import itertools
import time


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
        result = Node
        start = time.time()
        print(f'Inicio do {self.algorithm}: {time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())}')
        if self.algorithm == 'BFS':
            result = self.BFS()
        elif self.algorithm == 'IDFS':
            result = self.IDFS()
        elif self.algorithm == 'UCS':
            exit(1)
        elif self.algorithm == 'A*':
            exit(1)
        end = time.time()
        print('Tempo total:', end - start)
        return result

    def BFS(self):
        queue = ['']
        explored = []
        while queue:
            self.num_visited += 1
            path = queue.pop(0)
            node = path
            for neighbour in self.problem.successors():
                new_path = path
                new_path += str(neighbour) + ','
                if new_path not in queue:
                    queue.append(new_path)
                if self.problem.is_target(new_path):
                    print(f'Solution found! {self.num_visited} nodes visited')
                    return new_path
            explored.append(node)

        return "So sorry, but a connecting path doesn't exist :("

    def IDFS(self):
        for depth in itertools.count():
            route, remaining = self.DFS('', depth)
            if route:
                return route
            elif not remaining:
                return None

    def DFS(self, route, depth):
        if depth == 0:
            if self.problem.is_target(route):
                return route, True
            else:
                return None, True
        any_remaining = False
        for move in self.problem.successors():
            found, remaining = self.DFS(route + move + ',', depth - 1)
            if found:
                return found, True
            if remaining:
                any_remaining = True
        return None, any_remaining
