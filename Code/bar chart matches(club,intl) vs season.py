import matplotlib.pyplot as plt
import numpy as np

# Seasons (x-axis)
seasons = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15', 
           '2015-16', '2016-17', '2017-18', '2018-19', '2019-20',
           '2020-21', '2021-22', '2022-23', '2023-24', '2024-25']

# Example data (replace with your actual numbers)
club_matches = [55,60,50,46,57,49,52,54,50,44,47,34,41,29,39]
international_matches = [10,13,9,7,14,8,11,7,5,10,4,16,14,8,11]

# Setting position of bars on X-axis
x = np.arange(len(seasons))
width = 0.35  # width of each bar

# Creating the bar chart
plt.bar(x - width/2, club_matches, width, label='Club Matches', color='skyblue', edgecolor='black')
plt.bar(x + width/2, international_matches, width, label='International Matches', color='salmon', edgecolor='black')

# Add labels, title and legend
plt.xlabel("Season")
plt.ylabel("Number of Matches Played")
plt.title("Messi: Club vs International Matches per Season")
plt.xticks(x, seasons, rotation=45)
plt.legend()

# Adjust layout for better spacing
plt.tight_layout()
plt.show()