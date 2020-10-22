#CALCULATOR
while 1:
    op = input("enter your calculation method:\n")
    calc1 = int(input("Enter your number:\n"))
    calc2 = int(input("enter second number:\n"))

    if op == '1':
        print("Addition is:\n", calc1+calc2)

    elif op == '-':
        print("Subtraction is:\n", calc1-calc2)

    elif op == '/':
        print("Division is:\n", calc1/calc2)

    elif op == '*':
        print("Multiplication is:\n", calc1*calc2)