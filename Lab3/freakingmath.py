from random import randint, choice
from simple_caculator import eval

operation = ['+', '-', '*', '/']

check = True

while check:
    x = randint(0, 9)
    y = randint(0, 9)
    operation_choice = choice(operation)
    if operation_choice == '+':
        true_result = x + y
    elif operation_choice == '-':
        true_result = x - y
    elif operation_choice == '*':
        true_result = x * y
    elif operation_choice == '/':
        true_result = x / y
    error = randint(-1, 1)
    result = true_result + error
    print('*' * 10)
    print('{0} {1} {2} = {3}'.format(x, operation_choice, y, result))
    print('*' * 10)
    answer = input('Y/N? ')
    if answer.upper() in ['Y', 'N']:
        if answer.upper() == 'Y':
            if result == real_result:
                print('Yay')
            else:
                print('Wrong')
                check = False
        elif answer.upper() == 'N':
            if result != true_result:
                print('Yay')
            else:
                print('Wrong')
                check = False
    else:
        print('Your input is unavailable')
