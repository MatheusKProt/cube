import itertools
import time
from queue import PriorityQueue


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
        print(f'Algorithm: {self.algorithm}')
        print(f'Start: {time.strftime("%H:%M:%S %d/%m/%Y", time.localtime())}')
        if self.algorithm == 'BFS':
            result = self.BFS()
        elif self.algorithm == 'IDFS':
            result = self.IDFS()
        elif self.algorithm == 'UCS':
            result = self.UCS()
        elif self.algorithm == 'A*':
            result = self.ASTAR()
        end = time.time()
        print(f'Total time: {end - start} seconds')
        print(f'Nodes visited: {self.num_visited}')
        self.problem.print_sequence(result)

    def BFS(self):
        queue = ['']
        while queue:
            self.num_visited += 1
            path = queue.pop(0)

            for neighbour in self.problem.successors():
                new_path = f'{path}{neighbour},'
                if new_path not in queue:
                    queue.append(new_path)
                if self.problem.is_target(new_path):
                    return new_path

    def IDFS(self):
        for depth in itertools.count():
            route, remaining = self.DFS('', depth)
            if route:
                return route
            elif not remaining:
                return None

    def DFS(self, route, depth):
        self.num_visited += 1

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

    def UCS(self):
        queue = PriorityQueue()
        queue.put((0, ''))

        while queue:
            self.num_visited += 1
            cost, path = queue.get()

            for neighbour in self.problem.successors():
                new_path = f'{path}{neighbour},'
                queue.put((cost + 1, new_path))

                if self.problem.is_target(new_path):
                    return new_path

    def heuristic(self):
        total = 0
        for right in self.problem.cube['R']:
            for r in right:
                if r != 'red   ':
                    total += 1
        for left in self.problem.cube['L']:
            for l in left:
                if l != 'orange':
                    total += 1
        for front in self.problem.cube['F']:
            for f in front:
                if f != 'blue  ':
                    total += 1
        for back in self.problem.cube['B']:
            for b in back:
                if b != 'green ':
                    total += 1
        for up in self.problem.cube['U']:
            for u in up:
                if u != 'yellow':
                    total += 1
        for down in self.problem.cube['D']:
            for d in down:
                if d != 'white ':
                    total += 1
        return total

    def ASTAR(self):
        queue = PriorityQueue()
        queue.put((0, ''))
        cost_so_far = {'': 0}

        while queue:
            self.num_visited += 1
            cost, path = queue.get()

            for neighbour in self.problem.successors():
                new_path = f'{path}{neighbour},'
                new_cost = cost + 1

                if self.problem.is_target(new_path):
                    return new_path

                if neighbour not in cost_so_far or new_cost < cost_so_far[new_path]:
                    cost_so_far[new_path] = new_cost
                    priority = new_cost + self.heuristic()
                    queue.put((priority, new_path))

