import random
import numpy as np


class Cube:

    def __init__(self, n: int, num_moves=1, sequence=None):
        self.R = []
        self.L = []
        self.U = []
        self.D = []
        self.F = []
        self.B = []
        self.sequence = ''
        self.n = n

        count = 0
        for i in range(n):
            self.R.append([])
            self.L.append([])
            self.U.append([])
            self.D.append([])
            self.F.append([])
            self.B.append([])
            for _ in range(n):
                count += 1
                self.R[i].append(f'R{count}')
                self.L[i].append(f'L{count}')
                self.U[i].append(f'U{count}')
                self.D[i].append(f'D{count}')
                self.F[i].append(f'F{count}')
                self.B[i].append(f'B{count}')
        self.cube = {'R': self.R,
                     'L': self.L,
                     'U': self.U,
                     'D': self.D,
                     'F': self.F,
                     'B': self.B}
        self.goal = self.cube.copy()
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

    def successors(self, path):
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

        if path:
            for s in suc:
                if s == path.split(",")[:-1][-1]:
                    suc.pop(suc.index(s.split("-")[0] + '-' + s.split("-")[1] + '-' + str(4 - int(s.split("-")[2]))))
        return suc

    def scramble(self, cube, num_moves, sequence=None):
        if sequence:
            for seq in sequence.split(','):
                cube = self.move(cube, seq)
            self.sequence = sequence + ','
        else:
            suc = self.successors("")
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
        cube = self.cube.copy()
        for m in moves:
            y = np.rot90(np.array(self.cube[m[1][0]]), m[1][1])
            y[row] = np.rot90(np.array(self.cube[m[0][0]]), m[0][1])[row][::1]
            cube[m[1][0]] = np.rot90(y, -m[1][1]).tolist()

        self.cube = cube

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
        cube = self.apply_path(path)
        for face in ['R', 'L', 'U', 'D', 'F', 'B']:
            for cc in cube[face]:
                for c in cc:
                    if c[0] != cube[face][0][0][0]:
                        return False
        return True

    def apply_path(self, path):
        cube = self.start.copy()
        for p in path.split(',')[:-1]:
            cube = self.move(cube, p)

        return cube
