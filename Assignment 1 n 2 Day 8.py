# Assignment 1 Day 8

# write a decorator function for taking input for you 
# any kind of function you want to build

def getInput(calculate_arg_fuc):
    def wrap_function():
        print("Enter two numbers  ")
        a=int(input("Enter first number = "))
        b=int(input("Enter second number = "))
        calculate_arg_fuc(a,b)

    return wrap_function

@getInput
def addition(num1,num2):
    print("Addition = ",num1+num2)

@getInput
def subtraction(num1,num2):
    print("Subtraction = ",num1-num2)

@getInput
def multiplication(num1,num2):
    print("Multiplication = ",num1*num2)

@getInput
def division(num1,num2):
    print("Division = ",num1/num2)

addition()
subtraction()
multiplication()
division()


# Assignment 2  day 8

# you need to develop a python program to open a file in read only mode and 
# try writing something to it and handlethe subsequent errorusing Exception Handling

try:
    f=open("abc.txt","r");
    f.write("Heyy, i am prajval");
    f.close();

except:
    print("File is in read only mode...")
