import os
import time

from cube import Cube
from solver import Solver

if __name__ == '__main__':
    d = 5
    n = 2
    time_out = 300
    start_time = time.time()
    dirName = f'results/{start_time}'

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    for i in range(1, d + 1):
        for j in range(2, n + 1):
            cube = Cube(j, i)

            Solver(cube, 'A* 0', time_out, start_time).solve()
            Solver(cube, 'A* 1', time_out, start_time).solve()
            Solver(cube, 'UCS', time_out, start_time).solve()
            Solver(cube, 'IDFS', time_out, start_time).solve()
            Solver(cube, 'BFS', time_out, start_time).solve()
