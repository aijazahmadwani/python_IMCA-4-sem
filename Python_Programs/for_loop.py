# sum upto a number
def sum(num):
    result=0
    for i in range(1,num+1):
        result=result+i
    return result
num=int(input("Enter number: "))
print("SUM = "+ str(sum(num)))
