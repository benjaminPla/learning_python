def my_function():
    print('my first python function!')

my_function()

def parameters_function(name, age):
    print("My name is %s, and I'm %s years old."%(name, age))
#
parameters_function("Ben", 29)

def sum_two_numbers(x, y):
    return x + y

x = sum_two_numbers(1, 2)
print(x)

# Exercise
# Add a function named list_benefits() that returns the following list of strings:
    # "More organized code",
    # "More readable code",
    # "Easier code reuse",
    # "Allowing programmers to share and connect code together"
# Add a function named build_sentence(info)
    # which receives a single argument containing a string and
    # returns a sentence starting with the given string and
    # ending with the string " is a benefit of functions!"
# Run and see all the functions work together!

# Modify this function to return a list of strings as defined above
def list_benefits():
    return [
        'More organized code',
        'More readable code',
        'Easier code reuse',
        'Allowing programmers to share and connect code together'
        ]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return ('%s is a benefit of functions!' % benefit)

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
