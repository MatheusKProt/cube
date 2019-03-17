

class Solver:
    def __init__(self, problem, algorithm='BFS'):
        self.num_visited = 0
        self.algorithm = algorithm
        self.problem = problem

    def solve(self):
        if self.algorithm == 'BFS':
            return self.BFS()
        elif self.algorithm == 'DFS':
            exit(1)
        elif self.algorithm == 'IDFS':
            exit(1)
        elif self.algorithm == 'UCS':
            exit(1)
        elif self.algorithm == 'A*':
            exit(1)

    def BFS(self):
        open_set = [['']]
        closed_set = []

        while open_set:
            path = open_set.pop(0)
            self.num_visited += 1

            if self.problem.isTarget(path):
                print(f'Solution found! {self.num_visited} nodes visited')
                return path

            for new_path in self.problem.getSuccessors(path):

                if new_path in closed_set:
                    continue

                if new_path not in open_set:
                    open_set.append(new_path)

            closed_set.append(path)

        return None
