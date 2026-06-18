import matplotlib.pyplot as plt
import numpy as np

# Seasons (x-axis)
seasons = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15',
           '2015-16', '2016-17', '2017-18', '2018-19', '2019-20',
           '2020-21', '2021-22', '2022-23', '2023-24', '2024-25']

# Example data (replace with actual numbers)
club_passes = [2030,2270,1900,1765,2333,1838,1646,1883,1830,1975,2255,1604,1935,1520,1580]
international_passes = [360,380,415,430,450,470,405,410,330,380,430,365,395,335,360]

# Bar positions
x = np.arange(len(seasons))
width = 0.35

# Create grouped bars
plt.bar(x - width/2, club_passes, width, label='Club Passes', color='cornflowerblue', edgecolor='black')
plt.bar(x + width/2, international_passes, width, label='International Passes', color='lightcoral', edgecolor='black')

# Labels, title, legend
plt.xlabel("Season")
plt.ylabel("Total Passes")
plt.title("Messi: Club vs International Passes per Season")
plt.xticks(x, seasons, rotation=45)
plt.legend()

# Layout adjustment
plt.tight_layout()

# Show plot
plt.show()

# Optional: save the chart
# plt.savefig("messi_passes_per_season.png", dpi=300)
