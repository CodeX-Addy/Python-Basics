# Creating pandas columns using for loop
# GFG Reference
import pandas as pd
import numpy as np

raw_Data = {'Voter_name': ['Geek1', 'Geek2', 'Geek3', 'Geek4',
						'Geek5', 'Geek6', 'Geek7', 'Geek8'],
			'Voter_age': [15, 23, 25, 9, 67, 54, 42, np.NaN]}

df = pd.DataFrame(raw_Data, columns = ['Voter_name', 'Voter_age'])
#	 //DataFrame will look like
#
# Voter_name		 Voter_age
# Geek1			 15
# Geek2			 23
# Geek3			 25
# Geek4			 09
# Geek5			 67
# Geek6			 54
# Geek7			 42
# Geek8		 not a number

eligible = []

# For each row in the column
for age in df['Voter_age']:	
	if age >= 18:				 # if Voter eligible
		eligible.append('Yes')
	elif age < 18:				 # if voter is not eligible
		eligible.append("No")
	else:
		eligible.append("Not Sure")

# Create a column from the list
df['Voter'] = eligible
			
print(df)
