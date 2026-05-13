x = int(input("Enter the x's value: "))
y = int(input("Enter the y's value: "))

if x == 50 or x == 10 and y == 20 or y == 80:
	print("On the adge")
else:
	if 10 <= x <= 50 and 20 <= y <= 80:
		print("Inside the rectangle")
	else:
		print("Outside the rectangle")
