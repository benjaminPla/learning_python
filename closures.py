def father(msg):
    def child():
        print(msg)
    child()

father('Hello World!')

def print_msg(number):
    def printer():
        nonlocal number
        number = 3
        print(number)
    printer()
    print(number)

print_msg(9)
