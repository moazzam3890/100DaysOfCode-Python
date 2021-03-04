# import csv
#
#
# # with open("weather_data.csv") as weather_data:
# #     data = weather_data.readlines()
# #     for stripped_data in data:
# #         stripped_data.strip()
# #         print(stripped_data)
# #     print(data)
#
# # Data Extraction using csv:
# # with open("weather_data.csv") as weather_data:
# #     # .reader returns the object with each row in a list format. We can loop through it.
# #     data = csv.reader(weather_data)
# #     temperature = []
# #     loop_count = 0
# #     for row in data:
# #         loop_count += 1
# #         if loop_count > 1:
# #             temperature.append(int(row[1]))
# #         # print(row)
# #     print(temperature)
#
#
# # Data Extraction Using Pandas:
# import pandas
# data = pandas.read_csv("weather_data.csv")
# # print(data["condition"])
#
# # Converting dataframe into dictionary format:
# data_in_dict_format = data.to_dict()
# print(data_in_dict_format)
#
# # Converting series or column in list format:
# data_in_list_format = data["temp"].to_list()
# print(data_in_list_format)
#
# # Calculating average temperature of the week without using pandas:
# total_days = len(data_in_list_format)
# total_temp = sum(data_in_list_format)
#
# average_temp = total_temp/total_days
# print(average_temp)
#
# # Calculating average temperature using pandas:
# print(data["temp"].mean())
#
# # getting maximum temperature from file using Pandas:
# print(data["temp"].max())
#
# # getting data from row in pandas:
# print(data[data.temp == data.temp.max()])
#
# # getting row of Monday:
# monday = data[data.day == "Monday"]
# in_fahrenheit = ((int(monday.temp) + 9)/5) + 32
# print(in_fahrenheit)

import pandas

# creating csv from pandas:
data_dict = {
    "students" : ["Moazzam", "Adil", "Khan"],
    "scores": [34, 24, 46],
}

data = pandas.DataFrame(data_dict)
data.to_csv("testing_fie.csv")

students_data = pandas.read_csv("testing_fie.csv")
print(students_data[students_data["students"] == "Moazzam"])
