file = open("text.txt")
contents=file.read()
print(contents)
file.close()

with open("text.txt") as file: #./text.txt
    contents=file.read()
    print(contents)

with open("text.txt", mode="w") as file:   #r,w,a
    file.write("\nmeow")

with open("../../OneDrive/Desktop/text2.txt", "w") as file:
    file.write("wow")

import csv

with open("data.csv") as f:
    data= csv.reader(f) #csv reader obj
    for _ in data:
        print(_)

import pandas

data=pandas.read_csv("data.csv") #pandas dataframe obj
column=data["temp"] #pandas series obj
#column=data.temp
print(data)
print(column)

print(data.to_dict())
print(column.to_list())
print(column.mean()) #median, mode, max....
#sum(list)

monday=data[data.day=="Monday"]
print(monday) #pandas dataframe obj (also a table)
print(monday.condition)
print(monday.temp[0]) #int

#dict to pandas dataframe obj
dicti={
    "students": ["amy","ama","ara"],
    "scores":[45,56,78]
}
dataa= pandas.DataFrame(dicti)

dataa.to_csv("newdata.csv") #./newdata.csv

table=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors=table["Primary Fur Color"]
lcolors=colors.to_list()
scolors=set(lcolors)
lcolors=list(scolors)
nlcolors=[]
for _ in lcolors:
    if str(_) != 'nan':
        nlcolors.append(_)
lcount=[]
for _ in nlcolors:
        count=len(table[table["Primary Fur Color"]==_])
        lcount.append(count)
newdict={
    "Fur Color":nlcolors,
    "Count":lcount
}
dataframe=pandas.DataFrame(newdict)
dataframe.to_csv("newtable.csv")