char = input("Enter a character: ")

if char.isalpha() and char.isascii():
	if char in ['a', 'e','i', 'o', 'u']:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Invalid")
