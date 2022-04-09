# map
names = ['Ben', 'Flor', 'Mona']

for name in names:
    print(name.upper())

mymap = list(map(str.upper, names))
print(mymap)

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

mymap = list(map(round, numbers, range(1, len(numbers) + 1)))
print(mymap)

# filter
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

for score in scores:
    if score > 75:
        print(score)

myfilter = list(filter(lambda x : x > 75, scores))
print(myfilter)

words = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk", "neuquen")

palindromes = list(filter(lambda w : w == w[::-1], words))
print(palindromes)

# reduce
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

myreduce = reduce(lambda x, y : x + y, numbers)
myreduceinitial = reduce(lambda x, y : x + y, numbers, 10)
print(myreduce, myreduceinitial)

# Exercise
# In this exercise, you'll use each of map, filter, and reduce to fix broken code.

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
map_result = list(map(lambda f : round(f ** 2, 3), my_floats))

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
filter_result = list(filter(lambda n : len(n) < 7, my_names))

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
reduce_result = reduce(lambda x, y : x * y, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
