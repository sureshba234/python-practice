number = int(input("Enter a number:"))
number = abs(number)
for i in range(1,number+1):
	if number % i == 0:
		print(i)