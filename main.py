from Cube import Cube


if __name__ == '__main__':
    cube = Cube(3)
    cube.print_cube()
    # print(cube.scramble(1))
    # cube.move([['2', 'L'], '1'])
    # cube.move([['1', 'L'], '1'])
    # cube.move([['1', 'R'], '-1'])
    # cube.move([['2', 'R'], '-1'])
    cube.move([['1', 'U'], '1'])
    # cube.move([['2', 'D'], '-1'])
    # cube.move([['2', 'L'], '-1'])
    # cube.move([['1', 'L'], '-1'])
    # cube.move([['1', 'R'], '1'])
    # cube.move([['2', 'R'], '1'])
    cube.print_cube()

    # for i in [['D', '2'], ['L', '-1'], ['R', '2'], ['D', '1'], ['U', '1']]:
    #     cube.move(i)
    #
    # cube.print_cube()
