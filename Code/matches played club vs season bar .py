import matplotlib.pyplot as plt

seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]
club_matches = [55,60,50,46,57,49,52,54,50,44,47,34,41,29,39]



plt.figure(figsize=(10,6))
plt.bar(seasons, club_matches, color='royalblue')
plt.title("Messi: Matches Played per Season (Club)")
plt.xlabel("Season")
plt.ylabel("Matches Played")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("messi_club_matches_bar.png", dpi=300)
plt.show()
