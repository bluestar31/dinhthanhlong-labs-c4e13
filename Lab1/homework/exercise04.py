mature_rabbits = 2
newborn_rabbits = 0
new_newborn_rabbits = 0
total_rabbits = mature_rabbits + newborn_rabbits

for i in range(5):
    if i == 0:
        print("Month {0}: {1} pair(s) of rabbit".format(i, total_rabbits // 2))
    else:
        new_newborn_rabbits = mature_rabbits
        mature_rabbits += newborn_rabbits
        newborn_rabbits = new_newborn_rabbits
        total_rabbits = mature_rabbits + newborn_rabbits
        print("Month {0}: {1} pair(s) of rabbit".format(i, total_rabbits // 2))
