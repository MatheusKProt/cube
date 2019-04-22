import os
import time
from threading import Thread

from cube import Cube
from solver import Solver

if __name__ == '__main__':
    d = [1, 10]
    n = [2, 10]
    time_out = 1800
    start_time = time.time()
    dirName = f'results/{start_time}'
    cubes = []

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    for i in range(d[0], d[1] + 1):
        for j in range(n[0], n[1] + 1):
            cube = Cube(j, i)

            Thread(target=Solver(cube, 'A* 0', time_out, start_time).solve).start()
            Thread(target=Solver(cube, 'A* 1', time_out, start_time).solve).start()
            Thread(target=Solver(cube, 'UCS', time_out, start_time).solve).start()
            Thread(target=Solver(cube, 'IDFS', time_out, start_time).solve).start()
            Thread(target=Solver(cube, 'BFS', time_out, start_time).solve).start()
