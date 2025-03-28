# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Reading the Netflix data
netflix_df = pd.read_csv('netflix_data.csv')

# Filtering the dataframe to include only movies
netflix_movies = netflix_df[netflix_df['type'] == "Movie"].loc[:, ['title', "country", "genre", "release_year", "duration"]]

# Identifying short movies with duration less than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Initializing an empty list to store colors for the scatter plot
colors = []

# Assigning colors based on the genre of the movie
for _, row in netflix_movies.iterrows():
    if row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == 'Documentaries':
        colors.append('blue')
    elif row['genre'] == 'Stand-Up':
        colors.append('yellow')
    else:
        colors.append('green')

# Creating a scatter plot to visualize movie duration by year of release
fig = plt.figure(figsize=(10, 6))
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")
plt.show()

# The variable 'answer' seems to be unused and its purpose is unclear.
# If it was intended to be part of a conditional logic or output, it needs to be integrated properly.
