import random
import numpy as np


class Cube:
    n = 0

    # 2x2
    # R = [[' 0', ' 1'], [' 2', ' 3']]
    # L = [[' 4', ' 5'], [' 6', ' 7']]
    # U = [[' 8', ' 9'], ['10', '11']]
    # D = [['12', '13'], ['14', '15']]
    # F = [['16', '17'], ['18', '19']]
    # B = [['20', '21'], ['22', '23']]

    # 3x3
    # U = [[' 0', ' 1', ' 2'], [' 3', ' 4', ' 5'], [' 6', ' 7', ' 8']]
    # L = [[' 9', '10', '11'], ['12', '13', '14'], ['15', '16', '17']]
    # F = [['18', '19', '20'], ['21', '22', '23'], ['24', '25', '26']]
    # R = [['27', '28', '29'], ['30', '31', '32'], ['33', '34', '35']]
    # D = [['36', '37', '38'], ['39', '40', '41'], ['42', '43', '44']]
    # B = [['45', '46', '47'], ['48', '49', '50'], ['51', '52', '53']]

    R = []
    L = []
    U = []
    D = []
    F = []
    B = []

    sequence = []

    def __init__(self, n: int, num_moves: int):
        """
        Front => Blue
        Down => White
        Right => Red
        Left => Orange
        Up => Yellow
        Back => Green

        n: n*n*n
        """
        self.n = n

        for i in range(n):
            self.R.append([])
            self.L.append([])
            self.U.append([])
            self.D.append([])
            self.F.append([])
            self.B.append([])
            for _ in range(n):
                self.R[i].append('red   ')
                self.L[i].append('orange')
                self.U[i].append('yellow')
                self.D[i].append('white ')
                self.F[i].append('blue  ')
                self.B[i].append('green ')
        self.cube = {'R': self.R,
                     'L': self.L,
                     'U': self.U,
                     'D': self.D,
                     'F': self.F,
                     'B': self.B}
        self.start = self.cube
        self.scramble(num_moves)
        self.goal = self.cube

    def print_cube(self):
        space = ''
        for n in range((len(self.R[0][0]) + 4) * self.n):
            space += ' '
        for n in range(self.n):
            print(space + str(self.cube['U'][n]))
        for n in range(self.n):
            print(str(self.cube['L'][n]) + str(self.cube['F'][n]) + str(self.cube['R'][n]))
        for n in range(self.n):
            print(space + str(self.cube['D'][n]))
        for n in range(self.n):
            print(space + str(self.cube['B'][n]))
        print()

    def print_sequence(self):
        text = ""
        for seq in self.sequence:
            if seq[0][0] == '1':
                text += seq[0][1]
            else:
                text += seq[0][0] + seq[0][1]
            if seq[1] == '2':
                text += "2 "
            elif seq[1] == '-1':
                text += "' "
            else:
                text += " "
        print(text)

    def successors(self):
        suc = [['1', 'R'], ['1', 'L'], ['1', 'U'], ['1', 'D'], ['1', 'F'], ['1', 'B']]
        for i in range(2, int(self.n/2) + 1):
            suc.append([str(i), 'R'])
            suc.append([str(i), 'L'])
            suc.append([str(i), 'U'])
            suc.append([str(i), 'D'])
            suc.append([str(i), 'F'])
            suc.append([str(i), 'B'])
        return suc

    def scramble(self, num_moves):
        suc = self.successors()
        z = None
        sequence = []
        for _ in range(num_moves):
            y = random.randint(0, len(suc) - 1)
            sequence.append([suc[y], random.choice(['1', "-1", '2'])])
            if z:
                suc.append(z)
            z = suc[y]
            suc.pop(y)
            self.move(sequence[len(sequence) - 1])
        self.sequence = sequence

    # noinspection PyTypeChecker
    def move_(self, moves: list, row):
        """
        moves: [[Face que vai ser pego, Rotacao do que vai ser pego(-1, 0, 1, 2), ordem(1, -1)],[Face que recebe, Rotacao para receber]]
        """
        cube = self.cube.copy()
        for m in moves:
            y = np.rot90(np.array(self.cube[m[1][0]]), m[1][1])
            y[row] = np.rot90(np.array(self.cube[m[0][0]]), m[0][1])[row][::1]
            cube[m[1][0]] = np.rot90(y, -m[1][1]).tolist()

        self.cube = cube

    # noinspection PyTypeChecker
    def move(self, suc):
        row = int(suc[0][0]) - 1
        if suc[0][0] == '1':
            self.cube[suc[0][1]] = np.rot90(np.array(self.cube[suc[0][1]]), -int(suc[1])).tolist()

        if suc[0][1] == 'R':
            if suc[1] == '1':
                self.move_([[['F', 1], ['U', 1]],
                            [['D', 1], ['F', 1]],
                            [['B', 1], ['D', 1]],
                            [['U', 1], ['B', 1]]], row)
            elif suc[1] == '2':
                self.move_([[['F', 1], ['B', 1]],
                            [['B', 1], ['F', 1]],
                            [['U', 1], ['D', 1]],
                            [['D', 1], ['U', 1]]], row)
            elif suc[1] == '-1':
                self.move_([[['B', 1], ['U', 1]],
                            [['D', 1], ['B', 1]],
                            [['F', 1], ['D', 1]],
                            [['U', 1], ['F', 1]]], row)
        elif suc[0][1] == 'L':
            if suc[1] == '1':
                self.move_([[['B', -1], ['U', -1]],
                            [['D', -1], ['B', -1]],
                            [['F', -1], ['D', -1]],
                            [['U', -1], ['F', -1]]], row)
            elif suc[1] == '2':
                self.move_([[['F', -1], ['B', -1]],
                            [['B', -1], ['F', -1]],
                            [['U', -1], ['D', -1]],
                            [['D', -1], ['U', -1]]], row)
            elif suc[1] == '-1':
                self.move_([[['F', -1], ['U', -1]],
                            [['D', -1], ['F', -1]],
                            [['B', -1], ['D', -1]],
                            [['U', -1], ['B', -1]]], row)
        elif suc[0][1] == 'U':
            if suc[1] == '1':
                self.move_([[['R', 0], ['F', 0]],
                            [['F', 0], ['L', 0]],
                            [['L', 0], ['B', 2]],
                            [['B', 2], ['R', 0]]], row)
            elif suc[1] == '2':
                self.move_([[['R', 0], ['L', 0]],
                            [['L', 0], ['R', 0]],
                            [['B', 2], ['F', 0]],
                            [['F', 0], ['B', 2]]], row)
            elif suc[1] == '-1':
                self.move_([[['L', 0], ['F', 0]],
                            [['F', 0], ['R', 0]],
                            [['R', 0], ['B', 2]],
                            [['B', 2], ['L', 0]]], row)
        elif suc[0][1] == 'D':
            if suc[1] == '1':
                self.move_([[['L', 2], ['F', 2]],
                            [['F', 2], ['R', 2]],
                            [['R', 2], ['B', 0]],
                            [['B', 0], ['L', 2]]], row)
            elif suc[1] == '2':
                self.move_([[['R', 2], ['L', 2]],
                            [['L', 2], ['R', 2]],
                            [['B', 0], ['F', 2]],
                            [['F', 2], ['B', 0]]], row)
            elif suc[1] == '-1':
                self.move_([[['R', 2], ['F', 2]],
                            [['F', 2], ['L', 2]],
                            [['L', 2], ['B', 0]],
                            [['B', 0], ['R', 2]]], row)
        elif suc[0][1] == 'F':
            if suc[1] == '1':
                self.move_([[['U', 2], ['R', -1]],
                            [['R', -1], ['D', 0]],
                            [['D', 0], ['L', 1]],
                            [['L', 1], ['U', 2]]], row)
            elif suc[1] == '2':
                self.move_([[['R', -1], ['L', 1]],
                            [['L', 1], ['R', -1]],
                            [['D', 0], ['U', 2]],
                            [['U', 2], ['D', 0]]], row)
            elif suc[1] == '-1':
                self.move_([[['U', 2], ['L', 1]],
                            [['L', 1], ['D', 0]],
                            [['D', 0], ['R', -1]],
                            [['R', -1], ['U', 2]]], row)
        elif suc[0][1] == 'B':
            if suc[1] == '1':
                self.move_([[['L', -1], ['D', 2]],
                            [['D', 2], ['R', 1]],
                            [['R', 1], ['U', 0]],
                            [['U', 0], ['L', -1]]], row)
            elif suc[1] == '2':
                self.move_([[['R', 1], ['L', -1]],
                            [['L', -1], ['R', 1]],
                            [['D', 2], ['U', 0]],
                            [['U', 0], ['D', 2]]], row)
            elif suc[1] == '-1':
                self.move_([[['U', 0], ['R', 1]],
                            [['R', 1], ['D', 2]],
                            [['D', 2], ['L', -1]],
                            [['L', -1], ['U', 0]]], row)
