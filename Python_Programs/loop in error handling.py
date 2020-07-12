# greater of two numbers
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
while True:
    try:
        if (int(num1) > int(num2)):
            print(num1+' is greater')
        else:
            print(num2+' is greater')
    except ValueError:
            print("Enter numeric values")
            print("Please enter again: ")
            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")
            continue
            
    else:
        print("Two numbers compared successfully")
        break
    
