from cube import Cube
from solver import Solver

if __name__ == '__main__':
    d = 5
    n = 10
    time_out = 60
    for i in range(1, d + 1):
        for j in range(2, n + 1):
            cube = Cube(j, i)

            Solver(cube, 'A* 0', time_out).solve()
            Solver(cube, 'A* 1', time_out).solve()
            Solver(cube, 'UCS', time_out).solve()
            Solver(cube, 'IDFS', time_out).solve()
            Solver(cube, 'BFS', time_out).solve()
