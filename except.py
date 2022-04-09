def printer(param):
    print(param)

def except_function():
    list = (1, 2, 3, 4, 5)
    for n in range(10):
        try:
            printer(list[n])
        except IndexError:
            printer('exception')

except_function()

# Exercise
# Handle all the exception! Think back to the previous lessons to return the last name of the actor.
actor = { "name": "John Cleese", "rank": "awesome" }

# Function to modify
def get_last_name():
    try:
        return actor["last_name"]
    except:
        return actor["name"].split()[1]

# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
