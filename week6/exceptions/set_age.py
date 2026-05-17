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