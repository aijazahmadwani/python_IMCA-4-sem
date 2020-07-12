# greater of two numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

try:
    if (int(num1) > int(num2)):
        print(num1+' is greater')
    else:
        print(num2+' is greater')
except ValueError:
        print("please enter numeric value")
else:
    print("Two numbers compared successfully")
finally:
    print("Program executed")
