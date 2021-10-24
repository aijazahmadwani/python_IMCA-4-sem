# LIST
courses = ['BCA','Math','Chemistry','Computer']
# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[-1])

#SLICING
# print(courses[:2])
# print(courses[2:])


# courses.append('Science')
# print(courses)

# courses.insert(0,'Arts')
# print(courses)

# courses_2 = ['Humanities','Botany']
# courses.extend(courses_2)
# print(courses)

# courses.remove('Math')
# print(courses)

# courses.pop() # removes last item

# courses.reverse()
# print(courses)

# courses.sort()
# print(courses)

#sorted function sorts the  list but not alters the original list
# print(sorted(courses))
# print(courses)

# nums = [1,45,67,2,23]
# print(min(nums))
# print(max(nums))
# print(sum(nums)) # add all numbers

# print('Math' in courses)
# for item in courses:
#     print(item)

# enumerate function helps to print index of items of a list.
# for index,course in enumerate(courses):
#     print(index, course)


# course_str = ', '.join(courses) # comma separated items
# print(course_str)


# TUPLES: immutable
# tuple1 = ('History','Math','Physics')
# print(tuple1)

#SET
s = {'History','Math','Physics'}
print(s)