def equate(eq):
    global op1, op, op2, sign, result
    op1, op, op2, sign, result = eq.split()
    if op1.lower() == 'x':
        op2, result = int(op2), int(result)
        if op == '+':
            print(result - op2)
        elif op == '-':
            print(result + op2)
        elif op == '*':
            print(result / op2)
        elif op == '/':
            print(result * op2)
    elif op2.lower() == 'x':
        op1, result = int(op1), int(result)
        if op == '+':
            print(result - op1)
        elif op == '-':
            print(op1 - result)
        elif op == '*':
            print(result / op1)
        elif op == '/':
            print(result * op1)     
a = 3
print(a = 5)  