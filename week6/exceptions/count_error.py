def count_errors(list_func):
    cnt_errors = 0
    for func in list_func:
        try:
            result = func()
        except Exception as e:
            print(e)
            cnt_errors += 1
    return result, cnt_errors

print(count_errors([lambda: 1, lambda: 1/0, lambda: int("x"), lambda: 2]))