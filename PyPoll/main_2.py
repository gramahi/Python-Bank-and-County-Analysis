# -*- coding: utf-8
import os
import csv

# Initializing the file locations on my machine
file_name = os.path.join("election_data_final.csv")

# Create and idnetify our variables for our compiler to iterate through
Candidate_Choices = []
Candidate_Votes = {}


# Kick-ff Total Vote Count
Total_Votes = 0

# Winning Tracker && Winner
Winning_Count = 0
Winner_Candidate = ""

# Open/read CSV Thereafter convert to Dictionaries
with open(file_name, newline="") as election_data:
    # Store contents of csv file in variable in csv-reader
    reader = csv.reader(election_data)
    header = next(reader)
    # Loop through the CSV file
    for row in reader:
        #print(row)
        # # Go through file && add to the total vote count, thereafter Print
        # print(".", end="")
        Total_Votes = Total_Votes + 1
        # Take Into Consideration every Candidate name from each given 'Row'
        Candidate_Name = row[2]
        # Adding Restriction (Rule) for non-Exsisting Candidates
        if Candidate_Name not in Candidate_Choices:
            print(Candidate_Name)
            # Loop through the prior Rule and incorporate Candidates Name along with the vote count
            Candidate_Choices.append(Candidate_Name)
            Candidate_Votes[Candidate_Name] = 0

        # Thereafter incorporate Candidate's vote count and Move Along
        Candidate_Votes[Candidate_Name] = Candidate_Votes[Candidate_Name] + 1

print(Candidate_Votes)
# Initializing the output file locations on my machine ".csv"
Output_File = os.path.join("election_data.csv")

# Utilizing the 'W' to write our outputs
with open(Output_File, "w") as file:
    # Print & Write out Results
    file.write("Eelection_Results")
    file.write("\n")
    file.write("-----------------")
    file.write("\n")
    file.write("Total_Votes")
    file.write("\n")
    print(Candidate_Votes)
    # Deciding the Winner through running a loop in the data set given
    for candidate in Candidate_Votes:

        # Vote and Count %
        Votes = Candidate_Votes.get(candidate)
        Vote_Percent = float(Votes) / float(Total_Votes) * 100
        # Decide Winning Candidate and Winnning Vote
        if (Votes > Winning_Count):
            Winning_Count = Votes
            Winner_Candidate = candidate
        # Print Declaired Outputs
        Voter_Output = f"{candidate}: {Vote_Percent:.3f}% ({Votes})"
        file.write("\n")
        print(Voter_Output, end="")
    # Initializing the output file locations on my machine ".csv"
    # Print Output
    print("Winning Candidtae Summary")
    print("\n")
    print("---------------------")
    print(f"Winner: {Winner_Candidate}")
    print("\n")
    print("---------------------")
    print("\n")
    print("Winner_Candidate_Summary")
    # Save Information to txt.File
    file.write(str(Candidate_Votes))
