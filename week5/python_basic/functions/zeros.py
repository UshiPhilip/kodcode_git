def order_zeros(list):
    for num in list[-1:0:-1]:
        if num == 0:
            list.remove(num)
            list.insert(-1, 0)
    return list


list_0 = [1,3,2,0,4,0,3,0]
print(order_zeros(list_0))