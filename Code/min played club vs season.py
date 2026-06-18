import matplotlib.pyplot as plt

# Seasons
seasons = [
    "2010-11","2011-12","2012-13","2013-14","2014-15",
    "2015-16","2016-17","2017-18","2018-19","2019-20",
    "2020-21","2021-22","2022-23","2023-24","2024-25"
]

# Club minutes played (your dataset)
club_minutes = [4574,5221,4067,3743,5061,4229,4452,4471,4024,3812,4192,2871,3630,2321,3202]

plt.figure(figsize=(11,6))
plt.bar(seasons, club_minutes, color='navy')

plt.title("Messi: Minutes Played per Season (Club)", fontsize=14, fontweight='bold')
plt.xlabel("Season")
plt.ylabel("Minutes Played")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
