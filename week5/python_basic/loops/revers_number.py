num = int(input("Enter a number: "))
  
nums_dict = dict()
tmp = 1
while num:
	current = num % 10
	nums_dict[tmp] = current
	tmp += 1
	num = num // 10

tmp = 1
cnt = 0

while nums_dict:
	multiply = 1
	for _ in nums_dict:
		multiply *= 10 
	cnt += nums_dict[tmp] * multiply
	nums_dict.pop(tmp)
	tmp += 1


print(cnt // 10)
