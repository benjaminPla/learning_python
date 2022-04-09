class MyClass:
    string = 'Ben'
    interger = 29
    float = 10.5
    list = [1, 2, 3, 4 ,5]
    def function(self, param):
        return ('MyClass.function! (with param: %s)' % param)

myClass = MyClass()

print(myClass.string)
print(myClass.interger)
print(myClass.float)
print(myClass.list)
print(myClass.function('randomParam'))

myClassModified = MyClass()

myClassModified.string = 'Flor'

print(myClassModified.string)

# __init__()
class PracticeInit:
    def __init__(self, number):
        self.number = number

myInitClass = PracticeInit(5)

print(myInitClass.number)

# Exercise
# We have a class defined for vehicles.
# Create two new vehicles called car1 and car2.
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer,
# and car2 to be a blue van named Jump worth $10,000.00.
class Vehicles:
    def __init__(self, name, color, model, price):
        self.name = name
        self.color = color
        self.model = model
        self.price = price
    def description(self):
        return ("%s color is %s, it's a %s and worth $%s.00" % (self.name, self.color, self.model, self.price))

car1 = Vehicles('car1', 'red', 'convertible', 60000)
car2 = Vehicles('car2', 'blue', 'van', 10000)

print(car1.description())
print(car2.description())
