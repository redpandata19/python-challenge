# Dependencies
import os
import csv

# Path to data
pypoll_csv = os.path.join("Resources", "election_data.csv")

# Empty list(s)
candidate_list = []

# Read in csv data and save header data
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
# For each row:
# Count each vote
    # Need to append to dictionary?
    # Perhaps I need a list of candidates before I can make a dictionary for them?
    for row in csv_reader:
        candidate_value = row[2]
        if candidate_value not in candidate_list:
            candidate_list.append(candidate_value)

# Determine who the vote belongs to with a dictionary (dictionary comprehension)
candidate_votes = {candidate: [] for candidate in candidate_list}
# re-open CSV to iterate through once more
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
# iterate through rows and add votes to the relevant candidate's list in the dictionary
    for row in csv_reader:
# Variables to represent the candidate in column 3 and the Ballot ID in column 1 (zero index)
        vote_id = row[0]
        candidate_value = row[2]
# Record Ballot ID to the relevant candidate's list in the dictionary
        if candidate_value in candidate_votes: 
            candidate_votes[candidate_value].append(vote_id)
# Count the vote results for each candidate
for candidate, votes in candidate_votes.items():
    print(f'{candidate}: {len(votes)} votes')

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