import pandas

data = pandas.read_csv("central_park_squirrel_sightings_2018.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

gray_count = len(gray_squirrels)
cinnamon_count = len(cinnamon_squirrels)
black_count = len(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count_by_color.csv")

