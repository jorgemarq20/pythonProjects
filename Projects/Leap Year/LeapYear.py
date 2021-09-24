# Chosen year is entered here
year = int (input("Please enter chosen year here: "))

# If the year is divisible by 4 and not 400 = leap year
if year / 4 and year not / 400:
			print(“The year”, year, “is a leap year!”)

# If the year is not divisible by 4 and 400 = not leap year
elif year not / 4 and year not / 400:
			print(“The year”, year, “is not a leap year!”)

# If the year is divisible by 400 and not 4 = not leap year
elif year / 400 and year not / 4:
			print(“The year”, year, “is not a leap year!”)

# If the year is divisible by 4 and 400 = not leap year
else year / 4 and year / 400:
			print(“The year”, year, “is not a leap year!”)
