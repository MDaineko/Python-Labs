with open('config_sw1.txt','r') as f:
    for line in f:
        if not '!' in line and not '\n' == line[0]:
            print(line[:-1])

