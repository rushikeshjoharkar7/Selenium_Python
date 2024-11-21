name = "Shree Ram"                 # Global variable created outside function and can be accessed inside and outside functions


def my_function():
    global name                     # stated name as a global variable to the function
    name = "Jai Mahakal"            # updated the global variable value
    print(name)                     # inside function this will print oly local variable


my_function()
print(name)