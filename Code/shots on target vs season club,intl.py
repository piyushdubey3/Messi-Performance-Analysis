import matplotlib.pyplot as plt
import numpy as np

# Seasons
seasons = [
    "2010-11","2011-12","2012-13","2013-14","2014-15",
    "2015-16","2016-17","2017-18","2018-19","2019-20",
    "2020-21","2021-22","2022-23","2023-24","2024-25"
]

# Example data – replace with your real shots on target
club_shots = [115,135,100,81,120,89,93,120,113,86,111,39,66,37,67]
intl_shots = [9,15,17,11,16,10,13,9,8,12,3,19,26,14,15]

# X positions
x = np.arange(len(seasons))
width = 0.4

plt.figure(figsize=(11,6))

# Bars
plt.bar(x - width/2, club_shots, width, label="Club Shots on Target", color='royalblue')
plt.bar(x + width/2, intl_shots, width, label="International Shots on Target", color='crimson')

# Labels & layout
plt.title("Messi: Shots on Target per Season (Club vs International)", fontsize=14, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Shots on Target")
plt.xticks(x, seasons, rotation=45)
plt.legend()
plt.tight_layout()

plt.show()
