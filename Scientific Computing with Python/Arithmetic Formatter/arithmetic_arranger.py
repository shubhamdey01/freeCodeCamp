def arithmetic_arranger(problems, flag=False):
    # too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    op1, opr, op2 = [], [], []  # to store operands and operators
    length = []  # to store length of each problem

    # splitting the problems
    for prob in problems:
        ele = prob.split()
        op1.append(ele[0])
        opr.append(ele[1])
        op2.append(ele[2])
        length.append((len(ele[0]) + 2) if (len(ele[0]) > len(ele[2])) else (len(ele[2]) + 2))

    # checking for errors
    for i in range(len(problems)):
        if opr[i] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if len(op1[i]) > 4 or len(op2[i]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not op1[i].isdigit() or not op2[i].isdigit():
            return "Error: Numbers must only contain digits."

    # to store the output row by row
    str1, str2, str3, str4 = "", "", "", ""

    # caulculating the output
    for i in range(len(problems)):
        str1 += ' ' * (length[i] - len(op1[i])) + op1[i]
        str2 += opr[i] + ' ' * (length[i] - len(op2[i]) - 1) + op2[i]
        str3 += '-' * length[i]
        
        if opr[i] == '+':
            str4 += ' ' * (length[i] - len(str(int(op1[i]) + int(op2[i])))) + str(int(op1[i]) + int(op2[i]))
        else:
            str4 += ' ' * (length[i] - len(str(int(op1[i]) - int(op2[i])))) + str(int(op1[i]) - int(op2[i]))
            
        if i < len(problems) - 1:
            str1 += ' ' * 4
            str2 += ' ' * 4
            str3 += ' ' * 4
            str4 += ' ' * 4

    # final string to be returned
    arranged_problems = ""
    if flag == False:
        arranged_problems = str1 + '\n' + str2 + '\n' + str3
    else:
        arranged_problems = str1 + '\n' + str2 + '\n' + str3 + '\n' + str4

    return arranged_problems
