lower = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))
divisior = int(input("Enter divisior:"))
print(f"Numbers divisible by {divisior} between {lower} and {upper} are:")
for num in range(lower,upper+1):
	if num % divisior == 0:
		print(num)