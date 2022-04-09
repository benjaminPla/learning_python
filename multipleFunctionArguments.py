def multiplefunctionarguments(first, second, *therest):
    print('First argument: %s' % first)
    print('Second argument: %s' % second)
    print('The rest of the arguments: %s' % list(therest))

print(multiplefunctionarguments('first', 'second', 'third', 'another'))

def noorder(first, second, **others):
    if others.get('action') == 'sum':
        return first + second
    elif others.get('action') == 'mult':
        return first * second
    else:
        return 'No action recognized'

print(noorder(2, 3, action = 'sum'))
print(noorder(2, 3, action = 'mult'))
print(noorder(2, 3, action = 'div'))

# Exercise
# Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more)
# The foo function must return the amount of extra arguments received.
# The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.
def foo(a, b, c, *others):
    return 'The "others" arguments are: %s' % list(others)

def bar(a, b, c, **others):
    # if others.get('magicnumber') == 7:
    if others['magicnumber'] == 7:
        return True
    else:
        return False


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
