NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(NAT.replace('FastEthernet', 'GigabitEthernet'))
MAC = 'AAAA:BBBB:CCCC'
print(MAC.replace(':', '.'))


CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
def parse(command):
    return command.split('vlan ')[1].split(',')
print(parse(CONFIG))


command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
vlan1 = parse(command1)
vlan2 = parse(command2)
result = []
for num in vlan1:
    if num in vlan2:
        result.append(num)
print(result)


VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(sorted(list(set(VLANS))))


ospf_route = '10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.split(' ')
print('protocol\tOSPF\n'
      'prefix\t{}\n'
      'AD/metric\t{}\n'
      'Next-hop\t{}\n'
      'Last update\t{}\n'
      'Putbound Intreface\t{}\n'.format(ospf_route[0],
                                        ospf_route[1],
                                        ospf_route[3].rstrip(','),
                                        ospf_route[4].rstrip(','),
                                        ospf_route[5]))


MAC = 'AAAA:BBBB:CCCC'
print(''.join(format(ord(i), 'b') for i in MAC.replace(':', '')))


IP = '192.168.3.1'
IP = IP.split('.')
for num in IP:
    print(num, end="        ")
print('')
temp_list = []
for num in IP:
    temp_list.append(bin(int(num)).lstrip('0b'))
for i in range(0, len(temp_list)):
    k = len(temp_list[i])
    if k < 8:
        temp_list[i] = '0'*(8 - k) + temp_list[i]
    print(temp_list[i], end=" ")
print('\n')


num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
el = input('Введите елемент: ')
index = None
try:
    el = int(el)
    print('Вы ввели число')
    for i in range(0, len(num_list)):
        if el == num_list[i]:
            index = i
except:
    print('Вы ввели строку')
    for i in range(0, len(word_list)):
        if el == word_list[i]:
            index = i
print(index)