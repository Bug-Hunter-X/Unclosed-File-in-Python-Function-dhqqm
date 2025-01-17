def function_with_unclosed_file(filename):
    file = open(filename, 'w')
    file.write('This file will not be closed!')
    # Missing file.close() or using 'with' statement

function_with_unclosed_file('my_file.txt')