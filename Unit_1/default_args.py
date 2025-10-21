#python program to define a function with default arguments
def greet(name, msg="Welcome to Python"):
    print("Hello", name + ', ' + msg)
greet("Alice")
greet("Bob", "Good to see you again!")