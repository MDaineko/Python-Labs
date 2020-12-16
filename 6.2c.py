ignore = ['duplex', 'alias', 'Current configuration']
open_file = input('File to open: ')
write_file = input('Final config file: ')
with open(open_file,'r') as f, open(write_file,'w+') as f1:
    for line in f:
        k = True
        for i in range(3):
            if ignore[i] in line:
                k = False
                break
        if not '!' in line and not '\n' == line[0] and k:
            print(line)
            f1.write(line)