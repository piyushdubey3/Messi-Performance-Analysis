import matplotlib.pyplot as plt

seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

club_assists = [23,30,15,14,27,23,16,18,19,25,12,14,20,16,9]
plt.figure(figsize=(10,6))
plt.bar(seasons, club_assists, color='mediumorchid')
plt.title("Messi: Assists per Season (Club)")
plt.xlabel("Season")
plt.ylabel("Assists")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("messi_club_assists_bar.png", dpi=300)
plt.show()
