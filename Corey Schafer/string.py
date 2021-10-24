message = 'Hello World'
#print(message)
#print(len(message)) #length of string
#print(message[0])   #access character of string
#print(message[0:5]) #slicing

#print(message.lower())
#print(message.upper())
#print(message.count('Hello'))
#print(message.find('o'))
# print(message.replace('World','Aijaz'))
s1 = 'aijaz'
s2 = 'ahmad'
s3 = 'wani'
message = s1 +' ' + s2 + ' ' + s3
# print(message)

message = 'Welcome {} {} {}!'.format(s1,s2,s3)
# print(message)

message = f'Welcome {s1} {s2} {s3}!'
# print(message)
print(dir(message)) #prints all attributes and methods