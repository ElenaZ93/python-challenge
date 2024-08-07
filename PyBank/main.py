import pandas as pd
import os

# Construct file path
file_path = os.path.join("C:\\Users\\elena\\Documents\\Bootcamp\\Challenge 3\\Starter_Code (1)\\Starter_Code\\PyBank\\Resources", "budget_data.csv")

# Read CSV file
budget_data = pd.read_csv(file_path)

# Total number of months included in the dataset
total_months = budget_data['Date'].nunique()

# Net total amount of "Profit/Losses" over the entire period
net_total = budget_data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
budget_data['Change'] = budget_data['Profit/Losses'].diff()

# Average of those changes
average_change = budget_data['Change'].mean()

# Greatest increase in profits (date and amount) over the entire period
greatest_increase = budget_data.loc[budget_data['Change'].idxmax()]

# Greatest decrease in profits (date and amount) over the entire period
greatest_decrease = budget_data.loc[budget_data['Change'].idxmin()]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Change']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Change']})")
