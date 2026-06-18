import matplotlib.pyplot as plt
import numpy as np

# Seasons
seasons = [
    "2010-11","2011-12","2012-13","2013-14","2014-15",
    "2015-16","2016-17","2017-18","2018-19","2019-20",
    "2020-21","2021-22","2022-23","2023-24","2024-25"
]

# Example data (replace with real numbers)
club_dribbles = [265,222,143,169,266,151,154,222,169,239,188,87,160,62,98]
intl_dribbles = [28,36,40,22,42,25,30,20,15,28,9,45,48,26,33]

# Bar width + X positions
x = np.arange(len(seasons))
width = 0.4

plt.figure(figsize=(11,6))

# Bars
plt.bar(x - width/2, club_dribbles, width, label="Club Successful Dribbles", color='mediumseagreen')
plt.bar(x + width/2, intl_dribbles, width, label="International Successful Dribbles", color='darkgreen')

# Labels
plt.title("Messi: Successful Dribbles per Season (Club vs International)", fontsize=13, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Successful Dribbles")
plt.xticks(x, seasons, rotation=45)
plt.legend()
plt.tight_layout()

plt.show()
