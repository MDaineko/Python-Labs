#3.7
MAC = 'AAAA:BBBB:CCCC'
print(''.join(format(ord(i), 'b') for i in MAC.replace(':', '')))