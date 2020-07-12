#QUESTION 1: Write a program which accepts a sequence of comma-separated numbers 
#from console and generate a list and a tuple which contains every number.


# numbers = input("Enter sequence of comma separated numbers:")
# l = []  #list
# temp = ''    #to store intermediate results
# t = ()  #tuple

# for n in numbers:
#     if(n == ','):
#         l.append(temp) # append element to list
#         t = t + (temp,) # append element to tuple
#         temp = ''	# reinitializing temp
#     else:
#         temp = temp + n

# l.append(temp)	#  append last element to list
# t = t + (temp,)	#  append last element to tuple
# print('List',l)
# print('Tuple',t)





# QUESTION 2:
# Q2: Write a function that takes an ordered list of numbers (a list where the elements
# are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list 
# and returns (then prints) an appropriate boolean.


# def check(ordered_list,num):
# 	if(num in ordered_list): # checks if number is present in list 
# 		return True
# 	else:
# 		return False

# ordered_list = [1,3,5,6,8,11,67,123]

# print(check(ordered_list,123))	# passing ordered list and the number to be checked 
# print(check(ordered_list,100))
# print(check(ordered_list,8))
# print(check(ordered_list,1))
# print(check(ordered_list,11))
# print(check(ordered_list,0))





# QUESTION 3 PASSWORD GENERATOR
# Q3: Write a password generator in Python. Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
#  The passwords should be random, generating a new password every time the user asks for a new password. 
#  Include your run-time code in a main method.

import string
import random
def main():
	s1 = string.ascii_lowercase # all lower case letters
	s2 = string.ascii_uppercase 	## all upper case letters
	s3 = string.digits # digits
	s4 = string.punctuation	# special characters / symbols

	PassLen = int(input("Enter password lenght: "))
	s = []
	s.extend(s1)	# storing s1 elements in list s
	s.extend(s2)	# storing s2 elements in list s
	s.extend(s3)	# storing s3 elements in list s
	s.extend(s4)	# storing s4 elements in list s


	random.shuffle(s) # to shuffle elements

	print("Your password is : ")
	print("".join(s[:PassLen]))	# printing the password of lenght as inputted by user

main()	#call main method










