n1 = int(input())
n2 = int(input())
op = input()

if op == '+':
    print("Result:",n1+n2)

elif op == '-':
    print("Result:",n1-n2)

elif op == '*':
    print("Result:",n1*n2)

elif op == '/':
    if n2!=0:
        print("Result:",n1/n2)
    else:
        print("Division by zero not allowed")

elif op == '%':
    if n2!= 0:
        print("Result:", n1%n2)
    else:
        print("Modulus by zero not allowed")

else:
    print("Invalid operator")
