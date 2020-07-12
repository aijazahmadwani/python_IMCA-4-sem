l=[1,2,3,4,5]   # l is list
d={'a':1,'b':10,'c':8,'d':3}    # d is dictionary
print(d.keys())
for i in l:
    if i not in d.values():
        print(i)
