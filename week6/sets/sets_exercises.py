# ======= Exercise 1 =====

def remove_duplicates(list_items: list[any]) -> list:
    return list(set(list_items))

# ======= Exercise 2  ======

def count_unique(list_items: list[any]) -> int:
    unique: list = []
    for i in list_items:
        if not i in unique:
            unique.append(i)
    return len(unique)

# ===== Exercise 3 =======

def common_elements(list1: list[any], list2: list[any]) -> list:
    return list(set(list1) & set(list2))

# ===== Exercise 4 =======

def element_is_only_one(list1: list[any], list2: list[any]) -> list:
    return list(set(list1) ^ set(list2))

# ===== Exercise 5 ======

def is_subset(list1: list[any], list2: list[any]) -> bool:
    for i in list1:
        if i not in list2:
            return False
    return True

# ===== Exercise 6 ======

def unique_characters(string: str) -> bool:
    return len(string) == len(set(string))

# ====== Exercise 7 ======

def first_repeated(list_items: list[any]) -> any:
    tmp_list: list = []
    for i in list_items:
        if i in tmp_list:
            return i
        tmp_list.append(i)
    return None

# ===== Exercise 8 ========

def distinct_words(string: str) -> int:
    return len(set(string.lower().split()))

# ===== Exercise 9 ========

def pair_sum_exists(list_nums: list[int], target: int) -> bool | tuple:
    for i, num in enumerate(list_nums):
        if target - num in list_nums[i+1:]:
            return True, (num, target-num)
    return False

# ====== Exercise 10 =======

def symmetric_difference(list1: list[any], list2: list[any]) -> list[any]:
    returned_list = []
    for i in list1:
        if i not in list2 and i not in returned_list:
            returned_list.append(i)
    for i in list2:
        if i not in list1 and i not in returned_list:
            returned_list.append(i)
    return returned_list

    