tunnel = """ 
Protocol: {}\nPrefix: {}\nAD/Metrix: {}\nNext-Hop: {}\nLast update: {}\nOutbound: {}
"""

with open('ospf.txt', 'r') as f:
    for line in f:
        a = line.split('\n')[0].replace(',','').replace('[','').replace(']','').replace('O','OSPF').split()
        a.remove('via')
        Protocol,Prefix,Metrix,Next,update,outbound = a
        print(tunnel.format(Protocol,Prefix,Metrix,Next,update,outbound))
