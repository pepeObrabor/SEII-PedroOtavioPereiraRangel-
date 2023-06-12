

message =  'hello world'

new_message = message.replace('world' , 'universe')

gretting = 'Hello'
name = 'Michael'

message_2 = gretting + ', ' + name +'. Welcome;'

message_3 = '{}, {}. Welcome' .format(gretting, name) 

message_4 = f'{gretting}, {name}. Welcome' 

message_5 = f'{gretting}, {name.upper()}. Welcome' 

print(message)
print(new_message)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(dir(name))
