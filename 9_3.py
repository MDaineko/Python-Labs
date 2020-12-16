#9_3
import re
from pprint import pprint

def parse_cfg(filename):
    output = []

    reg_e = r'\d+\.\d+\.\d+\.\d+ \d+\.\d+\.\d+\.\d+'

    with open(filename) as f:
        file = f.read()
    data = re.findall(reg_e, file)

    for i in data:
        output.append(tuple(i.split()))

    return output


pprint(parse_cfg('config_r1.txt'))

#9_3a
def parse_cfg(filename):
    output = {}

    with open(filename) as f:
        file = f.read()
    data = re.findall(r'interface Ethernet[\s\S]*?!', file)

    for string in data:
        name = re.search(r'interface (Ethernet\d/\d)', string)[1]

        string = re.search(r'ip address (?P<ip>[\d.]{7,}) (?P<mac>[\d.]{7,})', string)

        if string:
            ip = string['ip']
            mac = string['mac']
            output[name] = (ip, mac)
        else:
            output[name] = None

    return output


pprint(parse_cfg('config_r1.txt'))

#9_3b
def parse_cfg(filename):
    output = {}

    with open(filename) as f:
        file = f.read()
    data = re.findall(r'interface Ethernet[\s\S]*?!', file)

    for string in data:
        name = re.search(r'interface (Ethernet\d/\d)', string)[1]
        string = re.findall(r'ip address ([\d.]{7,}) ([\d.]{7,})', string)
        output[name] = string if string else None

    return output

pprint(parse_cfg('config_r2.txt'))
