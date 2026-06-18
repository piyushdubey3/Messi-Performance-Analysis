import matplotlib.pyplot as plt

# Seasons on X-axis
seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

# Example data (in minutes) — replace with your real stats
club_minutes = [4574,5221,4067,3743,5061,4229,4452,4471,4024,3812,4192,2871,3630,2321,3202]
intl_minutes = [866,1200,810,491,1161,685,888,630,450,802,360,1364,1263,652,909]

# Plot the line chart
plt.figure(figsize=(10,6))
plt.plot(seasons, club_minutes, marker='o', linestyle='-', color='navy', label='Club Minutes Played')
plt.plot(seasons, intl_minutes, marker='o', linestyle='--', color='crimson', label='International Minutes Played')

# Titles and labels
plt.title("Messi: Minutes Played per Season (Club vs International)")
plt.xlabel("Season")
plt.ylabel("Minutes Played")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Save and show chart
plt.tight_layout()
plt.savefig("messi_minutes_linechart.png", dpi=300)
plt.show()
