import matplotlib.pyplot as plt

# Seasons
seasons = [
    "2010-11","2011-12","2012-13","2013-14","2014-15",
    "2015-16","2016-17","2017-18","2018-19","2019-20",
    "2020-21","2021-22","2022-23","2023-24","2024-25"
]

# Example club successful dribbles (replace with real data)
club_dribbles = [265,222,143,169,266,151,154,222,169,239,188,87,160,62,98]

plt.figure(figsize=(11,6))
plt.bar(seasons, club_dribbles, color='mediumseagreen')

plt.title("Messi: Successful Dribbles per Season (Club)", fontsize=13, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Successful Dribbles")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
