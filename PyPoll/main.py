#election data analysis
#Import the necessary dependencies for os.path.join()

import os
import csv


#Read in a .csv file
election_data_csv = os.path.join("Resources", "election_data.csv")

#Read in the CSV file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

# create lists and dict
    votes_list = []
    candidates = {}
    candidate_list = []
    total_votes = 0   
    voted_percentage_list = []
    winner = ""
    winner_votes = 0
    complete_list = []

# create a loop
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        
        if candidate_name in candidate_list:
            candidates[candidate_name] = candidates[candidate_name] + 1
                    
        else:
            candidate_list.append(candidate_name)
            candidates[candidate_name] = 1

    #calculate the percentages
    for key, value in candidates.items():
        votes_list.append(value)
        votes_percentage = round((float(value)/total_votes * 100), 3)
        voted_percentage_list.append(votes_percentage)

        if (value > winner_votes):
            winner_votes = value
            winner = key

    #combine lists to create one list
        complete_list = zip(candidate_list, voted_percentage_list, votes_list)
        complete_list = list(complete_list)

        
     
    print(f"Election Results")
    print(f"-------------------------------------")
    print(f"Total Votes:", total_votes)
    print(f"-------------------------------------")
    for item in complete_list:
        print(f"{item[0]} : {item[1]}00% ({item[2]})")
    print(f"-------------------------------------")
    print(f"Winner : {winner}")
    print(f"-------------------------------------")
   