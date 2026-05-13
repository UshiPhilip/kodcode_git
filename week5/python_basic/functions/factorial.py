def factorial(num):
	acc = 0
	for i in range(1, num):
		acc += i * i
	return acc

num = int(input("Enter a number: "))
result = factorial(num)
print(result)
