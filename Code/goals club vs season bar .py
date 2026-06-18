import matplotlib.pyplot as plt

seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

club_goals = [53,73,60,41,58,41,54,45,51,31,38,11,21,25,33]

plt.figure(figsize=(10,6))
plt.bar(seasons, club_goals, color='green')
plt.title("Messi: Goals per Season (Club)")
plt.xlabel("Season")
plt.ylabel("Goals Scored")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("messi_club_goals_bar.png", dpi=300)
plt.show()
