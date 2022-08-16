import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data)#["temp"])

# DataFrame - 2D array
# Series - 1D array (like a list)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = sum(temp_list)/len(temp_list)
print(average_temp)

print(data["temp"].mean())

print(data["temp"].max())

print(data["condition"])
print(data.condition)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])