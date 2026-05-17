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