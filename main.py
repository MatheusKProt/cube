import os
import time
from concurrent.futures import ThreadPoolExecutor

from cube import Cube
from solver import Solver

if __name__ == '__main__':
    d = [1, 5]
    n = [10, 10]
    time_out = 600
    start_time = "1"
    # start_time = time.time()
    dirName = f'results/{start_time}'
    cubes = []

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    pool = ThreadPoolExecutor(max_workers=500)

    cubes = []
    for i in range(d[0], d[1] + 1):
        for j in range(n[0], n[1] + 1):
            cubes.append(Cube(j, i))

    for cube in sorted(cubes, key=lambda x: x.n):
        print(cube.n, str(cube.sequence).count(","))
        pool.submit(Solver(cube, 'A* 0', time_out, start_time).solve)
        pool.submit(Solver(cube, 'A* 1', time_out, start_time).solve)
        pool.submit(Solver(cube, 'UCS', time_out, start_time).solve)
        pool.submit(Solver(cube, 'IDFS', time_out, start_time).solve)
        pool.submit(Solver(cube, 'BFS', time_out, start_time).solve)
