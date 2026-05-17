def retry(func, n):
    excepts = None
    try:
        for _ in range(n):
            return func()
    except Exception as e:
        excepts = e
    if not excepts:
        raise excepts