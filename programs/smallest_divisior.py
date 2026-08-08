number = int(input("Enter a number:"))
number = abs(number)
if number == 0:
	    print("0 has no smallest divisor (every number divides 0).")
elif number == 1:
	print("smallest divisior of 1 is 1")
else:
	smallest = None
	for i in range(2, number+1):
		if number % i == 0:
			smallest = i
			break
	print(f"smallest divisior of {number} is {smallest}")
