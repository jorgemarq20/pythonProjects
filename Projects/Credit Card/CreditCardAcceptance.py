Name = string (input("Enter name here: "))

Salary = float(input("Please enter salary here: €"))

careerLength = int (input("Years contributed to job:"))

if Salary > 30000 or (Salary > 20000 and careerLength > 3):
print("You are entitled to a credit-card.")

else:
print("You are not entitled to a credit-card.")
