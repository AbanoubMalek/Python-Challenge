
# Import os module
import os
 

# Module for CSV file
import csv
 
csv_file_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')
 

# Reading CSV file 
with open(csv_file_path) as csv_file:
 
    
    # CSV reader will specify delimiter and the variable that holds the contents
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
 
    csv_header = next(csv_reader)
 
   
    # Setting counters for month, total Profit/Losses, and change
    num_months = 0
    total_pl = 0
    pl_value = 0
    change = 0
 
    # Setting lists for Profit
    profit = []
 
    
    # Setting lists for Date
    date = []
 
    
    
    # Reading the first row
    first_row = next(csv_reader)
    num_months += 1
    total_pl += int(first_row[1])
    pl_value = int(first_row[1])
 
    # Reading each row after the header
    for row in csv_reader:
 
        # Keeping a list of dates
        date.append(row[0])
 
        # Change is calculated
        change = int(row[1]) - pl_value
 
        # Stored in profit list
        profit.append(change)
        pl_value = int(row[1])
 
        # Add to month count
        num_months += 1
 
        # Calculate total PL over the entire period
        total_pl = total_pl + int(row[1])
 
  
    # Find highest increase amount and date
    increase = max(profit)
    increase_index = profit.index(increase)
    increase_date = date[increase_index]
 
   
   
    # Find the highest decrease amount and date
    decrease = min(profit)
    decrease_index = profit.index(decrease)
    decrease_date = date[decrease_index]
 
  
    # Calculate average change in PL
    average = sum(profit) / len(profit)
 
    
    
    # Print results
    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {num_months}")
    print(f"Total: ${total_pl}")
    print(f"Average Change: ${round(average, 2)}")
    print(f"Greatest Increase in Profits: {increase_date} (${increase})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease})")
 
   


# Specify file to write to
output_file_path = os.path.join("PyBank", "output.txt")
 


# List of text for each line
lines = ["Financial Analysis", "---------------------", f"Total Months: {num_months}",
         f"Total: ${total_pl}", f"Average Change: ${round(average, 2)}",
         f"Greatest Increase in Profits: {increase_date} (${increase})",
         f"Greatest Decrease in Profits: {decrease_date} (${decrease})"]
 


# Writing to the output.txt file
with open(output_file_path, 'w') as output_file:
    for line in lines:
        output_file.write(line + '\n')