import matplotlib.pyplot as plt

seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

intl_assists = [2,9,1,4,2,3,6,0,3,2,0,5,6,1,5]
plt.figure(figsize=(10,6))
plt.bar(seasons, intl_assists, color='darkorange')
plt.title("Messi: Assists per Season (International)")
plt.xlabel("Season")
plt.ylabel("Assists")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("messi_international_assists_bar.png", dpi=300)
plt.show()
