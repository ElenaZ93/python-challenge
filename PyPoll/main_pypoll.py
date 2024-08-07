import os
import pandas as pd

# Construct file path
file_path = os.path.join("C:\\Users\\elena\\Documents\\Bootcamp\\Challenge 3\\Starter_Code (1)\\Starter_Code\\PyPoll\\Resources", "election_data.csv")

# Read CSV file
data = pd.read_csv(file_path)

# The total number of votes cast
total_votes = len(data)

# A complete list of candidates who received votes
candidates = data['Candidate'].unique()

# The percentage of votes each candidate won
votes_per_candidate = data['Candidate'].value_counts()

# The total number of votes each candidate won
percent_votes_per_candidate = (votes_per_candidate / total_votes) * 100

# The winner of the election based on popular vote
winner = votes_per_candidate.idxmax()

results_summary = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

for candidate in candidates:
    results_summary += (
        f"{candidate}: {percent_votes_per_candidate[candidate]:.3f}% "
        f"({votes_per_candidate[candidate]})\n"
    )

results_summary += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# Display the results summary
print(results_summary)

# Exporting the results to a text file
output_file_path = os.path.join("C:\\Users\\elena\\Documents\\Bootcamp\\Challenge 3\\Starter_Code (1)\\Starter_Code\\PyPoll\\Resources", "election_results.txt")
with open(output_file_path, 'w') as file:
    file.write(results_summary)