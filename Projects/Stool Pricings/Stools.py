# The amount of legs the user has
NumberLegsAvailable = (int)(input("Enter number of legs available: "))

# The amount of stools that can be created from the amount of legs
NoStools = NumberLegsAvailable // 3

# Extra stool legs left over
Numberlegsleft = NumberLegsAvailable % 3

# Amount Needed to make extra one
ExtrasNeeded = 3 - Numberlegsleft

# This displays the results
print("The number of stools that can be made from: ", NumberLegsAvailable, "is: ", NoStools)

print("Number of legs left after the:", NoStools , "is", Numberlegsleft)

print("Amount needed to make another one with", Numberlegsleft, "is", ExtrasNeeded)
