
def hello_func():
    pass

print(hello_func())

def hello_func():
    print('Hello Function.')

hello_func()

def hello_func():
    return'Hello Function.'

print(hello_func().upper())


def hello_func(greeting):
   return '{} Function.'.format(greeting)

print(hello_func('Hi'))

def hello_func(greeting, name):
   return '{}, {}'.format(greeting, name)

print(hello_func('Hi', 'Pepe'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name='Pepe', age = 22)

print('\n')
courses =  ['Math', 'Art']
info = {'name': 'Pepe', 'age':22}

student_info(*courses, **info)

print('\n\n')

