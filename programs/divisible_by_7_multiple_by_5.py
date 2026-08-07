lower = int(input("Enter lower limti:"))
upper = int(input("Enter upper limit:"))
print(f"Numbers bivible by 7 and multiple of 5 between {lower} and {upper} are:")
for i in range (lower,upper+1):
	if i % 7 == 0 and i % 5 == 0:
		print(i)
