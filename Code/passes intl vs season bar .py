import matplotlib.pyplot as plt

seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

intl_passes = [360,380,415,430,450,470,405,410,330,380,430,365,395,335,360]

plt.figure(figsize=(10,6))
plt.bar(seasons, intl_passes, color='aqua')
plt.title("Messi: Passes per Season (International)")
plt.xlabel("Season")
plt.ylabel("Passes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("messi_international_passes_bar.png", dpi=300)
plt.show()
