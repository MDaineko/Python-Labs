#7.2
from pprint import pprint

trunk = {'FastEthernet0/1': [10, 20],
         'FastEthernet0/2': [11, 30],
         'FastEthernet0/4': [17]}


def trunk_port_config_generator(trunk: dict) -> list:
    out = []

    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']

    for k, v in trunk.items():
        out.append('interface ' + k)
        for i in trunk_template:
            if i == trunk_template[-1]:
                out.append(f'{i} {str(v).replace("[", "").replace("]", "")}')
            else:
                out.append(i)
    return out


pprint(trunk_port_config_generator(trunk))