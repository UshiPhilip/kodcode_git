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
            