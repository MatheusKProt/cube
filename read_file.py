def main():
    file = open(f'teste.txt', 'r')
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
                dados[algorithm]['time'].append(time)
        if 'nodes' in r:
            nodes = r.split('nodes:')[1]
            if nodes != 'Time out':
                dados[algorithm]['nodes'].append(nodes)
        if 'sequence:' in r:
            sequence = r.split('sequence:')[1]
            if sequence != 'Time out':
                dados[algorithm]['depth'].append(len(str(sequence).split(',')))
    return dados


if __name__ == '__main__':
    print(main())
