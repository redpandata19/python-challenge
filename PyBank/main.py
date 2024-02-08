import os
import csv

PyBank_csv = os.path.join("Resources", "budget_data.csv")

with open(PyBank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

total_months = 0
net_Profit_loss = 0


for row in csv_reader
    total_months += 1
