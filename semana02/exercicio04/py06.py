
if True:
    print('Condititional is True')

if False:
    print('Condititional is True')

language = 'Python'

if language == 'Python':
        print('Language is Python')
else:
    print('No match')

language = 'Java'

if language == 'Python':
        print('Language is Python')
elif language == 'Java':
        print('Language is Java')
elif language == 'Javascript':
        print('Language is Javascript')
else:
     print('No match')


user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

    
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')


if not logged_in:
    print('please log in')
else:
    print('Welcome')

a = [1,2,3]
b = [1,2,3]

print(a is b)
print(id(a))
print(id(b))

b=a
print(a is b)
print(id(a))
print(id(b))


condition = None

if condition:
    print('Evalueted to True')
else:
    print('Evalueted to False')



condition = 1

if condition:
    print('Evalueted to True')
else:
    print('Evalueted to False')

