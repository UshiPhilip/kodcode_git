def load_config(path):
    excep = None
    try:
        with open(path, "r") as file:
            return int(file.readline)
    except Exception as e:
        excep = e
    return excep

print(load_config("cont_error"))