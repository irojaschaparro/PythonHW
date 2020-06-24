import os
import csv

csvpath = os.path.join("budget_data.csv")
output_path = os.path.join("budget_data_output.txt")

file_data = []
date_values = []
pnl_values = []

# NEED TO CREATE THE FUNCTION THAT ALLOWS YOU TO EXPORT AS A CSV


# Extract the information in a dictionary or list that allows you to manipulate it from there
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    for row in csvreader:
        file_data.append(row)
        date_values.append(row[0])
        pnl_values.append(row[1])


# This creates the count of how many months there are
month_count = len(date_values)

# This creates the Net Total of the PnL and assigns the numbers to integers 
pnl_values = list(map(int, pnl_values))
total = sum(pnl_values)


# Create a for loop and if statements in order to create the variances and then add the values to a list
var_list = [] 
for x, y in zip(pnl_values[0::], pnl_values[1::]): 
    var_list.append(y-x)
var_list = list(map(int, var_list))
#print(var_list)
# Python program to get average of a list 
def Average(lst): 
    return sum(lst) / len(lst) 
average = Average(var_list)  
average = round(average,2)
#check point
#print(len(var_list))
#print(len(date_values))

#add a zero value to the start of the var list
var_list.insert(0,0)
#print(len(var_list))
#print(var_list)

#Create a list that zips the var and the date_values lists making the first
date_var_list = zip(date_values, var_list)
date_var_list = dict(date_var_list)
#print(date_var_list)

#Create statements that allows you to find the greatest decrease and increase from the Var list
max_value = max(date_var_list.values())  # maximum value
max_keys = [k for k, v in date_var_list.items() if v == max_value] # getting all keys containing the `maximum`

min_value = min(date_var_list.values()) 
min_keys = [k for k, v in date_var_list.items() if v == min_value]

# prints final results
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {max_keys}, $({max_value})")
print(f"Greatest Decrease in Profits: {min_keys}, $({min_value})")

with open(output_path, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------------------------"])
    csvwriter.writerow([f"Total Months: {month_count}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f"Average Change: ${average}"])
    csvwriter.writerow([f'Greatest Increase in Profits: {max_keys}, $({max_value})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {min_keys}, $({min_value})'])
    