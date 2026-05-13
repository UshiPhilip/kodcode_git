def sum_of(list_num):
    return sum(list_num)


def average(list_num):
    return sum(list_num) / len(list_num)


def minimum(list_num):
    return min(list_num)


def maximum(list_num):
    return max(list_num)


numbers = [4, 7, 2, 9, 1, 5]

print(f"Sum: {sum_of(numbers)}\nAverage: {average(numbers)}\nMinimum: {minimum(numbers)}\nMaximum: {maximum(numbers)}")