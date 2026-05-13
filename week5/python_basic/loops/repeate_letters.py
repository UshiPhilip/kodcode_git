user_string = input("Enter a string: ")

accumulator = ''

for letter in user_string:
	accumulator += letter * 2

print(accumulator)
