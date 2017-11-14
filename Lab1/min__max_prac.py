numbers = [1, 5, 16, 27, -38, 49, 66, 73, 83, 94, -6]

min_num = numbers[0]
max_num = numbers[0]

for index, num in enumerate(numbers):
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print("Min:",min_num)
print("Max:",max_num)
