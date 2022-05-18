import enum

class errors(enum.Enum):

    """
    An enum class that contains the error codes that the various verification functions output.

    
    """
    INVALID_FUNC_CHAR = 0
    INVALID_FUNC_EXPRESSION = 1
    INVALID_MAX_VAL = 2
    INVALID_MIN_VAL = 3
    EMPTY_FUNC_VAL = 4
    MIN_BIGGER_THAN_MAX = 5
    ALL_NAN = 6
    SUCCESS = 7

def getErrorMsg(enumVal):

    """
    This function maps the error codes from the errors enum to the message that will be displayed to the user.

    Parameters
    ----------
    enumVal : enum
        the enumCode returned by the verification function.
    
    Returns
    -------
    str
        the error message that is to be displayed to the user.

    
    """

    errorMessages = {
        errors.EMPTY_FUNC_VAL: 'The function field cannot be empty',
        errors.INVALID_FUNC_CHAR: 'the Function field can only accept numbers, the operators + - / * ^ and the character \'x\' for variables',
        errors.INVALID_FUNC_EXPRESSION: 'Invalid Function Expression, please make sure that the expression is written correctly and that there is an operator between every two numbers/variables',
        errors.INVALID_MIN_VAL: 'Invalid Minimum Value, this field only accepts integers or floating decimals',
        errors.INVALID_MAX_VAL: 'Invalid Maximum Value, this field only accepts integers or floating decimals',
        errors.MIN_BIGGER_THAN_MAX: 'he minimum value can\'t be bigger than the maximum value',
        errors.ALL_NAN: 'Invalid input, all inputs are division by zero, which can\'t be drawn',
        errors.SUCCESS: 'Success!',
    }
    return errorMessages[enumVal]