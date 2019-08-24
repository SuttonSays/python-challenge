#Import modules
#Dependencies
import pandas as pd

#Set the path from the Resources folder
poll_data_path = "Resources/election_data.csv"

#Use Pandas to read data
poll_data_pd = pd.read_csv(poll_data_path)
poll_data_pd.head()

#Total Votes Cast
Total_Votes = poll_data_pd["Candidate"].value_counts().sum()
Total_Votes

#Total Votes Cast by Candidate
candidate_count = poll_data_pd["Candidate"].value_counts()
candidate_count

