import matplotlib.pyplot as plt

# Seasons
seasons = [
    "2010-11","2011-12","2012-13","2013-14","2014-15",
    "2015-16","2016-17","2017-18","2018-19","2019-20",
    "2020-21","2021-22","2022-23","2023-24","2024-25"
]

# Example data (replace with real dribble stats)
club_dribbles = [265,222,143,169,266,151,154,222,169,239,188,87,160,62,98]
intl_dribbles = [28,36,40,22,42,25,30,20,15,28,9,45,48,26,33]

plt.figure(figsize=(11,6))

# Club dribbles line
plt.plot(seasons, club_dribbles, marker='o', linestyle='-', color='mediumseagreen',
         label='Club Successful Dribbles')

# International dribbles line
plt.plot(seasons, intl_dribbles, marker='o', linestyle='--', color='darkgreen',
         label='International Successful Dribbles')

plt.title("Messi: Successful Dribbles per Season (Club vs International)", fontsize=13, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Successful Dribbles")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()
