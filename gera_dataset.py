import random

import numpy as np

from cube import Cube
import pandas as pd

if __name__ == '__main__':
    r = []
    l = []
    u = []
    d = []
    f = []
    b = []
    solutions = []
    for _ in range(2):
        cube = Cube(3, random.randint(1, 20))
        sequence = cube.sequence
        if sequence[0][2] == '-1':
            sequence[0][2] = '1'
        elif sequence[0][2] == '1':
            sequence[0][2] = '-1'
        r.append(cube.get_numeric('R'))
        l.append(cube.get_numeric('L'))
        u.append(cube.get_numeric('U'))
        d.append(cube.get_numeric('D'))
        f.append(cube.get_numeric('F'))
        b.append(cube.get_numeric('B'))
        solutions.append(sequence)
    dataset = {'cubes': r, 'solutions': solutions}
    df = pd.DataFrame(data=np.asarray(dataset))
    print(df)
