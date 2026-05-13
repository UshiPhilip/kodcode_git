highest_num = 0

while True:
	num = int(input("Enter a number or 0 to finish: "))
	if num == 0:
		break
	if num > highest_num:
		highest_num = num

print(highest_num)
