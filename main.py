from cube import Cube
from solver import Solver

if __name__ == '__main__':
    cube = Cube(3, 6)
    cube.print_sequence()
    cube.print_cube()
    solver = Solver(cube)
    cube.print_sequence(solver.solve())
