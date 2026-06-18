import matplotlib.pyplot as plt
import numpy as np

# Seasons (x-axis)
seasons = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15',
           '2015-16', '2016-17', '2017-18', '2018-19', '2019-20',
           '2020-21', '2021-22', '2022-23', '2023-24', '2024-25']

# Example data (replace with actual stats)
club_goals = [53,73,60,41,58,41,54,45,51,31,38,11,21,25,33]
international_goals = [2,4,12,6,8,4,8,4,4,5,1,9,18,8,6]

# Bar positions
x = np.arange(len(seasons))
width = 0.35

# Create grouped bars
plt.bar(x - width/2, club_goals, width, label='Club Goals', color='royalblue', edgecolor='black')
plt.bar(x + width/2, international_goals, width, label='International Goals', color='crimson', edgecolor='black')

# Labels, title, legend
plt.xlabel("Season")
plt.ylabel("Goals Scored")
plt.title("Messi: Club vs International Goals per Season")
plt.xticks(x, seasons, rotation=45)
plt.legend()

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()

# Optionally, save as image
# plt.savefig("messi_goals_per_season.png", dpi=300)
