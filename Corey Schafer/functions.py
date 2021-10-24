# def hello_func(greeting,name):
#     return(f'{greeting} {name}')

#  print(hello_func().upper()
# print(hello_func('HI','Aijaz'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

# student_info('Aijaz','18600006','Comp Science',section='A',address='Srinagar')

courses = ['Math','Science']
info = {'name':'Aijaz','age':22}
student_info(*courses,**info)
