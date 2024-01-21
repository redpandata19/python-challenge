import os
import csv

PyPoll_csv = os.path.join("Resources", "election_data.csv")

with open(PyPoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")