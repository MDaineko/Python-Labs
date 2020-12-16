ignore = ['duplex', 'alias', 'Current configuration']
with open('config_sw1.txt','r') as f:
    for line in f:
        Ku = True
        for i in range(3):
            if ignore[i] in line:
                Ku = False
                break
        if not '!' in line and not '\n' == line[0] and Ku:
            print(line[:-1])
