#3.6
ospf_route = '10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split()
print('protocol\tOSPF\n'
      'prefix\t{}\n'
      'AD/metric\t{}\n'
      'Next-hop\t{}\n'
      'Last update\t{}\n'
      'Outbound Intreface\t{}\n'.format(ospf_route[0],
                                        ospf_route[1],
                                        ospf_route[3].rstrip(','),
                                        ospf_route[4].rstrip(','),
                                        ospf_route[5]))
print(ospf_route)