# The Nobel Foundation has made a dataset available of all prize winners from the outset of the awards from 1901 to 2023. The dataset used in this project is from the Nobel Prize API and is available in the nobel.csv file in the data folder.

# In this project, you'll get a chance to explore and answer several questions related to this prizewinning data. And we encourage you then to explore further questions that you're interested in!

# Loading in required libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


nobel = pd.read_csv('data/nobel.csv')
nobel.head()

top_gender = nobel.value_counts('sex').index[0]
top_gender 
#'male'


top_country =  nobel.groupby('birth_country')['prize'].count()
top_country = top_country.sort_values(ascending=False).index[0]
top_country
# 'United States of America'

# Calculating the proportion of USA born winners per decade

nobel['usa_born_winner'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby(['decade'], as_index=False)['usa_born_winner'].mean()
​

# Display the proportions of USA born winners per decade
max_decade_usa = 2000
nobel['female_winner'] = nobel['sex'] == 'Female'
df_female = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
max_female_dict = {
    df_female[df_female['female_winner'] == df_female['female_winner'].max()]['decade'].values[0]: df_female[df_female['female_winner'] == df_female['female_winner'].max()]['category'].values[0]
}

max_female_dict
# {2020: 'Literature'}

new_df = nobel[nobel['female_winner']]

min_row = new_df[new_df['year'] == new_df['year'].min()]

first_woman_name, first_woman_category = min_row['full_name'].values[0], min_row['category'].values[0]

print(first_woman_name)

print(first_woman_category)
# Marie Curie, née Sklodowska
# Physics
repeat_winners = pd.DataFrame(nobel['full_name'].value_counts()).reset_index()
repeat_winners.columns = ['full_name', 'count']
repeat_list = list(repeat_winners[repeat_winners['count'] >= 2]['full_name'])
repeat_list

repeat_winners = pd.DataFrame(nobel['full_name'].value_counts()).reset_index()

repeat_winners.columns = ['full_name', 'count']

repeat_list = list(repeat_winners[repeat_winners['count'] >= 2]['full_name'])

repeat_list
