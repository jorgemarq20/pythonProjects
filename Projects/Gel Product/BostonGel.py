
NumOfBGSold = int (input("Enter amount of Boston Gel sold: "))

NumOfCCSold = int (input("Enter amount of California Color sold: "))

TotalSaleValue = NumOfBGSold * 12.99 + NumOfCCSold * 18.99

if TotalSaleValue > 200:
    commission = TotalSaleValue * 0.05

else:
      commission = TotalSaleValue * 0.08

print("Total commission for sale of", NumOfBGSold, "units of Boston Gel and", NumOfCCSold, "units of California Color is", commission)
