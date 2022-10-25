import random 

def create_list(k):
    m = []
    for i in range(k):
        m.append(random.randint(0,100)) 
    return m
    
def add_write():
    data_file = ''
    if len(m) < 1:
        data_file = 'x = 0'
    else:
        for i in range(len(m)):
            if i != len(m) - 1 and m[i] != 0 and i != len(m) - 2:
                data_file += f'{m[i]}x^{len(m)-i-1}'
                if m[i+1] != 0:
                    data_file += ' + '
            elif i == len(m) - 2 and m[i] != 0:
                data_file += f'{m[i]}x'
                if m[i+1] != 0:
                    data_file += ' + '
            elif i == len(m) - 1 and m[i] != 0:
                data_file += f'{m[i]} = 0'
            elif i == len(m) - 1 and m[i] == 0:
                data_file += ' = 0'
    print(data_file)
    return data_file

k = int(input("Введите степень k = "))
m = create_list(k)

with open('data.txt', 'w') as data:
    data.write(add_write())