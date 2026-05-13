def is_palindrome(list):
	return list == list[::-1]

list = []
for i in range(5):
	num = input(f"Enter a {i} item: ")
	list.append(num)

print(is_palindrome(list))
