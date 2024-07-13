## import os module
import os 

## import csv file
import csv

# Get the current working directory (the directory where this script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the CSV file
csvpath = os.path.join(current_dir, "Resources", "budget_data.csv")

# Construct the relative path to the output directory
output_dir = os.path.join(current_dir, "analysis")
os.makedirs(output_dir, exist_ok=True) 

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
        ## Count total number of months
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

            ## Set previous profit/loss for next iteration
        PPL = PL

## Calculate the average change in Profit/Losses                 
average_change = sum(PLC) / len(PLC)

## Prepare the analysis output
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Total: ${Net_Total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {GIP['Date']} (${GIP['Amount']})\n"
    f"Greatest Decrease in Profits: {GDP['Date']} (${GDP['Amount']})\n"
)

## Print the analysis to the terminal
print(output)

## Export the results to a text file
output_path = os.path.join(output_dir, "Result.txt")

with open(output_path, "w") as txtfile:
     txtfile.write(output)