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
# iterate through each row of the CSV and add unique candidates to the candidate list
    for row in csv_reader:
        candidate_value = row[2]
        if candidate_value not in candidate_list:
            candidate_list.append(candidate_value)

# Determine who the vote belongs to with a dictionary
# (dictionary comprehension)
candidate_votes = {candidate: [] for candidate in candidate_list}
# open CSV
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

# Calculate percentage of votes per candidate
# Tally the vote
total_votes_per = {candidate: len(votes) for candidate, votes in candidate_votes.items()}
# sum the tallied votes
total_votes = sum(total_votes_per.values())
# for each candidate, divide the tallied vote by the total votes * 100 for percentage
percentage_votes = {candidate: ((tally / total_votes) * 100) for candidate, tally in total_votes_per.items()}
# round each percentage to 3 decimal places
rounded_percents = {candidate: round(perc_vote,3) for candidate, perc_vote in percentage_votes.items()}
print(rounded_percents)

# create a dataframe? :/ that's pandas which is technically after this homework
# combine dictionaries?
combined_data = {candidate: (rounded_percents[candidate], total_votes_per[candidate]) for candidate in candidate_votes}

print(combined_data)


# Winner of election based on popular vote


# print results to console
print('')
print('Election Results')
print('')
print('------------------------------------------')
print('')
print(f'Total Votes: {total_votes}')
print('')
print('------------------------------------------')
print('')
for candidate,data in combined_data.items():
        percentage,tally = data
        print(f'{candidate}: {percentage}% ({tally})')
print('')
print('------------------------------------------')
print('')
print('Winner:<pop.vote_winner>')
print('')
print('------------------------------------------')

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