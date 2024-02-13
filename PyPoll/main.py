import os

import csv



csv_file_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csv_file_path) as file:
    csv_reader = csv.reader(file, delimiter=',')
    print(csv_reader)

    csv_header = next(csv_reader)

    candidates = []
    votes = []
    percentages = []
    total_votes = 0

    for row in csv_reader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_index = candidates.index(row[2])
            votes.append(1)
        else:
            candidate_index = candidates.index(row[2])
            votes[candidate_index] += 1

    for vote in votes:
        percentage = (vote / total_votes)
        percentage = "{:.3%}".format(percentage)
        percentages.append(percentage)

    winner_votes = max(votes)
    winner_index = votes.index(winner_votes)
    winning_candidate = candidates[winner_index]

    print("Election Results")
    print("--------------")
    print(f"Total Votes: {total_votes}")
    print("--------------")

    for i in range(len(candidates)):
        print(f"{candidates[i]}: {percentages[i]} ({votes[i]})")
    print("---------------")
    print(f"Winner: {winning_candidate}")
    print("---------------")


output_file_path = os.path.join("PyPoll", "output.txt")

with open(output_file_path, "w") as file:
    line1 = "Election Results\n"
    line2 = "---------------------\n"
    line3 = f"Total Votes: {total_votes}\n"
    line4 = "----------------------\n"
    file.writelines([line1, line2, line3, line4])

    
    for i in range(len(candidates)):
        file.write(f"{candidates[i]}: {percentages[i]} ({votes[i]})\n")

    line5 = "-----------------------\n"
    line6 = f"Winner: {winning_candidate}\n"
    line7 = "------------------------\n"
    file.writelines([line5, line6, line7])