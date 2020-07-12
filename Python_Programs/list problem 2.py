l = []
while True:
    answer=input("Do you want to add an item (y/n): ")
    if answer=='y':
        item = input("Enter item: ")
        if item in l: # if item is already present it will return True else False
            print("This item is already in your list")
        else:
            l.append(item)
    else:
        print(l)
        break
