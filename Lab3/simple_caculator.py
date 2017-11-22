def eval(x, y, op):
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        if y == 0:
            print('NaN')
        else:
            result = x / y
    return result

# x1 = 10
# y2 = 5
# op3 = '*'
# r = eval(x1, y2, op3)
# print(r)

# x = int(input('x = '))
# op = input('Operation (+,-,*,/): ')
# y = int(input('y = '))
#
# if op in ['+', '-', '*', '/']:
#     r = eval()
#     print(r)
# else:
#     print('Operation is not available')
