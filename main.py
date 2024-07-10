# BOS
# Boolean operation system

__author__ = 'VDN'
__email__ = 'nikolaev.v.d@ya.ru'
__version__ = '0.0.0'

import operations

booleans = dict()


def operation_parser(operation_str):
    operation_str = operation_str.replace('!', '_n').replace('-', '_n').replace('&', '_a_').replace('|', '_o_').\
                    replace('||', '_x_').replace('==', '_e_').replace('_ne_', '!=').replace('>', '_m_').\
                    replace('<', '_l_').replace('>=', '_me_').replace('<=', '_le_')
    for key, value in booleans.items():
        operation_str = operation_str.replace(key, str(value))
    while '_n' in operation_str:
        if '_n' in operation_str:
            index = operation_str.index('_n')
            val_name = operation_str[index + 2]
            val = (False if val_name == '0' else True)
            operation_str = operation_str.replace(f'_n{val_name}', str(operations._not(val)))
    while '_a_' in operation_str or '_o_' in operation_str or '_x_' in operation_str:
        if '_a_' in operation_str:
            index = operation_str.index('_a_')
            valA_name = operation_str[index - 1]
            valA = (False if valA_name == '0' else True)
            valB_name = operation_str[index + 3]
            valB = (False if valB_name == '0' else True)
            operation_str = operation_str.replace(f'{valA_name}_a_{valB_name}', str(operations._and(valA, valB)))
        if '_o_' in operation_str:
            index = operation_str.index('_o_')
            valA_name = operation_str[index - 1]
            valA = (False if valA_name == '0' else True)
            valB_name = operation_str[index + 3]
            valB = (False if valB_name == '0' else True)
            operation_str = operation_str.replace(f'{valA_name}_o_{valB_name}', str(operations._or(valA, valB)))
        if '_x_' in operation_str:
            index = operation_str.index('_x_')
            valA_name = operation_str[index - 1]
            valA = (False if valA_name == '0' else True)
            valB_name = operation_str[index + 3]
            valB = (False if valB_name == '0' else True)
            operation_str = operation_str.replace(f'{valA_name}_x_{valB_name}', str(operations._xor(valA, valB)))
    while '_e_' in operation_str or '!=' in operation_str or '_m_' in operation_str or '_l_' in operation_str:
        if '!=' in operation_str:
            index = operation_str.index('!=')
            valA_name = operation_str[index - 1]
            valA = (False if valA_name == '0' else True)
            valB_name = operation_str[index + 2]
            valB = (False if valB_name == '0' else True)
            operation_str = operation_str.replace(f'{valA_name}!={valB_name}', str(operations._neq(valA, valB)))
        if '_e_' in operation_str:
            index = operation_str.index('_e_')
            valA_name = operation_str[index - 1]
            valA = (False if valA_name == '0' else True)
            valB_name = operation_str[index + 3]
            valB = (False if valB_name == '0' else True)
            operation_str = operation_str.replace(f'{valA_name}_e_{valB_name}', str(operations._eq(valA, valB)))
        if '_m_' in operation_str:
            index = operation_str.index('_m_')
            valA_name = operation_str[index - 1]
            valA = (False if valA_name == '0' else True)
            valB_name = operation_str[index + 3]
            valB = (False if valB_name == '0' else True)
            operation_str = operation_str.replace(f'{valA_name}_m_{valB_name}', str(operations._more(valA, valB)))
        if '_l_' in operation_str:
            index = operation_str.index('_l_')
            valA_name = operation_str[index - 1]
            valA = (False if valA_name == '0' else True)
            valB_name = operation_str[index + 3]
            valB = (False if valB_name == '0' else True)
            operation_str = operation_str.replace(f'{valA_name}_l_{valB_name}', str(operations._less(valA, valB)))
    while '_me_' in operation_str or '_le_' in operation_str:
        if '_me_' in operation_str:
            print(operation_str)
            index = operation_str.index('_me_')
            valA_name = operation_str[index - 1]
            valA = (False if valA_name == '0' else True)
            valB_name = operation_str[index + 4]
            valB = (False if valB_name == '0' else True)
            print(valA, valB, operations._me(valA, valB))
            operation_str = operation_str.replace(f'{valA_name}_me_{valB_name}', str(operations._me(valA, valB)))
            print(operation_str)
        if '_le_' in operation_str:
            index = operation_str.index('_le_')
            valA_name = operation_str[index - 1]
            valA = (False if valA_name == '0' else True)
            valB_name = operation_str[index + 4]
            valB = (False if valB_name == '0' else True)
            operation_str = operation_str.replace(f'{valA_name}_le_{valB_name}', str(operations._le(valA, valB)))
    return operation_str


def parse_str(string):
    string = string[:string.find("#")]
    string = string.split()
    if string == []: return -1

    if string[0] == 'v':
        type_str = 0
    else:
        type_str = 1

    if type_str == 0:
        name = string[1]
        value = string[2]
        return [type_str, name, value]
    else:
        out_v = string[1:]
        return [type_str, out_v]


def parse_file(filename):
    f = open(filename, 'r').readlines()
    for i in f:
        todo = parse_str(i)
        if todo == -1:
            continue
        if todo[0] == 0:
            if todo[2] == '0' or todo[2] == '1':
                booleans[todo[1]] = int(todo[2])
            else:
                booleans[todo[1]] = operation_parser(todo[2])
        else:
            out_list = " ".join(todo[1])
            for key, value in booleans.items():
                out_list = out_list.replace(key, str(value))
            print(out_list)


parse_file('code.bos')
