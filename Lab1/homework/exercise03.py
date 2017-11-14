bacteria_number = int(input("How many B bacterias are there? "))
time_wait = int(input("How much time  in minutes will we wait? "))


for i in range(2, time_wait + 1, 2):
    bacteria_number += bacteria_number

print("After {0} minutes, we would have {1} bacterias".format(time_wait, bacteria_number))
