Titles = ["AEW World Championship", "WWE Universal Championship", "WWE World Championship"]
MidCard_Titles = ["US Title", "IC Title", "TNT Title", "NA Title"]
Titles.extend(MidCard_Titles)
Titles.append("AA Title")
Titles.insert(2, "Impact World Title")
Titles.remove("WWE Universal Championship")
Titles.pop()
print(Titles)
print(Titles.index("TNT Title"))
print(Titles.count("IC Title"))
Titles.sort()
print(Titles)
Titles.reverse()
print(Titles)

Titles2 = Titles.copy()
print(Titles2)
Titles.clear()
print(Titles)





