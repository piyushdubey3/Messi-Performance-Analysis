import matplotlib.pyplot as plt

seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

intl_matches = [10,13,9,7,14,8,11,7,5,10,4,16,14,8,11]

plt.figure(figsize=(10,6))
plt.bar(seasons, intl_matches, color='tomato')
plt.title("Messi: Matches Played per Season (International)")
plt.xlabel("Season")
plt.ylabel("Matches Played")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("messi_international_matches_bar.png", dpi=300)
plt.show()
