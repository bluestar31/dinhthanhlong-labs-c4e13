numbers = [1, 5, 16, 27, 38, 49, 66, 73, 83, 94]
x = int(input("Enter a number: "))

start = 0
stop = len(numbers)
found_index = -1

while start != stop:
    mid = (start + stop) // 2
    if x == numbers[mid]:
        found_index = mid
        break
    else:
        if mid == start or mid == stop:
            break
        elif x < numbers[mid]:
            stop = mid
        else:
            start = mid

if found_index == -1:
    print("Not found")
else:
    print("Found at:", found_index)
