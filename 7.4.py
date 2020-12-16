#7.4
from pprint import pprint

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command: str, ignore: list = ignore) -> bool:
    for word in ignore:
        if word in command:
            return True
    return False


def config_to_dict(config):
    text = []
    output = dict()

    with open(config) as f:
        file = f.readlines()
        for i in file:
            if not ignore_command(i) and '!' not in i and i != '\n':
                i = i.replace('\n', '')
                text.append(i)

    name = ''
    for i in text:
        if i[0] != ' ':
            name = i
            output[name] = []
        else:
            output[name].append(i)

    return output


pprint(config_to_dict('config_sw1.txt'))