def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n* recur_factorial(n-1) 
    
num = int(input("Enter a number :"))

if num < 0:
    print("Sorry! the factorial of number doesnot exist")
elif num==0 :
    print( "The factorial of 0 is 1")
else :
    print("The factoraial of number", num , recur_factorial(num))
