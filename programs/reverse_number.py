n = int(input("Enter a number :"))
temp = n
rev = 0
while n > 0 :
    digit = n % 10
    rev   = rev * 10 + digit
    n     = n // 10
print(f"Reverse of {temp} is {rev}")