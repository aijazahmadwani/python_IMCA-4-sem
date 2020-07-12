n=int(input("HOW MANY ITEMS YOU WANT TO STORE: "))
l=[]
print("Enter list items: ")
i=0
while(i<n):
    y = input("Enter item at "+ str(i)+" position: ")
    l.append(y)
    i=i+1


print("LIST AFTER ALPHABETICALLY ARRANGED: ")
l=sorted(l)
print(l)
print("Do you want to change any item in your list (y / n): ")
answer=input()

if(answer == 'y'):
    print("Enter item you want to change: ")
    change=input()
    i = l.index(change)
    name=input("Enter name: ")
    l[i]=name
    print("Successfuly changed\n")
    l=sorted(l)
    print(l)

    

    
