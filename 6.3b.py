f = open('CAM_table.txt')
print(f.read())
with open('CAM_table.txt','r') as f:
    i = 0
    s = list('')
    for line in f:
        if '.' in line:
            s +=[line.split()]
s.sort()
vlan = str(input('Enter vlan,list vlan[100,200,300,400,500]:'))
for i in range (len(s)):
    a, b, c, d = s[i]
    if a == vlan:
        print('{}     {}    {}     {}'.format(a, b, c, d))