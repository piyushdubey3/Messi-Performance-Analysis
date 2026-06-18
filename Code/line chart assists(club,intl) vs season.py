import matplotlib.pyplot as plt

# Seasons on X-axis
seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

# Example data — replace with your real assists data
club_assists = [23,30,15,14,27,23,16,18,19,25,12,14,20,16,9]
intl_assists = [2,9,1,4,2,3,6,0,3,2,0,5,6,1,5]


# Plot line chart
plt.figure(figsize=(10,6))
plt.plot(seasons, club_assists, marker='o', linestyle='-', color='purple', label='Club Assists')
plt.plot(seasons, intl_assists, marker='o', linestyle='--', color='orange', label='International Assists')

# Titles and labels
plt.title("Messi: Assists per Season (Club vs International)")
plt.xlabel("Season")
plt.ylabel("Assists")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Save and show chart
plt.tight_layout()
plt.savefig("messi_assists_linechart.png", dpi=300)
plt.show()
