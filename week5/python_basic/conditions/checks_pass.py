PASSWD = 12345678
user_password = input("Enter your password: ")

if user_password == PASSWD:
	print("Access granted")
else:
	if len(user_password) < 8:
		print("Too short")
	else:
		print("Wronge password")
