num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("And now the last number: "))

positive_count = (num1 > 0) + (num2 > 0) + (num3 > 0)

print(f"Sum of the even numbers you entered: {positive_count}")
