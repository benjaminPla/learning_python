phones1 = {}
phones1['Ben'] = '345 500 0346'
phones1['Flor'] = '+34 697 97 1651'

phones2 = {
    'Ben': '345 500 0346',
    'Flor': '+34 697 97 1651'
}

print(phones1)
print(phones2)

# iterating dictionaries
for name, phone in phones2.items():
    print('%s number is: %s' % (name, phone))

# remove a value
del phones1['Ben']
phones2.pop('Flor')

print(phones1)
print(phones2)

# Exercise
# Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

phonebook['Jake'] = 938273443
# del phonebook['Jill']
phonebook.pop('Jill')

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
