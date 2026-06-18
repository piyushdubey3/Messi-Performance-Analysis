import matplotlib.pyplot as plt
import numpy as np

# Seasons
seasons = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15',
           '2015-16', '2016-17', '2017-18', '2018-19', '2019-20',
           '2020-21', '2021-22', '2022-23', '2023-24', '2024-25']

# Total passes and successful passes (same as earlier)
club_passes = [2030,2270,1900,1765,2333,1838,1646,1883,1830,1975,2255,1604,1935,1520,1580]
international_passes = [360,380,415,430,450,470,405,410,330,380,430,365,395,335,360]
club_successful_passes = [1670,1865,1540,1430,1934,1505,1320,1529,1487,1629,1918,1393,1613,1250,1300]
international_successful_passes = [290,310,335,350,365,375,315,330,260,310,355,300,325,270,290]
# Calculate success rate
club_success_rate = [round((s / t) * 100, 1) for s, t in zip(club_successful_passes, club_passes)]
international_success_rate = [round((s / t) * 100, 1) for s, t in zip(international_successful_passes, international_passes)]
print(club_success_rate)
print(international_success_rate)
# X positions and width
x = np.arange(len(seasons))
width = 0.35

# Create grouped bars for pass success rate
plt.bar(x - width/2, club_success_rate, width, label='Club Pass Success %', color='teal', edgecolor='black')
plt.bar(x + width/2, international_success_rate, width, label='International Pass Success %', color='goldenrod', edgecolor='black')

# Labels, title, legend
plt.xlabel("Season")
plt.ylabel("Pass Success Rate (%)")
plt.title("Messi: Club vs International Pass Accuracy per Season")
plt.xticks(x, seasons, rotation=45)
plt.ylim(50, 100)
plt.legend()

plt.tight_layout()
plt.show()

# Optional save
# plt.savefig("messi_pass_success_rate.png", dpi=300)
