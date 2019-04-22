import itertools
import time
from queue import PriorityQueue


def save(algorithm, total_time, nodes, n, sequence, start_time, max_mem, depth):
    dados = {
        'algorithm': algorithm,
        'sequence': sequence,
        'time': total_time,
        'nodes': nodes,
        'memory': max_mem,
        'depth': depth
    }
    file = open(f'results/{start_time}/{n}.txt', 'a')
    file.write(str(dados) + "\n")

    file.close()


class Solver:
    def __init__(self, problem, algorithm='BFS', time_limit=float('inf'), start_time=0):
        self.num_visited = 0
        self.algorithm = algorithm
        self.problem = problem
        self.time_limit = time_limit
        self.start_time = start_time
        self.start = 0
        self.max_mem = -1

    def solve(self):
        result = None
        self.start = time.time()
        if self.algorithm == 'BFS':
            result = self.BFS()
        elif self.algorithm == 'IDFS':
            result = self.IDFS()
        elif self.algorithm == 'UCS':
            result = self.UCS()
        elif self.algorithm == 'A* 0':
            result = self.ASTAR(0)
        elif self.algorithm == 'A* 1':
            result = self.ASTAR(1)
        end = time.time()
        if result == 'TimeOut':
            save(self.algorithm, -1, -1, self.problem.n, -1, self.start_time, -1, str(self.problem.sequence).count(","))
        else:
            save(self.algorithm, end - self.start, self.num_visited, self.problem.n, self.problem.sequence[:-1], self.start_time, self.max_mem, str(self.problem.sequence).count(","))

    def print_nodes(self):
        pass
        # print(f'\rNodes visited: {self.num_visited}', end='')

    def BFS(self):
        queue = ['']
        while queue:
            if (time.time() - self.start) > self.time_limit:
                return 'TimeOut'
            self.print_nodes()
            self.num_visited += 1
            if self.max_mem < len(queue):
                self.max_mem = len(queue)
            path = queue.pop(0)

            for neighbour in self.problem.successors():
                new_path = f'{path}{neighbour},'
                if new_path not in queue:
                    queue.append(new_path)
                if self.problem.is_target(new_path):
                    return new_path

    def IDFS(self):
        for depth in itertools.count():
            route, remaining = self.DLS('', depth, 0)
            if route:
                return route
            elif not remaining:
                return None

    def DLS(self, route, depth, count):
        count += 1
        if self.max_mem < count:
            self.max_mem = count
        if (time.time() - self.start) > self.time_limit:
            return 'TimeOut', True
        self.print_nodes()
        self.num_visited += 1

        if depth == 0:
            if self.problem.is_target(route):
                return route, True
            else:
                return None, True

        any_remaining = False
        for move in self.problem.successors():
            found, remaining = self.DLS(route + move + ',', depth - 1, count)
            if found:
                return found, True
            if remaining:
                any_remaining = True

        return None, any_remaining

    def UCS(self):
        queue = PriorityQueue()
        queue.put((0, ''))

        while queue:
            if (time.time() - self.start) > self.time_limit:
                return 'TimeOut'
            self.print_nodes()
            self.num_visited += 1
            if self.max_mem < queue.qsize():
                self.max_mem = queue.qsize()

            cost, path = queue.get()

            for neighbour in self.problem.successors():
                new_path = f'{path}{neighbour},'
                queue.put((cost + 1, new_path))

                if self.problem.is_target(new_path):
                    return new_path

    def heuristic1(self):
        total = 0
        for right in self.problem.cube['R']:
            for r in right:
                if r[0] != 'R':
                    total += 1
        for left in self.problem.cube['L']:
            for l in left:
                if l[0] != 'L':
                    total += 1
        for front in self.problem.cube['F']:
            for f in front:
                if f[0] != 'F':
                    total += 1
        for back in self.problem.cube['B']:
            for b in back:
                if b[0] != 'G':
                    total += 1
        for up in self.problem.cube['U']:
            for u in up:
                if u[0] != 'U':
                    total += 1
        for down in self.problem.cube['D']:
            for d in down:
                if d[0] != 'D':
                    total += 1
        return total

    def heuristic2(self):
        total = 0

        ul = 1
        ur = 0
        dl = 0
        dr = self.problem.n * self.problem.n
        count = 0
        for i in range(self.problem.n):
            for j in range(self.problem.n):
                count += 1
                if i == 0 and j == self.problem.n - 1:
                    ur = count
                elif i == self.problem.n - 1 and j == 0:
                    dl = count

        target = self.problem.cube['F'][0][0]
        if target == f'F{ul}':
            total += 0
        elif target in [f'F{ur}', f'F{dl}', f'F{dr}', f'U{ul}', f'L{ul}', f'D{ul}', f'R{ul}', f'B{ul}', f'B{dr}']:
            total += 1
        else:
            total += 2

        target = self.problem.cube['B'][0][0]
        if target == f'B{ul}':
            total += 0
        elif target in [f'B{ur}', f'B{dl}', f'B{dr}', f'U{ul}', f'L{dr}', f'D{ul}', f'R{dr}', f'F{ul}', f'F{dr}']:
            total += 1
        else:
            total += 2

        target = self.problem.cube['R'][0][0]
        if target == f'R{ul}':
            total += 0
        elif target in [f'R{ur}', f'R{dl}', f'R{dr}', f'U{dl}', f'D{ur}', f'B{dr}', f'F{ul}', f'L{ul}', f'L{dr}']:
            total += 1
        else:
            total += 2

        target = self.problem.cube['L'][0][0]
        if target == f'L{ul}':
            total += 0
        elif target in [f'L{ur}', f'L{dl}', f'L{dr}', f'U{ur}', f'D{dl}', f'B{dr}', f'F{ul}', f'R{ul}', f'R{dr}']:
            total += 1
        else:
            total += 2

        target = self.problem.cube['U'][0][0]
        if target == f'U{ul}':
            total += 0
        elif target in [f'U{ur}', f'U{dl}', f'U{dr}', f'F{ul}', f'B{ul}', f'L{dl}', f'R{ur}', f'D{ul}', f'D{dr}']:
            total += 1
        else:
            total += 2

        target = self.problem.cube['D'][0][0]
        if target == f'D{ul}':
            total += 0
        elif target in [f'D{ur}', f'D{dl}', f'D{dr}', f'U{ul}', f'B{ul}', f'L{ur}', f'R{dl}', f'F{ul}', f'F{dr}']:
            total += 1
        else:
            total += 2
        return total

    def ASTAR(self, heuristic):
        queue = PriorityQueue()
        queue.put((0, ''))
        cost_so_far = {'': 0}

        while queue:
            if (time.time() - self.start) > self.time_limit:
                return 'TimeOut'
            self.print_nodes()
            self.num_visited += 1
            if self.max_mem < queue.qsize():
                self.max_mem = queue.qsize()
            cost, path = queue.get()

            for neighbour in self.problem.successors():
                new_path = f'{path}{neighbour},'
                new_cost = cost + 1

                if self.problem.is_target(new_path):
                    return new_path

                if neighbour not in cost_so_far or new_cost < cost_so_far[new_path]:
                    cost_so_far[new_path] = new_cost
                    if heuristic == 0:
                        priority = new_cost + self.heuristic1()
                    else:
                        priority = new_cost + self.heuristic2()
                    queue.put((priority, new_path))
