def arithmetic_arranger(problems, display_solutions=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # get operators
    operators = list(map(lambda x: x.split()[1], problems))

    # check if all operators are + or -
    is_correct_operators = all(list(map(lambda x: x in ['+', '-'], operators)))
    if not is_correct_operators:
        return "Error: Operator must be '+' or '-'."

    # get all operands
    operands = []
    for arr in problems:
        items = arr.split()
        operands.extend([items[0], items[2]])

    # check if all operands are digit
    if not all(map(lambda x: x.isdigit(), operands)):
        return "Error: Numbers must only contain digits."

    # check if all operands are less than 10000
    if not all(map(lambda x: len(x) < 5, operands)):
        return "Error: Numbers cannot be more than four digits."
    
    # compute all values
    values = list(map(lambda x: eval(x), problems))
    top_row = ''
    bottom_row = ''
    dashes = ''
    solutions = ''

    # get even index
    top_values = operands[::2]

    # get odd index
    bottom_values = operands[1::2]

    for i in range(len(top_values)):
        space = max(len(top_values[i]), len(bottom_values[i])) + 2
        top_row += top_values[i].rjust(space)
        dashes += '-' * space
        solutions += str(values[i]).rjust(space)
        if i != len(top_values) - 1:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    for i in range(len(bottom_values)):
        space = max(len(top_values[i]), len(bottom_values[i]))
        bottom_row += operators[i] + ' ' + bottom_values[i].rjust(space)
        if i != len(bottom_values) - 1:
            bottom_row += ' ' * 4
        
    if display_solutions:
        arranged = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        arranged = '\n'.join((top_row, bottom_row, dashes))

    return arranged
    

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]))     
