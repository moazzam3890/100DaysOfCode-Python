import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])
gray_count = 0
black_count = 0
cinnamon_count = 0
color_list = data["Primary Fur Color"].to_list()


for color in color_list:
    if color == "Gray":
        gray_count += 1
    elif color == "Black":
        black_count += 1
    elif color == "Cinnamon":
        cinnamon_count += 1


data_dict = {
    "Fur_Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cinnamon_count],
}


counting_data = pandas.DataFrame(data_dict)
counting_data.to_csv("squirrel_count_color-wise")
