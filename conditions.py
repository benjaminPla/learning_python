x = 2
if x == 2:
    print(x == 2)
    print(x == 3)
    print(x < 3)

name = 'Ben'
age = 29
if name == 'Ben' and age == 29:
    print('Your name is "Ben" and you have 29 years old.')
    print('Your name is "%s" and you have %d years old.' % (name, age))
if name == 'Ben' or name == 'Flor':
    print('Your name is "Ben" or "Flor"')

# in
list = [1, 2, 3, 4, 5]
if 1 in list:
    print('1 is in list')
if 6 in list:
    print('6 is in list')

# identation
statement = False
another_statement = True
if statement is True:
    print('statement is True')
    pass
elif another_statement is True: # else if
    print('another_statement is True')
    pass
else:
    print('else')
    pass

#Excercise
#Change the variables in the first section, so that each if statement resolves as True.
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
