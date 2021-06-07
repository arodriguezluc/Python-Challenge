#Python-Challenge_Budget_Data
# Import dependencies
import os
import csv

# variables

total_num_of_months = 0
net_total_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0


# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")


# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (Skip if NO Header)
    csv_header = next(csv_reader)
    row = next(csv_reader)
    
    # Calculate Total number of months, Net total amount of "Profit/Losses" & set variables for Rows
    previous_row = int(row[1])
    total_num_of_months += 1
    net_total_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Read Each Row Of Data After The Header
    for row in csv_reader:
        
        # Calculate Total number of months included in the Dataset
        total_num_of_months += 1
        # Calculate Net Amount Of "Profit/Losses" Over The Entire Period
        net_total_amount += int(row[1])

        # Calculate the revenue change from the current month to the previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculates Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculates Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate the average/arithmitic mean & the date
    average_change = round(sum(monthly_change)/ len(monthly_change),2)
    
    greatest = max(monthly_change)
    lowest = min(monthly_change)


# Prints Analysis
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_num_of_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${greatest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")


output_file = os.path.join("Analysis", "budget_data.text")


with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months: {total_num_of_months}\n")
    txtfile.write(f"Total: ${net_total_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${greatest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")

    
