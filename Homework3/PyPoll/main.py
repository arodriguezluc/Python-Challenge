#Python-Challenge_Election_Data

# Import dependencies
import os
import csv

# Variables
total_votes = 0
votes_for_khan = 0
votes_for_correy = 0
votes_for_li = 0
votes_for_otooley = 0

# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")


# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    
     # Read the header row first (Skip if NO Header)
    csv_header = next(csvfile)

    for row in csv_reader:
        
        # Calculate total number of votes cast
        total_votes += 1
        
        # Calculate total number of votes each candidate received
        if (row[2] == "Khan"):
            votes_for_khan += 1
        elif (row[2] == "Correy"):
            votes_for_correy += 1
        elif (row[2] == "Li"):
            votes_for_li += 1
        else:
            votes_for_otooley += 1
            
    # Calculate the percentage of votes each candidate received
    percent_of_khan_votes = round((votes_for_khan/ total_votes),1)
    percent_of_correy_votes = round((votes_for_correy/ total_votes),1)
    percent_of_li_votes = round((votes_for_li/ total_votes),1)
    percent_of_otooley_votes = round((votes_for_otooley/ total_votes),1)
    
    # Calculate the winner (candidate with most votes) of the election
    winner = max(votes_for_khan, votes_for_correy, votes_for_li, votes_for_otooley)

    if winner == votes_for_khan:
        name_of_winner = "Khan"
    elif winner == votes_for_correy:
        name_of_winner = "Correy"
    elif winner == votes_for_li:
        name_of_winner = "Li"
    else:
        name_of_winner = "O'Tooley" 

# Print Analysis
print("Election Results")
print("---------------------------")
print("Total Votes: {total_votes}")
print("---------------------------")
print(f"Kahn: {percent_of_khan_votes:.1%}({votes_for_khan})")
print(f"Correy: {percent_of_correy_votes:.1%}({votes_for_correy})")
print(f"Li: {percent_of_li_votes:.1%}({votes_for_li})")
print(f"O'Tooley: {percent_of_otooley_votes:.1%}({votes_for_otooley})")
print("---------------------------")
print(f"Winner: {name_of_winner}")
print("---------------------------")


output_file = os.path.join("Analysis", "election_data.text")

with open(output_file, 'w',) as txtfile:


    txtfile.write("Election Results\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Khan: {percent_of_khan_votes:.1%}({votes_for_khan})\n")
    txtfile.write(f"Correy: {percent_of_correy_votes:.1%}({votes_for_correy})\n")
    txtfile.write(f"Li: {percent_of_li_votes:.1%}({votes_for_li})\n")
    txtfile.write(f"O'Tooley: {percent_of_otooley_votes:.1%}({votes_for_otooley})\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Winner: {name_of_winner}\n")
    txtfile.write("---------------------------\n")