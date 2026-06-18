import matplotlib.pyplot as plt

# Seasons on X-axis
seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

# Example data — replace with your actual data
club_matches = [55,60,50,46,57,49,52,54,50,44,47,34,41,29,39]
intl_matches = [10,13,9,7,14,8,11,7,5,10,4,16,14,8,11]

# Plot line chart
plt.figure(figsize=(10,6))
plt.plot(seasons, club_matches, marker='o', linestyle='-', color='blue', label='Club Matches')
plt.plot(seasons, intl_matches, marker='o', linestyle='--', color='orange', label='International Matches')

# Titles and labels
plt.title("Messi: Matches Played per Season (Club vs International)")
plt.xlabel("Season")
plt.ylabel("Matches Played")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Save chart and display
plt.tight_layout()
plt.savefig("messi_matches_linechart.png", dpi=300)
plt.show()
