num = int(input("Enter a number: "))

cnt_evens = 0

while num:
	current_num = num % 10
	if current_num % 2 == 0:
		cnt_evens += 1
	num = num // 10

print(cnt_evens)
