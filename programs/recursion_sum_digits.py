def sum_of_digits(n):
	n = abs(n)
	if n < 10 :
		return n
	else:
		return n % 10 + sum_of_digits(n // 10)
num = int(input("Enter a number:"))
print(f"sum digits of a {num} is {sum_of_digits(num)}")