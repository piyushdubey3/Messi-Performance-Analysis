import matplotlib.pyplot as plt

seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

club_passes = [2030,2270,1900,1765,2333,1838,1646,1883,1830,1975,2255,1604,1935,1520,1580]

plt.figure(figsize=(10,6))
plt.bar(seasons, club_passes, color='pink')
plt.title("Messi: Passes per Season (Club)")
plt.xlabel("Season")
plt.ylabel("Passes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("messi_club_passes_bar.png", dpi=300)
plt.show()
