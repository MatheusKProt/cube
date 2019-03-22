from cube import Cube
from solver import Solver

if __name__ == '__main__':
    cube = Cube(3, 1)
    cube.print_sequence()
    solver = Solver(cube, 'IDFS')
    cube.print_sequence(solver.solve())
    solver = Solver(cube, 'BFS')
    cube.print_sequence(solver.solve())
