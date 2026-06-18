import matplotlib.pyplot as plt
import numpy as np

# Seasons (x-axis)
seasons = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15',
           '2015-16', '2016-17', '2017-18', '2018-19', '2019-20',
           '2020-21', '2021-22', '2022-23', '2023-24', '2024-25']

# Example data (replace with real stats)
club_assists = [23,30,15,14,27,23,16,18,19,25,12,14,20,16,9]
international_assists = [2,9,1,4,2,3,6,0,3,2,0,5,6,1,5]

# Bar positions
x = np.arange(len(seasons))
width = 0.35

# Create grouped bars
plt.bar(x - width/2, club_assists, width, label='Club Assists', color='mediumseagreen', edgecolor='black')
plt.bar(x + width/2, international_assists, width, label='International Assists', color='gold', edgecolor='black')

# Labels, title, legend
plt.xlabel("Season")
plt.ylabel("Number of Assists")
plt.title("Messi: Club vs International Assists per Season")
plt.xticks(x, seasons, rotation=45)
plt.legend()

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()

# Optional: save the chart
# plt.savefig("messi_assists_per_season.png", dpi=300)
