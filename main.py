import os

from cube import Cube
from solver import Solver

if __name__ == '__main__':
    n = [2, 2]  # 2 - 5
    d = [3, 3]  # 1 - 5
    time_out = 300
    start_time = "2"
    dirName = f'results/{start_time}'
    cubes = []

    if not os.path.exists(dirName):
        os.makedirs(dirName)

    cubes = []
    for i in range(d[0], d[1] + 1):
        for j in range(n[0], n[1] + 1):
            cubes.append(Cube(j, i))

    for cube in sorted(cubes, key=lambda x: x.n):
        cube.print_sequence()
        Solver(cube, 'A* 0', time_out, start_time).solve()
        Solver(cube, 'A* 1', time_out, start_time).solve()
        Solver(cube, 'IDFS', time_out, start_time).solve()
        Solver(cube, 'BFS', time_out, start_time).solve()
        Solver(cube, 'UCS', time_out, start_time).solve()
