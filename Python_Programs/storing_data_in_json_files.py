import json
#----------writing to json file
filename="numbers.json"
sentence="hello this is Aijaz"
with open(filename,'w') as file_object:
    json.dump(sentence,file_object)

#---------reading from json file
with open(filename) as file_object:
    data=json.load(file_object)
print(data)
