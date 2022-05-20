import sympy as sp
import numpy as np
from .errorCodes import errors, getErrorMsg

def isFuncEmpty(function_input):
    """Check if the Function string is empty.

    Parameters
    ----------
    function_input : str
        the input of the function field

    """

    if function_input == '':
        return errors.EMPTY_FUNC_VAL
    return errors.SUCCESS


def isFuncCharsValid(function_input):

    """Check if the Function string contains invalid characters.


    valid characters are numbers, operators '+', '-', '*', '/', '^' and '.' for float numbers.If any other 
    characters are detected in the string, this function will find out and return the corresponding error code.
    Other operators that are made up of multiple characters like '++' or '**' will also be detected and are not allowed.

    Parameters
    ----------
    function_input : str
        the input of the function field

    """

    if any(c not in ' /*+-^0123456789x.' for c in function_input):
        return errors.INVALID_FUNC_CHAR
    if '**' in function_input or '++' in function_input:
        return errors.INVALID_FUNC_CHAR
    if '--' in function_input or '//' in function_input:
        return errors.INVALID_FUNC_CHAR
    if '^^' in function_input or 'xx' in function_input:
        return errors.INVALID_FUNC_CHAR

    return errors.SUCCESS


def isFuncExpValid(function_input):

    """Checks if the function expression is valid.


    This basically checks if the expression raises an exception during calculation and catches it if it does.

    Parameters
    ----------
    function_input : str
        the input of the function field

    """

    try:
        x = sp.Symbol('x')
        expr = sp.lambdify(x, function_input, 'math')
        return errors.SUCCESS
    except:
        return errors.INVALID_FUNC_EXPRESSION


def isMinValid(minVal):

    """Checks if the minimum value is valid.

    it checks if casting the minimum value to float would raise an exception and catches it, this usually happens if the field
    is empty or contains things other than numbers. 

    Parameters
    ----------
    minVal : str
        the input of the minimum value field

    """
    try:
        minVal = float(minVal)
        return errors.SUCCESS
    except:
        return errors.INVALID_MIN_VAL


def isMaxValid(maxVal):

    """Checks if the maximum value is valid.

    it checks if casting the maximum value to float would raise an exception and catches it, this usually happens if the field
    is empty or contains things other than numbers. 

    Parameters
    ----------
    maxVal : str
        the input of the maximum value field

    """
    try:
        minVal = float(maxVal)
        return errors.SUCCESS
    except:
        return errors.INVALID_MAX_VAL


def isMinLargerThanMax(minVal, maxVal):

    """Checks if the minimum value is larger than the maximum value.

    Parameters
    ----------
    minVal : str
        the input of the minimum value field

    maxVal : str
        the input of the maximum value field

    """
    try:
        if float(minVal) >= float(maxVal):
            return errors.MIN_BIGGER_THAN_MAX
        return errors.SUCCESS
    except:
        return errors.MIN_BIGGER_THAN_MAX # Placeholder, this doesn't matter

# def isInvalidNumberCalc(function_input, minVal, maxVal):
#     warnings.filterwarnings("error")
#     try:
#         x = sp.Symbol('x')
#         expr = sp.lambdify(x, function_input, 'math')
#         minVal = float(minVal)
#         maxVal = float(maxVal)
#         num = (maxVal - minVal + 1) * 10
#         x_axis = np.arange(start=minVal, stop=maxVal, step=1.0 / num)
#         y_axis = expr(x_axis)
        # for y in y_axis:
        #     if np.isnan(y):
        #         return errors.INVALID_NUMBER_CALC

        # y_axis = np.array(y_axis)
        # y_axis_range = y_axis[(y_axis > np.quantile(y_axis, 0.02)) and (y_axis < np.quantile(y_axis, 0.98))]
        # y_axis_range_median = np.median(y_axis_range)

        # if any(y > 1000 * np.median(y_axis) for y in y_axis):
        #     return errors.INVALID_NUMBER_CALC

    #     return errors.SUCCESS
    # except :
    #     return errors.INVALID_NUMBER_CALC

def verifyInput(function_input, minVal, maxVal):

    """This function calls all the verification functions in order of priority and returns the corresponding error message
    if an error is detected and returns True otherwise.


    Parameters
    ----------
    function_input : str
        the input of the function field

    minVal : str
        the input of the minimum value field

    maxVal : str
        the input of the maximum value field

    Returns
    -------
    enum
        errors.SUCCESS if there are no errors in the function input
    str
        the error message to be displayed to the user if there are errors in the function input
    """

    errorCodes = [
        isFuncEmpty(function_input),
        isFuncCharsValid(function_input),
        isFuncExpValid(function_input),
        isMinValid(minVal),
        isMaxValid(maxVal),
        isMinLargerThanMax(minVal, maxVal),
    ]
    for errorCode in errorCodes:
        if errorCode != errors.SUCCESS:
            return getErrorMsg(errorCode)

    return errors.SUCCESS


def get_x_y_vals(function_input, minVal, maxVal):

    """This function transforms the function input from a string into a mathematical expression and calculates the output given
    inputs between minVal & maxVal

    it first checks the input using the verifyInput function and then uses the sympy library to transform it into a mathematical expression
    then it makes a list of numbers between minVal and maxVal that's between 50 & 100 in length and calculates the value of the 
    expression for all of those values.


    Parameters
    ----------
    function_input : str
        the input of the function field
        
    minVal : str
        the input of the minimum value field

    maxVal : str
        the input of the maximum value field

    Returns
    -------
    bool
        whether there was an error detected in the verification step or not
    
    tuple
        (x_axis, y_axis) that were calculated so they can be plotted

    str
        if the previous bool is False, instead of the tuple, it returns an error message to be displayed to the user
    """

    validInput = verifyInput(function_input, minVal, maxVal)
    
    if validInput != errors.SUCCESS:
        return False, validInput 
    
    x = sp.Symbol('x')
    expr = sp.lambdify(x, function_input, 'math')
    minVal = float(minVal)
    maxVal = float(maxVal)
    num = (maxVal - minVal + 1)
    if num < 50:
        num = 50
    if num > 100:
        num = 100
    axis = np.arange(start=minVal, stop=maxVal, step=1.0 / num)
    expr = expr(axis)

    if type(expr) != np.ndarray:
        if np.isnan(expr):
            return False, getErrorMsg(errors.ALL_NAN)
        else:
            expr = [expr for i in range(len(axis))]

    for i in range(len(expr)):
        if np.isnan(expr[i]):
            expr[i] =  np.inf 
        elif np.abs(expr[i]) > np.abs(np.median(expr)) * 1000:
            expr[i] =  np.inf * np.sign(expr[i])
    
    
    

    return True, (axis, expr)
