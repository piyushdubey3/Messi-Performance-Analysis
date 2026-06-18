import matplotlib.pyplot as plt
import numpy as np

# Seasons
seasons = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15',
           '2015-16', '2016-17', '2017-18', '2018-19', '2019-20',
           '2020-21', '2021-22', '2022-23', '2023-24', '2024-25']

# Example data (replace with real numbers)
club_successful_passes = [1670,1865,1540,1430,1934,1505,1320,1529,1487,1629,1918,1393,1613,1250,1300]
international_successful_passes = [290,310,335,350,365,375,315,330,260,310,355,300,325,270,290]

# X positions and bar width
x = np.arange(len(seasons))
width = 0.35

# Plot grouped bars
plt.bar(x - width/2, club_successful_passes, width, label='Club Successful Passes', color='mediumturquoise', edgecolor='black')
plt.bar(x + width/2, international_successful_passes, width, label='International Successful Passes', color='sandybrown', edgecolor='black')

# Labels, title, legend
plt.xlabel("Season")
plt.ylabel("Successful Passes")
plt.title("Messi: Club vs International Successful Passes per Season")
plt.xticks(x, seasons, rotation=45)
plt.legend()

plt.tight_layout()
plt.show()

# Optionally save
# plt.savefig("messi_successful_passes.png", dpi=300)
