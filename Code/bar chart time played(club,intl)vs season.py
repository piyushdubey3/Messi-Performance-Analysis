import matplotlib.pyplot as plt
import numpy as np

# Seasons (x-axis)
seasons = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15', 
           '2015-16', '2016-17', '2017-18', '2018-19', '2019-20',
           '2020-21', '2021-22', '2022-23', '2023-24', '2024-25']

# Example data (replace with actual minutes)
club_minutes = [4574,5221,4067,3743,5061,4229,4452,4471,4024,3812,4192,2871,3630,2321,3202]
international_minutes = [866,1200,810,491,1161,685,888,630,450,802,360,1364,1263,652,909]

# Bar positioning
x = np.arange(len(seasons))
width = 0.35

# Create grouped bars
plt.bar(x - width/2, club_minutes, width, label='Club Minutes', color='lightseagreen', edgecolor='black')
plt.bar(x + width/2, international_minutes, width, label='International Minutes', color='orange', edgecolor='black')

# Labels, title, legend
plt.xlabel("Season")
plt.ylabel("Minutes Played")
plt.title("Messi: Club vs International Minutes Played per Season")
plt.xticks(x, seasons, rotation=45)
plt.legend()

# Layout adjustment
plt.tight_layout()

# Show the plot
plt.show()

# Optionally, save as image file
# plt.savefig("messi_minutes_played.png", dpi=300)
