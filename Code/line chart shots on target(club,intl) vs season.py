import matplotlib.pyplot as plt

# Seasons
seasons = [
    "2010-11","2011-12","2012-13","2013-14","2014-15",
    "2015-16","2016-17","2017-18","2018-19","2019-20",
    "2020-21","2021-22","2022-23","2023-24","2024-25"
]

# Example data — replace with real values
club_shots = [115,135,100,81,120,89,93,120,113,86,111,39,66,37,67]
intl_shots = [9,15,17,11,16,10,13,9,8,12,3,19,26,14,15]


plt.figure(figsize=(11,6))

# Club line
plt.plot(seasons, club_shots, marker='o', linestyle='-', color='royalblue', label='Club Shots on Target')

# International line
plt.plot(seasons, intl_shots, marker='o', linestyle='--', color='crimson', label='International Shots on Target')

plt.title("Messi: Shots on Target per Season (Club vs International)", fontsize=13, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Shots on Target")
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()

plt.show()
