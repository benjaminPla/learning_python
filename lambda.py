sum = lambda a, b : a + b
print(sum(1, 2))

# Exercise
# Write a program using lambda functions to check if a number in the given list is odd.
# Print "True" if the number is odd or "False" if not for each element.
list = [2, 4, 7, 3, 14, 19]
for n in list:
    my_lamda = lambda n : n % 2 == 0
    print(my_lamda(n))
