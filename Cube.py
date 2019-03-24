import random
import numpy as np


class Cube:

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

    def __init__(self, n: int, num_moves=1, sequence=None):
        """
        Front => Blue
        Down => White
        Right => Red
        Left => Orange
        Up => Yellow
        Back => Green

        n: n*n*n
        """
        self.R = []
        self.L = []
        self.U = []
        self.D = []
        self.F = []
        self.B = []
        self.sequence = ''
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
        self.goal = self.cube
        if sequence:
            self.scramble(self.cube, num_moves, sequence)
        else:
            self.scramble(self.cube, num_moves)
        self.start = self.cube

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

    def print_sequence(self, sequence=None):
        text = "Solution: "
        if not sequence:
            sequence = self.sequence
            text = "Scramble: "
        for seq in sequence.split(',')[:-1]:
            seq = seq.split('-')
            if seq[0] == '1':
                text += seq[1]
            else:
                text += seq[0] + seq[1]
            if seq[2] == '2':
                text += "2 "
            elif seq[2] == '3':
                text += "' "
            else:
                text += " "
        print(f'{text}\n')

    def successors(self, scramble=False):
        suc = ['1-R-1', '1-R-2', '1-R-3',
               '1-L-1', '1-L-2', '1-L-3',
               '1-U-1', '1-U-2', '1-U-3',
               '1-D-1', '1-D-2', '1-D-3',
               '1-F-1', '1-F-2', '1-F-3',
               '1-B-1', '1-B-2', '1-B-3']
        for i in range(2, int(self.n/2) + 1):
            suc.append(f'{i}-R-1')
            suc.append(f'{i}-R-2')
            suc.append(f'{i}-R-3')
            suc.append(f'{i}-L-1')
            suc.append(f'{i}-L-2')
            suc.append(f'{i}-L-3')
            suc.append(f'{i}-U-1')
            suc.append(f'{i}-U-2')
            suc.append(f'{i}-U-3')
            suc.append(f'{i}-D-1')
            suc.append(f'{i}-D-2')
            suc.append(f'{i}-D-3')
            suc.append(f'{i}-F-1')
            suc.append(f'{i}-F-2')
            suc.append(f'{i}-F-3')
            suc.append(f'{i}-B-1')
            suc.append(f'{i}-B-2')
            suc.append(f'{i}-B-3')

        return suc
        # if scramble:
        #     return suc
        # else:
        #     return random.sample(suc, len(suc))

    def scramble(self, cube, num_moves, sequence=None):
        if sequence:
            for seq in sequence.split(','):
                cube = self.move(cube, seq)
            self.sequence = sequence + ','
        else:
            suc = self.successors(True)
            a = []
            for _ in range(num_moves):
                i = random.randint(0, len(suc) - 1)
                s = suc[i].split('-')
                if s[2] == '1':
                    x, y, z = i, i + 1, i + 2
                elif s[2] == '2':
                    x, y, z = i - 1, i, i + 1
                else:
                    x, y, z = i - 2, i - 1, i
                self.sequence += str(suc[i]) + ','
                cube = self.move(cube, suc[i])
                if a:
                    for aa in a:
                        suc.append(aa)
                    a.pop(0)
                    a.pop(0)
                    a.pop(0)
                a.append(suc[x])
                a.append(suc[y])
                a.append(suc[z])
                suc.pop(x)
                suc.pop(x)
                suc.pop(x)

    def move_(self, moves: list, row):
        """
        moves: [[Face que vai ser pego, Rotacao do que vai ser pego(-1, 0, 1, 2)],[Face que recebe, Rotacao para receber]]
        """
        cube = self.cube.copy()
        for m in moves:
            y = np.rot90(np.array(self.cube[m[1][0]]), m[1][1])
            y[row] = np.rot90(np.array(self.cube[m[0][0]]), m[0][1])[row][::1]
            cube[m[1][0]] = np.rot90(y, -m[1][1]).tolist()

        self.cube = cube

    # noinspection PyTypeChecker
    def move(self, cube, suc: list):
        self.cube = cube
        suc = str(suc).split('-')
        row = int(suc[0]) - 1
        if suc[0] == '1':
            self.cube[suc[1]] = np.rot90(np.array(self.cube[suc[1]]), -int(suc[2])).tolist()

        if suc[1] == 'R':
            if suc[2] == '1':
                self.move_([[['F', 1], ['U', 1]],
                            [['D', 1], ['F', 1]],
                            [['B', 1], ['D', 1]],
                            [['U', 1], ['B', 1]]], row)
            elif suc[2] == '2':
                self.move_([[['F', 1], ['B', 1]],
                            [['B', 1], ['F', 1]],
                            [['U', 1], ['D', 1]],
                            [['D', 1], ['U', 1]]], row)
            elif suc[2] == '3':
                self.move_([[['B', 1], ['U', 1]],
                            [['D', 1], ['B', 1]],
                            [['F', 1], ['D', 1]],
                            [['U', 1], ['F', 1]]], row)
        elif suc[1] == 'L':
            if suc[2] == '1':
                self.move_([[['B', -1], ['U', -1]],
                            [['D', -1], ['B', -1]],
                            [['F', -1], ['D', -1]],
                            [['U', -1], ['F', -1]]], row)
            elif suc[2] == '2':
                self.move_([[['F', -1], ['B', -1]],
                            [['B', -1], ['F', -1]],
                            [['U', -1], ['D', -1]],
                            [['D', -1], ['U', -1]]], row)
            elif suc[2] == '3':
                self.move_([[['F', -1], ['U', -1]],
                            [['D', -1], ['F', -1]],
                            [['B', -1], ['D', -1]],
                            [['U', -1], ['B', -1]]], row)
        elif suc[1] == 'U':
            if suc[2] == '1':
                self.move_([[['R', 0], ['F', 0]],
                            [['F', 0], ['L', 0]],
                            [['L', 0], ['B', 2]],
                            [['B', 2], ['R', 0]]], row)
            elif suc[2] == '2':
                self.move_([[['R', 0], ['L', 0]],
                            [['L', 0], ['R', 0]],
                            [['B', 2], ['F', 0]],
                            [['F', 0], ['B', 2]]], row)
            elif suc[2] == '3':
                self.move_([[['L', 0], ['F', 0]],
                            [['F', 0], ['R', 0]],
                            [['R', 0], ['B', 2]],
                            [['B', 2], ['L', 0]]], row)
        elif suc[1] == 'D':
            if suc[2] == '1':
                self.move_([[['L', 2], ['F', 2]],
                            [['F', 2], ['R', 2]],
                            [['R', 2], ['B', 0]],
                            [['B', 0], ['L', 2]]], row)
            elif suc[2] == '2':
                self.move_([[['R', 2], ['L', 2]],
                            [['L', 2], ['R', 2]],
                            [['B', 0], ['F', 2]],
                            [['F', 2], ['B', 0]]], row)
            elif suc[2] == '3':
                self.move_([[['R', 2], ['F', 2]],
                            [['F', 2], ['L', 2]],
                            [['L', 2], ['B', 0]],
                            [['B', 0], ['R', 2]]], row)
        elif suc[1] == 'F':
            if suc[2] == '1':
                self.move_([[['U', 2], ['R', -1]],
                            [['R', -1], ['D', 0]],
                            [['D', 0], ['L', 1]],
                            [['L', 1], ['U', 2]]], row)
            elif suc[2] == '2':
                self.move_([[['R', -1], ['L', 1]],
                            [['L', 1], ['R', -1]],
                            [['D', 0], ['U', 2]],
                            [['U', 2], ['D', 0]]], row)
            elif suc[2] == '3':
                self.move_([[['U', 2], ['L', 1]],
                            [['L', 1], ['D', 0]],
                            [['D', 0], ['R', -1]],
                            [['R', -1], ['U', 2]]], row)
        elif suc[1] == 'B':
            if suc[2] == '1':
                self.move_([[['L', -1], ['D', 2]],
                            [['D', 2], ['R', 1]],
                            [['R', 1], ['U', 0]],
                            [['U', 0], ['L', -1]]], row)
            elif suc[2] == '2':
                self.move_([[['R', 1], ['L', -1]],
                            [['L', -1], ['R', 1]],
                            [['D', 2], ['U', 0]],
                            [['U', 0], ['D', 2]]], row)
            elif suc[2] == '3':
                self.move_([[['U', 0], ['R', 1]],
                            [['R', 1], ['D', 2]],
                            [['D', 2], ['L', -1]],
                            [['L', -1], ['U', 0]]], row)
        return self.cube

    def is_target(self, path):
        board = self.apply_path(path)
        return self.goal == board

    def apply_path(self, path):
        board = self.start.copy()
        for p in path.split(',')[:-1]:
            board = self.move(board, p)

        return board

    def get_numeric(self, face):
        """
        r 0
        o 1
        y 2
        w 3
        b 4
        g 5

        :return: Cube
        """
        cube = self.cube
        matrix = []
        for r in cube[face]:
            vector = []
            for i in r:
                vector.append(set_numeric(i))
            matrix.append(vector)
        return matrix

    def numeric_sequence(self, sequence=None):
        vector = []
        for r in sequence:
            for i in r:
                vector.append(int(set_numeric(i)))
        return vector


def set_numeric(cor):
    if cor == 'red   ':
        return 0
    elif cor == 'orange':
        return 1
    elif cor == 'yellow':
        return 2
    elif cor == 'white ':
        return 3
    elif cor == 'blue  ':
        return 4
    elif cor == 'green ':
        return 5
    elif cor == 'R':
        return 6
    elif cor == 'L':
        return 7
    elif cor == 'U':
        return 8
    elif cor == 'D':
        return 9
    elif cor == 'F':
        return 10
    elif cor == 'B':
        return 11
    else:
        return cor
