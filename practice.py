string = 'The quick fox jumps over the lazy dog'
list = string.split()
dictionary = {}

for item in list:
    if item != 'The':
        dictionary[item] = 'len: %d' % len(item)

print(dictionary)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [n for n in numbers if n > 0]
print(newlist)
