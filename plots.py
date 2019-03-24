import matplotlib.pyplot as plt


if __name__ == '__main__':
    alg = ['A*', 'BFS', 'IDFS', 'UCS']

    a_time = [0.00099945068359375,
              0.004997968673706055,
              0.1109309196472168,
              0.44272732734680176,
              6.275137901306152,
              116.12919807434082]
    ucs_time = [0.0009992122650146484,
                0.07095551490783691,
                2.727321147918701,
                18.781439781188965]
    idfs_time = [0.0009992122650146484,
                 0.1229245662689209,
                 1.54305100440979,
                 97.86576008796692]
    bfs_time = [0.00099945068359375,
                0.12192654609680176,
                1.5980169773101807,
                217.7340075969696]

    a_nodos = [1, 2, 14, 41, 439, 6737]
    ucs_nodos = [1, 10, 226, 1198]
    idfs_nodos = [5, 291, 2350, 113501]
    bfs_nodos = [1, 16, 124, 5956]

    plt.subplot(121)
    plt.plot(range(1, len(bfs_time) + 1), bfs_time)
    plt.title('BFS Time')
    plt.grid(True)
    plt.ylabel('Seconds')
    plt.xlabel('Depth')

    plt.subplot(122)
    plt.plot(range(1, len(bfs_nodos) + 1), bfs_nodos)
    plt.title('BFS Nodes')
    plt.grid(True)
    plt.ylabel('Nodes')
    plt.xlabel('Depth')

    plt.show()

    plt.subplot(121)
    plt.plot(range(1, len(idfs_time) + 1), idfs_time)
    plt.title('IDFS Time')
    plt.grid(True)
    plt.ylabel('Seconds')
    plt.xlabel('Depth')

    plt.subplot(122)
    plt.plot(range(1, len(idfs_nodos) + 1), idfs_nodos)
    plt.title('IDFS Nodes')
    plt.grid(True)
    plt.ylabel('Nodes')
    plt.xlabel('Depth')

    plt.show()

    plt.subplot(121)
    plt.plot(range(1, len(ucs_time) + 1), ucs_time)
    plt.title('UCS Time')
    plt.grid(True)
    plt.ylabel('Seconds')
    plt.xlabel('Depth')

    plt.subplot(122)
    plt.plot(range(1, len(ucs_nodos) + 1), ucs_nodos)
    plt.title('UCS Nodes')
    plt.grid(True)
    plt.ylabel('Nodes')
    plt.xlabel('Depth')

    plt.show()

    plt.subplot(121)
    plt.plot(range(1, len(a_time) + 1), a_time)
    plt.title('A* Time')
    plt.grid(True)
    plt.ylabel('Seconds')
    plt.xlabel('Depth')

    plt.subplot(122)
    plt.plot(range(1, len(a_nodos) + 1), a_nodos)
    plt.title('A* Nodes')
    plt.grid(True)
    plt.ylabel('Nodes')
    plt.xlabel('Depth')

    plt.show()
