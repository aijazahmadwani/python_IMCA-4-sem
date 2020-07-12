# list containing dictionaries

user1 = {'name':'aijaz','age':'20'}
user2 = {'name':'sahil','age':'22'}
users = [user1,user2]
for i in users:
    for u,n in i.items():
        print('\n'+" user's "+ str(u)+' is '+str(n))
