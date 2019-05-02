from ast import literal_eval


def main(n, path):
    file = open(f'../results/{path}/{n}.txt', 'r')
    dados = []
    saida = {
        'BFS': {'sequence': [], 'time': [], 'nodes': [], 'memory': [], 'depth': []},
        'IDFS': {'sequence': [], 'time': [], 'nodes': [], 'memory': [], 'depth': []},
        'UCS': {'sequence': [], 'time': [], 'nodes': [], 'memory': [], 'depth': []},
        'A* 0': {'sequence': [], 'time': [], 'nodes': [], 'memory': [], 'depth': []},
        'A* 1': {'sequence': [], 'time': [], 'nodes': [], 'memory': [], 'depth': []},
    }

    my_own_order = ['BFS', 'IDFS', 'UCS', 'A* 0', 'A* 1']
    order = {key: i for i, key in enumerate(my_own_order)}

    for r in file.read().split('\n'):
        if r:
            dados.append(literal_eval(r))

    dados = sorted(dados, key=lambda x: (order[x['algorithm']], x['algorithm'], x['depth']))

    for dado in dados:
        saida[dado['algorithm']]['sequence'].append(dado['sequence'])
        saida[dado['algorithm']]['time'].append(dado['time'])
        saida[dado['algorithm']]['nodes'].append(float(dado['nodes']))
        saida[dado['algorithm']]['memory'].append(float(dado['memory']))
        saida[dado['algorithm']]['depth'].append(float(dado['depth']))

    return saida
