# ==== Exercise 1 ====
def safe_int(num):
    try:
        return int(num)
    except ValueError:
        print("We can not convert this param into a integer.")
        return None
    except Exception as e:
        print("An error occur:", e)
        return None

print(safe_int("4"))
print(safe_int(2))
print(safe_int("d"))


# ==== Exercise 2 ====
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("ERROR: you can not divide by zero")
        return "undefined"
    except TypeError:
        print("ERROR: you can not divide by a string")
        return "undefined"
    except Exception as e:
        print(e)
        return 

print(safe_divide(4, 5))
print(safe_divide(3, 0))
print(safe_divide(4, "5"))


# ==== Exercise 3 ====
def get_value(dict, key):
    try:
        return dict[key]
    except KeyError:
        print("Key not found")
        return "missing"
    except Exception as e:
        print("An error occur:", e)
        return "missing"

dictionary = {
    1: "Hello",
    2: "World"
}

print(get_value(dictionary, 2))
print(get_value(dictionary, 5))

# ==== Exercise 4 ====
def parse_ints(values):
    int_list = []
    for val in values:
        try:
            int_list.append(int(val))
            continue
        except ValueError:
            print(f"Can not convert '{val}' into a integer")
        except Exception as e:
            print("An error occur:", e)
        print("Skipping...")
    return int_list

print(parse_ints(["1", "2", "3", "4"]))
print(parse_ints(["1.3", "w", "3", "q"]))
print(parse_ints(["", "2", False]))


# ==== Exercise 5 ====
def set_age(age):
    try:
        age = int(age)
        if 0 > age or age > 150:
            raise ValueError("An age can not be under 0 or greater than 150")
        return age
    except Exception as e:
        print("An error occur:", e)
        return None

print(set_age("33"))
print(set_age("-34"))
print(set_age("190"))
print(set_age("hello"))

# ==== Exercise 6 ====
def retry(func, n):
    excepts = None
    try:
        for _ in range(n):
            return func()
    except Exception as e:
        excepts = e
    if not excepts:
        raise excepts
    
# ==== Exercise 7 ====
def count_errors(list_func):
    cnt_errors = 0
    for func in list_func:
        try:
            result = func()
        except Exception as e:
            print(e)
            cnt_errors += 1
    return result, cnt_errors

print(count_errors([lambda: 1, lambda: 1/0, lambda: int("x"), lambda: 2]))# ==== Exercise 8 ====
def load_config(path):
    excep = None
    try:
        with open(path, "r") as file:
            return int(file.readline)
    except Exception as e:
        excep = e
    return excep

print(load_config("cont_error"))