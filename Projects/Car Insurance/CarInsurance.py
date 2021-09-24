# Author: Jorge Marques
# Date: 21/03/20
# Subject Matter: This program determines if a person if eligable for car insurance.

# User's age is entered 
age = int (input("Please enter name here: "))

# The amount of years they have been driving is entered
yearsDriving = int (input("Please enter the amount of years you have been driving here:"))

# Does the user drink alcohol or not.
drink = string (input("Do you drink alcohol?: "))

if age < 22:
    print("Sorry, you are not eligible for car insurance because you are below 22 years old.”)
               
elif age >= 22 and age <=30 and drink = “no” and yearsDriving >= 3:
	print("You are eligible for car insurance”)

elif age >= 22 and age <=30 and drink = “yes” and yearsDriving < 3 or  age >= 22 and age <=30 and drink = “yes” and yearsDriving > 3:
    	print("Sorry, you are not eligible for car insurance”)
	
elif age >= 30 and yearsDriving >= 6:
        print("You are eligible for car insurance")

else age >= 30 and yearsDriving < 6 or age < 30 and yearsDriving < 6 or age < 30 and yearsDriving > 6 :
        print("Sorry, you are not eligible for car insurance")
