#7.1a
from pprint import pprint

access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}


def aceess_port_congig_generation(access: dict, psecurity: bool = False) -> list:
    out = []

    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport	nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']

    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']

    for k, v in access.items():
        out.append('interface ' + k)
        for i in access_template + port_security:
            if i == access_template[1]:
                out.append(f'{i} {v}')
            else:
                out.append(i)

    return out


pprint(aceess_port_congig_generation(access_dict))