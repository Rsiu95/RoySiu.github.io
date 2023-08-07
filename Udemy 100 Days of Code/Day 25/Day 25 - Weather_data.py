# with open("C:/Users/RSiu9\OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 25/weather_data.csv") as data_file:
#     weather_data = data_file.readlines()

# #print(weather_data)    
# data = []
# for d in weather_data:
#     data.append(d.strip('\n'))
    
# print(data)

# import csv
# with open("C:/Users/RSiu9\OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 25/weather_data.csv") as data_file:
#     weather_data = csv.reader(data_file)
#     temperature = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
        

#print(data)
# temperature_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data["condition"])
# print(data.condition)
import pandas
# file_path = "C:/Users/RSiu9\OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 25/"
# data = pandas.read_csv(file_path + "weather_data.csv")

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(type(monday.temp))
# print(monday.temp.to_numeric)
# print((monday.temp)*9/5+32)

# data_dict = {
#     "students": ["Amy", "John", "Jim"],
#     "scores": [76, 65, 67]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("C:/Users/RSiu9\OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 25/news_data.csv")


file_path = "C:/Users/RSiu9\OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 25/"
data = pandas.read_csv(file_path + "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data)

fur_color = data["Primary Fur Color"].unique()
fur_count = []

for color in fur_color:
    count = 0
    for d in data["Primary Fur Color"]:
        if color == d:
            count += 1
    
    fur_count.append(count)
print(fur_color)
print(fur_count)
fur_dict = {
    "Fur Color": fur_color,
    "Count": fur_count
}

data = pandas.DataFrame(fur_dict)
data.to_csv("C:/Users/RSiu9\OneDrive/Documents/GitHub/RoySiu.github.io/Udemy 100 Days of Code/Day 25/squirrel_data.csv")