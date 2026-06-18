import matplotlib.pyplot as plt

# Seasons
seasons = [
    "2010-11","2011-12","2012-13","2013-14","2014-15",
    "2015-16","2016-17","2017-18","2018-19","2019-20",
    "2020-21","2021-22","2022-23","2023-24","2024-25"
]

# Example international shots on target (replace with your real data)
intl_shots = [9,15,17,11,16,10,13,9,8,12,3,19,26,14,15]

plt.figure(figsize=(11,6))
plt.bar(seasons, intl_shots, color='green')

plt.title("Messi: Shots on Target per Season (International)", fontsize=13, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Shots on Target")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
