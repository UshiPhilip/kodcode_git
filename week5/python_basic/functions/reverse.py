def reverse_all(list_num):
    new_list = []
    for num in list_num[::-1]:
        new_list.append(num)
    return new_list

numbers = [1,2,3,4,5,6,7,8]

print(reverse_all(numbers))