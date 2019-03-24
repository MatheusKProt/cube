from cube import Cube
from solver import Solver

if __name__ == '__main__':
    cube = Cube(3, sequence='1-R-1,1-F-1,1-L-1,1-B-1,1-U-1,1-D-1,1-R-1')
    cube = Cube(3, sequence='1-R-1,1-F-1,1-L-1,1-B-1,1-U-1,1-D-1')
    cube = Cube(3, sequence='1-R-1,1-F-1,1-L-1,1-B-1,1-U-1')
    cube = Cube(3, sequence='1-R-1,1-F-1,1-L-1,1-B-1')
    cube = Cube(3, sequence='1-R-1,1-F-1,1-L-1')
    cube = Cube(3, sequence='1-R-1,1-F-1')
    cube = Cube(3, sequence='1-R-1')
    # cube = Cube(3, 1)
    cube.print_sequence()
    Solver(cube, 'A*').solve()
    Solver(cube, 'UCS').solve()
    Solver(cube, 'IDFS').solve()
    Solver(cube, 'BFS').solve()
