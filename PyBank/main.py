e#tive pathwq import os module
import os 

## import csv file
import csv
csvpath = os.path.join("C:/Users/shadow/Resources/budget_data.csv")

## Declarate and Initialize variables
Total_Months = 0
Net_Total = 0

## Set previous Profit / Loss and Initialize as 0
PPL = 0

## Set Empty List For Date and Profit / Loss Changes
PLC = []
Date = []

## Set Dictionary For Greatest Increase & Decrease in Profit / Loss
GIP = {"Date": "","Amount": float("-inf")}
GDP = {"Date": "", "Amount": float("inf")}

## Open  And Read Csv File
with open(csvpath, newline="") as csvfile:

    ## Use Read Module TO Create A Csv Reader
    csvreader = csv.reader(csvfile, delimiter=",")
    
    ## Read First Line Of Csv file
    csv_header = next(csvreader)

    ## Loop through rows in the CSV file
    for row in csvreader:
        # Count total number of months
        Total_Months = Total_Months + 1
    
        ## Loop Through Profit / Lose Row Since Second Row And Set Vaule as Integer
        PL = int(row[1])
        ## Sum Net Total Amount
        Net_Total = Net_Total + PL
        
        ## Calculation Strat From Second Month
        if Total_Months > 1 :
            ## Changes Based on Current Month P/L - Previous Moth P/L
            change = PL - PPL

            ## Loop Through Rows Add Change Values To PLC List
            PLC.append(change)

            ## Loop Through dates Add current date To Date List
            Date.append(row[0])
            
            ## If change is great than value recorded in GIP Dictory, Update Date and Value
            if change > GIP["Amount"]:
                GIP["Date"] = row[0]
                GIP["Amount"] = change
            
            ## If change is less than value recorded in GIP Dictory, Update Date and Value
            if change < GDP["Amount"]:
                GDP["Date"] = row[0]
                GDP["Amount"] = change

            # Set previous profit/loss for next iteration
        PPL = PL

# Calculate the average change in Profit/Losses                 
average_change = sum(PLC) / len(PLC)

# Print results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Net_Total}")
print(f"Average Change: ${average_change:.2f}")
print(f"GIP: {GIP['Date']} (${GIP['Amount']})")
print(f"GDP: {GDP['Date']} (${GDP['Amount']})")



        
       

