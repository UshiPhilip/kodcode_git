def read_first_line(path):
    try:
        f = open(path, "r")
        first_line = f.readline()
    except FileNotFoundError:
        print(f"I can't find {path} file")
        return None
    except TypeError:
        print("Expected a string, not any type else")
        return None
    except Exception as e:
        print("ERROR:", type(e))
        return None
    else:
        f.close()
        print("File is close!")
        return first_line

print(read_first_line("safe_int.py"))
print(read_first_line("abs.py"))
print(read_first_line(1 / 3))