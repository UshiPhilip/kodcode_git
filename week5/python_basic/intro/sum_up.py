three_digits = int(input("Enter a three digits number: "))



"""
hello
"""
ones = three_digits % 10
tens = three_digits % 100 // 10
hundreds = three_digits % 1000 // 100

print("Sum off all three numbers is:", ones + tens + hundreds)
