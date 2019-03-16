from Cube import Cube


if __name__ == '__main__':
    cube = Cube(3)

    for i in [['D', '2'], ['L', '-1'], ['R', '2'], ['D', '1'], ['U', '1']]:
        cube.move(i)

    cube.print_cube()
