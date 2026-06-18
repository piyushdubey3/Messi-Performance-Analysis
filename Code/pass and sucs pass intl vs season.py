import matplotlib.pyplot as plt
import numpy as np

# Seasons
seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

# Data
intl_passes = [360,380,415,430,450,470,405,410,330,380,430,365,395,335,360]
intl_successful_passes = [290,310,335,350,365,375,315,330,260,310,355,300,325,270,290]

# Calculate pass accuracy (%)
accuracy = [round((s / t) * 100, 1) for s, t in zip(intl_successful_passes, intl_passes)]

# Bar positions
x = np.arange(len(seasons))
width = 0.4

# Plot bars
plt.figure(figsize=(11,6))
bars1 = plt.bar(x - width/2, intl_passes, width, color='pink', label='Total Passes')
bars2 = plt.bar(x + width/2, intl_successful_passes, width, color='firebrick', label='Successful Passes')

# Add accuracy labels
for i, acc in enumerate(accuracy):
    plt.text(x[i], max(intl_passes[i], intl_successful_passes[i]) + 5,
             f"{acc}%", ha='center', va='bottom', fontsize=8, fontweight='bold', color='black')

# Labels and title
plt.title("Messi: Passes vs Successful Passes per Season (International)", fontsize=13, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Number of Passes")
plt.xticks(x, seasons, rotation=45)
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig("messi_international_passes_accuracy.png", dpi=300)
plt.show()
