def main(n):
    file = open(f'results/1553942010.1523118/{n}.txt', 'r')
    dados = {}
    algorithm = ''
    for r in file.read().split('\n'):
        if 'algorithm:' in r:
            algorithm = r.split('algorithm:')[1]
            if algorithm not in str(dados):
                dados[algorithm] = {'time': [], 'nodes': [], 'depth': []}
        if 'time' in r:
            time = r.split('time:')[1]
            if time != 'Time out':
                dados[algorithm]['time'].append(float(time))
            else:
                dados[algorithm]['time'].append(-1)
        if 'nodes' in r:
            nodes = r.split('nodes:')[1]
            if nodes != 'Time out':
                dados[algorithm]['nodes'].append(float(nodes))
            else:
                dados[algorithm]['nodes'].append(-1)
        if 'sequence:' in r:
            sequence = r.split('sequence:')[1]
            if sequence != 'Time out':
                dados[algorithm]['depth'].append(len(str(sequence).split(',')))
            else:
                dados[algorithm]['depth'].append(-1)
    return dados
