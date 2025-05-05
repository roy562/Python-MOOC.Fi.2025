# Write your solution here
def validate_expression(parts:list):
    expr = parts[1]
    total = int(parts[2].strip())

    if parts[1].find('+') != -1:
        operator_index = expr.find('+')
        operand1 = int(expr[:operator_index])
        operand2 = int(expr[operator_index+1:])
        operands_result = operand1+operand2
    else:
        operator_index = expr.find('-')
        operand1 = int(expr[:operator_index])
        operand2 = int(expr[operator_index+1:])
        operands_result = operand1-operand2
    
    if operands_result == total:
        return True
    else:
        return False
    
def filter_solutions():
    correct = []
    incorrect = []

    open('correct.csv', 'w').close()
    open('incorrect.csv', 'w').close()

    with open('solutions.csv','r') as ip_file:
        for line in ip_file:
            parts = line.split(";")
            valid_expr = validate_expression(parts)
            if valid_expr:
                correct.append(line)
            else:
                incorrect.append(line)

    with open('correct.csv','w') as correct_file:
        for row in correct:
            correct_file.write(row)

    with open('incorrect.csv','w') as incorrect_file:
        for row in incorrect:
            incorrect_file.write(row)