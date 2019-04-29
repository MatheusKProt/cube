import os
import time
from concurrent.futures import ThreadPoolExecutor

from cube import Cube
from solver import Solver

if __name__ == '__main__':
    d = [3, 3]
    n = [3, 3]
    time_out = 600
    start_time = "2"
    # start_time = time.time()
    dirName = f'results/{start_time}'
    cubes = []

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    cubes = []
    # for i in range(d[0], d[1] + 1):
    #     for j in range(n[0], n[1] + 1):
    #         cubes.append(Cube(j, i))
    # cubes.append(Cube(3, sequence='1-F-3,1-L-3,1-B-2,1-R-3'))
    cube = Cube(3, sequence='1-B-1,1-L-1,1-D-3,1-F-1,1-B-1,1-F-3,1-L-3,1-B-2,1-R-3')
    cube.print_cube()
    cube.print_sequence()
    cubes.append(cube)

    for cube in sorted(cubes, key=lambda x: x.n):
        Solver(cube, 'A* 0', time_out, start_time).solve()
        Solver(cube, 'A* 1', time_out, start_time).solve()
        Solver(cube, 'IDFS', time_out, start_time).solve()
        Solver(cube, 'BFS', time_out, start_time).solve()
        Solver(cube, 'UCS', time_out, start_time).solve()
