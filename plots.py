import matplotlib.pyplot as plt

from plots import read_file

figsize = (9.6, 6)
depth = [1, 5]
num = [2, 10]
time_out = 5
path = '1'

time_out_lim = (4 * time_out) / 100


def _plot_time(data, algorithms, i):
    x = []
    y = []
    count = 1
    for d in data[algorithms[i]]['time']:
        if d != -1:
            x.append(count)
            y.append(d)
        count += 1
    plt.plot(x + [99999], y + [time_out / 2], 'o-')


def plot_time(data, algorithms, n):
    plt.figure(figsize=figsize)
    plt.title(f'Cube: {n}x{n}x{n}')
    plt.xlim(0.8, depth[1] + 0.2)
    plt.ylim(-time_out_lim, time_out + time_out_lim)
    for i in range(0, 5):
        _plot_time(data, algorithms, i)

    plt.legend(algorithms)
    plt.grid()
    plt.xlabel('Depth')
    plt.ylabel('Time (seconds)')
    plt.xticks(range(depth[0], depth[1] + 1))
    plt.savefig(f'results/images/{n}.png')
    plt.close()


def _plot_solutions(data, algorithms, i):
    plt.title(algorithms[i])
    plt.xlabel('Depth')
    plt.ylabel('Found')
    plt.yticks([0, 1])
    y = []
    [y.append(1) if j in data[algorithms[i]]['depth'] else y.append(0) for j in range(depth[0], depth[1] + 1)]
    plt.bar(range(depth[0], depth[1] + 1), y, tick_label=range(depth[0], depth[1] + 1))


def plot_solutions(data, algorithms, n):
    plt.figure(figsize=figsize)
    plt.suptitle(f'Solutions found\nTime limit: {time_out} seconds\nCube: {n}x{n}x{n}')

    plt.subplot(231)
    _plot_solutions(data, algorithms, 0)

    plt.subplot(233)
    _plot_solutions(data, algorithms, 1)

    plt.subplot(234)
    _plot_solutions(data, algorithms, 2)

    plt.subplot(235)
    _plot_solutions(data, algorithms, 3)

    plt.subplot(236)
    _plot_solutions(data, algorithms, 4)

    # plt.savefig(f'results/images/s{n}.png')
    plt.show()
    plt.close()


def _plot_n(data, algorithms, i, j):
    x = []
    y = []
    count = 2
    for k in range(num[1] + 1 - num[0]):
        d = data[k][algorithms[i]]['time'][j]
        if d != -1:
            x.append(count)
            y.append(d)
        count += 1
    plt.plot(x + [99999], y + [time_out / 2], 'o-')


def plot_n(data, algorithms):
    for j in range(depth[1]):
        plt.figure(figsize=figsize)
        plt.title(f'Depth: {j + 1}')
        plt.xlim(1.68, 10.32)
        plt.ylim(-time_out_lim, time_out + time_out_lim)
        for i in range(0, 5):
            _plot_n(data, algorithms, i, j)
        plt.legend(algorithms)
        plt.grid()
        plt.xlabel('N')
        plt.ylabel('Time (seconds)')
        plt.savefig(f'results/images/n{j}.png')
        plt.close()


if __name__ == '__main__':
    datas = []
    algorithms = ['BFS', 'IDFS', 'UCS', 'A* 0', 'A* 1']
    for i in range(num[0], num[1] + 1):
        datas.append(read_file.main(i, path))
    #     data = read_file.main(i, path)
    #     plot_time(data, algorithms, i)
    #     plot_solutions(data, algorithms, i)
    plot_n(datas, algorithms)

