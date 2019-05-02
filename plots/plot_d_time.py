import matplotlib.pyplot as plt
import numpy as np

import read_file

fig_size = (9.6, 6)

if __name__ == '__main__':
    n = 5
    alpha = 0.7
    dados = read_file.main(n, '2')

    plt.figure(figsize=fig_size)
    plt.title(f'Cube {n}x{n}x{n}')
    plt.grid(axis='y')
    plt.xlabel('Depth')
    plt.ylabel('Time (seconds)')

    X = np.arange(5)
    bar1 = plt.bar(X - 0.3, dados['BFS']['time'], color='b', width=0.15, alpha=alpha)
    bar2 = plt.bar(X - 0.15, dados['IDFS']['time'], color='g', width=0.15, alpha=alpha)
    bar3 = plt.bar(X + 0.0, dados['UCS']['time'], color='r', width=0.15, alpha=alpha)
    bar4 = plt.bar(X + 0.15, dados['A* 0']['time'], color='c', width=0.15, alpha=alpha)
    bar5 = plt.bar(X + 0.3, dados['A* 1']['time'], color='m', width=0.15, alpha=alpha)

    plt.legend(['BFS', 'IDFS', 'UCS', 'A* 0', 'A* 1'])

    for rect in bar1 + bar2 + bar3 + bar4 + bar5:
        if rect.get_height() > 0.0:
            pos = str(round(rect.get_x() + 1 + rect.get_width() / 2.0, 2)).split(".")[1]
            if pos == "7":
                algorithm = 'BFS'
            elif pos == "85":
                algorithm = 'IDFS'
            elif pos == "0":
                algorithm = 'UCS'
            elif pos == "15":
                algorithm = 'A* 0'
            elif pos == "3":
                algorithm = 'A* 1'
            plt.text(rect.get_x() + rect.get_width() / 2.0, 0, f' {algorithm} (%.6f)' % rect.get_height(), ha='center', va='bottom', rotation=90)

    plt.xticks(range(0, 5), [1, 2, 3, 4, 5], rotation=0)
    plt.show()
