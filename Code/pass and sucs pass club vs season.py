import matplotlib.pyplot as plt
import numpy as np

# Seasons
seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

# Data (example club stats)
club_passes = [2030,2270,1900,1765,2333,1838,1646,1883,1830,1975,2255,1604,1935,1520,1580]
club_successful_passes = [1670,1865,1540,1430,1934,1505,1320,1529,1487,1629,1918,1393,1613,1250,1300]


# Calculate pass accuracy (%)
accuracy = [round((s / t) * 100, 1) for s, t in zip(club_successful_passes, club_passes)]

# Bar positions
x = np.arange(len(seasons))
width = 0.4

# Plot bars
plt.figure(figsize=(11,6))
bars1 = plt.bar(x - width/2, club_passes, width, color='skyblue', label='Total Passes')
bars2 = plt.bar(x + width/2, club_successful_passes, width, color='royalblue', label='Successful Passes')

# Add accuracy labels
for i, acc in enumerate(accuracy):
    plt.text(x[i], max(club_passes[i], club_successful_passes[i]) + 10,
             f"{acc}%", ha='center', va='bottom', fontsize=8, fontweight='bold', color='black')

# Labels and title
plt.title("Messi: Passes vs Successful Passes per Season (Club)", fontsize=13, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Number of Passes")
plt.xticks(x, seasons, rotation=45)
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig("messi_club_passes_accuracy.png", dpi=300)
plt.show()
