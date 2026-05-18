# ====== Exercise 1 =======

def sum_tuple(tup):
    acc = 0
    for num in tup:
        acc += num
    return acc

# ====== Exercise 2 ========

def maximum(tup):
    maximum = tup[0]
    for num in tup:
        if num > maximum:
            maximum = num
    return maximum

# ====== Exercise 3 ========

def counting(tup, val):
    appear = 0
    for num in tup:
        if num == tup:
            appear += 1
    return appear

# ====== Exercise 4 =========

def reverse(tup):
    tmp_list = []
    for i in range(len(tup)):
        tmp_list.insert(0,tup[i])
    return tuple(tmp_list)

# ====== Exercise 5 =======

def swap_pairs(tup):
    tmp_list = list()
    for i in (tup[::2]):
        tmp_list.append(tup[i])
        tmp_list.append(tup[i-1])
    return tuple(tmp_list)

# ====== Exercise 6 ======

def min_and_max(tup):
    maxi = maximum(tup)
    mini = tup[0]
    for num in tup:
        if num < mini:
            mini = num
    return maxi, mini

# ====== Exercise 7 ========

def distance(tup1, tup2):
    return (((tup2[0] - tup1[0]) ** 2) + ((tup2[1] - tup1[1]) ** 2)) ** 0.5

# ====== Exercise 8 =======

def merge_and_sort(tup1, tup2):
    new_list = list(tup1) + list(tup2)
    new_list.sort()
    return new_list

# ======  Exercise 9 =====

def frequency_table(tup):
    return tuple((item, tup.count(item)) for item in set(tup))

# ===== Exercise 10 =====

def rotate(tup, key):
    key = key % len(tup)
    return tup[key+1:] + tup[:key+1]
