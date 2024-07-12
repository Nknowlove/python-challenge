## import os module
import os 

## import csv file
import csv

# Get the current working directory (the directory where this script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the CSV file
csvpath = os.path.join(current_dir, "Resources", "election_data.csv")

# Construct the relative path to the output directory
output_dir = os.path.join(current_dir, "analysis")
os.makedirs(output_dir, exist_ok=True)

## Declarate And Initialize Variables
Total_Vote = 0

## Dict New Dictionary
candidate_votes ={}

## Open  and read Csv File
with open(csvpath, newline="") as csvfile:

    ## Use read module to create a csv reader
    csvreader = csv.reader(csvfile, delimiter=",")
    
    ## Read first line of CSV file
    csv_header = next(csvreader)

    ## Loop through rows in the CSV file
    for row in csvreader:
        ## Count total number of months
        Total_Vote = Total_Vote + 1

        ## Loop through to find canditate name
        candidate = row[2]
        ## If the candidate is not in the dictionary, add them with a vote count of 0
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        ## Count the candidate's vote 
        candidate_votes[candidate] =float(candidate_votes[candidate]) + 1    

## Dict new dictionary
candidate_percentages = {}

## Calculate the percentage of votes each candidate won
for candidate, votes in candidate_votes.items():
    candidate_percentages[candidate] = (votes / Total_Vote) * 100
    
# Determine the winner of the election 
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Vote}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({int(votes)})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Prepare the analysis output
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {Total_Vote}\n"
    "-------------------------\n"
)
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    output += f"{candidate}: {percentage:.3f}% ({int(votes)})\n"
output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Export the results to a text file
output_dir = os.path.join(current_dir, "analysis")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "election_results.txt")
with open(output_path, "w") as txtfile:
    txtfile.write(output)