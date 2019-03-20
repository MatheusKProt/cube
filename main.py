from cube import Cube
from solver import Solver

if __name__ == '__main__':
    cube = Cube(3, 4)
    cube.print_sequence()
    cube.print_cube()
    solver = Solver(cube, 'IDFS')
    cube.print_sequence(solver.solve())
    solver = Solver(cube, 'BFS')
    cube.print_sequence(solver.solve())
