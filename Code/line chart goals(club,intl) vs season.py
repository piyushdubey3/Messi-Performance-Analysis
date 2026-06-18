import matplotlib.pyplot as plt

# Seasons on X-axis
seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

# Example data — replace with your actual goal counts
club_goals = [53,73,60,41,58,41,54,45,51,31,38,11,21,25,33]
intl_goals = [2,4,12,6,8,4,8,4,4,5,1,9,17,8,6]

# Create line chart
plt.figure(figsize=(10,6))
plt.plot(seasons, club_goals, marker='o', linestyle='-', color='green', label='Club Goals')
plt.plot(seasons, intl_goals, marker='o', linestyle='--', color='red', label='International Goals')

# Add titles and labels
plt.title("Messi: Goals per Season (Club vs International)")
plt.xlabel("Season")
plt.ylabel("Goals Scored")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Save and show chart
plt.tight_layout()
plt.savefig("messi_goals_linechart.png", dpi=300)
plt.show()
