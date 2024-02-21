d = int(input("Enter the number of days: "))
year = d//365
print("No of years ",year)
remaining = d%365
month = remaining//30
print("No of months = ",month)
rem = remaining%30
print("No of remaining days are: ",rem)