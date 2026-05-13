def greeting(name,/,age, address):
    print(f"{name} you are {age} years old, and you live in {address}")


def non_known(*arr):
    for item in arr:
        print(item)


def everithing_in(name, /, *, age):
    print(f"name: {name} age: {age}")
