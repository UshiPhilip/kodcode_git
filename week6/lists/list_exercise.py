# ====== Exercise 1 =========

def sum_list(numbers):
    sum_up = 0
    for num in numbers:
        sum_up += num
    return sum_up

# ===== Exercise 2 ==========

def maximum(numbers):
    prev_max = 0
    for num in numbers:
        if num > prev_max:
            prev_max = num
    return prev_max

# ======  Exercise 3 ========

def occurrence(arr, value):
    return arr.count(value)

# ====== Exercise 4 =========

def reversing(arr):
    new_arr = []
    for i in arr:
        new_arr.insert(0, i)
    return new_arr

# ====== Exercise 5 ======

def remove_duplication(arr):
    new_arr = []
    for item in arr:
        if item in new_arr:
            continue
        new_arr.append(item)
    return new_arr

# ===== Exercise 6 =========

def second_max(arr):
    largest = maximum(arr)
    for num in arr[-1::-1]:
        if num == largest:
            arr.remove(num)
    return maximum(arr)

# ===== Exercise 7 =======

def merging_lists(arr1, arr2):
    final_arr = []
    for i, v in enumerate(arr1):
        final_arr.append(v)
        final_arr.append(arr2[i])
    return final_arr

# ===== Exercise 8 ======

def rotate(arr, key):
    key = key % len(arr) # bonus
    new_arr = arr[key+1:]
    new_arr.extend(arr[:key+1])
    return new_arr

print(rotate( [1, 2, 3, 4, 5], 7))