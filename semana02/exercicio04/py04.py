
courses = ['History', 'Math', 'Phisics', 'CompSci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[2:])

courses.append('Art')

print(courses)

courses.insert(0,'Art')

print(courses) 

courses_2 = ['Art', 'Education']

courses.insert(0,courses_2)

print(courses) 

courses.extend(courses_2)

print(courses) 

courses.remove('Math')

print(courses) 

courses.pop()

print(courses)

courses.reverse()

print(courses)

courses = ['History', 'Math', 'Phisics', 'CompSci']

nums=[1,5,2,4,3]

nums.sort()

print(nums)

nums.sort(reverse=True)

print(nums)

sorted_courses = sorted(courses)

print(courses)

print(sorted_courses)

print(min(nums))

print(courses.index('CompSci'))

print('Art' in courses)
print('Math' in courses)

for item in courses:
    print(item)

for index, course in enumerate(courses):
    print(index, course)

course_str = ', '.join(courses) 
print(course_str)

new_list = course_str.split(', ')

print(new_list)

list_1 = ('History', 'Math', 'Phisics', 'CompSci')
list_2 = list_1
print(list_1)

cs_courses = {'History', 'Math', 'Phisics', 'CompSci', 'Math'}

print(cs_courses)

print('Math' in cs_courses)

art_courses = {'Math', 'Phisics', 'Art', 'Desigh'}


print(cs_courses.intersection(art_courses))
print(cs_courses.union(art_courses))

