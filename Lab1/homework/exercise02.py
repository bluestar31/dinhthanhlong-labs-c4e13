input_number = int(input("Enter a number: "))
check = 0

for i in range(2, input_number):
    if input_number % i == 0:
        check += 1
    else:
        pass

if check == 0:
    print(input_number, "is a prime number")
else:
    print(input_number, "is not a prime number")
