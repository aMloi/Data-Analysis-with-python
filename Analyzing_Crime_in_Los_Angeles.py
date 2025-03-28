

# Every year, American high school students take SATs, which are standardized tests intended to measure literacy, numeracy, and writing skills. There are three sections - reading, math, and writing, each with a maximum score of 800 points. These tests are extremely important for students and colleges, as they play a pivotal role in the admissions process.

# Analyzing the performance of schools is important for a variety of stakeholders, including policy and education professionals, researchers, government, and even parents considering which school their children should attend.

# You have been provided with a dataset called schools.csv, which is previewed below.

# You have been tasked with answering three key questions about New York City (NYC) public school SAT performance.


import pandas as pd

schools = pd.read_csv("schools.csv")

# Preview the data

schools.head()

ath_result = schools[schools["average_math"] >= 800 * 0.8].sort_values("average_math", ascending= False)
best_math_result

best_math_result = schools[schools["average_math"] >= 800 * 0.8].sort_values("average_math", ascending= False)

best_math_result

best_math_schools = best_math_result[['school_name','average_math']].sort_values("average_math", ascending= False)

best_math_schools = best_math_result[['school_name','average_math']].sort_values("average_math", ascending= False)

best_math_schools

schools['total_SAT'] = schools["average_math"]+schools["average_reading"]+schools["average_writing"]

top_10_schools = schools[['school_name','total_SAT']].sort_values("total_SAT",ascending = False).iloc[:10]

top_10_schools

largest_std_dev = schools[schools["borough"]== 'Manhattan'].count()

largest_std_dev

boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

boroughs

​
largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

largest_std_dev


largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

​

largest_std_dev

​
Hidden output
