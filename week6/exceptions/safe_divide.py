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