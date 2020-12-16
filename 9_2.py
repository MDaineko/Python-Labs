#9_2
import re
def return_match(filename, reg_e):
    with open(filename) as f:
        file = f.read()
        print(re.findall(reg_e, file))

return_match('sh_ip_int_br.txt', r'\d+\.\d+\.\d+\.\d+')
