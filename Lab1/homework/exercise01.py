numbers = [1, 6, 8, 1, 2, 1, 5, 6]
input_number = int(input("Enter a number? "))
count = 0

# This is a solution without count() function
for number in numbers:
    if input_number == number:
        count += 1

print(input_number, "appears", count, "times in my list")

# This is a solution with count() function
print(input_number, "appears", numbers.count(input_number), "times in my list")
