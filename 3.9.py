#3.9
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