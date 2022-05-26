# import dependencies
import csv
import os

# declare csv path
election_csv = os.path.join("/Users/russ/Desktop/python_challenge/pyPoll/Resources/election_data.csv")

# set necessary variables, list and dict
candidate_options = []
votes = {} # dict
lead_candidate = ""
lead_count = 0
total_vote_count = 0

# open the csv and read the file using the python inbult reader
# in this code we read the csv file as a list dict
# sourced from https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file
with open(election_csv) as election_data:
    reader = csv.DictReader(election_data)

    # iterate through the rows
    for row in reader:

        # initiate vote counting
        total_vote_count = total_vote_count + 1

        # get candidate name from each row
        name = row["Candidate"]

        # if candidate not in the count then append
        if name not in candidate_options:

            # add candidate name to the list
            candidate_options.append(name)

            # count the votes for each candidate and set the counter to zero
            votes[name] = 0

        # for each extracted candidate add vote count
        votes[name] = votes[name] + 1
    
    print("Electionn Results")
    print("---------------------------")
    print(f"Total votes: {total_vote_count}")
    print("---------------------------")

    # Determine the winner by looping through the counts
    for candidate in votes:

        # Retrieve vote count and percentage
        vote_count = votes.get(candidate)
        vote_percentage = float(vote_count) / float(total_vote_count) * 100

        # check the votes and return the top count 
        if (vote_count > lead_count):
            lead_count = vote_count
            lead_candidate = candidate

        
        # print the vote count for each candidate and round the % to 3 decimal places
        # sourced from https://www.codegrepper.com/code-examples/objectivec/print+3+decimal+places+python
        # also print each candidate on a different row using \n function
        #sourced from https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/#:~:text=The%20new%20line%20character%20in%20Python%20is%20%5Cn%20.,used%20to%20separate%20the%20lines.
        final = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(final, end="")
        print(f"winner: {lead_candidate}")
        
        output = os.path.join("/Users/russ/Desktop/python_challenge/PyPoll/Analysis/analysis.txt")
        with open(output, "w") as analysis:
            writer = csv.writer(analysis)
            analysis.write("Election Results")
            analysis.write("\n")
            analysis.write("----------------------------------------")
            analysis.write("\n")
            analysis.write(f"Total votes:{total_vote_count}")
            for candidate in votes:
                vote_count = votes.get(candidate)
                vote_percentage = float(vote_count) / float(total_vote_count) * 100 
                if (vote_count > lead_count):
                    lead_count = vote_count
                    lead_candidate = candidate
                final = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            analysis.write(f"final", end="")
            analysis.write(f"Winner: {lead_candidate}")
