#for
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# For loops can iterate over a sequence of numbers using the "range" and "xrange" functions.
# The difference between range and xrange is that
# the range function returns a new list with numbers of that specified range,
# whereas xrange returns an iterator, which is more efficient.
# (Python 3 uses the range function, which acts like xrange).
# Note that the range function is zero based.
for x in range(5):
    print(x)
for x in range(1,5):
    print(x)
for x in range(1, 5, 2):
    print(x)

# while
count = 0
while count < 5:
    print('count: %d' % count)
    count += 1

# 'beack' and 'continue' statements
x = 0
while True:
    print('x: %d' % x)
    x += 1
    if x >= 5:
        break

for x in range(10):
    if x % 2 == 0:
        continue
    print('odd number found: %d' % x)

# else in loop
x = 0
while x < 5:
    print('x: %d' % x)
    x += 1
else:
    print('Condition failed')

for x in range(10):
    if x == 5:
        print('break!')
        break
    print('x: %d' % x)
else:
    print('Condition failed')

# Exercise
# Loop through and print out all even numbers from the numbers list in the same order they are received.
# Don't print any numbers that come after 237 in the sequence.
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        print('break! = Found %d' % number)
        break
    if number % 2:
        continue
    print('even number: %d' % number)
