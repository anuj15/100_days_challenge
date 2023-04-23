import csv

import pandas

with open("weather_data.csv") as f:
    data = f.readlines()
print(data)

with open("weather_data.csv") as f:
    data = csv.reader(f)
    temp = []
    for i in data:
        temp.append(i[1])
temp.pop(0)
temp = [int(x) for x in temp]
print(temp)

data = pandas.read_csv("weather_data.csv")
print(data)
print(data.temp.tolist())

temp_list = data.temp.tolist()
print(sum(temp_list) / len(temp_list))
print(data.temp.mean())
print(data.temp.max())
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.temp)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "score": [75, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")

data = pandas.read_csv("squirrel_data.csv")
g = len(data[data["Primary Fur Color"] == "Gray"])
r = len(data[data["Primary Fur Color"] == "Red"])
b = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "fur color": ["grey", "red", "black"],
    "count": [g, r, b]
}
d = pandas.DataFrame(data_dict)
d.to_csv("new_sq_data.csv")

if __name__ == '__main__':
    print("Start")
