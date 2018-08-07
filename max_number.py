# Here is the task I would like you to accomplish
# I want you to define a function that takes in a list of integers as an
# argument and returns the highest integer from the list
#
# YOUR CODE SHOULD START ON LINE 6:



###############################################################################
# DO NOT EDIT ANYTHING BELOW THIS LINE                                        #
###############################################################################
from types import *
import os

rows, columns = os.popen('stty size', 'r').read().split()
maxLength = int(columns) - 1
ellipsisLength = maxLength - 4

tests = {
    1: {
        'description': 'The variable \'max_number\' should be defined',
        'function': lambda a : max_number is not None,
    },
    2: {
        'description': 'The variable \'max_number\' should be a function',
        'function': lambda a : type(max_number) is FunctionType,
    },
    3: {
        'description': '\'max_number\' should take a list as an argument',
        'function': lambda a : max_number([]) == max_number([]),
    },
    4: {
        'description': '\'max_number\' should return False for an empty list',
        'function': lambda a : max_number([]) is False,
    },
    5: {
        'description': '\'max_number\' should return an integer for valid input',
        'function': lambda a : type(max_number([1])) is int,
    },
    6: {
        'description': '\'max_number\' should return 3 from [1, 2, 3]',
        'function': lambda a : max_number([1,2,3]) is 3,
    },
    7: {
        'description': '\'max_number\' should return handle negative integers',
        'function': lambda a : max_number([-1,-2,-3]) is -1,
    },
    8: {
        'description': '\'max_number\' should return handle negative infinity',
        'function': lambda a : max_number([-9e99999]) == -9e99999,
    },
}

print('')
print('==============================')
print('| TEST RESULTS:              |')
print('==============================')
print('')

oneFailed = False
for key in tests:
    if oneFailed:
        continue

    test = tests[key]
    function = test['function']
    description = test['description']

    try:
        result = function(key)
    except:
        result = False

    if result is False:
        oneFailed = True

    resultString = description

    if len(resultString) > ellipsisLength:
        resultString = resultString[0:ellipsisLength] + '...'

    while len(resultString) < maxLength:
        resultString += ' '


    if (result):
        resultString += '✓'
    else:
        resultString += '×'

    print(resultString)

print('')
if not oneFailed:
    print('You passed all the tests! Good goin!')
print('')
