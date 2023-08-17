
student = {'name': 'John', 'age': 25, 'courses': ['Math','CompSci']}

print(student)

print(student['name'])

student_1 = {1: 'John', 'age': 25, 'courses': ['Math','CompSci']}
print(student_1[1])

print(student.get('age'))

print(student.get('phone', 'Not found'))

student['phone'] = '555-5555'

print(student.get('phone', 'Not found'))

student['name'] = 'Jane'

print(student.get('name'))

student.update({'name': 'Pepe'})

print(student['name'])

del student['age']

print(student)

name = student.pop('name')

print(student)

student = {'name': 'John', 'age': 25, 'courses': ['Math','CompSci']}

print(student.keys())

print(student.items())

for key, value in student.items():
    print(key, value)