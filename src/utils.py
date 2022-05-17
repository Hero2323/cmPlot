import sympy as sp
import numpy as np
import enum

class errors(enum.Enum):
    INVALID_FUNC_CHAR = 0
    INVALID_FUNC_EXPRESSION = 1
    INVALID_MAX_VAL = 2
    INVALID_MIN_VAL = 3
    EMPTY_FUNC_VAL = 4
    MIN_BIGGER_THAN_MAX = 5

def getErrorMsg(enumVal):
    errorMessages = {
        errors.EMPTY_FUNC_VAL: 'The function field cannot be empty',
        errors.INVALID_FUNC_CHAR: 'the Function field can only accept numbers, the operators + - / * ^ and the character \'x\' for variables',
        errors.INVALID_FUNC_EXPRESSION: 'Invalid Function Expression, please make sure that the expression is written correctly and that there is an operator between every two numbers/variables',
        errors.INVALID_MIN_VAL: 'Invalid Minimum Value, this field only accepts integers or floating decimals',
        errors.INVALID_MAX_VAL: 'Invalid Maximum Value, this field only accepts integers or floating decimals',
        errors.MIN_BIGGER_THAN_MAX: 'he minimum value can\'t be bigger than the maximum value'
    }
    return errorMessages[enumVal]


def get_x_y_vals(function_input, minVal, maxVal):
    if any(c not in ' /*+-^0123456789x.' for c in function_input):
        return False, errors.INVALID_FUNC_CHAR

    if function_input == '':
        return False, errors.EMPTY_FUNC_VAL

    try:
        minVal = float(minVal)
    except:
        return False, errors.INVALID_MIN_VAL

    try:
        maxVal = float(maxVal)
    except:
        return False, errors.INVALID_MAX_VAL

    if minVal > maxVal:
        return False, errors.MIN_BIGGER_THAN_MAX

    try:
        x = sp.Symbol('x')
        expr = sp.lambdify(x, function_input, 'math')
        num = (maxVal - minVal + 1) * 10
        axis = np.arange(start=minVal, stop=maxVal, step=1.0 / num)
        return True, (axis, expr(axis))
    except:
        return False, errors.INVALID_FUNC_EXPRESSION