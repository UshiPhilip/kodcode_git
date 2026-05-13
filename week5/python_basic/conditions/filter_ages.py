age = int(input("Enter your age: "))

if age < 0 or age > 120:
	print("Invalid")
elif age < 12:
	print("Child")
elif age < 17:
	print("Teen")
else:
	print("Adult")
