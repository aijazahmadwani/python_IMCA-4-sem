
def ap(a,d,l):
    sum=0
    for i in range(a,l+1,d):
        sum=sum+i
    return sum

first_term = int(input("Enter first term of A.P.: "))
diff = int(input("Enter common difference: "))
n = int(input("Enter no. of terms: "))
l = first_term+(n-1)*diff
print(ap(first_term,diff,l))

