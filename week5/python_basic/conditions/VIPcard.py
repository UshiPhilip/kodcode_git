age = int(input("Enter yout age "))
if age < 16:
	print("Reject")
else:
	if age > 19:
		print("Allow entry")
	else:
		has_vip = input("Do you have a VIP card [yes / no]? ")
		if has_vip.lower() == "yes":
			print("Allow entry")
		else:
			print("Reject") 
