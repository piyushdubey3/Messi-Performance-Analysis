import matplotlib.pyplot as plt

# Seasons
seasons = [
    "2010-11","2011-12","2012-13","2013-14","2014-15",
    "2015-16","2016-17","2017-18","2018-19","2019-20",
    "2020-21","2021-22","2022-23","2023-24","2024-25"
]

# Example international successful dribbles (replace with real data)
intl_dribbles = [28,36,40,22,42,25,30,20,15,28,9,45,48,26,33]

plt.figure(figsize=(11,6))
plt.bar(seasons, intl_dribbles, color='darkgreen')

plt.title("Messi: Successful Dribbles per Season (International)", fontsize=13, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Successful Dribbles")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
