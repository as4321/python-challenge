import os
import csv

votecount = 0 
winner = 0
counts = dict()
counter = 0 

pypollpath = os.path.join('.', "election_data.csv")
with open (pypollpath, newline="") as pypollfile:
    pypollreader = csv.reader(pypollfile, delimiter=",")
    i = next(pypollreader, None) 

    for row in pypollreader:
        votecount = votecount +1
        counts[row[2]] = counts.get(row[2], 0) + 1     
 
    print("=======================")
    print("Election Results")
    print("=======================")
    print(f"Total Votes: {votecount}") 
    print("=======================")
    
    for x in counts: 
        print(f"{x}: {round((counts[x]/votecount), 2) *100}% ({counts[x]}) ")
        if counts[x] > counter:
            counter = counts[x]
            winner = x
    print("=======================")
    print(f"Winner: {winner}")
    print("=======================")


