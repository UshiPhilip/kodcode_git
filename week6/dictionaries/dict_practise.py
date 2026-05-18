# ======= Exercise 1  =======

def sum_of_value(dict_nums: dict[str:int]) -> int:
    acc = 0
    for v in dict_nums.values():
        acc += v
    return acc

# ====== Exercise 2 ===========

def key_with_max_value(dict_nums: dict[str:int]) -> str:
    for k, v in dict_nums.items():
        if v == max(dict_nums.values()):
            return k

# ===== Exercise 3 =========

def count_characters(string: str) -> dict[str:int]:
    dictionary = {}
    for i in set(string):
        dictionary[i] = list(string).count(i)
    return dictionary

# ===== Exercise 4 ======

def invert_dict(dictionary: dict[any:any]) -> dict[any:any]:
    return {v:k for k, v in dictionary.items()}

# ===== Exercise 5 =======

def merge_two_dictionaries(dict1: dict[str:int], dict2: dict[str:int]) -> dict[str:int]:
    dict1.update(dict2)
    return dict1

# ====== Exercise 6 ========

def filter_by_value(dict_nums: dict[str:int], threshold: int) -> dict[str:int]:
    return {k: v for k, v in dict_nums.items() if v > threshold}

# ====== Exercise 7 ========

def group_by_first_letter(words_list: list[str]) -> dict[str:str]:
    sorted_dict = {}
    for word in words_list:
        first_letter = word[0]
        if first_letter not in sorted_dict:
            sorted_dict[first_letter] = word
        else:
            sorted_dict[first_letter] = [sorted_dict[first_letter], word]
    return sorted_dict

# ====== Exercise 8 =========

def word_frequency(string: str) -> dict[str:int]:
    words_dict = {}
    for word in string.lower().split():
        words_dict[word] = string.count(word)
    return words_dict

# ====== Exercise 9 =========

def common_keys(dict1: dict[str:int], dict2: dict[str:int]) -> dict[str:int]:
    return [key for key in dict1 if key in dict2]

# ====== Exercise 10 =========

def most_frequent(dictionary: dict[str:int]) -> int:
    v = set([v for v in dictionary.values()])
    most = 0
    val = [v for v in dictionary.values()]
    for i in v:
        if val.count(i) > most:
            most = i
    return most
