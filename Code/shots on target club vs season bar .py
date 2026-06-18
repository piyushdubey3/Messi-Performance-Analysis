import matplotlib.pyplot as plt

# Seasons
seasons = [
    "2010-11","2011-12","2012-13","2013-14","2014-15",
    "2015-16","2016-17","2017-18","2018-19","2019-20",
    "2020-21","2021-22","2022-23","2023-24","2024-25"
]

# Example club shots on target (replace with your real data)
club_shots = [115,135,100,81,120,89,93,120,113,86,111,39,66,37,67]

plt.figure(figsize=(11,6))
plt.bar(seasons, club_shots, color='pink')

plt.title("Messi: Shots on Target per Season (Club)", fontsize=13, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Shots on Target")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
