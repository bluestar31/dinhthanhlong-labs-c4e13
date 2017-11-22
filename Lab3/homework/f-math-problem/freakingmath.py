from random import *
def eval(x, y, operation_choice):
    if operation_choice == '+':
        true_result = x + y
    elif operation_choice == '-':
        true_result = x - y
    elif operation_choice == '*':
        true_result = x * y
    elif operation_choice == '/':
        true_result = x / y
    return true_result


def generate_quiz():
    operation = ['+', '-', '*', '/']
    x = randint(0, 10)
    y = randint(1, 10)
    operation_choice = choice(operation)
    error = randint(-1, 1)
    true_result = eval(x, y, operation_choice)
    result = true_result + error
    return [x, y, operation_choice, result]

def check_answer(x, y, op, result, user_choice):
    true_result = eval(x, y, op)
    if true_result == result:
        if user_choice:
            return True
        else:
            return False
    else:
        if user_choice:
            return False
        else:
            return True
    pass
