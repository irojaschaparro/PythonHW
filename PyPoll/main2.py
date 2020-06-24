import os
import csv
import numpy as np

csvpath = os.path.join("election_data.csv")
output_path = os.path.join("election_data_output.txt")
month_total = 0

file_data = []
vote_values = []
cand_values = []

# NEED TO CREATE THE FUNCTION THAT ALLOWS YOU TO EXPORT AS A CSV


# Extract the information in a dictionary or list that allows you to manipulate it from there
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
        file_data.append(row)
        vote_values.append(row[0])
        cand_values.append(row[2])

# This creates the count of how many votes there are
vote_count = len(vote_values)
#print(vote_count)

#CHECK FOR DUPLICATES?
# This checks for duplicates by converting the list into a set  
check_and_set = set(cand_values)
#print(check_and_set)

# Counts how many votes each candidate gets
khan_count = cand_values.count("Khan")
#print(khan_count)
li_count = cand_values.count("Li")
correy_count = cand_values.count("Correy")
otooley_count = cand_values.count("O'Tooley")

# Calculates the percentages of each vote candidate. Create a FUNC
def percent_create(candidate_votes):
    percent_calc =  (candidate_votes / vote_count)
    percent_calc = "{:.2%}".format(percent_calc)
    return percent_calc

khan_percent = percent_create(khan_count)
li_percent = percent_create(li_count)
correy_percent = percent_create(correy_count)
otooley_percent = percent_create(otooley_count)

# create an if statement that determines the winner, create a list with the candidiate, percent, and votes
cand_outcomes = {"Khan":{khan_count},"Li":{li_count},"Correy":{correy_count},"O'Tooley":{otooley_count}}
#print(cand_outcomes)
cand_winner = max(cand_outcomes, key=cand_outcomes.get)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
print(f"Khan: {khan_percent} {khan_count}")
print(f"Correy: {correy_percent} {correy_count}")
print(f"Li: {li_percent} {li_count}")
print(f"O'Tooley: {otooley_percent} {otooley_count}")
print("-------------------------")
print(f"Winner: {cand_winner}")
print("-------------------------")

with open(output_path, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {vote_count}"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Khan: {khan_percent} {khan_count}"])
    csvwriter.writerow([f"Correy: {correy_percent} {correy_count}"])
    csvwriter.writerow([f"Li: {li_percent} {li_count}"])
    csvwriter.writerow([f"O'Tooley: {otooley_percent} {otooley_count}"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {cand_winner}"])
    csvwriter.writerow(["-------------------------"])

