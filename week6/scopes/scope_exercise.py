# ======== Exercise 1 =======

def bump(): # adding 1 each time
    global counter  # using the global variable
    counter += 1

def value():return counter

counter = 0
for _ in range(3): # runs the bump func 3 times
    bump()

# ======== Exercise 3 =======

x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x) # local
    inner()
    print(x) # enclosing
outer()
print(x) # global

# ======== Exercise 4 =======

list = [1, 2, 3]
print(list(range(5))) # TypeError: 'list' object is not callable
# The built-in function - list, was overwritten by a variable assignment

# here is how to fix it
my_list = [1, 2, 3]
print(list(range(5)))