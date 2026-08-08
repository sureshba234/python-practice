def to_binary(n):
    if n <= 1:
        return str(n)
    else:
        return to_binary(n // 2) + str(n % 2)

# Driver code
num = int(input("Enter an integer: "))

if num < 0:
    print("Binary of", num, "is -" + to_binary(-num))
else:
    print("Binary equivalent of", num, "is", to_binary(num))