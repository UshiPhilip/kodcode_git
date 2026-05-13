user_string = input("Enter a string: ")

status = True

for char in user_string:
	if not char.isdigit() and not char.isalpha():
		status = False
		break
print(status)
