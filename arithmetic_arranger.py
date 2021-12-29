import re

def arithmetic_arranger(problems, ans=False):

    tmpArr = []
    out = ''
    space = 4

    for p in problems:
        arr = p.split()
        tmpArr.append(arr)

    # Check for user errors
    if len(problems) > 5:
        return 'Error: Too many problems.'


    for s in tmpArr:
        for t in s[::2]:
            if re.search(r'\D', t):
                return 'Error: Numbers must only contain digits.'
            if len(t) > 4:
                return 'Error: Numbers cannot be more than four digits.'

    for s in tmpArr:
        for t in s[1]:
            if re.search(r'[^+-]', t):
                return "Error: Operator must be '+' or '-'."

    arrLen = len(tmpArr)

    # Add the upper integers to string
    i = 0
    for o in tmpArr:
        out += ' ' * (max(len(x) for x in o) - len(o[0]) + 2)
        out += o[0]
        if i == arrLen - 1:
            out += '\n'
        else:
            i += 1
            out += ' ' * space


    # Add the second line of operators and integers
    i = 0
    for o in tmpArr:
        out += o[1]
        out += ' ' * (max(len(x) for x in o) - len(o[2]) + 1)
        out += o[2]
        if i == arrLen - 1:
            out += '\n'
        else:
            i += 1
            out +=  ' ' * space


    # Add the dashes in the third line
    i = 0
    for o in tmpArr:
        out += '-' * (max(len(x) for x in o) + 2)
        if i != arrLen - 1:
            i += 1
            out += ' ' * space


    # Add the answer if arg is given
    if ans:
        out += '\n'
        i = 0
        for o in tmpArr:
            if o[1] == '+':
                res = str(int(o[0]) + int(o[2]))
            elif o[1] == '-':
                res = str(int(o[0]) - int(o[2]))
            out += ' ' * (max(len(x) for x in o) - len(res) + 2)
            out += res
            if i != arrLen - 1:
                i += 1
                out += ' ' * space


    return out