string = 'my name is Ben and Ben is my name'
list = string.split()
myset = set(list)
print(myset)

amembers = set(['Ben', 'Flor', 'Mona'])
bmembers = set(['Daniel', 'Marcelo', 'Mona'])

# intersection
print (amembers.intersection(bmembers))
print (bmembers.intersection(amembers))

# symmetric_difference
print (amembers.symmetric_difference(bmembers))
print (bmembers.symmetric_difference(amembers))

# difference
print (amembers.difference(bmembers))
print (bmembers.difference(amembers))

# union
print (amembers.union(bmembers))
