num=int(input("Enter a number: "))
result=0
while(num>0):
    r=num%10
    result=result+r
    num=num//10     #floor division

print("sum = "+str(result))
