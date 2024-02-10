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
    greatest_increase = {'date': 'none',
                        'increase': int(0)
    }
# Need to distinguish between no change and prev_amount being undefined
    prev_amount = 'none'
    for row in csv_reader:
    # setup iterative variables
        current_date, current_amount = row
        if prev_amount != 'none':
        # calculation from those variable to get change
            change_amount = int(int(current_amount) - int(prev_amount))
        # the change should be the absolute value for comparison
            change_abs = abs(change_amount)
        # Need to compare change_abs to absolute value of previous increase
            increase_abs = abs(greatest_increase['increase'])
        # and update the dictionary if the change_abs is greater inrease_abs
        # two ifs: it is greater than, it is less than
            # actually only need the second one if I wanted to combine greatest and least decrease?
            if change_abs > increase_abs:
                greatest_increase['date'] = current_date
                greatest_increase['increase'] = change_amount
    prev_amount = current_amount
    
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
print(f'Greatest Increase in Profits: {greatest_increase["date"]} ({greatest_increase["increase"]})')
print('')
# print(f'Greatest Decrease in Profits: {greatest_decrease}')

# EXPORT A TEXT FILE!!!!!!!!!!!!!!!!!!!!!!!