def count_digits(number):
    acc = 0
    while number > 0:
        acc += 1
        number = number // 10
    return acc

number = int(input("Enter a number: "))
print(count_digits(number))