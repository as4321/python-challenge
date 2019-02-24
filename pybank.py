import os
import csv
monthcount = []
net = 0
rowcount = 0
greatest= 0 
change = 0 
least = -1 
changetotal = 0 
change= 0
averagechange = 0
prevend = 0 
greatestdate = ""
leastdate ="" 
pybankpath = os.path.join('.', "budget_data.csv")

with open (pybankpath, newline="") as pybankfile:
    pybankreader = csv.reader(pybankfile, delimiter=",")
    next(pybankreader, None)
    for row in pybankreader:
        net = int(row[1]) + net
        rowcount = rowcount + 1 
        if prevend == 0:
            prevend = int(row[1])
        else:
            change = (int(row[1])-prevend) 
            changetotal = change +changetotal 
            prevend = int(row[1])
            if change > greatest:
                greatest = change
                greatestdate = (row[0])
            elif change < least:
                least = change
                leastdate = (row[0])
average = net / 86
averagechange = changetotal / (rowcount-1)

print("=============================")
print("Fincancial Analysis:")
print("=============================")
print(f"Total Months: {rowcount}")
print(f"Total: ${net}")
print(f"Average Change: ${round((averagechange), 2)}")
print(f"The greatest increase in profits was ${greatest}, which occured on {greatestdate}.")
print(f"The greatest decrease in profits was ${least} which occured on {leastdate}.")

