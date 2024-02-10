import os
import csv

pybank_data = os.path.join("Resources", "budget_data.csv")

months = []
profit_loss = []
changes = []

with open(pybank_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    
# appending the dates to the list 
    for row in csv_reader:
        months.append(row[0]) 

# # re-opening and moving past headers to iterate through rows again
with open(pybank_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")  
    next(csv_reader) 

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
    next(csv_reader)
#dictionary for great_increase to include both a date and a time
    greatest_increase = {'date': 'none',
                        'increase': int(0)
    }
# dictionary for greatest_decrease 
    greatest_decrease = {'date': 'none',
                         'decrease': int(0) }    
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
            decrease_abs = abs(greatest_decrease['decrease'])
        # and update the dictionary if the change_abs is greater increase_abs
        # two ifs: both greater than for abs comparison, but need > 0 and < 0 to indicate sign of change
            if change_amount > 0 and change_abs > increase_abs:
                greatest_increase['date'] = current_date
                greatest_increase['increase'] = change_amount
            if change_amount < 0 and change_abs > decrease_abs:
                greatest_decrease['date'] = current_date
                greatest_decrease['decrease'] = change_amount
        prev_amount = current_amount
    

# print to console
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
print(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["increase"]})')
print('')
print(f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["decrease"]})')

# Export as text file
analysis_txt = 'Financial_Analysis.txt'
analysis_path = os.path.join("analysis","Financial_Analysis.txt")

with open(analysis_path, 'w') as analysis_txt:
    print('Financial Analysis', file=analysis_txt)
    print('', file=analysis_txt)
    print('----------------------------------------------', file=analysis_txt)
    print('', file=analysis_txt)
    print(f'Total Months: {len(months)}', file=analysis_txt)
    print('', file=analysis_txt)
    print(f'Total: ${net_profit_loss}', file=analysis_txt)
    print('', file=analysis_txt)
    print(f'Average Change: ${avg_change}', file=analysis_txt)
    print('', file=analysis_txt)
    print(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["increase"]})', file=analysis_txt)
    print('', file=analysis_txt)
    print(f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["decrease"]})', file=analysis_txt)