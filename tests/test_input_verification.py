from audioop import minmax
import unittest
from src.utils import isFuncEmpty, isFuncCharsValid, isFuncExpValid, isMinValid, isMaxValid, isMinLargerThanMax, verifyInput
from src.errorCodes import errors, getErrorMsg

class TestInputVerification(unittest.TestCase):
    def test_isFuncEmpty(self):
        # Test 1
        functionField = ''
        output = isFuncEmpty(functionField)
        self.assertEqual(output, errors.EMPTY_FUNC_VAL, functionField)

        # Test 2
        functionField = '3*x + 2'
        output = isFuncEmpty(functionField)
        self.assertEqual(output, errors.SUCCESS, functionField)
    
    def test_isFuncCharsValid(self):
        validFunctionFields = ['30', '12 * 4.5 * x', '6.7*x', ' 89+x ', '30*x', '3.0^x + 2 / 3']
        invalidFunctionFields = ['30X', 'X + Y', 'Z / W', 'z ** l', 'x ** 2']
        for field in validFunctionFields:
            output = isFuncCharsValid(field)
            self.assertEqual(output, errors.SUCCESS, field)
        for field in invalidFunctionFields:
            output = isFuncCharsValid(field)
            self.assertEqual(output, errors.INVALID_FUNC_CHAR, field)

    def test_isFuncExpValid(self):
        validFunctionExpressions = ['30', '12 * 4.5 * x', '6.7*x', ' 89+x ', '30*x', '3.0^x + 2 / 3']
        invalidFunctionExpressions = ['30X', 'x++', 'x += 1']
        for expression in validFunctionExpressions:
            output = isFuncExpValid(expression)
            self.assertEqual(output, errors.SUCCESS, expression)
        for expression in invalidFunctionExpressions:
            output = isFuncExpValid(expression)
            self.assertEqual(output, errors.INVALID_FUNC_EXPRESSION, expression)
        
    def test_isMinValid(self):
        validMinValues = ['1', '-1', '5', '-10', '10.0', '3.5',]
        invalidMinValues = ['x', '', '3  + 2', '.', '3 / 2']
        for minValue in validMinValues:
            output = isMinValid(minValue)
            self.assertEqual(output, errors.SUCCESS, minValue)
        for minValue in invalidMinValues:
            output = isMinValid(minValue)
            self.assertEqual(output, errors.INVALID_MIN_VAL, minValue)

    def test_isMaxValid(self):
        validMaxValues = ['1', '-1', '5', '-10', '10.0', '3.5',]
        invalidMaxValues = ['x', '', '3 + 2', '.', '3 / 2']
        for maxValue in validMaxValues:
            output = isMaxValid(maxValue)
            self.assertEqual(output, errors.SUCCESS, maxValue)
        for maxValue in invalidMaxValues:
            output = isMaxValid(maxValue)
            self.assertEqual(output, errors.INVALID_MAX_VAL, maxValue)
    
    def test_isMinLargerThanMax(self):
        validMinMaxValuePairs = [('1', '2'), ('2', '10'), ('-10', '190'), ('-999', '1')]
        invalidMinMaxValuePairs = [('2', '1'), ('10', '2'), ('199', '-10'), ('999', '-1')]
        for minMaxValuePair in validMinMaxValuePairs:
            output = isMinLargerThanMax(minMaxValuePair[0], minMaxValuePair[1])            
            self.assertEqual(output, errors.SUCCESS, minMaxValuePair)
        for minMaxValuePair in invalidMinMaxValuePairs:
            output = isMinLargerThanMax(minMaxValuePair[0], minMaxValuePair[1])
            self.assertEqual(output, errors.MIN_BIGGER_THAN_MAX, minMaxValuePair)
    

if __name__ == '__main__':
    unittest.main()
