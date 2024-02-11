# Dependencies
import os
import csv

# Path to data
PyPoll_csv = os.path.join("Resources", "election_data.csv")

# Empty list(s)
candidate_list = []

# Read in csv data and save header data
with open(PyPoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
# For each row:
# Count each vote
    # Need to append to dictionary?
    # Perhaps I need a list of candidates before I can make a dictionary for them?
    for row in csv_reader:
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
print(candidate_list)

# Determine who the vote belongs to
# candidates_dict = {"Cand1_Name": 'none',
#                    "cand2"}

# Calculate percentage of votes per candidate
    # Idea: len each list? Get a total?
    # Is there an activity close to this?
# Winner of election based on popular vote


# # print results to console
# print('')
# print('Election Results')
# print('')
# print('------------------------------------------')
# print('')
# print('Total Votes:')
# print('')
# print('------------------------------------------')
# print('')
# print('cand1results')
# print('cand2results')
# print('cand3results')
# print('')
# print('------------------------------------------')
# print('')
# print('Winner:<pop.vote_winner>')
# print('')
# print('------------------------------------------')

# # Export results as text file
# elect_txt = 'Election_Results.txt'
# analysis_path = os.path.join("analysis","Election_Results.txt")

# with open(analysis_path, 'w') as elect_txt:
#     print('', file=elect_txt)
#     print('Election Results', file=elect_txt)
#     print('', file=elect_txt)
#     print('------------------------------------------', file=elect_txt)
#     print('', file=elect_txt)
#     print('Total Votes:', file=elect_txt)
#     print('', file=elect_txt)
#     print('------------------------------------------', file=elect_txt)
#     print('', file=elect_txt)
#     print('cand1results', file=elect_txt)
#     print('cand2results', file=elect_txt)
#     print('cand3results', file=elect_txt)
#     print('', file=elect_txt)
#     print('------------------------------------------', file=elect_txt)
#     print('', file=elect_txt)
#     print('Winner:<pop.vote_winner>', file=elect_txt)
#     print('', file=elect_txt)
#     print('------------------------------------------', file=elect_txt)