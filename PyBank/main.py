import os
import csv

pybank_data = os.path.join("Resources", "budget_data.csv")

months = []
profit_loss = []
changes = []

with open(pybank_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")
    
# appending the dates to the list 
    for row in csv_reader:
        months.append(row[0]) 

# # re-opening and moving past headers to iterate through rows again
with open(pybank_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_reader) 

# appending profits/losses to a list and summing
    for row in csv_reader:
        profit_loss.append(int(row[1]))
    net_profit_loss = sum(profit_loss)
    
# Calculte the average change in profit/losses
# using profit_loss instead of reopening the CSV
    change = []
    for i in range(1, len(profit_loss)):
        change.append(profit_loss[i] - profit_loss[i-1])
    sum_change = sum(change)
    avg_change = round(sum_change / len(change),2)

# greatest increase in profits (date and amount) over the entire period
# reopen the CSV bc need both date and value, can't use profit_loss
with open(pybank_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    csv_header = next(csv_reader)
#dictionary for great_increase to include both a date and a time
    greatest_increase = {'date':none,
                        'increase': int(0)
    }

    for j in range(1, len(profit_loss)):
        # setup iterative variables
        current_date, current_amount = rows[j]
        prev_date, prev_amount = rows[j - 1]
        # calculation from those variable to get change
        # the change should be the absolute value for comparison
        change_amount = int((current_amount) - (prev_amount))
        change_abs = abs(change_amount)
        # setup initial variables to go in the greatest_increase dictionary
        greatest_increase['date'] = current_date
        greatest_increase['increase'] = change_amount
        # Need to compare the the increase stored in the dictionary 
        # to the calculated change_amount
        # and update the dictionary if the change amount is greater


    
# greatest decrease in profits (date and amount) over the entire period
    # greatest_decrease = 0
    # for h in change: 



# EXPORT A TEXT FILE!!!!!!!!!!!!!!!!!!!!!!!

print('Financial Analysis')
print('')
print('----------------------------------------------')
print('')
print(f'Total Months: {len(months)}')
print('')
print(f'Total: ${net_profit_loss}')
print('')
print(f'Average Change: ${avg_change}')
print('')
# print(f'Greatest Increase in Profits: {greatest_increase}')
# print('')
# print(f'Greatest Decrease in Profits: {greatest_decrease}')

# EXPORT A TEXT FILE!!!!!!!!!!!!!!!!!!!!!!!