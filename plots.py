import matplotlib.pyplot as plt


def plot_time(subplot, dados, title):
    plt.subplot(subplot)
    plt.plot(range(1, len(dados) + 1), dados)
    plt.title(title)
    plt.grid(True)
    plt.ylabel('Seconds')
    plt.xlabel('Depth')
    plt.axis([0.5, 7.5, -100, 2500])


def plot_nodos(subplot, dados, title):
    plt.subplot(subplot)
    plt.plot(range(1, len(dados) + 1), dados)
    plt.title(title)
    plt.grid(True)
    plt.ylabel('Nodes')
    plt.xlabel('Depth')
    plt.axis([0.5, 7.5, -100, 2050000])


if __name__ == '__main__':
    title = 'L F D R B U L'

    a_0_time = [0, 0, 0.12493324279785156, 2.7745113372802734, 7.649450063705444, 204.15198278427124, 2412.2397713661194]
    a_0_nodos = [1, 2, 20, 283, 743, 16363, 163085]

    a_1_time = [0, 0, 0.1718580722808838, 28.037848711013794, 290.6446952819824]
    a_1_nodos = [1, 2, 25, 1782, 14867]

    ucs_time = [0, 0.062465667724609375, 1.0660386085510254, 54.78349542617798, 372.39924597740173]
    ucs_nodos = [1, 10, 118, 4978, 22474]

    idfs_time = [0, 0.09372997283935547, 2.211777448654175, 13.14039158821106, 1576.95729804039]
    idfs_nodos = [8, 294, 4411, 22937, 2023656]

    bfs_time = [0, 0.09372663497924805, 2.133387327194214, 17.15380048751831]
    bfs_nodos = [1, 16, 232, 1204]

    plot_time(121, bfs_time, 'BFS Time')
    plot_nodos(122, bfs_nodos, 'BFS Nodes')
    plt.suptitle(title)
    plt.show()

    plot_time(121, idfs_time, 'IDFS Time')
    plot_nodos(122, idfs_nodos, 'IDFS Nodes')
    plt.suptitle(title)
    plt.show()

    plot_time(121, ucs_time, 'UCS Time')
    plot_nodos(122, ucs_nodos, 'UCS Nodes')
    plt.suptitle(title)
    plt.show()

    plot_time(121, a_0_time, 'A* 0 Time')
    plot_nodos(122, a_0_nodos, 'A* 0 Nodes')
    plt.suptitle(title)
    plt.show()

    plot_time(121, a_1_time, 'A* 1 Time')
    plot_nodos(122, a_1_nodos, 'A* 1 Nodes')
    plt.suptitle(title)
    plt.show()

    plt.plot(bfs_time)
    plt.plot(idfs_time)
    plt.plot(ucs_time)
    plt.plot(a_0_time)
    plt.plot(a_1_time)
    plt.title('Times 3x3x3')
    plt.legend(['BFS', 'IDFS', 'UCS', 'A* 0', 'A* 1'])
    plt.grid()
    plt.show()

    plt.plot(bfs_nodos)
    plt.plot(idfs_nodos)
    plt.plot(ucs_nodos)
    plt.plot(a_0_nodos)
    plt.plot(a_1_nodos)
    plt.title('Nodes 3x3x3')
    plt.legend(['BFS', 'IDFS', 'UCS', 'A* 0', 'A* 1'])
    plt.grid()
    plt.show()

