from xmlrpc.client import Boolean, boolean

# Section 1: Tax
# Author: Eoghan Bryne

#This program calculates tax based on the users salary inputed on the amount of children he / she has
#And It also calculates the monthly mortgage of the user

#Enter the users salary FTA based on number of children and mortgage

def main():
  children = int(input("Do you have any children: "))
  mortgage = str(input("Do you have a mortgage Y/N: "))
  payment(mortgage)

def children (monthlyMortgage, children):
  if monthlyMortgage <= 300 and children <= 3:
    print("You get and alloance of €237.")
  elif monthlyMortgage > 300:
      print("You get and alloance of €275.")
  else:
      print("You do not get a allowance.")

def payment(mortgage):
  if mortgage == 'y' or mortgage == 'Y':
    monthlyMortgage = int(input("How much is your monthly mortgage: "))
    children(monthlyMortgage, children)
  else:
      print("You do not get an allowance.")

main()


# Section 2: Water Charges

# Author = Jorge Marques
# Date = 06/03/21
# Program = This program calculates the users water charges per year while taking certain allowances into consideration.

# This is the adult allowance = Households which have 5 or more adults.
def adultAllowence (userHouseholdAdults, userHouseholdChildren, usersLitresUsed):
    if userHouseholdAdults >= 5 and userHouseholdChildren < 3:
        basicUsage = 243000
        waterCharge(usersLitresUsed, basicUsage)
    elif userHouseholdAdults < 5 and userHouseholdChildren < 3:
        basicUsage = 213000
        waterCharge(usersLitresUsed, basicUsage)

# This is the children allowance = Households which have less than 3 adults and 3 or more children.
def childrenAllowence (userHouseholdAdults, userHouseholdChildren, usersLitresUsed):
    if userHouseholdAdults < 3 and userHouseholdChildren >= 3:
        childRegulation = 3
        userHouseholdChildren = userHouseholdChildren - childRegulation
        basicUsage = (5000 * userHouseholdChildren) + 213000
        waterCharge(usersLitresUsed, basicUsage)

# This is the adult and child allowance = Households which have 3 or more adults and 3 or more children.
def adultAndChildrenAllowence (userHouseholdAdults, userHouseholdChildren, usersLitresUsed):
    if userHouseholdAdults >= 3 and userHouseholdChildren >= 3:
        childRegulation = 2
        userHouseholdChildren = userHouseholdChildren - childRegulation
        basicUsage = (7000 * userHouseholdChildren) + 213000 + 20000
        waterCharge(usersLitresUsed, basicUsage)

def waterCharge (usersLitresUsed, basicUsage):
    remainderLitres = usersLitresUsed - basicUsage
    userWaterCharge = remainderLitres * 3.70
    print("Your water charge for this year is", "€{:.2f}".format(userWaterCharge) + "\n")
    print("Your total allowence is " + str("{:.2f}".format(basicUsage) + "Ltrs of water per year."))

# This is where the users information is taken and users water charge is displayed.
def main ():
    usersLitresUsed = float(input("Enter the amount of water (litres) you have used this year: \n"))
    userHouseholdAdults = int(input("Enter the number of adults in your household: \n"))
    userHouseholdChildren = int(input("Enter the number of children in your household: \n"))
    if userHouseholdAdults >= 5 or userHouseholdAdults < 5 and userHouseholdChildren < 3:
        adultAllowence(userHouseholdAdults, userHouseholdChildren, usersLitresUsed)
    elif userHouseholdAdults < 3 and userHouseholdChildren >= 3:
        childrenAllowence(userHouseholdAdults, userHouseholdChildren, usersLitresUsed)
    elif userHouseholdAdults >= 3 and userHouseholdChildren >= 3:
        adultAndChildrenAllowence(userHouseholdAdults, userHouseholdChildren, usersLitresUsed)

main()


# Section 3: Property Tax
# Author: Kate O'Donovan

# allowance is defined by your monthly mortgage and the value of your property in Dublin.
def allowance(monthlyMortgage, valuePropertyDublin, ):
      liveInDublin = boolean(input(" Do you live in Dublin?"))
      print(liveInDublin)
      valuePropetyDublin = float(input("How much is your property in Dublin worth?"))
      print(valuePropertyDublin)
      monthlyMortgage = float(input("How much is your monthly mortgage?"))
      print(monthlyMortgage)
# If you live in Dublin and your property is <500000, then multiply the value of your roperty by 15.4%, otherwise if the value of your property is >500000, multiply the value of your property by 8.2%.
  if liveInDublin == True:
      if valuePropertyDublin < 500000:
          allowance = (15.4 * valuePropertyDublin) / 100
      else:
          allowance = (8.2 * valuePropertyDublin) / 100
  else:
      allowance = monthlyMortgage * 3

  # tax is defined by the value of your property multiplied by 0.2 if <300000, 0.25 if <500000, 0.25 if <1000000 and 0.35 if >1000000
def tax(propertyValuation):
      print(propertyValuation=float(input("How much is your property valued at?")))

      if propertyValuation < 300000:
          tax = (0.2 * propertyValuation) / 100
      elif propertyValuation < 500000:
          tax = (0.25 * propertyValuation) / 100
      elif propertyValuation < 1000000:
          tax = (0.3 * propertyValuation) / 100
      else:
          tax = (0.35 * propertyValuation) / 100

def main():
      liveIn1dublin = boolean(input("Do you live in Dublin?"))
      valuePropetyDublin = float(input("How much is your property in Dublin worth?"))
      monthlyMortgage = float(input("How much is your monthly mortgage?"))
      propertyValuation = float(input("How much is your property valued at?"))
      (monthlyMortgage, valuePropertyDublin) = allowance(monthlyMortgage, valuePropertyDublin)
      (propertyValuation) = tax(propertyValuation)

  print("Your tax is", '{:7d}'.format(tax), "and your allowance is" '{:09.2f}'.format(allowance))
