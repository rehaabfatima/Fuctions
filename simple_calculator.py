def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x / y

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

print("Addition :" , add(num1,num2))
print("Subtraction :" , sub(num1,num2))
print("Multiplication :" , mul(num1,num2))
print("Quotient :" , div(num1,num2))