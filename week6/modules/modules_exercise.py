# ====== Exercise 2 ======

def make_counter():
    count = 0
    def adding_one():
        nonlocal count
        count += 1
        return count
    return adding_one

c = make_counter()
c()
c()
c()

# ===== Exercise 5 ======

# created two files, mathutil.py - main.py

# ===== Exercise 6 ======

# created a tools.py file and verify to run a function only if the main file is running

# ===== Exercise 7 ======

from datetime import datetime as dt

dt.now()

# ===== Exercise 8 ======

import math

def public_names():
    return [i for i in math.__dict__ if not i.startswith("__")]

# ======= Exercise 9 ======

def add_item(item, bag):
    bag.append(item)
    return bag

# ===== Exercise 10 ======

import geometry

geometry.circle.area(5)
geometry.rectangle.area(4, 6)

