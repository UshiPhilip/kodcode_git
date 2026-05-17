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