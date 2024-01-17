num1 = eval(input("Please enter the first number: "))
num2 = eval(input("Please enter the second number: "))
operator = input("please provide the operator to be performed('+','-','/','*'): ")

def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)

if (operator == '+'):
    result= add(num1,num2)
    print(f'Addition of {num1} and {num2}: {result}')
elif (operator == '-'):
    result = sub(num1,num2)
    print(f'Subtraction of {num1} and {num2}: {result}')
elif (operator == '*'):
    result = mul(num1,num2)
    print(f'Multiplication of {num1} and {num2}: {result}')
elif (operator == '/'):
    result = div(num1,num2)
    print(f'Division of {num1} and {num2}: {result}')
else:
    print("Please provide the valid input")