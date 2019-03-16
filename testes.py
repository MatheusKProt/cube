import numpy as np

if __name__ == '__main__':
    cube = {'F': [[1, 2], [3, 4]], 'U': [[5, 6], [7, 8]]}
    for i in range(2):
        print(cube['F'][i], cube['U'][i])
    #   [[Face que vai ser pego, Rotacao do que vai ser pego(-1, 0, 1, 2), ordem(1, -1)],[Face que recebe, Rotacao para receber], linha]
    m = [['F', -1, 1], ['U', 2], 0]

    y = np.rot90(np.array(cube[m[1][0]]), m[1][1])
    y[m[2]] = np.rot90(np.array(cube[m[0][0]]), m[0][1])[m[2]][::m[0][2]]
    cube[m[1][0]] = np.rot90(y, -m[1][1]).tolist()

    for i in range(2):
        print(cube['F'][i], cube['U'][i])
