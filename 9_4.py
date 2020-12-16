#9_4
import re
from pprint import pprint

def parse_sh_ip_int_br(filename):
    with open(filename) as f:
        data = f.read()

    regex = r'(\S+[\d/]+) +([\d.]+|unassigned) +YES (?:manual|unset  administratively) +(up|down) +(up|down)'
    output = re.findall(regex, data)

    return output

pprint(parse_sh_ip_int_br('sh_ip_int_br_2.txt'))
data = parse_sh_ip_int_br('sh_ip_int_br_2.txt')


#9_4a
fields = ['Intrface', 'IP-Address', 'Status', 'Protocol']

def convert_to_dict(fields: list, data: list):
    output = []
    for i in data:
        output.append(dict(zip(fields, i)))

    return output

pprint(convert_to_dict(fields, data))

