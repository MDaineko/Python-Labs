#3.4
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
vlan1 = command1.split('vlan ')[1].split(',')
vlan2 = command2.split('vlan ')[1].split(',')
result = []
for num in vlan1:
    if num in vlan2:
        result.append(num)
print(result)