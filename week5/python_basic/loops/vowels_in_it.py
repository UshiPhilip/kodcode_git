user_string = input("Enter a string: ")

vowels  = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for _ in user_string:
	if _.lower() in vowels:
		cnt += 1

print(f"Your string has {cnt} vowels letters.")
