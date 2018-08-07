###############################################################################
# DO NOT EDIT ANYTHING IN THIS FILE                                           #
###############################################################################
import os

rows, columns = os.popen('stty size', 'r').read().split()
maxLength = int(columns) - 1
ellipsisLength = maxLength - 4

def run(tests):
    print('')
    print('==============================')
    print('| TEST RESULTS:              |')
    print('==============================')
    print('')

    oneFailed = False
    for item in tests():
        if oneFailed:
            continue

        test = item['test']
        description = item['description']

        try:
            result = test(function)
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
