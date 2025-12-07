import re

def solve_p1(data):
    grand_total = 0
    for j in range(len(data[0])):
        column = [data[i][j] for i in range(len(data))]
        grand_total += eval(column[-1].join(column[:-1]))
    print('Part 1:', grand_total)

def solve_p2(data):
    grand_total = 0
    new_string = ''
    for j in range(len(data[0])-1, -1, -1):
        column = ''.join([data[i][j] for i in range(len(data))])
        new_string += column + ('|' if column[-1] in '*+' else '')
    equations = new_string.split('|')
    for equation in equations:
        if equation == '':
            continue
        parts = re.sub(r'\ +', ' ', equation).split(' ')
        if parts[-1] == '':
            del parts[-1]
        operator = parts[-1][-1]
        parts[-1] = parts[-1][:-1]
        parts = [x for x in parts if x != '']
        calculation = operator.join(parts)
        result = eval(calculation)
        grand_total += result
    print('Part 2:', grand_total)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:     
        raw_data = f.read()
    
    data = re.sub(r'\ *\n\ *', '\n', raw_data)
    data = data.split('\n')
    data = [re.sub(r'\ +', ' ', line).split(' ') for line in data]

    solve_p1(data)

    datap2 = raw_data.split('\n')
    solve_p2(datap2)
