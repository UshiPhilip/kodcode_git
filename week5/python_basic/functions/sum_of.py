def sum_up(number):
	acc = 0
	while int(number) > 9:
		for num in number:
			print(num)
			print(type(num))
			acc += int(num)
			print(acc)
		number = str(acc)
	return acc

number = input("Enter a number: ")

print(sum_up(number))
