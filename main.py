from cube import Cube
from solver import Solver

if __name__ == '__main__':
    # cube = Cube(3, sequence='1-R-1,1-U-1,1-R-3,1-U-3')
    cube = Cube(3, 6)
    cube.print_sequence()
    Solver(cube, 'A*').solve()
    Solver(cube, 'BFS').solve()
    Solver(cube, 'IDFS').solve()
    Solver(cube, 'UCS').solve()
