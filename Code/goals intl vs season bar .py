import matplotlib.pyplot as plt

seasons = [
    "2010-11", "2011-12", "2012-13", "2013-14", "2014-15",
    "2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
    "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"
]

intl_goals = [2,4,12,6,8,4,8,4,4,5,1,9,17,8,6]

plt.figure(figsize=(10,6))
plt.bar(seasons, intl_goals, color='crimson')
plt.title("Messi: Goals per Season (International)")
plt.xlabel("Season")
plt.ylabel("Goals Scored")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("messi_international_goals_bar.png", dpi=300)
plt.show()
