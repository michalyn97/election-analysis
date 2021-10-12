import csv
import os

#file_to_load = os.path.join("Election_Analysis", "election_results.csv")
#with open(file_to_load) as election_data:
    #print(election_data)

file_to_save = os.path.join("analysis", "election.analysis.txt")
open(file_to_save, "w")  

with open(file_to_save, "w") as txt_file: 

#outfile.write("Hello World!")

#outfile.close()

#outfile.write("Arapahoe")
#outfile.write("Denver")
#outfile.write("Jefferson")

    txt_file.write("Arapahoe, Denver, Jefferson")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
print("Hello World!")

# Open the election results and read the file.
with open(file_to_load) as election_data:
        #to do: read and analyze data here.

    #file_reader = csv.reader(election_data)
    #for row in file_reader:
        #print(row)
    
    file_reader = csv.reader(election_data)
        #print the header row
    headers = next(file_reader)
    print(headers)